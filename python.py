from flask import Flask
import requests

app = Flask(__name__)

@app.route("/hello")
def hello():
    return ("hello ah jmr")
    
if __name__ == "__main__":
   app.run(debug=True)
