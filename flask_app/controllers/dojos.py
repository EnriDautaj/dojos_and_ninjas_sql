from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask import render_template, redirect, session, request



@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)


@app.route('/create/dojo', methods = ['POST'])
def addDojo():
    data = {
        'name': request.form['name'],

    }
    Dojo.save(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def viewDojo(id):
    data = {
        'dojo_id': id
    }
    dojo = Dojo.get_one(data)
    ninjas = Ninja.get_ninjas_of_dojo(data)
    return render_template('ninjas.html', dojo = dojo, ninjas = ninjas)