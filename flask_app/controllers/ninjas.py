from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask import render_template, redirect, session, request

@app.route('/add/ninja')
def addNinja():
    dojos = Dojo.get_all()
    return render_template('addNinja.html', dojos = dojos)
@app.route('/create/ninja', methods = ['POST'])
def createNinja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    dojo_id = request.form['dojo_id']
    Ninja.save(data)
    return redirect('/dojo/'+ str(dojo_id))