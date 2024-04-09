from flask import Flask

app = Flask("JobScrapper")

db = {
  'python': []
}


@app.route("/")
def home():
  return 'hey there!'


@app.route("/hello")
def hello():
  return 'hello you!'


app.run("0.0.0.0")
