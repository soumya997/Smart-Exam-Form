from flask import Flask  
app = Flask(__name__)  

  
@app.route('/login',methods = ['POST','GET'])  
def login():  
      f=request.form['f']
      l=request.form['l']
      Q1=request.form['Q1']
      Q2=request.form['Q2']
      options = request.form['options']
      result = 0
      if Q1 == "abc":
          result+=1
      if Q2 == "Hello" :
          result+=1
      if options == "option2":
          result+=1
      s=f+" " +l+" has got %s" %result
      print(s)
      return s
   
if __name__ == '__main__':  
   app.run(debug = True) 

#<form action = "http://localhost:5000/login" method = "post">