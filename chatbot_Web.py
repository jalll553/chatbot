from flask import Flask, render_template_string, request

app = Flask(__name__)

# Function to generate bot responses
def get_response(user_input, name):
    if user_input.lower() == "hi":
        return f"Hello {name}!"
    elif user_input.lower() == "how are you":
        return "I'm good, thanks for asking!"
    elif user_input.lower() == "hello":
        return "hello, how are you?!"
    elif user_input.lower() == "I am fine":
        return "Oh, good to hear!"
    elif user_input.lower() == "i am fine":
        return "Oh, good to hear!"
    elif user_input.lower() == "I am fine, how are you?":
        return "I am also fine, thanks for asking!"
    elif user_input.lower() == "thanks":
        return "No problem!"
    elif user_input.lower() == "bye":
        return f"Goodbye {name}!"
    else:
        return "Sorry, I don't understand that."

# HTML template for the page
HTML_PAGE = """
<!doctype html>
<html>
    <head>
        <title>ChatBot</title>
    </head>
    <body>
        <h1>Welcome to ChatBot!</h1>
        
        <!-- Form to capture user name and message -->
        <form method="post">
            <label>Your name:</label><br>
            <input type="text" name="name" value="{{ name }}" required><br><br>
            
            <label>Your message:</label><br>
            <input type="text" name="message" required><br><br>
            
            <input type="submit" value="Send">
        </form>
        
        <!-- Displaying the response if any -->
        {% if response %}
            <p><strong>You:</strong> {{ user_input }}</p>
            <p><strong>Bot:</strong> {{ response }}</p>
        {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    user_input = ""
    name = ""

    # When the form is submitted
    if request.method == "POST":
        name = request.form["name"]  # Capturing name input
        user_input = request.form["message"]  # Capturing user message input
        response = get_response(user_input, name)  # Generating response
    
    # Rendering the HTML page with the response, user input, and name
    return render_template_string(HTML_PAGE, response=response, user_input=user_input, name=name)

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5001)
