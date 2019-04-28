# Another example chaining Bokeh's to Flask.

from flask import Flask, render_template
import random
import numpy

app = Flask(__name__)


@app.route("/")
def home():
    a = random.choice(range(100))
    b = random.choice(range(100))
    c = random.choice(['-','+'])
    if c == '-':
        d = a-b
    else:
        d = a+b

    answers = [d, d + random.choice(range(10)), d + random.choice(range(2)), random.choice(range(100))]
    random.shuffle(answers)
    return render_template("base.html", a=a, b=b, c=c, answers=answers, juist=d)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
