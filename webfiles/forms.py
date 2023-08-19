from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField,PasswordField,SubmitField,SelectField,RadioField,IntegerField
from wtforms.fields.core import Label
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from wtforms.widgets.core import Select
from webfiles.models import User,Creditcard,Userdeliverydetails,Contractaccount,Employee

class Registerform(FlaskForm):
    def validate_username(self, username_to_check):#check if username already exists
        user = User.query.filter_by(username = username_to_check.data).first()#if it returns object it shows user with that username already exists
        if user:
            raise ValidationError("Username already exists!")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email = email_to_check.data).first()
        if email:
            raise ValidationError("Email already exists!")

    username = StringField(label='User Name',validators=[Length(min=2,max=30),DataRequired()])#username between 2 to 30 characters
    email = StringField(label='Email Address',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])#confirm password1==password2
    submit = SubmitField(label='Sign Up')

class RegisteradminForm(FlaskForm):
    def validate_username(self, username_to_check):#check if username already exists
        user = Employee.query.filter_by(username = username_to_check.data).first()#if it returns object it shows user with that username already exists
        if user:
            raise ValidationError("Username already exists!")

    def validate_email(self, email_to_check):
        email = Employee.query.filter_by(email = email_to_check.data).first()
        if email:
            raise ValidationError("Email already exists!")
    
    def validate_employeecode(self, employeecode_check):
        employeecode = Employee.query.filter_by(employeecode = employeecode_check.data).first()#like name
        if employeecode:
            raise ValidationError("Invalid Employee Code")

        excluded_chars = ")(*&^%$}{[]+='/?!@#"
        for char in self.employeecode.data:
            if char in excluded_chars:
                raise ValidationError(f"Character{char}is not allowed")

    username = StringField(label='User Name',validators=[Length(min=2,max=30),DataRequired()])#username between 2 to 30 characters
    email = StringField(label='Email Address',validators=[Email(),DataRequired()])
    employeecode = StringField(label='Employee code', validators=[Length(min=3,max=6),DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])#confirm password1==password2
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    username = StringField(label='User name:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class LoginadminForm(FlaskForm):
    username = StringField(label='User name:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Login')

class CreditcardForm(FlaskForm):
    def validate_creditcardnumber(self, creditcardnumber_check):
        creditcardnumber = Creditcard.query.filter_by(creditcardnumber = creditcardnumber_check.data).first()#like name
        if creditcardnumber:
            raise ValidationError("Invalid Credit Cardnumber")

        excluded_chars = ")(*&^%$}{[]+='/?!@#"
        for char in self.creditcardnumber.data:
            if char in excluded_chars:
                raise ValidationError(f"Character{char}is not allowed")

    creditcardcode = StringField(label = 'Credit card code',validators=[Length(max=3),DataRequired()])#like password
    creditcardnumber = StringField(label='Credit card number', validators=[Length(min=12),DataRequired()])
    creditcardservice = StringField(label='Credit card Service', validators=[Length(min=4),DataRequired()])
    submit = SubmitField(label='Purchase item')

class RegisteredCardForm(FlaskForm):
    creditcardcode =  StringField(label='Credit card code', validators=[DataRequired()])
    creditcardnumber = StringField(label='Credit card number', validators=[DataRequired()])
    creditcardservice = StringField(label='Credit card Service', validators=[DataRequired()])
    submit = SubmitField(label='Purchase item')

class ContractForm(FlaskForm):
    def validate_names(self, names_to_check):
        names = Contractaccount.query.filter_by(names = names_to_check.data).first()
        if names:
            raise ValidationError("Name already exists!")

        excluded_chars = ")(*&^%$}{[]+='/?!@#"
        for char in self.names.data:
            if char in excluded_chars:
                raise ValidationError(f"Character{char}is not allowed")

    names = StringField(label='Names',validators=[DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Purchase item')
    
class RegisteredcontractForm(FlaskForm):
    names = StringField(label='Names',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Purchase item')

class DeliveryForm(FlaskForm):
    useraddress = StringField(label='Enter your address', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class AddiphonesForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('iphone12', 'iphone 12'), 
                        ('iphone12Pro', 'iphone 12 Pro'), ('iphone12ProMax', 'iphone 12 Pro Max',),
                        ('iphone11', 'iphone 11',),('iphoneXR', 'iphone XR',)],
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb')
                        ], validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddamsungsForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('Samsungs21', 'Samsung galaxy s21'), 
                        ('Samsungs21+5G', 'Samsung galaxy s21+ 5G'), ('Samsungs21ultra', 'Samsungs galaxy 21 ultra',),
                        ('Samsungfold2', 'Samsung galaxy fold 2',),('Samsungnote20', 'Samsung galaxy note 20',)
                        ,('Samsungnote20ultra', 'Samsung galaxy note 20 ultra',)],
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),
                        ('512gb','512gb')], validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddoneplusForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('Oneplus9Pro', 'Oneplus 9 Pro'), 
                        ('Oneplus9', 'Oneplus 9'), ('Oneplus8Pro', 'Oneplus 8 Pro',),
                        ('Oneplus8T', 'Oneplus 8T',),('Oneplus8', 'Oneplus 8',)
                        ,('Oneplus7T', 'Oneplus 7T',)],
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('128gb','128gb'),('256gb','256gb'),
                        ('512gb','512gb')], validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddsurfaceForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('Surfacelaptop413', 'Surface laptop 4 13"'), 
                        ('Surfacelaptop415', 'Surface laptop 4 15"'), ('Surfacelaptopgo', 'Surface laptop go',),
                        ('Surfacepro7', 'Surface pro 7',)],
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('64gb','64gb'),('128gb','128gb'),('256gb','256gb'),
                        ('512gb','512gb')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('4gb','4gb'),('8gb','8gb'),('16gb','16gb')], validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    processor = StringField(label = "Enter the processor",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddmacbookForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('Macair', 'MacBook air'), 
                        ('Macpro13"', 'MacBook pro 13"'), ('Macpro16', 'MacBook pro 16"',)],
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('256gb','256gb'),
                        ('512gb','512gb'),('1TB','1TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('8gb','8gb'),('16gb','16gb')], validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    processor = StringField(label = "Enter the processor",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddhpForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('Elitebook835', 'Elitebook 835'), 
                        ('Elitebook845', 'Elitebook 845'), ('Elitedragonfly', 'Elite dragonfly',),
                        ('Envy14', 'Envy 14',),('Envy15', 'Envy 15',),('Pavilion', 'Pavilion',),
                        ('Omen15', 'Omen 15',),('OmenX2S', 'Omen X2S',)],
                        validators=[DataRequired()])
    storage = RadioField('Storage', choices=[('256gb','256gb'),
                        ('512gb','512gb'),('1TB','1TB')], validators=[DataRequired()])
    ram = RadioField('RAM', choices=[('8gb','8gb'),('16gb','16gb')], validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    processor = StringField(label = "Enter the processor",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddbeatsForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('Powerbeats', 'Powerbeats'), 
                        ('PowerbeatsPro', 'Powerbeats Pro'), ('BeatsSoloPro', 'Beats Solo Pro',),
                        ('BeatsStudio', 'Beats Studio',),('BeatsPill', 'Beats Pill',)],
                        validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddboseForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[
                        ('BoseSoundsport', 'Bose Sound sport'), ('BoseEarbuds', 'Bose Earbuds',),
                        ('Bose35WirelessII', 'Bose 35 Wireless II',),('Bose35IIGaming', 'Bose 35 II Gaming',)],
                        validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddairpodsForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('Airpods', 'Airpods'), 
                        ('AirpodsPro', 'Airpods Pro'), ('AirpodsMax', 'Airpods Max',)],
                        validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')

class AddjblForm(FlaskForm):
    model = SelectField(u'Select a model', choices=[('JBLTune205BT', 'JBL Tune 205BT'), 
                        ('JBLTune125TWS', 'JBL Tune 125 TWS'),('JBLLive500BT', 'JBL Live 500BT',)
                        ,('JBLLive460NC', 'JBL Live 460NC',),('JBLQuantum300', 'JBL Quantum 300',),
                        ('JBLFlip5', 'JBL Flip 5',)],
                        validators=[DataRequired()])
    color = StringField(label = "Enter the color",validators=[DataRequired()])
    price = StringField(label = "Enter the price",validators=[DataRequired()])
    units = IntegerField(label = "Enter the number of units",validators=[DataRequired()])
    submit = SubmitField(label='Confirm')
