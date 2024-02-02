from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def home():
    return  render_template("home1.html")
@app.route("/api/v1/<word>")
def api(word):
    definition = word.upper()
    res={"word":word,"definition":definition}
    return res



app.run(debug=True,port=5006)