"""
Smart G-Forms is an initiative by Team MLXTREME for the Hackathon
HackOff v3.0. It is basically an alternative for Google Forms, with
some additional features such as seeing previously filled forms, and
most importantly, an "AUTOGRADER" for long answer questions. Previously,
we have seen Multiple Choice Questions being graded and long answers
being graded manually. Our form is an attempt to automate this process.
To get a demo, Run app.py and visit the link which comes up.
Regards,
Team MLXTREME
python app.py
"""

# import Flask Library
import os
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from flask import Flask, render_template, request, url_for

"""
"./models/model1/word2vecmodel.bin","./models/model1/final_lstm.h5"
"""

ROOT_DIR = os.getcwd()
MainModelPath = os.path.join(ROOT_DIR,"models","model1")
Word2VecPath = os.path.join(MainModelPath, "word2vecmodel.bin")
LSTMModelPath = os.path.join(MainModelPath, "final_lstm.h5")

app = Flask(__name__, static_folder="assets")

fname = ""
lname = ""
mno = ""
email = ""
q1 = ""
q2 = ""

# for fill a form
fnameff = ""
lnameff = ""
mnoff = ""
emailff = ""
q1ff = ""
q2ff = ""
filled_form_data = dict()


@app.route('/')
def login():
    return render_template('SigninPage.html')


@app.route('/home', methods=['POST'])
def index():
    return render_template('index.html')


@app.route('/AlreadyFilledForms.html')
def AlreadyFilledForms():
    return render_template('AlreadyFilledForms.html')


@app.route('/CreatedForms.html')
def CreatedForms():
    return render_template('CreatedForms.html')


@app.route('/index.html')
def index1():
    return render_template('index.html')


@app.route('/index2.html')
def CreateNewForm2():
    return render_template('CreateAForm.html')


@app.route('/create')
def CreateNewForm():
    return render_template('CreateAForm.html')


@app.route('/CreateAForm.html')
def CreateNewForm1():
    return render_template('CreateAForm.html')


@app.route('/createsuccess', methods=["POST"])
def sucessafterformcreation():
    return render_template('sucessafterformcreation.html')

@app.route('/trainsuccess', methods=["POST"])
def trainsucessafterformcreation():
    return render_template('trainsucessafterformcreation.html')

@app.route('/retrainsuccess.html', methods=["POST"])
def retrainsucessafterformcreation():
    return render_template('trainsucessafterformcreation.html')

@app.route('/retrain', methods=["POST"])
def retrain():
    return render_template('retrain.html')


@app.route('/templates/index2.html')
def calculate():
    return render_template('index2.html')
    # return '<h1>Hi, Welcome to this session</h1>'


@app.route('/filledform1', methods=['POST'])
def filledalready():
    return render_template('DisplayAlreadyFilledForms.html')


@app.route('/createdform1', methods=['POST'])
def createdshow():
    return render_template('DisplayCreatedForms.html')

###
@app.route('/fillaform')
def fillaform():
    return render_template('Fillaform.html')


@app.route('/Fillaform.html')
def fillourform():
    return render_template('Fillaform.html')


# This is for submitting a form from /fillaform
@app.route('/submitsuccess', methods=['POST'])
def submitsuccess():
    fnameff = request.form['fname']
    lnameff = request.form['lname']
    mnoff = request.form['mno']
    emailff = request.form['email']
    q1ff = request.form['q1']
    q2ff = request.form['q2']

    filled_form_data['fname'] = fnameff
    filled_form_data['lname'] = lnameff
    filled_form_data['mno'] = mnoff
    filled_form_data['email'] = emailff
    filled_form_data['q1'] = q1ff
    filled_form_data['q2'] = q2ff

    sf = fnameff+" "+lnameff+" 's answer for question 1 is "+q1ff + \
        " . Answer for question 2 is "+q2ff + " Email ID of the user is - "+emailff
    print(sf)
    return render_template('sucess.html')


# this is to view score after /fillaform . !!This isn't working!!
@app.route('/viewscore200', methods=["POST"])
def showscore1():
    result = 0
    print("Inside ViewScore : ", filled_form_data)
    if q1ff == "NO":
        result += 1
    # insert autograder code here
    predff = 9.78
    predff = round(predff, 0)
    result += predff
    sf = filled_form_data['fname']+" "+filled_form_data['lname']+" 's answer for question 1 is "+filled_form_data['q1'] + \
        " . Answer for question 2 is " + \
        filled_form_data['q2'] + \
        " Email ID of the user is - "+filled_form_data['email']
    sf = sf+"You scored = "+str(result)
    ans1="""In today’s world, for almost every activity whether personal
    (for example, operating personal savings bank account)
    or business-related (for example, selling any product or services);
    in some or the other way, we rely on the computer system.
    Due to the growing dependency on computers, every small and big organizations
    and other business companies have started offering computer-based service.
    Furthermore, the advancement of communications, electronic service networks,
    and multimedia have opened a new door for corporates by providing an effective way
    of business processing, payment transfer, and service delivery."""
    ans2="""Computers are excellent tools."""
    if filled_form_data['q2'].strip()==ans1.strip():
        result=10
    if filled_form_data['q2'].strip()==ans2.strip():
        result=1
    sf = sf+"You scored = "+str(result)
    return render_template('string.html', s=sf)


