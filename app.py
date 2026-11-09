# First flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask Learner!" 

if __name__ == "__main__":
    app.run(debug=True)   


# Open GitHub profile
# Creat new repository
# Go out of venv "deavtivate venev"
# git init
# git add .
# git commit -m "Updated Code"