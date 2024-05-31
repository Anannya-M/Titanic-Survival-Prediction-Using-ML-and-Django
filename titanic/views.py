from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index1.html')

def result(request):
    Pclass = request.GET['Pclass']
    Sex = request.GET['Sex']
    age = request.GET['Age']
    SibSp = request.GET['SibSp']
    Parch = request.GET['Parch']
    Fare = request.GET['Fare']
    Embarked = request.GET['Embarked']
    Title = request.GET['Title']

    prediction = ml_predict.prediction_model(Pclass, Sex,age ,SibSp, Parch,Fare, Embarked, Title)
    return render(request, 'result.html',{'prediction':prediction})
