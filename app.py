from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample projects data (Can be fetched from a database later)
projects = [
    {"title": "DriveTo", "description": "A car rental service web application", "image": "https://plus.unsplash.com/premium_photo-1661290470322-a313098e7c2a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "link": "https://github.com/AtharvaPatil86/DriveTo"},
    {"title": "Digi Kissan", "description": "Digi kissan is a website that helps in infroming farmers about government scheme", "image": "https://images.unsplash.com/photo-1574943320219-553eb213f72d?q=80&w=1991&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "link": "https://github.com/Pratik9113/government_scheme"},
    {"title": "ganit app", "description": "Ganit app is a java based app that generates math questions", "image": "https://images.unsplash.com/photo-1518133910546-b6c2fb7d79e3?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "link": "https://github.com/laukik86/GanitApp"}
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html", projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    return render_template("contact.html")

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    return render_template("success.html", name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)
