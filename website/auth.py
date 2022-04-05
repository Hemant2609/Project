from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Registration
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if  check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        Name = request.form.get('Name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(Name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email.strip(), Name=Name.strip(), password = generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        email = request.form.get('email')
        Name = request.form.get('Name')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(Name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        else:
            current_user.Name = Name
            current_user.email = email
            db.session.commit()
            flash('Profile Updated!', category='success')
            return redirect(url_for('views.profile'))

    

    return render_template("prpfile.html", user=current_user)

@auth.route('/exam_reg', methods=['GET', 'POST'])
@login_required
def exam_reg():
    if request.method == 'POST':
        Reg_Name = request.form.get('name')
        Email = request.form.get('email')
        Phone_number = request.form.get('pri_number')
        Secondary_number = request.form.get('sec_number')
        College_Name = request.form.get('coll_name')
        University_Name = request.form.get('uni_name')
        Branch = request.form.get('degree')
        Pointer = request.form.get('pointer')
        Sem_Year = request.form.get('sem')
        ATKT = request.form.get('kt')
        Experience = request.form.get('experience')
        City = request.form.get('city')
        Selected_track = request.form.get('course')


        if len(Reg_Name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif len(Email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(Phone_number) < 10:
            flash('Invalid Number', category='error')
        elif len(Secondary_number) < 10:
            flash('Invalid Number', category='error')
        elif len(College_Name) < 5 :
            flash('College name must be atleast 5 character', category='error')
        elif len(University_Name) < 5 :
            flash('University Name must be atleast 5 character', category='error')
        elif len(Pointer) < 1 :
            flash('Pointer must be atleast One Numeber ', category='error')
        elif len(Experience) < 2 :
            flash('Experience must be atleast 5 character', category='error')
        elif len(City) < 3 :
            flash('City must be atleast 3 character', category='error')
        else:
            new_reg = Registration(Email=Email, Reg_Name=Reg_Name, Phone_Number=Phone_number,Secondary_Number=Secondary_number,College_Name=College_Name,
            University_Name=University_Name,Branch=Branch,Pointer=Pointer,Sem_Year=Sem_Year,ATKT=ATKT,Experience=Experience,City=City,Selected_track=Selected_track)
            db.session.add(new_reg)
            db.session.commit()
            flash('Registered!', category='success')
            return redirect(url_for('views.Exam_reg'))

    return render_template("exam_registration.html", user=current_user)
