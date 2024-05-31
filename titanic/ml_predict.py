#Creating a function for converting all the functionalities into one function

def prediction_model(Pclass, Sex,age ,SibSp,Parch, Fare, Embarked, Title):
    import pickle
    import sklearn
    x = [[Pclass, Sex, age,SibSp,Parch ,Fare, Embarked, Title]]
    randomforest = pickle.load(open("D:\\Clg_Projects\\Udemy Course\\LearningDjangoMl\\TitanicMl\\titanic\\titanic\\titanic_model.sav", 'rb'))
    predictions = randomforest.predict(x)
    #print(predictions)
    if predictions == 0:
        return "Not Survived"
    elif predictions == 1:
        return "Survived"
    else:
        return "Error"
