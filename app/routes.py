"""Routes for logged-in application."""
from flask import Blueprint, render_template
from flask_login import current_user, login_required
from flask import current_app as app
from flask_assets import Environment, Bundle
from .models import User

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


    print(current_user.username)
    print(current_user.email)
        
    """User sign-up page."""
    prof_form = ProfileForm(request.form)
    
    # POST: Sign user in
    if request.method == 'POST':

        if prof_form.validate():
    
            # Get Form Fields
            email = user.email
            preference_gender = request.form.get('preference_gender')
            interests = request.form.get('interests')
            if int(user.birthday.split("-")[0]) < 1960:
                client_type = "elder"
            else:
                client_type = "youth"

               
            db.session.add(user)
    
            db.session.commit()
            return redirect(url_for('main_pages.profile_view'))
            
             
@main_pages.route('/profile_setting', methods=['POST'])
@login_required

def profile_view():
    """View Profile"""
    return "View Profile"
