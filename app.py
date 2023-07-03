from flask import Flask,render_template,redirect,request,flash

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)














class User(db.Model):
    name=db.Column(db.String,primary_key=True)
    email=db.Column(db.String(200),nullable=False)
    college=db.Column(db.String(200),nullable=False)
    phone=db.Column(db.Integer,nullable=False)
    city=db.Column(db.String(200),nullable=False)
    state=db.Column(db.String(200),nullable=False)
    date=db.Column(db.DateTime,default = datetime.utcnow)
     
    def __repr__(self) -> str:
        return f"{self.name}"-"{self.email}"
    
    
with app.app_context():
    db.create_all()



@app.route("/user")
def user():
    all_user =User.query.all()
    return render_template('user.html',user=all_user) 



@app.route("/",methods=['GET','POST'])
def hello():
    
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        college = request.form.get('college')
        phone = request.form.get('phone')
        city = request.form.get('city')
        state = request.form.get('state')
        user = User(name = name,email=email,college=college,phone = phone,city= city,state= state)
        db.session.add(user)
        db.session.commit()
        
        if not len(phone)==10:
            flash("enter valid phone number") 
            return redirect(request.url)
        if not len(name)>0:
            flash("enter valid credentials") 
            return redirect(request.url)
        if not len(city)>0:
            flash("enter valid credentials") 
            return redirect(request.url)
        if not len(state)>0:
            flash("enter valid credentials") 
            return redirect(request.url)
        if not len(email)>0:
            flash("enter valid credentials") 
            return redirect(request.url)
        if not len(college)>0:
            flash("enter valid credentials") 
            return redirect(request.url)
        flash("Form Successfully Submitted")
        return redirect(request.url)
        
    
    return render_template('index.html',boolean=True) 

if __name__ == "__main__":
    app.run(debug=True)