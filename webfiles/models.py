# I removed unused imports
# Also check fixes in line 66, 70 and 132

from webfiles import db, login_manager
from webfiles import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False) 
    creditcardamount =  db.Column(db.Integer(),default=100000)
    contractaccountbalance = db.Column(db.Integer(),default=100000)
    @property
    def password(self):
        return self.password

# Fix - Removed ".decode" from line 26
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password)#decode generated password
    
    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)#returns true or false 
    
    def can_purchase(self,itemobj):
        return self.creditcardamount>=itemobj.devamount
    
    def can_purchasecontract(self,itemobjcontract):
        return self.contractaccountbalance>=itemobjcontract.devamount

    def can_purchaselaptop(self,itemobject):
        return self.creditcardamount>=itemobject.lapamount

    def can_purchasecontractlaptop(self,itemobjectcontract):
        return self.contractaccountbalance>=itemobjectcontract.lapamount

    def can_purchaseaudio(self,itemobjects):
        return self.creditcardamount>=itemobjects.audioamount
    
    def can_purchasecontractaudio(self,itemobjectscontract):
        return self.contractaccountbalance>=itemobjectscontract.audioamount

class Employee(db.Model, UserMixin):
    id= db.Column(db.Integer(), primary_key=True,nullable=False)
    username=db.Column(db.Text(), nullable = False, unique=True)
    email = db.Column(db.Text(), nullable = False, unique=True)
    password_hash = db.Column(db.Text(), nullable = False)
    employeecode = db.Column(db.Text(), nullable = False)
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')#decode generated password
    
    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)#returns true or false 

# Fix - Declared 'Company' manually instead of using automap_base()
class Company(db.Model):
     companyname = db.Column(db.Integer(), primary_key=True)

# Fix - Declared 'Model' manually instead of using automap_base()
class Model(db.Model):
     modelname = db.Column(db.Integer(), primary_key=True)     

class Devices(db.Model):
     devid = db.Column(db.Integer(), primary_key=True)

class Smartphones(db.Model):
    devid = db.Column(db.Integer(), db.ForeignKey('devices.devid'),primary_key=True)
    devname = db.Column(db.Text(), nullable = False)
    devcolor = db.Column(db.Text(), nullable = False)
    devstorage = db.Column(db.Text(),nullable = False)
    devamount = db.Column(db.Integer(), nullable = False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def buy(self,user):
        self.owner = user.id
        user.creditcardamount -= self.devamount
        db.session.commit()
    
    def buycontract(self,user):
        self.owner = user.id
        user.contractaccountbalance -= self.devamount
        db.session.commit()

class Laptops(db.Model):
    devid = db.Column(db.Integer(), db.ForeignKey('devices.devid'),primary_key=True)
    lapname = db.Column(db.Text(), nullable = False)
    lapcolor = db.Column(db.Text(), nullable = False)
    lapram = db.Column(db.Text(), nullable = False)
    lapprocessor =  db.Column(db.Text(), nullable = False)
    lapstorage = db.Column(db.Text(),nullable = False)
    lapamount = db.Column(db.Integer(), nullable = False)
    lapowner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def buylap(self,user):
        self.lapowner = user.id
        user.creditcardamount -= self.lapamount
        db.session.commit()
    
    def buylapcontract(self,user):
        self.lapowner = user.id
        user.contractaccountbalance -= self.lapamount
        db.session.commit()

class Audio(db.Model):
    devid = db.Column(db.Integer(), db.ForeignKey('devices.devid'),primary_key=True)
    audioname = db.Column(db.Text(), nullable = False)
    audiocolor = db.Column(db.Text(), nullable = False)
    audioamount = db.Column(db.Integer(), nullable = False)
    adowner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def buyad(self,user):
        self.adowner = user.id
        user.creditcardamount -= self.audioamount
        db.session.commit()
    
    def buyadcontract(self,user):
        self.adowner = user.id
        user.contractaccountbalance -= self.audioamount
        db.session.commit()

# Fix - Changed line 135, from "db.ForeignKey(' model.modelname')" to "db.ForeignKey('model.modelname')". Notice the space before model.
class Madeby(db.Model):
    companyname = db.Column(db.Text(), db.ForeignKey('company.companyname'), primary_key=True, nullable = False)
    modelname = db.Column(db.Text(), db.ForeignKey('model.modelname'), primary_key=True, nullable = False)

class Deliverycompany(db.Model):
    delid = db.Column(db.Integer(), primary_key=True,nullable = False)
    deltrackno = db.Column(db.Integer(), primary_key=True,nullable = False)
    delname =  db.Column(db.Text(), nullable = False)

class Of(db.Model):
    devid = db.Column(db.Integer(), db.ForeignKey('devices.devid'), primary_key=True, nullable = False)
    modelname = db.Column(db.Text(), db.ForeignKey('model.modelname'), primary_key=True, nullable = False) 

class Creditcard(db.Model):
    creditcardid = db.Column(db.Integer(), primary_key=True, nullable = False)
    creditcardnumber = db.Column(db.Integer(), unique=True , nullable = False)#like name of card
    creditcardcode = db.Column(db.Integer(), nullable = False)#like password for card
    creditcardservice = db.Column(db.Text(), nullable = False)

class Debitcard(db.Model):
    debitid = db.Column(db.Integer(), primary_key=True, nullable = False)
    creditcardid =  db.Column(db.Integer(), db.ForeignKey('creditcard.creditcardid'),nullable = False)
    regularuser = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = False)
    datedebited = db.Column(db.Date(), nullable = False)

