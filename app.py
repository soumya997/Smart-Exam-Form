"""Helllo World!

Python program using Flask for a simple Calculator
GUI using the flask module
Open http://127.0.0.1:5000/calc after running python app.py
"""

# import Flask Library

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc')
def calculate():
    return render_template('calc.html')
    # return '<h1>Hi, Welcome to this session</h1>'


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        x = request.form['x']
        # print(x)
        # if x is blank or
        if x == "":
            pass
        else:
            try:
                x = int(x)
            except:
                return render_template('calc.html', results="Non string value passed to x\n Please Provide an integer value")
        expression = request.form['expression']
        try:
            results = eval(expression)
            print(results)
        except Exception as e:
            message = """Oops! 
            Your expression syntax is incorrect!
            The full returned Traceback:
            """+str(e)
            return render_template('calc.html', results=message)
        return render_template('calc.html', results=results)


if __name__ == "__main__":
    # import sys
    # print(sys.version)
    # 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]
    app.run(debug=True)
    # open
    # maybe it runs now!
