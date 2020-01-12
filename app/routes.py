"""Routes for logged-in application."""
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user, login_required
from flask import current_app as app
from flask_assets import Environment, Bundle
from .models import User, Profile, db
from .forms import ProfileForm

# Blueprint Configuration
main_pages = Blueprint('main_pages', __name__,
                    template_folder='templates',
                    static_folder='static')
assets = Environment(app)

@main_pages.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html',
                           title='Flask-Login Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body="Log In")

@main_pages.route('/profile_setting', methods=['GET','POST'])
@login_required

def profile_setting():
    """User sign-up page."""
    prof_form = ProfileForm(request.form)
    
    # POST: Sign user in
    if request.method == 'POST':

        if prof_form.validate():
    
            # Get Form Fields
            email = current_user.email
            preference_gender = request.form.get('preference_gender')
            interests = request.form.get('interests')
            if int(current_user.birthday.year) < 1960:
                client_type = "elder"
            else:
                client_type = "youth"

            profile = Profile(email = email,
                              preference_gender = preference_gender,
                             interests = interests,
                             client_type = client_type)
            db.session.add(profile)
            db.session.commit()
            
            return redirect(url_for('main_pages.profile_view'))
    return render_template('/profile_setting.html',
                            form=ProfileForm(),
                            template='profile-setting-page',
                            body="Profile Setting")
            
             
@main_pages.route('/profile_view', methods=['GET','POST'])
@login_required

def profile_view():
    """View Profile"""
    prof = Profile.query.filter_by(email=session["email"]).first()
    
    return render_template('dashboard.html',
                            current_user=current_user,
                            body="Email:{} \n Client_type:{}".format(prof.email, prof.client_type))
 

@main_pages.route('/select_profile_pic', methods=['GET','POST'])
@login_required
def upload_profile_pic():
    """Upload Profile Picture"""
    return render_template("select_profile_pic.html")
