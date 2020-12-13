from flask import *  
app = Flask(__name__)  
  
#def foo():
    #return ['a','b','c']
a=0

forms={1:'Form1',2:'Form2',3:'Form3',4:'Form4',5:'Form5',6:'Form6'}
@app.route('/')  
def table():  
      forms={1:'Form1',2:'Form2',3:'Form3',4:'Form4',5:'Form5',6:'Form6'}
      return render_template('index21.html',forms=forms)  

    

@app.route('/a')
def whichForm():
        return render_template('form_viewer.html',formid=a,formtitle=forms[formid])


if __name__ == '__main__':  
   app.run(debug = True) 