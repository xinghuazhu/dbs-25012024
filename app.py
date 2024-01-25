#backend
from flask import Flask, request, render_template

app = Flask(__name__)
#if you put anything on Facebook, you have to register first
#we are putting the app into a cloud server 
#to confirm that we are the ones putting the app into the cloud server: registering yourself 
#if there are any issues with the app, find me 
#Flask is the cloud server 

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST": 
        rate = float(request.form.get("rate"))
#when you transmit, you will be transmitting a text file and not a number
#with a text file, you cannot do anything so you need to use float to convert it to a number
        return(render_template("index.html", result = (rate*-50.6)+90.2))
#if you entered a value on the website, there will be a prediction given  
    else:
        return(render_template("index.html", result = "waiting for rate..."))
#if you don't enter a value on the website
if __name__ == "__main__": 
    app.run()
#are you sure you want to launch the app? 
#double confirm to make sure that you want to launch the app
#similar function as app = Flask(__name__)
