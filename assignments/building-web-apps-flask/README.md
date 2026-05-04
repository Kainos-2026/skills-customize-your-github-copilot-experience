# 📘 Assignment: Building Web Apps with Flask

## 🎯 Objective

Create a simple web application using Flask that includes routes, templates, and form handling to understand the basics of web development in Python.

## 📝 Tasks

### 🛠️	Set Up Flask Routes

#### Description
Set up basic routes in your Flask application for the home page and a contact form page.

#### Requirements
Completed program should:

- Have a route for the home page (`/`) that renders an HTML template
- Have a route for the contact form (`/contact`) that handles both GET (display form) and POST (process form) requests
- Use Flask's `render_template` to display pages

### 🛠️	Create HTML Templates

#### Description
Create HTML templates using Jinja2 for your web pages, including a base layout and specific pages.

#### Requirements
Completed program should:

- Include a base template (`base.html`) with common HTML structure and navigation
- Create a home page template (`home.html`) that extends the base and displays a welcome message
- Create a contact form template (`contact.html`) that extends the base and includes a form with name and message fields

### 🛠️	Handle Form Submissions

#### Description
Implement form processing to handle user input and provide feedback.

#### Requirements
Completed program should:

- Process POST data from the contact form
- Validate that name and message fields are not empty
- Display a success message on the same page after successful submission
- Handle validation errors by re-displaying the form with error messages