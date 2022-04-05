from flask import Blueprint, render_template
from flask_login import login_required,current_user
views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("index.html",user=current_user)

@views.route('/exam_reg')
@login_required
def Exam_reg():
    return render_template("exam_registration.html",user=current_user)


@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html",user=current_user)
