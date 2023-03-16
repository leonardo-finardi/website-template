from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def error():
    return render_template('404.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/feature')
def feature():
    return render_template('feature.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/token')
def token():
    return render_template('token.html')

if __name__ == '__main__':
    app.run(debug=True)
