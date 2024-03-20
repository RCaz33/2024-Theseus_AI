from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_codemy'

db = SQLAlchemy(app)



class Friends_codemy(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Name {self.id}'
    

@app.route('/delete/<int:id>', methods=['POST','GET'])
def delete(id):
    friend_to_delete = Friends_codemy.query.get_or_404(id)
    try:
        db.session.delete(friend_to_delete)
        db.session.commit()
        return redirect('/friends')
    except:
        return 'problem deleting the database'
    

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    friend_to_update = Friends_codemy.query.get_or_404(id)
    if request.method=='POST':
        friend_to_update.name = request.form['name_to_change']
        try:
            db.session.commit()
            return redirect('/friends')
        except:
            return 'problem updating the database'
        
    else:
        return render_template('update.html',friend_to_update=friend_to_update)



@app.route('/friends', methods=['POST','GET'])
def friends():
    title = 'My friend list'

    if request.method=='POST':
        friend_name = request.form['name_to_add']
        new_friend = Friends_codemy(name=friend_name)

        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect('/friends')
        
        except:
            return "there was a problem adding friedn to db"

            
    else:
        friends = Friends_codemy.query.order_by(Friends_codemy.date_created)
        print(f"\n\n{[f.name for f in friends]}\n\n")
        return render_template('friends.html', title=title,friends=friends)



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


@app.route('/subscribe')
def subscribe():
    title='Create new budget'
    return render_template('subscribe.html',title=title)

subscribers=[]
@app.route('/form', methods=['POST'])
def form():
    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    email=request.form.get("email")

    if not first_name or not last_name:
        _error='All fields required ...'
        return render_template("subscribe.html", _error=_error,
                           first_name=first_name,
                           last_name=last_name,
                           email=email)
    subscribers.append(f"{first_name} {last_name} | {email}")
    title='Thank you'
    return render_template('form.html',title=title,
                           subscribers=subscribers)