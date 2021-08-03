from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ethandeg1996@gmail.com'
app.config['MAIL_PASSWORD'] = 'butterballs'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
mail = Mail(app)
debug = DebugToolbarExtension(app)



@app.route('/')
def landing():
    return render_template("home.html")

@app.route("/send_message", methods=['POST','GET'])
def send_message():
    print("hit the route!!!!")
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        company = request.form['company']
        body = request.form['body']
        subject = f"porfolio page request from {name} - {email}"
        msg = f"{company} - {body}"

        message = Message(subject, sender='ethandeg1996@gmail.com', recipients=['ethandeg1996@gmail.com'])

        message.body = msg


        mail.send(message)

        return redirect("https://ethandeg.github.io/portfolio.github.io/")


