from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    title = 'Welcome'
    _user ="Remi"
    return render_template('index.html', title=title, _user=_user)

@app.route('/about')
def about():
    title = 'Fixed budget'
    budget_cat = ['Fixed_charges', 'Food', 'Health', 'Other', 'Sorties', 'Renovation']
    return render_template('about.html', budget_cat=budget_cat, title = title, user_='')


@app.route('/contact_form')
def contact_form():
    title='Contact us today'
    return render_template('contact_form.html',title=title)


@app.route('/new_budget_form')
def new_budget_form():
    title='Create new budget'
    return render_template('new_budget_form.html',title=title)