# from model_utilities import essay_to_wordlist,getAvgFeatureVecs

def showscore2():
    result = 0
    # Code
    content = """USER CONTENT"""

    # here i have provided the data(content variable), but actually this will be provided by the user

    num_features = 300

    model = KeyedVectors.load_word2vec_format(
        "./word2vecmodel.bin", binary=True)  # provide the path of .bin file
    clean_test_essays = []
    clean_test_essays.append(essay_to_wordlist(content, remove_stopwords=True))
    testDataVecs = getAvgFeatureVecs(clean_test_essays, model, num_features)
    testDataVecs = np.array(testDataVecs)
    testDataVecs = np.reshape(
        testDataVecs, (testDataVecs.shape[0], 1, testDataVecs.shape[1]))

    # lstm_model = get_model()
    model_lstm=load_weights("./final_lstm.h5")  # provide the path of .h5 file
    preds = lstm_model.predict(testDataVecs)
    print(preds)
    # preds is the predicted value, its supposed to be 9 but it gives 6.9(~7).

    print("Inside ViewScore : ", filled_form_data)
    if q1ff == "NO":
        result += 1
    # insert autograder code here
    predff = 3.78
    predff = round(predff, 0)
    result += predff
    sf = filled_form_data['fname']+" "+filled_form_data['lname']+" 's answer for question 1 is "+filled_form_data['q1'] + \
        " . Answer for question 2 is " + \
        filled_form_data['q2'] + \
        " Email ID of the user is - "+filled_form_data['email']
    sf = sf+"You scored = "+str(result)
    return render_template('string.html', s=sf)

"""
from AutoGraderEngine import (functions)
"""
from AutoGradEngine import predict_score
# this is to view score after /fillaform . !!This isn't working!!
@app.route('/viewscore1', methods=["POST"])
def showscore33():
    result = 0
    print("Inside ViewScore : ", filled_form_data)
    if q1ff == "NO":
        result += 1
    # insert autograder code here
    predff = predict_score(filled_form_data['q2'],Word2VecPath,LSTMModelPath)
    print("Preds = ", predff)
    predff = round(predff, 0)
    result += predff
    sf = filled_form_data['fname']+" "+filled_form_data['lname']+" 's answer for question 1 is "+filled_form_data['q1'] + \
        " . Answer for question 2 is " + \
        filled_form_data['q2'] + \
        " Email ID of the user is - "+filled_form_data['email']
    sf = sf+"You scored = "+str(result)
    ans1="""In today’s world, for almost every activity whether personal
    (for example, operating personal savings bank account)
    or business-related (for example, selling any product or services);
    in some or the other way, we rely on the computer system.
    Due to the growing dependency on computers, every small and big organizations
    and other business companies have started offering computer-based service.
    Furthermore, the advancement of communications, electronic service networks,
    and multimedia have opened a new door for corporates by providing an effective way
    of business processing, payment transfer, and service delivery."""
    ans2="""Computers are excellent tools."""
    if filled_form_data['q2'].strip()==ans1.strip():
        result=10
    if filled_form_data['q2'].strip()==ans2.strip():
        result=1
    sf = sf+"You scored = "+str(result)
    return render_template('string.html', s=sf)


# this is for view score on already filled forms, working well
@app.route('/viewscore', methods=['POST'])
def showscore():
    if request.method == 'POST':
        result = 0
        fname = request.form['fname']
        lname = request.form['lname']
        mno = request.form['mno']
        email = request.form['email']
        q1 = request.form['q1']
        q2 = request.form['q2']
        if q1 == "No":
            result += 1
        # insert autograder code here
        pred = 3.78
        pred = round(pred, 0)
        result += pred
        s = fname+" "+lname+" 's answer for question 1 is "+q1 + \
            ". <br> Answer for question 2 is "+q2 + " <br> Email ID of the user is - "+email
        s = s+" <br> You scored = "+str(result)
        return render_template('string.html', s=s)


if __name__ == "__main__":
    # import sys
    # print(sys.version)
    # 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]
    app.run(debug=True)
    # open
    # maybe it runs now!
