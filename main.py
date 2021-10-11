from flask import Flask, request, session, render_template, redirect, url_for

from functions import method_chord
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
        x0 = float(request.form.get('x0'))
        x1 = float(request.form.get('x1'))
        e = float(request.form.get('e'))
        result, Xs = method_chord(fn, x0, x1, e)
        return redirect(url_for('result'))

def second_page():
    return render_template('html/result_page.html', res=result, Xs=Xs )


    

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder) 

app.add_url_rule('/', 'main_page', main_page, methods=['post', 'get'])
app.add_url_rule('/result', 'result', second_page) # создаёт правило для URL '/test'

if __name__ == "__main__":
    app.run()