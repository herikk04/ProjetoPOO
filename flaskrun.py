from flask import Flask, render_template, request, redirect, session, url_for, jsonify, make_response

import user, dataRecover, locator, renter, agenda

from pandas import read_csv, DataFrame


def dataManagement():
    firstRun = True
    try: 
        locatorData = read_csv("userData/locatorData.csv")
        if not locatorData.empty:
            ## print("______________________________________")
            ## print("Recovering locator data...")
            firstRun = False

    except: 
        ## print("locator data not found...")
        print()
    
    try:    
        renterData = read_csv("userData/renterData.csv")
        if not renterData.empty:
            ## print("______________________________________")
            ## print("Recovering renter data...")
            firstRun = False
        
                  
    except: 
        ## print("renter data not found...")
        print()
    
    if not firstRun:
        dataRecover.DataRecover.recoverLocatorObjects()
        dataRecover.DataRecover.recoverRenterObjects()

    if firstRun:
        ## print("______________________________________")
        ## print("Creating user first csv files...") 
        locatorData = DataFrame(user.User.userData["Locator"],columns=["userType","name","email","phoneNumber","username","password","locatorID","ownedCourts","object"])
        renterData = DataFrame(user.User.userData["Renter"], columns=["userType","name","email","phoneNumber","username","password","renterID","reservations","object"])
        locatorData.to_csv("userData/locatorData.csv", index=False)
        renterData.to_csv("userData/renterData.csv", index=False)


app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Em andamento


@app.route('/')
def redirect_to_login():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['userType']

        # Verificar as credenciais do usuário
        authentication = user.User.authenticateUser(username, password, user_type)
        if authentication[0]:
            session['username'] = username
            session['user_type'] = user_type
            if user_type == 'Locator':
                locatorID = authentication[1]
                return redirect(url_for('dashboard', locatorID=locatorID))
            elif user_type == 'Renter':
                renterID = authentication[1]
                return redirect(url_for('courts', renterID=renterID))
        else:
            error = 'Credenciais inválidas. Tente novamente.'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():

    return render_template('add_user.html')


@app.route('/add_user_locator', methods=['GET', 'POST'])
def add_user_locator():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone_number = request.form['phoneNumber']

        thisUser = locator.Locator(name, email, phone_number, username, password)
        userID = thisUser.locatorID
        userType = "Locator"


        return redirect(url_for('add_courts', userID=userID, userType=userType))

    return render_template('add_user_locator.html')


@app.route('/add_user_renter', methods=['GET', 'POST'])
def add_user_renter():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone_number = request.form['phoneNumber']

        thisUser = renter.Renter(name, email, phone_number, username, password)
        userID = thisUser.renterID
        userType = "Renter"

        return redirect(url_for('courts', userID=userID, userType=userType))

    return render_template('add_user_renter.html')


@app.route('/add_courts', methods=['GET', 'POST'])
def add_courts():
    if request.method == 'GET':
        userID = request.args.get('userID')
        userType = request.args.get('userType')

        return render_template('add_courts.html', userID=userID, userType=userType)
        
    elif request.method == 'POST':
        userID = int(request.args.get('userID'))
        userType = request.args.get('userType')
        data = request.get_json()
        courtType = data.get('courtType') 
        location = data.get('location') 
        pricePerHour = int(data.get('pricePerHour'))
        hour_0 = int(data.get("hour-0"))
        hour_1 = int(data.get("hour-1"))
        hour_2 = int(data.get("hour-2"))
        hour_3 = int(data.get("hour-3"))
        hour_4 = int(data.get("hour-4"))
        hour_5 = int(data.get("hour-5"))
        hour_6 = int(data.get("hour-6"))
        hour_7 = int(data.get("hour-7"))
        hour_8 = int(data.get("hour-8"))
        hour_9 = int(data.get("hour-9"))
        hour_10 = int(data.get("hour-10"))
        hour_11 = int(data.get("hour-11"))
        hour_12 = int(data.get("hour-12"))
        hour_13 = int(data.get("hour-13"))
        hour_14 = int(data.get("hour-14"))
        hour_15 = int(data.get("hour-15"))
        hour_16 = int(data.get("hour-16"))
        hour_17 = int(data.get("hour-17"))
        hour_18 = int(data.get("hour-18"))
        hour_19 = int(data.get("hour-19"))
        hour_20 = int(data.get("hour-20"))
        hour_21 = int(data.get("hour-21"))
        hour_22 = int(data.get("hour-22"))
        hour_23 = int(data.get("hour-23"))
        we_hour_0 = int(data.get("we-hour-0"))
        we_hour_1 = int(data.get("we-hour-1"))
        we_hour_2 = int(data.get("we-hour-2"))
        we_hour_3 = int(data.get("we-hour-3"))
        we_hour_4 = int(data.get("we-hour-4"))
        we_hour_5 = int(data.get("we-hour-5"))
        we_hour_6 = int(data.get("we-hour-6"))
        we_hour_7 = int(data.get("we-hour-7"))
        we_hour_8 = int(data.get("we-hour-8"))
        we_hour_9 = int(data.get("we-hour-9"))
        we_hour_10 = int(data.get("we-hour-10"))
        we_hour_11 = int(data.get("we-hour-11"))
        we_hour_12 = int(data.get("we-hour-12"))
        we_hour_13 = int(data.get("we-hour-13"))
        we_hour_14 = int(data.get("we-hour-14"))
        we_hour_15 = int(data.get("we-hour-15"))
        we_hour_16 = int(data.get("we-hour-16"))
        we_hour_17 = int(data.get("we-hour-17"))
        we_hour_18 = int(data.get("we-hour-18"))
        we_hour_19 = int(data.get("we-hour-19"))
        we_hour_20 = int(data.get("we-hour-20"))
        we_hour_21 = int(data.get("we-hour-21"))
        we_hour_22 = int(data.get("we-hour-22"))
        we_hour_23 = int(data.get("we-hour-23"))
        weedDays = [hour_0, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23]
        weekend = [we_hour_0, we_hour_1, we_hour_2, we_hour_3, we_hour_4, we_hour_5, we_hour_6, we_hour_7, we_hour_8, we_hour_9, we_hour_10, we_hour_11, we_hour_12, we_hour_13, we_hour_14, we_hour_15, we_hour_16, we_hour_17, we_hour_18, we_hour_19, we_hour_20, we_hour_21, we_hour_22, we_hour_23]
        ## print("______________________________________")
        ## print(f"userID: {userID}, userType: {userType}")
        thisUser = user.User.getUserObject(userType, userID)
        ## print(thisUser)
        courtagenda = dataRecover.DataRecover.filterAgendaData(weedDays, weekend)
        thisUser.addCourts(courtType, location, pricePerHour, courtagenda)
    
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return "Invalid request."        


