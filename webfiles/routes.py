import datetime
from flask import Flask, render_template,request,session
from webfiles import app
from flask import render_template, redirect, url_for, flash, request
from webfiles.models import (User,Devices,Smartphones,Laptops,Audio,Creditcard,Purchase,Deliverycompany,Hevadaelectronics,Userdeliverydetails,
                            Debitcard,Contractaccount,Bill,Contractuser,Regularuser,Store,Employee)
from webfiles.forms import (Registerform, LoginForm, CreditcardForm, RegisteredCardForm, DeliveryForm, ContractForm, RegisteredcontractForm,
                            RegisteradminForm, LoginadminForm,AddiphonesForm,AddamsungsForm,AddoneplusForm,AddsurfaceForm
                            ,AddhpForm,AddmacbookForm,AddairpodsForm,AddbeatsForm,AddboseForm,AddjblForm)
from webfiles import db
from flask_login import login_user,logout_user,login_required,current_user
from sqlalchemy.sql import exists
from flask_wtf import FlaskForm
import sqlite3

@app.route('/')
@app.route('/home')
@login_required
def home_page():
    return render_template('Home.html')

@app.route('/laptops')
@login_required
def laptops_page():
    return render_template('Laptops.html')

@app.route('/smartphones')
@login_required
def smartphones_page():
    return render_template('Smartphones.html')

@app.route('/audio')
@login_required
def audio_page():
    return render_template('Audio.html')

@app.route('/iPhone')
def iPhone_page():
    return render_template('baseiphone.html')

@app.route('/Samsung')
def Samsung_page():
    return render_template('basesamsung.html')

@app.route('/OnePlus')
def OnePlus_page():
    return render_template('baseoneplus.html')

@app.route('/SamsungS21')
def SamsungS21_page():
    return render_template('basesamsungs21.html')

@app.route('/SamsungNote')
def SamsungNote_page():
    return render_template('basesamsungnote.html')

@app.route('/Microsoft')
def Microsoft_page():
    return render_template('basemicrosoft.html')

@app.route('/Mac')
def Mac_page():
    return render_template('basemac.html')

@app.route('/HP')
def HP_page():
    return render_template('basehp.html')

@app.route('/ENVY')
def ENVY_page():
    return render_template('basenvy.html')

@app.route('/ELITE')
def ELITE_page():
    return render_template('baselite.html')

@app.route('/SurfaceLaptop4')
def SurfaceLaptop4_page():
    return render_template('basesurfacelaptop4.html')

@app.route('/OMEN')
def OMEN_page():
    return render_template('baseomen.html')

@app.route('/BeatsbyDre')
def BeatsbyDre_page():
    return render_template('basebeatsdre.html')

@app.route('/JBL')
def JBL_page():
    return render_template('basejbl.html')

@app.route('/Bose')
def Bose_page():
    return render_template('basebose.html')

@app.route('/AppleAudio')
def AppleAudio_page():
    return render_template('baseappleaudio.html')

@app.route('/samsungs21',methods = ['GET', 'POST'])
def samsungs21_page():
    getcolor = request.form.getlist('s21color')
    getstorage = request.form.getlist('s21storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Samsungs21', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()   
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))
    return render_template('samsungs21.html')

