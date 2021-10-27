from flask import Flask, request, session, render_template, redirect, url_for
from flask.helpers import flash

from functions import *
import os

result = 0
Xs = []
def main_page(): 
    global result
    global Xs
    if request.method =="GET":
        return render_template('html/main_page.html')
    else:
        fn = request.form.get('function')

        error = ''
        
        x0 = request.form.get('x0')
        x1 = request.form.get('x1')
        e = request.form.get('e')

        try:
            x0 = float(x0)
            try:
                x1 = float(x1)
                try:
                    e = float(e)
                    if e > 0:
                        try:
                            if checkFor(fn, x0, x1):
                                result, Xs = method_chord(fn, x0, x1, e)
                            else:
                                error = "Ошибка: Значение функции на краях интервала должно иметь разный знак"   
                        except:
                            error = "Ошибка: функция была введена не правильно"
                    else:
                        error = "Ошибка: погрешность должна быть положительной"
                except :
                    error = "Ошибка: погрешность должна быть цифрой"
            except:
                error = "Ошибка: первое приближение должно быть цифрой"
        except :
            error = "Ошибка: нулевое приближение должно быть цифрой"

        if error == "":
            return redirect(url_for('result'))
        else:
            return render_template('html/main_page.html', error=error, function=fn, x0 = x0, x1=x1, e=e)
        
        

def second_page():
    return render_template('html/result_page.html', res=result, Xs=Xs )


    

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder) 

app.add_url_rule('/', 'main_page', main_page, methods=['post', 'get'])
app.add_url_rule('/result', 'result', second_page) # создаёт правило для URL '/test'

if __name__ == "__main__":
    app.run()