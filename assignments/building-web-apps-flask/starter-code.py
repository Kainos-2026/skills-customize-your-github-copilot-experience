from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # TODO: Render the home template
    pass

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # TODO: Handle form submission
        # Get name and message from form
        # Validate inputs
        # Return success or error
        pass
    # TODO: Render the contact form template
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)