class Regularuser(db.Model):
    regid =  db.Column(db.Integer(), primary_key=True, nullable = False)
    regularuser = db.Column(db.Integer(), db.ForeignKey('user.id'),nullable = False)

class Contractaccount(db.Model):
    contractaccountid = db.Column(db.Integer(), primary_key=True, nullable = False)
    password_hash = db.Column(db.Text(), nullable = False)
    datecreated =  db.Column(db.Date(), nullable = False)
    names = db.Column(db.Text(), unique=True , nullable = False)
    dateend =  db.Column(db.Date(), nullable = False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')#decode generated password
    
    def check_password_correction(self,attempted_password1):
        return bcrypt.check_password_hash(self.password_hash,attempted_password1)

class Contractuser(db.Model):
    contractno =  db.Column(db.Integer(), primary_key=True, nullable = False)
    contractuserid =  db.Column(db.Integer(), db.ForeignKey('user.id'),nullable = False)

class Bill(db.Model):
    billid = db.Column(db.Integer(), primary_key=True, nullable = False)
    contractaccountid = db.Column(db.Integer(), db.ForeignKey('contractaccount.contractaccountid'), nullable = False)
    contractuser = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = False)
    datebilled =  db.Column(db.Date(), nullable = False)

class Purchase(db.Model):
    purchaseid =  db.Column(db.Integer(), primary_key=True, nullable = False,autoincrement = True)
    purchaseamount =  db.Column(db.Integer(), nullable = False)

class Recordedin(db.Model):
    devid =  db.Column(db.Integer(), db.ForeignKey('devices.devid'), primary_key=True, nullable = False)
    purchaseid =  db.Column(db.Integer(), db.ForeignKey('purchase.purchaseid'), primary_key=True, nullable = False)

class Doneby(db.Model):
    purchaseid = db.Column(db.Integer(), db.ForeignKey('purchase.purchaseid'), primary_key=True, nullable = False)
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'), primary_key=True, nullable = False)

class Sentto(db.Model):
    purchaseid = db.Column(db.Integer(), db.ForeignKey('purchase.purchaseid'), primary_key=True, nullable = False)
    delid = db.Column(db.Integer(), db.ForeignKey('deliverycompany.delid'), primary_key=True, nullable = False)

class Hevadaelectronics(db.Model):
    deltrackno = db.Column(db.Integer(), nullable = False)
    orderuserid = db.Column(db.Integer(), nullable = False)
    orderid =  db.Column(db.Integer(),primary_key=True, nullable = False)
    orderdate =  db.Column(db.Date(), nullable = False)
    devid = db.Column(db.Integer(),db.ForeignKey('devices.devid'), nullable = False)

class Store(db.Model):
    orderid = db.Column(db.Integer(), db.ForeignKey('hevadaelectronics.orderid'), primary_key=True, nullable = False)
    deltrackno = db.Column(db.Integer(), db.ForeignKey('deliverycompany.deltrackno'),nullable = False)

class With(db.Model):
    userid = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = False)
    deliverdetailid = db.Column(db.Integer(), db.ForeignKey('userdeliverydetails.deliverdetailid'), primary_key=True, nullable = False)

class Userdeliverydetails(db.Model):
    userdeliverid = db.Column(db.Integer(),nullable = False)
    useraddress =  db.Column(db.Text(), nullable = False)
    deliverdetailid =  db.Column(db.Integer(),primary_key=True, nullable = False)



