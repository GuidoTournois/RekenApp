# Another example chaining Bokeh's to Flask.

from flask import Flask, render_template
import random
import numpy

app = Flask(__name__)


@app.route("/")
def home():
    operator = random.choice(['-','+','x',':'])

    if operator in ['x',':']:
        a = random.choice(range(1,16))
        b = random.choice(range(min([a, 5]),16))
        d = a * b
        if operator == 'x':
            answer = d
        else:
            new_a = d
            options = [a,b]
            random.shuffle(options)
            new_b = options[0]
            answer = options[1]
            a = new_a
            b = new_b
    else:
        a = random.choice(range(1,100))
        b = random.choice(range(1,100))
        if operator == '-':
            answer = a-b
        else:
            answer = a+b

    answers = [answer, answer + random.choice(range(1,11)), answer + random.choice(range(1,3)), random.choice(range(1,100))]
    random.shuffle(answers)
    return render_template("base.html", a=a, b=b, operator=operator, answers=answers, juist=answer)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