@app.route('/samsungs215G',methods = ['GET', 'POST'])
def samsungs215G_page():
    getcolor = request.form.getlist('s215Gcolor')
    getstorage = request.form.getlist('s215Gstorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Samsungs21+5G', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('samsungs215G.html')

@app.route('/samsungs21ultra',methods = ['GET', 'POST'])
def samsungs21ultra_page():
    getcolor = request.form.getlist('s21ultracolor')
    getstorage = request.form.getlist('s21ultrastorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Samsungs21ultra', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('samsungs21ultra.html')

@app.route('/SamsungFold',methods = ['GET', 'POST'])
def SamsungFold_page():
    getcolor = request.form.getlist('foldcolor')
    getstorage = request.form.getlist('foldstorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Samsungfold2', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('samsungfold.html')

@app.route('/samsungnote20',methods = ['GET', 'POST'])
def samsungnote20_page():
    getcolor = request.form.getlist('notecolor')
    getstorage = request.form.getlist('notestorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Samsungnote20', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('samsungnote20.html')

@app.route('/samsungnote20ultra',methods = ['GET', 'POST'])
def samsungnote20ultra_page():
    getcolor = request.form.getlist('noteultracolor')
    getstorage = request.form.getlist('noteultrastorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Samsungnote20ultra', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('samsungnote20ultra.html')

@app.route('/oneplus9Pro',methods = ['GET', 'POST'])
def oneplus9Pro_page():
    getcolor = request.form.getlist('one9procolor')
    getstorage = request.form.getlist('one9prostorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Oneplus9Pro', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('oneplus9Pro.html')

@app.route('/oneplus9',methods = ['GET', 'POST'])
def oneplus9_page():
    getcolor = request.form.getlist('one9color')
    getstorage = request.form.getlist('one9storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Oneplus9', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('oneplus9.html')

@app.route('/oneplus8Pro',methods = ['GET', 'POST'])
def oneplus8Pro_page():
    getcolor = request.form.getlist('one8procolor')
    getstorage = request.form.getlist('one8prostorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Oneplus8Pro', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('oneplus8Pro.html')

@app.route('/oneplus8T',methods = ['GET', 'POST'])
def oneplus8T_page():
    getcolor = request.form.getlist('one8Tcolor')
    getstorage = request.form.getlist('one8Tstorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Oneplus8T', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('oneplus8T.html')

@app.route('/oneplus8',methods = ['GET', 'POST'])
def oneplus8_page():
    getcolor = request.form.getlist('one8color')
    getstorage = request.form.getlist('one8storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Oneplus8', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('oneplus8.html')

@app.route('/oneplus7T',methods = ['GET', 'POST'])
def oneplus7T_page():
    getcolor = request.form.getlist('one7Tcolor')
    getstorage = request.form.getlist('one7Tstorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'Oneplus7T', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('oneplus7T.html')
    
@app.route('/iphone12ProMax',methods = ['GET', 'POST'])
def iphone12ProMax_page():
    getcolor = request.form.getlist('12promaxcolor')
    getstorage = request.form.getlist('12promaxstorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'iphone12ProMax', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('iphone12ProMax.html')

@app.route('/iphone12Pro',methods = ['GET', 'POST'])
def iphone12Pro_page():
    getcolor = request.form.getlist('12procolor')
    getstorage = request.form.getlist('12prostorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'iphone12Pro', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('iphone12Pro.html')

@app.route('/iphone12',methods = ['GET', 'POST'])
def iphone12_page():
    getcolor = request.form.getlist('12color')
    getstorage = request.form.getlist('12storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'iphone12', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('iphone12.html')

@app.route('/iphone11',methods = ['GET', 'POST'])
def iphone11_page():
    getcolor = request.form.getlist('11color')
    getstorage = request.form.getlist('11storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'iphone11', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('iphone11.html')

@app.route('/iphoneXR',methods = ['GET', 'POST'])
def iphoneXR_page():
    getcolor = request.form.getlist('XRcolor')
    getstorage = request.form.getlist('XRstorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Smartphones.query.filter_by(devname = 'iphoneXR', devcolor = getcolor[0], devstorage = getstorage[0], owner = None).first()
            if chosendevice is None:
                flash('The item you chose out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['phone'] = chosendevice
                return redirect(url_for('checkout'))   
    return render_template('iphoneXR.html')

@app.route('/MacbookAir',methods = ['GET', 'POST'])
def MacbookAir_page(): 
    getcolor = request.form.getlist('aircolor')
    getstorage = request.form.getlist('airstorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Macair', lapcolor = getcolor[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('macair.html')

@app.route('/MacbookPro13inch',methods = ['GET', 'POST'])
def MacbookPro13inch_page():
    getcolor = request.form.getlist('pro13color')
    getstorage = request.form.getlist('pro13storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Macpro13', lapcolor = getcolor[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('macpro13.html')

@app.route('/MacbookPro16inch',methods = ['GET', 'POST'])
def MacbookPro16inch_page():
    getcolor = request.form.getlist('pro16color')
    getstorage = request.form.getlist('pro16storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select a color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Macpro16', lapcolor = getcolor[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('macpro16.html')

@app.route('/PAVILION',methods = ['GET', 'POST'])
def PAVILION_page():
    getstorage = request.form.getlist('pavilionstorage')
    if request.method == 'POST':
        if getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Pavilion',lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('pavilion.html')

@app.route('/Envy14inch',methods = ['GET', 'POST'])
def Envy14inch_page():
    getram = request.form.getlist('envy14ram')
    getprocessor = request.form.getlist('envy14proc')
    getstorage = request.form.getlist('envy14storage')
    if request.method == 'POST':
        if getram == []:
            flash ("Please select your RAM",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        elif getprocessor == []:
            flash("Please select a processor", category = 'danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Envy14', lapprocessor = getprocessor[0] , lapram = getram[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('envy14.html')

@app.route('/Envy15inch',methods = ['GET', 'POST'])
def Envy15inch_page():
    getstorage = request.form.getlist('envy15storage')
    if request.method == 'POST':
        if getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Envy15',lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('envy15.html')

@app.route('/Elitebook835',methods = ['GET', 'POST'])
def Elitebook835_page():
    getram = request.form.getlist('835ram')
    getprocessor = request.form.getlist('835proc')
    getstorage = request.form.getlist('835storage')
    if request.method == 'POST':
        if getram == []:
            flash ("Please select your RAM",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        elif getprocessor == []:
            flash("Please select a processor", category = 'danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Elitebook835', lapprocessor = getprocessor[0] , lapram = getram[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('elite835.html')

@app.route('/Elitebook845',methods = ['GET', 'POST'])
def Elitebook845_page():
    getram = request.form.getlist('845ram')
    getprocessor = request.form.getlist('845proc')
    getstorage = request.form.getlist('845storage')
    if request.method == 'POST':
        if getram == []:
            flash ("Please select your RAM",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        elif getprocessor == []:
            flash("Please select a processor", category = 'danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Elitebook845', lapprocessor = getprocessor[0] , lapram = getram[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('elite845.html')

@app.route('/EliteDragonfly',methods = ['GET', 'POST'])
def EliteDragonfly_page():
    getstorage = request.form.getlist('elitedragstorage')
    if request.method == 'POST':
        if getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Elitedragonfly',lapstorage= getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('elitedragonfly.html')

@app.route('/OMEN15',methods = ['GET', 'POST'])
def OMEN15_page():
    getstorage = request.form.getlist('omen15storage')
    if request.method == 'POST':
        if getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Omen15',lapstorage= getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('omen15.html')

@app.route('/OMENX2S',methods = ['GET', 'POST'])
def OMENX2S_page():
    getstorage = request.form.getlist('omenXstorage')
    if request.method == 'POST':
        if getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'OmenX2S',lapstorage= getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('omen2s.html')

@app.route('/SurfaceLaptopGo',methods = ['GET', 'POST'])
def SurfaceLaptopGo_page():
    getcolor = request.form.getlist('gocolor')
    getstorage = request.form.getlist('gostorage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Surfacelaptopgo', lapcolor = getcolor[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('surfacelaptopgo.html')

@app.route('/SurfaceLaptop413inch',methods = ['GET', 'POST'])
def SurfaceLaptop413inch_page():
    getcolor = request.form.getlist('413color')
    getram = request.form.getlist('413ram')
    getprocessor = request.form.getlist('413proc')
    getstorage = request.form.getlist('413storage')
    if request.method == 'POST':
        if getram == []:
            flash ("Please select your RAM",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        elif getprocessor == []:
            flash("Please select a processor", category = 'danger')
        elif getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Surfacelaptop413', lapcolor = getcolor[0],lapprocessor = getprocessor[0] , lapram = getram[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('surfacelaptop413.html')

@app.route('/SurfaceLaptop415inch',methods = ['GET', 'POST'])
def SurfaceLaptop415inch_page():
    getcolor = request.form.getlist('415color')
    getram = request.form.getlist('415ram')
    getprocessor = request.form.getlist('415proc')
    getstorage = request.form.getlist('415storage')
    if request.method == 'POST':
        if getram == []:
            flash ("Please select your RAM",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        elif getprocessor == []:
            flash("Please select a processor", category = 'danger')
        elif getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Surfacelaptop415', lapcolor = getcolor[0],lapprocessor = getprocessor[0] , lapram = getram[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('surfacelaptop415.html')

@app.route('/SurfacePro7',methods = ['GET', 'POST'])
def SurfacePro7_page():
    getcolor = request.form.getlist('pro7color')
    getstorage = request.form.getlist('pro7storage')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        elif getstorage == []:
            flash ("Please select a storage",category='danger')
        else:
            chosendevice = Laptops.query.filter_by(lapname = 'Surfacepro7', lapcolor = getcolor[0], lapstorage = getstorage[0], lapowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['laptop'] = chosendevice
                return redirect(url_for('checkoutlaptop'))  
    return render_template('surfacepro7.html')

@app.route('/BeatsPill',methods = ['GET', 'POST'])
def BeatsPill_page():
    getcolor = request.form.getlist('pillcolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'BeatsPill', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio'))  
    return render_template('beatspill.html')

@app.route('/SoloPro',methods = ['GET', 'POST'])
def SoloPro_page():
    getcolor = request.form.getlist('solocolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'BeatsSoloPro', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('beatsolopro.html')

@app.route('/BeatsStudio',methods = ['GET', 'POST'])
def BeatsStudio_page():
    getcolor = request.form.getlist('studiocolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'BeatsStudio', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('beatstudio.html')

@app.route('/PowerBeats',methods = ['GET', 'POST'])
def PowerBeats_page():
    getcolor = request.form.getlist('powercolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'Powerbeats', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('powerbeats.html')

@app.route('/PowerBeatsPro',methods = ['GET', 'POST'])
def PowerBeatsPro_page():
    getcolor = request.form.getlist('powerprocolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'PowerbeatsPro', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('powerbeatspro.html')

@app.route('/SoundSport',methods = ['GET', 'POST'])
def SoundSport_page():
    getcolor = request.form.getlist('sportcolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'BoseSoundsport', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('bosesoundsport.html')

@app.route('/BoseBuds',methods = ['GET', 'POST'])
def BoseBuds_page():
    getcolor = request.form.getlist('bosebudcolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'BoseEarbuds', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('bosebuds.html')

@app.route('/BoseHeadphones',methods = ['GET', 'POST'])
def BoseHeadphones_page():
    getcolor = request.form.getlist('boseheadcolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'Bose35WirelessII', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('boseheadphones.html')

@app.route('/BoseGamingHeadphones',methods = ['GET', 'POST'])
def BoseGamingHeadphones_page():
    if request.method == 'POST':
        chosendevice = Audio.query.filter_by(audioname = 'Bose35IIGaming', audiocolor = 'Tripleblackcopper', adowner = None).first()
        if chosendevice is None:
            flash('This item is out of stock at the moment.Please choose another',category='danger')
        else:
            chosendevice = chosendevice.devid
            chosendevice = str(chosendevice)
            session['audio'] = chosendevice
            return redirect(url_for('checkoutaudio')) 
    return render_template('bosegamehead.html')

@app.route('/JBLFlip5',methods = ['GET', 'POST'])
def JBLFlip5_page():
    getcolor = request.form.getlist('flipcolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'JBLFlip5', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('jblflip.html')

@app.route('/JBL460',methods = ['GET', 'POST'])
def JBL460_page():
    getcolor = request.form.getlist('j460color')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'JBLLive460NC', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('jbl460.html')

@app.route('/JBLQuantum',methods = ['GET', 'POST'])
def JBLQuantum_page():
    if request.method == 'POST':
        chosendevice = Audio.query.filter_by(audioname = 'JBLQuantum300', audiocolor = 'Black', adowner = None).first()
        if chosendevice is None:
            flash('This item is out of stock at the moment.Please choose another',category='danger')
        else:
            chosendevice = chosendevice.devid
            chosendevice = str(chosendevice)
            session['audio'] = chosendevice
            return redirect(url_for('checkoutaudio')) 
    return render_template('jblq.html')

@app.route('/JBLLive500BT',methods = ['GET', 'POST'])
def JBLLive500BT_page():
    getcolor = request.form.getlist('j500color')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'JBLLive500BT', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('jbl500.html')

@app.route('/JBLTune205BT',methods = ['GET', 'POST'])
def JBLTune205BT_page():
    getcolor = request.form.getlist('j205color')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'JBLTune205BT', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('jbl205.html')

@app.route('/JBLTune125TWS',methods = ['GET', 'POST'])
def JBLTune125TWS_page():
    getcolor = request.form.getlist('j125color')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'JBLTune125TWS', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio'))  
    return render_template('jbl125.html')

@app.route('/Airpods',methods = ['GET', 'POST'])
def Airpods_page():
    if request.method == 'POST':
        chosendevice = Audio.query.filter_by(audioname = 'Airpods', audiocolor = 'White', adowner = None).first()
        if chosendevice is None:
            flash('This item is out of stock at the moment.Please choose another',category='danger')
        else:
            chosendevice = chosendevice.devid
            chosendevice = str(chosendevice)
            session['audio'] = chosendevice
            return redirect(url_for('checkoutaudio')) 
    return render_template('airpods.html')

@app.route('/AirpodsPro',methods = ['GET', 'POST'])
def AirpodsPro_page():
    if request.method == 'POST':
        chosendevice = Audio.query.filter_by(audioname = 'AirpodsPro', audiocolor = 'White', adowner = None).first()
        if chosendevice is None:
            flash('This item is out of stock at the moment.Please choose another',category='danger')
        else:
            chosendevice = chosendevice.devid
            chosendevice = str(chosendevice)
            session['audio'] = chosendevice
            return redirect(url_for('checkoutaudio')) 
    return render_template('airpodspro.html')

@app.route('/AirpodsMax',methods = ['GET', 'POST'])
def AirpodsMax_page():
    getcolor = request.form.getlist('airmaxcolor')
    if request.method == 'POST':
        if getcolor == []:
            flash ("Please select your color",category='danger')
        else:
            chosendevice = Audio.query.filter_by(audioname = 'AirpodsMax', audiocolor = getcolor[0], adowner = None).first()
            if chosendevice is None:
                flash('This item is out of stock at the moment.Please choose another',category='danger')
            else:
                chosendevice = chosendevice.devid
                chosendevice = str(chosendevice)
                session['audio'] = chosendevice
                return redirect(url_for('checkoutaudio')) 
    return render_template('airpodsmax.html')

@app.route('/creditcard',methods=['GET', 'POST'])
def creditcard_page():
    chosendevice = session.get('phone', None)
    items = Smartphones.query.get(chosendevice)
    user = current_user.id
    tday = datetime.date.today()
    form = CreditcardForm()
    if form.validate_on_submit():
        credit_card_details = Creditcard(creditcardnumber=form.creditcardnumber.data, creditcardcode=form.creditcardcode.data, creditcardservice=form.creditcardservice.data)
        db.session.add(credit_card_details)
        p_item_object = Smartphones.query.filter_by(devid=chosendevice).first()
        devprice = p_item_object.devamount
        usercard = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
        carduser = usercard.creditcardid
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash("Item purchased successfully",category = 'info')
                purchasedetails = Purchase(purchaseamount = devprice) 
                db.session.add(purchasedetails)
                credituser = Regularuser(regularuser = user)
                try:
                    db.session.add(credituser)
                except:
                    pass
                creditcarduser = Debitcard(creditcardid = carduser,regularuser = user,datedebited = tday)
                db.session.add(creditcarduser)
                db.session.commit()
                return redirect(url_for('delivery_page'))  
            else:
                 flash("You have insufficient funds to purchase",category = 'danger')  
    if form.errors != {}:#if there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'Invalid Credit Card Details:{err_msg}',category='danger') 
    return render_template('registercreditcard.html', form=form, item=items)

@app.route('/creditcardlaptops',methods=['GET', 'POST'])
def creditcardlaptops_page():
    chosendevice = session.get('laptop', None)
    items = Laptops.query.get(chosendevice)
    form = CreditcardForm()
    tday = datetime.date.today()
    user = current_user.id
    if form.validate_on_submit():
        credit_card_details = Creditcard(creditcardnumber=form.creditcardnumber.data, creditcardcode=form.creditcardcode.data, creditcardservice=form.creditcardservice.data)
        db.session.add(credit_card_details)
        p_item_object = Laptops.query.filter_by(devid=chosendevice).first()
        devprice = p_item_object.lapamount
        usercard = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
        carduser = usercard.creditcardid
        if p_item_object:
            if current_user.can_purchaselaptop(p_item_object):
                p_item_object.buylap(current_user)
                flash("Item purchased successfully",category = 'info')
                purchasedetails = Purchase(purchaseamount = devprice) 
                db.session.add(purchasedetails)
                credituser = Regularuser(regularuser = user)
                db.session.add(credituser)
                creditcarduser = Debitcard(creditcardid = carduser,regularuser = user,datedebited = tday)
                db.session.add(creditcarduser)
                db.session.commit()
                return redirect(url_for('deliverylaptop_page'))
            else:
                 flash("You have insufficient funds to purchase",category = 'danger')
    if form.errors != {}:#if there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'Invalid Credit Card Details:{err_msg}',category='danger')
    return render_template('registercreditcardlaptops.html', form=form, item=items)

@app.route('/creditcardaudio',methods=['GET', 'POST'])
def creditcardaudio_page():
    chosendevice = session.get('audio', None)
    items = Audio.query.get(chosendevice)
    form = CreditcardForm()
    tday = datetime.date.today()
    user = current_user.id
    if form.validate_on_submit():
        credit_card_details = Creditcard(creditcardnumber=form.creditcardnumber.data, creditcardcode=form.creditcardcode.data, creditcardservice=form.creditcardservice.data)
        db.session.add(credit_card_details)
        p_item_object = Audio.query.filter_by(devid=chosendevice).first()
        devprice = p_item_object.audioamount
        usercard = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
        carduser = usercard.creditcardid
        if p_item_object:
            if current_user.can_purchaseaudio(p_item_object):
                p_item_object.buyad(current_user)
                flash("Item purchased successfully",category = 'info')
                purchasedetails = Purchase(purchaseamount = devprice) 
                db.session.add(purchasedetails)
                credituser = Regularuser(regularuser = user)
                db.session.add(credituser)
                creditcarduser = Debitcard(creditcardid = carduser,regularuser = user,datedebited = tday)
                db.session.add(creditcarduser)
                db.session.commit()
                return redirect(url_for('deliveryaudio_page'))
            else:
                 flash("You have insufficient funds to purchase",category = 'danger')
    if form.errors != {}:#if there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'Invalid Credit Card Details:{err_msg}',category='danger')
    return render_template('registercreditcardaudio.html', form=form, item=items)

@app.route('/registeredcreditcard',methods=['GET', 'POST'])
def registeredcard_page():
    chosendevice = session.get('phone', None)
    items = Smartphones.query.get(chosendevice)
    user = current_user.id
    tday = datetime.date.today()
    form = RegisteredCardForm()
    if form.validate_on_submit():#check is the card exists and if so,if there details match
        attempted_number = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
        attempted_code = Creditcard.query.filter_by(creditcardcode=form.creditcardcode.data).first()
        if attempted_number and attempted_code:#receives attempted code as parameter
            p_item_object = Smartphones.query.filter_by(devid=chosendevice).first()
            devprice = p_item_object.devamount
            usercard = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
            carduser = usercard.creditcardid
            if p_item_object:
                if current_user.can_purchase(p_item_object):
                    p_item_object.buy(current_user)
                    flash("Item purchased successfully",category = 'info')
                    purchasedetails = Purchase(purchaseamount = devprice) 
                    db.session.add(purchasedetails)
                    creditcarduser = Debitcard(creditcardid = carduser,regularuser = user,datedebited = tday)
                    db.session.add(creditcarduser)
                    db.session.commit() 
                    return redirect(url_for('delivery_page')) 
                else:
                    flash("You have insufficient funds to purchase",category = 'danger')  
        else:
            flash('Credit Card number or Credit Card code is invalid',category='danger') 
    return render_template('recordedcreditcard.html', form=form, item=items)

@app.route('/registeredcardlaptop',methods=['GET', 'POST'])
def registeredcardlaptop_page():
    chosendevice = session.get('laptop', None)
    items = Laptops.query.get(chosendevice)
    user = current_user.id
    tday = datetime.date.today()
    form = RegisteredCardForm()
    if form.validate_on_submit():#check is the card exists and if so,if there details match
        attempted_number = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
        attempted_code = Creditcard.query.filter_by(creditcardcode=form.creditcardcode.data).first()
        if attempted_number and attempted_code:#receives attempted code as parameter
            p_item_object = Laptops.query.filter_by(devid=chosendevice).first()
            devprice = p_item_object.lapamount
            usercard = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
            carduser = usercard.creditcardid
            if p_item_object:
                if current_user.can_purchaselaptop(p_item_object):
                    p_item_object.buylap(current_user)
                    flash("Item purchased successfully",category = 'info')
                    purchasedetails = Purchase(purchaseamount = devprice) 
                    db.session.add(purchasedetails)
                    creditcarduser = Debitcard(creditcardid = carduser,regularuser = user,datedebited = tday)
                    db.session.add(creditcarduser)
                    db.session.commit() 
                    return redirect(url_for('deliverylaptop_page')) 
                else:
                    flash("You have insufficient funds to purchase",category = 'danger')  
        else:
            flash('Credit Card number or Credit Card code is invalid',category='danger') 
    return render_template('recordedcreditcardlaptop.html', form=form, item=items)

@app.route('/registeredcardaudio',methods=['GET', 'POST'])
def registeredcardaudio_page():
    chosendevice = session.get('audio', None)
    items = Audio.query.get(chosendevice)
    user = current_user.id
    tday = datetime.date.today()
    form = RegisteredCardForm()
    if form.validate_on_submit():#check is the card exists and if so,if there details match
        attempted_number = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
        attempted_code = Creditcard.query.filter_by(creditcardcode=form.creditcardcode.data).first()
        if attempted_number and attempted_code:#receives attempted code as parameter
            p_item_object = Audio.query.filter_by(devid=chosendevice).first()
            devprice = p_item_object.audioamount
            usercard = Creditcard.query.filter_by(creditcardnumber=form.creditcardnumber.data).first()
            carduser = usercard.creditcardid
            if p_item_object:
                if current_user.can_purchaseaudio(p_item_object):
                    p_item_object.buyad(current_user)
                    flash("Item purchased successfully",category = 'info')
                    purchasedetails = Purchase(purchaseamount = devprice) 
                    db.session.add(purchasedetails)
                    creditcarduser = Debitcard(creditcardid = carduser,regularuser = user,datedebited = tday)
                    db.session.add(creditcarduser)
                    db.session.commit() 
                    return redirect(url_for('deliveryaudio_page')) 
                else:
                    flash("You have insufficient funds to purchase",category = 'danger')  
        else:
            flash('Credit Card number or Credit Card code is invalid',category='danger') 
    return render_template('recordedcreditcardaudio.html', form=form, item=items)

@app.route('/contractaccount',methods=['GET', 'POST'])
def contractaccount_page():
    chosendevice = session.get('phone', None)
    items = Smartphones.query.get(chosendevice)
    form = ContractForm()
    user = current_user.id
    tday = datetime.date.today()
    tdelta = datetime.timedelta(days=30)
    tlimit = tday + tdelta
    if form.validate_on_submit():
        contract_to_create = Contractaccount(names = form.names.data, password=form.password1.data, datecreated = tday, dateend = tlimit)
        db.session.add(contract_to_create)
        p_item_object = Smartphones.query.filter_by(devid=chosendevice).first()
        devprice = p_item_object.devamount
        usercontract = Contractaccount.query.filter_by(names=form.names.data).first()
        contractuserid = usercontract.contractaccountid
        contractend = usercontract.dateend
        if p_item_object:
            if current_user.can_purchasecontract(p_item_object):
                p_item_object.buycontract(current_user) 
                purchasedetails = Purchase(purchaseamount = devprice) 
                db.session.add(purchasedetails)
                contractuser = Contractuser(contractuserid = user)
                db.session.add(contractuser)
                contractaccuser = Bill(contractaccountid = contractuserid,contractuser = user, datebilled = tday)
                db.session.add(contractaccuser)
                contractend = str(contractend)
                flash("Item purchased successfully.Your contract account will expire in "+str(contractend),category = 'info')
                db.session.commit()
                return redirect(url_for('delivery_page')) 
            else:
                 flash("You have insufficient funds to purchase",category = 'danger')    
    if form.errors != {}:#if there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'Invalid Contract account Details:{err_msg}',category='danger') 
    return render_template('registercontract.html', form=form, item=items)

@app.route('/contractaccountlaptop',methods=['GET', 'POST'])
def contractaccountlaptop_page():
    chosendevice = session.get('laptop', None)
    items = Laptops.query.get(chosendevice)
    form = ContractForm()
    user = current_user.id
    tday = datetime.date.today()
    tdelta = datetime.timedelta(days=30)
    tlimit = tday + tdelta
    if form.validate_on_submit():
        contract_to_create = Contractaccount(names = form.names.data, password=form.password1.data, datecreated = tday, dateend = tlimit)
        db.session.add(contract_to_create)
        p_item_object = Laptops.query.filter_by(devid=chosendevice).first()
        devprice = p_item_object.lapamount
        usercontract = Contractaccount.query.filter_by(names = form.names.data).first()
        contractuserid = usercontract.contractaccountid
        contractend = usercontract.dateend
        if p_item_object:
            if current_user.can_purchasecontractlaptop(p_item_object):
                p_item_object.buylapcontract(current_user) 
                purchasedetails = Purchase(purchaseamount = devprice) 
                db.session.add(purchasedetails)
                contractuser = Contractuser(contractuserid = user)
                db.session.add(contractuser)
                contractaccuser = Bill(contractaccountid = contractuserid,contractuser = user, datebilled = tday)
                db.session.add(contractaccuser)
                contractend = str(contractend)
                flash("Item purchased successfully.Your contract account will expire in "+str(contractend),category = 'info')
                db.session.commit()
                return redirect(url_for('deliverylaptop_page'))
            else:
                 flash("You have insufficient funds to purchase",category = 'danger')
    if form.errors != {}:#if there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'Invalid Contract account Details:{err_msg}',category='danger') 
    return render_template('registercontractlaptop.html', form=form, item=items)

@app.route('/contractaccountaudio',methods=['GET', 'POST'])
def contractaccountaudio_page():
    chosendevice = session.get('audio', None)
    items = Audio.query.get(chosendevice)
    form = ContractForm()
    user = current_user.id
    tday = datetime.date.today()
    tdelta = datetime.timedelta(days=30)
    tlimit = tday + tdelta
    if form.validate_on_submit():
        contract_to_create = Contractaccount(names = form.names.data, password=form.password1.data, datecreated = tday, dateend = tlimit)
        db.session.add(contract_to_create)
        p_item_object = Audio.query.filter_by(devid=chosendevice).first()
        devprice = p_item_object.audioamount
        usercontract = Contractaccount.query.filter_by(names = form.names.data).first()
        contractuserid = usercontract.contractaccountid
        contractend = usercontract.dateend
        if p_item_object:
            if current_user.can_purchasecontractaudio(p_item_object):
                p_item_object.buyadcontract(current_user) 
                purchasedetails = Purchase(purchaseamount = devprice) 
                db.session.add(purchasedetails)
                contractuser = Contractuser(contractuserid = user)
                db.session.add(contractuser)
                contractaccuser = Bill(contractaccountid = contractuserid,contractuser = user, datebilled = tday)
                db.session.add(contractaccuser)
                contractend = str(contractend)
                flash("Item purchased successfully.Your contract account will expire in "+str(contractend),category = 'info')
                db.session.commit()
                return redirect(url_for('deliveryaudio_page'))
            else:
                 flash("You have insufficient funds to purchase",category = 'danger')
        
    if form.errors != {}:#if there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'Invalid Contract account Details:{err_msg}',category='danger') 
    return render_template('registercontractaudio.html', form=form, item=items)

@app.route('/registeredcontract',methods=['GET', 'POST'])
def registeredcontract_page():
    chosendevice = session.get('phone', None)
    items = Smartphones.query.get(chosendevice)
    tday = datetime.date.today()
    user = current_user.id
    form = RegisteredcontractForm()
    if form.validate_on_submit():#check is the card exists and if so,if there details match
        attempted_user = Contractaccount.query.filter_by(names = form.names.data).first()
        contractuserid = attempted_user.contractaccountid
        if attempted_user and attempted_user.check_password_correction(attempted_password1=form.password.data):#receives attempted code as parameter
            p_item_object = Smartphones.query.filter_by(devid=chosendevice).first()
            devprice = p_item_object.devamount
            if p_item_object:
                if current_user.can_purchasecontract(p_item_object):
                    p_item_object.buycontract(current_user)
                    flash("Item purchased successfully",category = 'info')
                    purchasedetails = Purchase(purchaseamount = devprice) 
                    db.session.add(purchasedetails)
                    contractaccuser = Bill(contractaccountid = contractuserid,contractuser = user, datebilled = tday)
                    db.session.add(contractaccuser)
                    db.session.commit() 
                    return redirect(url_for('delivery_page')) 
                else:
                    flash("You have insufficient funds to purchase",category = 'danger')  
        else:
            flash('Contract name or password is invalid',category='danger') 
    return render_template('recordedcontract.html', form=form, item=items)

@app.route('/registeredcontractlaptop',methods=['GET', 'POST'])
def registeredcontractlaptop_page():
    chosendevice = session.get('laptop', None)
    items = Laptops.query.get(chosendevice)
    tday = datetime.date.today()
    user = current_user.id
    form = RegisteredcontractForm()
    if form.validate_on_submit():#check is the card exists and if so,if there details match
        attempted_user = Contractaccount.query.filter_by(names = form.names.data).first()
        contractuserid = attempted_user.contractaccountid
        if attempted_user and attempted_user.check_password_correction(attempted_password1=form.password.data):#receives attempted code as parameter
            p_item_object = Laptops.query.filter_by(devid=chosendevice).first()
            devprice = p_item_object.lapamount
            if p_item_object:
                if current_user.can_purchasecontractlaptop(p_item_object):
                    p_item_object.buylapcontract(current_user)
                    flash("Item purchased successfully",category = 'info')
                    purchasedetails = Purchase(purchaseamount = devprice) 
                    db.session.add(purchasedetails)
                    contractaccuser = Bill(contractaccountid = contractuserid,contractuser = user, datebilled = tday)
                    db.session.add(contractaccuser)
                    db.session.commit() 
                    return redirect(url_for('deliverylaptop_page')) 
                else:
                    flash("You have insufficient funds to purchase",category = 'danger')  
        else:
            flash('Contract name or password is invalid',category='danger') 
    return render_template('recordedcontractlap.html', form=form, item=items)

@app.route('/registeredcontractaudio',methods=['GET', 'POST'])
def registeredcontractaudio_page():
    chosendevice = session.get('audio', None)
    items = Audio.query.get(chosendevice)
    tday = datetime.date.today()
    user = current_user.id
    form = RegisteredcontractForm()
    if form.validate_on_submit():#check is the card exists and if so,if there details match
        attempted_user = Contractaccount.query.filter_by(names = form.names.data).first()
        contractuserid = attempted_user.contractaccountid
        if attempted_user and attempted_user.check_password_correction(attempted_password1=form.password.data):#receives attempted code as parameter
            p_item_object = Audio.query.filter_by(devid=chosendevice).first()
            devprice = p_item_object.audioamount
            if p_item_object:
                if current_user.can_purchasecontractaudio(p_item_object):
                    p_item_object.buyadcontract(current_user)
                    flash("Item purchased successfully",category = 'info')
                    purchasedetails = Purchase(purchaseamount = devprice) 
                    db.session.add(purchasedetails)
                    contractaccuser = Bill(contractaccountid = contractuserid,contractuser = user, datebilled = tday)
                    db.session.add(contractaccuser)
                    db.session.commit() 
                    return redirect(url_for('deliveryaudio_page')) 
                else:
                    flash("You have insufficient funds to purchase",category = 'danger')  
        else:
            flash('Contract name or password is invalid',category='danger') 
    return render_template('recordedcontractad.html', form=form, item=items)

@app.route('/checkoutphone', methods=['GET', 'POST'])
def checkout(): 
    chosendevice = session.get('phone', None)
    items = Smartphones.query.get(chosendevice)
    return render_template('checkout.html', item=items)

@app.route('/checkoutlaptop', methods=['GET', 'POST'])
def checkoutlaptop(): 
    chosendevice = session.get('laptop', None)
    items = Laptops.query.get(chosendevice)
    return render_template('checkoutlaptop.html', item=items)

@app.route('/checkoutaudio', methods=['GET', 'POST'])
def checkoutaudio(): 
    chosendevice = session.get('audio', None)
    items = Audio.query.get(chosendevice)
    return render_template('checkoutaudio.html', item=items)

@app.route('/deliverypage',methods=['GET','POST'])
def delivery_page():
    getname = request.form.getlist('delcompany')
    chosendevice = session.get('phone', None)
    form = DeliveryForm()
    tday = datetime.date.today()
    user = current_user.id
    if request.method == 'POST':
        user_delivery_details = Userdeliverydetails(userdeliverid = user, useraddress = form.useraddress.data)
        db.session.add(user_delivery_details)
        chosendelivery = Deliverycompany.query.filter_by(delname = getname[0]).first()
        if chosendelivery is None:
            flash('This delivery means is currently unserviceable,please choose another',category='danger')
        else:
            chosendelivery = chosendelivery.delid
            chosendelivery = str(chosendelivery)
            session['selected company'] = chosendelivery
            p_delivery = Deliverycompany.query.filter_by(delid = chosendelivery).first()
            userdeliver = p_delivery.deltrackno
            deliverdetails = Hevadaelectronics(deltrackno = userdeliver ,orderuserid = user ,devid = chosendevice ,orderdate = tday)
            db.session.add(deliverdetails)
            orderno = Hevadaelectronics.query.filter_by(devid = chosendevice).first()
            userorder = orderno.orderid
            store = Store(deltrackno = userdeliver, orderid = userorder)
            db.session.add(store)
            userorder = str(userorder)
            db.session.commit()
            flash('Your item will be delivered in one day. Incase of any query,please contact us and provide your order number .Your order number is '+str(userorder),category='info')
        return redirect(url_for('delivery_page'))
    if request.method == 'GET':  
        return render_template('Delivery.html',form=form)

@app.route('/deliverypagelaptop',methods=['GET','POST'])
def deliverylaptop_page():
    getname = request.form.getlist('delcompany')
    chosendevice = session.get('laptop', None)
    form = DeliveryForm()
    tday = datetime.date.today()
    user = current_user.id
    if request.method == 'POST':
        user_delivery_details = Userdeliverydetails(userdeliverid = user, useraddress = form.useraddress.data)
        db.session.add(user_delivery_details)
        chosendelivery = Deliverycompany.query.filter_by(delname = getname[0]).first()
        if chosendelivery is None:
            flash('This delivery means is currently unserviceable,please choose another',category='danger')
        else:
            chosendelivery = chosendelivery.delid
            chosendelivery = str(chosendelivery)
            session['selected company'] = chosendelivery
            p_delivery = Deliverycompany.query.filter_by(delid = chosendelivery).first()
            userdeliver = p_delivery.deltrackno
            deliverdetails = Hevadaelectronics(deltrackno = userdeliver ,orderuserid = user ,devid = chosendevice,orderdate = tday)
            db.session.add(deliverdetails)
            orderno = Hevadaelectronics.query.filter_by(devid = chosendevice).first()
            userorder = orderno.orderid
            store = Store(deltrackno = userdeliver, orderid = userorder)
            db.session.add(store)
            userorder = str(userorder)
            db.session.commit()
            flash('Your item will be delivered in one day. Incase of any query,please contact us and provide your order number .Your order number is '+str(userorder),category='info')
        return redirect(url_for('deliverylaptop_page'))
    if request.method == 'GET':  
        return render_template('Deliverylaptop.html',form=form)

@app.route('/deliverypageaudio',methods=['GET','POST'])
def deliveryaudio_page():
    getname = request.form.getlist('delcompany')
    chosendevice = session.get('audio', None)
    form = DeliveryForm()
    tday = datetime.date.today()
    user = current_user.id
    if request.method == 'POST':
        user_delivery_details = Userdeliverydetails(userdeliverid = user, useraddress = form.useraddress.data)
        db.session.add(user_delivery_details)
        chosendelivery = Deliverycompany.query.filter_by(delname = getname[0]).first()
        if chosendelivery is None:
            flash('This delivery means is currently unserviceable,please choose another',category='danger')
        else:
            chosendelivery = chosendelivery.delid
            chosendelivery = str(chosendelivery)
            session['selected company'] = chosendelivery
            p_delivery = Deliverycompany.query.filter_by(delid = chosendelivery).first()
            userdeliver = p_delivery.deltrackno
            deliverdetails = Hevadaelectronics(deltrackno = userdeliver ,orderuserid = user ,devid = chosendevice,orderdate = tday)
            db.session.add(deliverdetails)
            orderno = Hevadaelectronics.query.filter_by(devid = chosendevice).first()
            userorder = orderno.orderid
            store = Store(deltrackno = userdeliver, orderid = userorder)
            db.session.add(store)
            userorder = str(userorder)
            db.session.commit()
            flash('Your item will be delivered in one day. Incase of any query,please contact us and provide your order number .Your order number is '+str(userorder),category='info')
        return redirect(url_for('deliveryaudio_page'))
    if request.method == 'GET':  
        return render_template('Deliveryaudio.html',form=form)

@app.route('/adminregister', methods=['GET', 'POST'])
def adminregister():
    form = RegisteradminForm()
    if form.validate_on_submit():
        user_to_create = Employee(username=form.username.data, email=form.email.data, employeecode=form.employeecode.data, password=form.password1.data)
        # submit changes to database 
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('adminpage'))
    #if there are no errors from the validations
    if form.errors !={}:
        for err_msg in form.errors.values():
           flash(f'Error in creating user:{err_msg}',category='danger') 
    return render_template('adminregister.html', form=form)
     
@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin_page():
    form = LoginadminForm()
    if form.validate_on_submit():#check is the user exists and if so,if there details match
        attempted_user = Employee.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):#receives attempted password as parameter
            login_user(attempted_user)
            return redirect(url_for('adminpage'))
        else:
            flash('Username or Password is invalid',category='danger')
    return render_template('adminlogin.html', form=form)

@app.route('/adminlogout')
def adminlogout_page():
    logout_user()
    return redirect(url_for('login_page'))

@app.route('/admin')
def adminpage():
    laptops = Laptops.query.all()
    smartphones = Smartphones.query.all()
    audio = Audio.query.all()
    smartphones2=[]
    laptops2 = []
    audios2 = []
    for smartphone in smartphones:
        if smartphone.owner is not None:
            smartphones2.append(smartphone)
    for laptop in laptops:
        if laptop.lapowner is not None:
            laptops2.append(laptop)
    for a in audio:
        if a.adowner is not None:
            audios2.append(a)
    deliverydates = []
    odates = []
    for s in smartphones2:
        odate = Hevadaelectronics.query.filter_by(devid = s.devid).first()
        odate = odate.orderdate
        deliverydate = odate + datetime.timedelta(days=1)
        deliverydates.append(deliverydate)
        odates.append(odate)
    owners = []
    for smartphone in smartphones2:
        ownerid = smartphone.owner
        owners.append(ownerid)
    usernames = []
    for o in owners:
        ownerdetails = User.query.filter_by(id = o).first()
        username = ownerdetails.username
        usernames.append(username)
    companies = []
    for s in smartphones2:
        deltrack = Hevadaelectronics.query.filter_by(devid = s.devid).first()
        deltrack = deltrack.deltrackno
        cname = Deliverycompany.query.filter_by(deltrackno = deltrack).first()
        cname = cname.delname
        companies.append(cname)

    ldeliverydates = []
    lodates = []
    for l in laptops2:
        lodate = Hevadaelectronics.query.filter_by(devid = l.devid).first()
        lodate = lodate.orderdate
        ldeliverydate = lodate + datetime.timedelta(days=1)
        ldeliverydates.append(ldeliverydate)
        lodates.append(lodate)
    lowners = []
    for laptop in laptops2:
        ownerid = laptop.lapowner
        lowners.append(ownerid)
    lusernames = []
    for o in lowners:
        ownerdetails = User.query.filter_by(id = o).first()
        username = ownerdetails.username
        lusernames.append(username)
    lcompanies = []
    for l in laptops2:
        deltrack = Hevadaelectronics.query.filter_by(devid = l.devid).first()
        deltrack = deltrack.deltrackno
        cname = Deliverycompany.query.filter_by(deltrackno = deltrack).first()
        cname = cname.delname
        lcompanies.append(cname)

    adeliverydates = []
    aodates = []
    for a in audios2:
        aodate = Hevadaelectronics.query.filter_by(devid = a.devid).first()
        aodate = aodate.orderdate
        adeliverydate = aodate + datetime.timedelta(days=1)
        adeliverydates.append(adeliverydate)
        aodates.append(aodate)
    aowners = []
    for a in audios2:
        ownerid = a.adowner
        aowners.append(ownerid)
    ausernames = []
    for o in aowners:
        ownerdetails = User.query.filter_by(id = o).first()
        username = ownerdetails.username
        ausernames.append(username)
    acompanies = []
    for a in audios2:
        deltrack = Hevadaelectronics.query.filter_by(devid = a.devid).first()
        deltrack = deltrack.deltrackno
        cname = Deliverycompany.query.filter_by(deltrackno = deltrack).first()
        cname = cname.delname
        acompanies.append(cname)
    return render_template('admin.html', laptops = laptops2, smartphones = smartphones2,
                           audio = audios2, deliverydates = deliverydates, 
                           orderdates = odates, usernames = usernames,
                           companies = companies, ldeliverydates = ldeliverydates, lodates = lodates,
                           lusernames = lusernames, lcompanies = lcompanies, adeliverydates = adeliverydates, 
                           aodates = aodates,
                           ausernames = ausernames, acompanies = acompanies)

@app.route('/managesmartphones')
def managesmartphones():
    smartphones = Smartphones.query.all()
    return render_template('managesmartphones.html', smartphones = smartphones)

@app.route('/managelaptops')
def managelaptops():
    laptops = Laptops.query.all()
    return render_template('managelaptops.html', laptops = laptops)

@app.route('/manageaudio')
def manageaudio():
    audio = Audio.query.all()
    return render_template('manageaudio.html', audio = audio)

@app.route('/addiphones',methods = ['GET','POST'])
def addiphones():
    form = AddiphonesForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        storage = form.storage.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            phone = Smartphones(devid = did.devid, devname = model, devcolor = color,
                                devstorage = storage, devamount = price)
            db.session.add(phone)
            db.session.commit()
        flash("Item(s) added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockiphones.html', form = form)

@app.route('/addsamsungs',methods = ['GET','POST'])
def addsamsungs():
    form = AddamsungsForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        storage = form.storage.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            phone = Smartphones(devid = did.devid, devname = model, devcolor = color,
                                devstorage = storage, devamount = price)
            db.session.add(phone)
            db.session.commit()
        flash("Item(s)added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restocksamsung.html', form = form)

@app.route('/addoneplus',methods = ['GET','POST'])
def addoneplus():
    form = AddoneplusForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        storage = form.storage.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            phone = Smartphones(devid = did.devid, devname = model, devcolor = color,
                                devstorage = storage, devamount = price)
            db.session.add(phone)
            db.session.commit()
        flash("Item(s) added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockoneplus.html', form = form)

@app.route('/addsurface',methods = ['GET','POST'])
def addsurface():
    form = AddsurfaceForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        ram = form.ram.data
        processor = form.processor.data
        storage = form.storage.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            laptop = Laptops(devid = did.devid, lapname = model, lapprocessor = processor,lapcolor = color,
                                lapstorage = storage, lapram = ram, lapamount = price)
            db.session.add(laptop)
            db.session.commit()
        flash("Item(s)added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restocksurface.html', form = form)

@app.route('/addmacbook',methods = ['GET','POST'])
def addmacbook():
    form = AddmacbookForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        ram = form.ram.data
        processor = form.processor.data
        storage = form.storage.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            laptop = Laptops(devid = did.devid, lapname = model, lapprocessor = processor,lapcolor = color,
                                lapstorage = storage, lapram = ram, lapamount = price)
            db.session.add(laptop)
            db.session.commit()
        flash("Item(s) added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockmacbook.html', form = form)

@app.route('/addhp',methods = ['GET','POST'])
def addhp():
    form = AddhpForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        ram = form.ram.data
        processor = form.processor.data
        storage = form.storage.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            laptop = Laptops(devid = did.devid, lapname = model, lapprocessor = processor,lapcolor = color,
                                lapstorage = storage, lapram = ram, lapamount = price)
            db.session.add(laptop)
            db.session.commit()
        flash("Item(s) has been added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockhp.html', form = form)

@app.route('/addairpods',methods = ['GET','POST'])
def addairpods():
    form = AddairpodsForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            aud = Audio(devid = did.devid, audioname = model, audiocolor = color, 
                                audioamount = price)
            db.session.add(aud)
            db.session.commit()
        flash("Item(s) added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockairpods.html', form = form)

@app.route('/addbose',methods = ['GET','POST'])
def addbose():
    form = AddboseForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            aud = Audio(devid = did.devid, audioname = model, audiocolor = color, 
                                audioamount = price)
            db.session.add(aud)
            db.session.commit()
        flash("Item(s) added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockbose.html', form = form)

@app.route('/addbeats',methods = ['GET','POST'])
def addbeats():
    form = AddbeatsForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            aud = Audio(devid = did.devid, audioname = model, audiocolor = color, 
                                audioamount = price)
            db.session.add(aud)
            db.session.commit()
        flash("Item(s) added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockbeats.html', form = form)

@app.route('/addjbl',methods = ['GET','POST'])
def addjbl():
    form = AddjblForm()
    if form.validate_on_submit():
        model = form.model.data
        color = form.color.data
        price = form.price.data
        units = form.units.data
        for i in range(units):
            dev = Devices()
            db.session.add(dev)
            db.session.commit()
            did = Devices.query.filter_by(devid = dev.devid).first()
            aud = Audio(devid = did.devid, audioname = model, audiocolor = color, 
                                audioamount = price)
            db.session.add(aud)
            db.session.commit()
        flash("Item(s) added",category = 'info')
        return redirect(url_for('adminpage'))
    return render_template('restockjbl.html', form = form)

@app.route('/register',methods = ['GET','POST'])
def register_page():
    form = Registerform()
    # comments will be executed when user has clicked the submit button
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email=form.email.data, password=form.password1.data)
        # submit changes to database 
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        return redirect(url_for('home_page'))
    #if there are no errors from the validations
    if form.errors !={}:
        for err_msg in form.errors.values():
           flash(f'Error in creating user:{err_msg}',category='danger')
    return render_template('Register.html',form = form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():#check is the user exists and if so,if there details match
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):#receives attempted password as parameter
            login_user(attempted_user)
            return redirect(url_for('home_page'))
        else:
            flash('Username or Password is invalid',category='danger')
    return render_template('Login.html',form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out",category='info')
    return redirect(url_for('login_page'))

if __name__ =='__main__':
    app.run(debug=True)