@app.route('/dashboard', methods=['GET'])
def dashboard():
    locatorID = int(request.args.get('locatorID'))
    username = user.User.getUserObject("Locator", locatorID).username
    return render_template('dashboard.html', locatorID=locatorID, username=username)


@app.route('/courts', methods=['GET'])
def courts():
    renterID = int(request.args.get('renterID'))
    username = user.User.getUserObject("Renter", renterID).username
    resp = make_response(render_template('courts.html', username=username))
    resp.set_cookie('renterID', str(renterID))
    return resp


@app.route('/user_profile', methods=['GET'])
def user_profile():
    userId = int(request.args.get('userID'))
    userType = request.args.get('userType')
    thisUser = user.User.getUserObject(userType, userId)
    name = thisUser.name
    email = thisUser.email
    username = thisUser.username
    phoneNumber = thisUser.phoneNumber
    user_page = f"/dashboard?locatorID={userId}" if userType == "Locator" else f"/courts?renterID={userId}"
    return render_template('user_profile.html', name=name, email=email, username=username, phoneNumber=phoneNumber, user_page=user_page)

@app.route('/request_courts', methods=['GET'])
def request_courts():
    locatorID = request.args.get('locatorID')
    if locatorID != None:
        thisLocator = (user.User.getUserObject("Locator", int(locatorID)))
        courts = []
        for court in thisLocator.ownedCourts:
            courts.append(court.getDetails())
        return jsonify(courts=courts, locatorID=locatorID)
    else:
        courts = []
        for locator in user.User.userData["Locator"]:
            locatorID = locator["locatorID"]
            thisLocator = (user.User.getUserObject("Locator", locatorID))
            for court in thisLocator.ownedCourts:
                details = court.getDetails()
                details["locatorName"] = thisLocator.username
                courts.append(details)
        return jsonify(courts=courts)

## EM ANDAMENTO
@app.route('/request_agenda', methods=['GET'])
def request_agenda():
    courtID = int(request.args.get('courtID'))
    thisCourt = (user.User.getUserObject("Court", courtID))
    return jsonify(agenda=thisCourt.agenda)

## EM ANDAMENTO
@app.route('/request_locator_data', methods=['GET'])
def request_locator_data():
    locatorID = int(request.args.get('locatorID'))
    thisLocator = (user.User.getUserObject("Locator", locatorID))
    courts = []
    for court in thisLocator.ownedCourts:
        courts.append(court.getDetails())
    return jsonify(courts=courts, locatorID=locatorID)

## EM ANDAMENTO
@app.route('/request_renter_data', methods=['GET'])
def request_renter_data():
    renterID = int(request.args.get('renterID'))
    thisRenter = (user.User.getUserObject("Renter", renterID))
    reservations = []
    for reservation in thisRenter.reservations:
        reservations.append(reservation.getDetails())
    return jsonify(reservations=reservations, renterID=renterID)


@app.route('/rent_court', methods=['GET', 'POST'])
def rent_court():
    renterID = int(request.cookies.get('renterID'))
    courtID = int(request.args.get('courtID'))
    thisRenter = (user.User.getUserObject("Renter", renterID))
    locatorID = int(request.args.get('locatorID'))
    thisLocator = (user.User.getUserObject("Locator", locatorID))
    for court in thisLocator.ownedCourts:
        if court.courtID == courtID:
            thisCourt = court
    courtAgenda = court.agenda
    if request.method == 'GET':
        courtAgendaData = courtAgenda.courtAgenda
        courtAgendaData = agenda.Agenda.filterAgenda(courtAgendaData)
        return render_template('rent_court.html', courtID=courtID, renterID=renterID, tables=[courtAgendaData.to_html(classes='data')], titles=[''])
    elif request.method == 'POST':
        hours = request.getlist('rented')
        for hour in hours:
            thisCourt.rentCourt(hour, thisRenter)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_type', None)
    
    return redirect('/')


@app.route('/user_created')
def user_created():
    return render_template('user_created.html')


if __name__ == '__main__':
    dataManagement()
    app.run(debug=True, port=5000)
