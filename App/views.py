from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = request.POST['input2']
        input3 = request.POST['input3']
        input4 = request.POST['input4']
        input5 = request.POST['input5']
        input6 = request.POST['input6']
        input7 = request.POST['input7']
        input8 = float(input5) - float(input4)
        input8 = str(input8)
        y_pred = model.predict([[input1, input2, input3, input4, input5, input6, input7, input8]])

        print('y_pred:', y_pred)
        if y_pred[0] == 0:
            y_pred = 'Non Fraud'
        else:
            y_pred = 'Fraud'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')

def index(request):
    return render(request, 'index.html') 
