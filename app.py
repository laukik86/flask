from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample projects data - in a real application, this might come from a database

projects = [
    {
        'id': 1,
        'title': 'DriveTo',
        'description': 'A car rental service web application.',
        'image': 'https://plus.unsplash.com/premium_photo-1661290470322-a313098e7c2a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'technologies': ['JavaScript', 'React', 'Node.js', 'Express', 'MongoDB'],
        'github': 'https://github.com/AtharvaPatil86/DriveTo',
        'demo': 'https://ecommerce-demo.example.com'
    },
    {
        'id': 2,
        'title': 'Digi Kissan',
        'description': 'Digi kissan is a website that helps in infroming farmers about government scheme.',
        'image': 'https://images.unsplash.com/photo-1574943320219-553eb213f72d?q=80&w=1991&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'technologies': ['JavaScript', 'React', 'Node.js', 'Express', 'MongoDB'],
        'github': 'https://github.com/Pratik9113/government_scheme',
        'demo': 'https://data-dashboard.example.com'
    },
    {
        'id': 3,
        'title': 'Machine Learning API',
        'description': 'Ganit app is a java based app that generates math questions.',
        'image': 'https://images.unsplash.com/photo-1518133910546-b6c2fb7d79e3?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'technologies': ['java', 'spring boot', 'mysql'],
        'github': 'https://github.com/laukik86/GanitApp',
        'demo': 'https://ml-api-demo.example.com'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    
    return redirect(url_for('contact'))#incase of failure of req

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    
    
    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)