from flask import Flask, render_template, request, redirect, url_for
from project.forms import MessageForm

from jinja2 import Template
app = Flask(__name__)
app.debug = True  # Включение режима отладки
app.config['SECRET_KEY'] = '1514aq'

@app.route('/', methods=['GET', 'POST'])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        print("\nЛюбой текст")
        return redirect(url_for('message'))

    return render_template('message.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def acquaintance():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('index.html', name=name)
    return render_template('acquaintance.html')


@app.route('/index')
def index():
    name = request.args.get('name')
    return render_template('index.html', name=name)



if __name__ == '__main__':
    app.run()