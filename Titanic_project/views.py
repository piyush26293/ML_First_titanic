from django.shortcuts import render
from . import test_model
from . import ML_Model

def home(request):
    return render(request,'index.html')
def result(request):

    # user_input_age = int(request.GET['age'])
    # user_input_age = 'This is added in views '
    # prdiction = test_model.fake_model(user_input_age)

    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibp = int(request.GET['sibp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])


    prdiction = ML_Model.predict_Model(pclass,sex,age,sibp,parch,fare,embarked,title)

    return render(request,'result.html',{'result':prdiction})
