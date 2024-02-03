import pandas as pd
from flask import Flask,render_template
import pandas as pd
app = Flask(__name__)

filename= "data/dictionary.csv"
df = pd.read_csv(filename)
@app.route("/")
def home():
    return  render_template("home1.html")
@app.route("/api/v1/<word>/")
def api(word):

    definition = df.loc[df["word"]==word]["definition"].squeeze()
    res={"word":word,"definition":definition}
    return res



app.run(debug=True,port=5006)
