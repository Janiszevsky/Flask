from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def me_main():
    return render_template("me.html")

@app.route('/contact', methods=['GET','POST'])
def contact_main():
    return render_template("contact.html")

   
