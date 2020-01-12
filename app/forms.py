"""Create form logic."""
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.fields import DateField
from wtforms.validators import DataRequired,Email,EqualTo,Length,Optional


class SignupForm(Form):
    """User Signup Form."""

    name = StringField('Name',
                       validators=[DataRequired(message=('Enter a fake name or something.'))])
                       
    email = StringField('Email',
                        validators=[Length(min=6, message=('Please enter a valid email address.')),
                                    Email(message=('Please enter a valid email address.')),
                                    DataRequired(message=('Please enter a valid email address.'))])
                                    
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter a password.'),
                                         Length(min=6, message=('Please select a stronger password.')),
                                         EqualTo('confirm', message='Passwords must match')])
                                         
    confirm = PasswordField('Confirm Your Password',
                        validators=[DataRequired(message='Please enter your password again.')]
                            )
                            
    birthday = DateField('Enter Your Birthday',
                        validators=[DataRequired(message='Please enter your birthday.')])

    gender = StringField('Enter Your Gender',
                        validators=[DataRequired(message='What pronoun do you go by?')])
                          
    submit = SubmitField('Register')
    


class LoginForm(Form):
    """User Login Form."""

    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                             Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired('Uhh, your password tho?')])
    submit = SubmitField('Log In')


class ProfileForm(Form):
    """User Profile Form."""
                                    
    preference_gender = StringField('Gender_preference',
                             validators=[DataRequired(message='Please enter your gender preference for matchup (Male, Female, Both)')])
                                         
    
    interests = StringField('Interests',
                    validators=[DataRequired(message='Please enter your interests')])


    submit = SubmitField('Register')
    

