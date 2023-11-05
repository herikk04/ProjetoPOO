from flask import Flask, render_template, request, redirect, session, url_for, Response, jsonify
import user
import json       

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Defina uma chave secreta para a sessão

# Dados de usuários (para fins de demonstração)
usuarios = {
    'locador': {'username': 'locador', 'password': 'senha_locador'},
    'locatario': {'username': 'locatario', 'password': 'senha_locatario'}
}

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
        if username == usuarios[user_type]['username'] and password == usuarios[user_type]['password']:
            session['username'] = username
            session['user_type'] = user_type
            return redirect('/dashboard')
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

        thisUser = user.Locator(name, email, phone_number, username, password)
        userID = thisUser.getSelfUserID()
        userType = thisUser.getSelfType()


        return redirect(url_for('add_courts', userID=userID, userType=userType))

    return render_template('add_user_locator.html')


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
        hour_0 = int(data.get("hour-0", 0))
        hour_1 = int(data.get("hour-1", 0))
        hour_2 = int(data.get("hour-2", 0))
        hour_3 = int(data.get("hour-3", 0))
        hour_4 = int(data.get("hour-4", 0))
        hour_5 = int(data.get("hour-5", 0))
        hour_6 = int(data.get("hour-6", 0))
        hour_7 = int(data.get("hour-7", 0))
        hour_8 = int(data.get("hour-8", 0))
        hour_9 = int(data.get("hour-9", 0))
        hour_10 = int(data.get("hour-10", 0))
        hour_11 = int(data.get("hour-11", 0))
        hour_12 = int(data.get("hour-12", 0))
        hour_13 = int(data.get("hour-13", 0))
        hour_14 = int(data.get("hour-14", 0))
        hour_15 = int(data.get("hour-15", 0))
        hour_16 = int(data.get("hour-16", 0))
        hour_17 = int(data.get("hour-17", 0))
        hour_18 = int(data.get("hour-18", 0))
        hour_19 = int(data.get("hour-19", 0))
        hour_20 = int(data.get("hour-20", 0))
        hour_21 = int(data.get("hour-21", 0))
        hour_22 = int(data.get("hour-22", 0))
        hour_23 = int(data.get("hour-23", 0))
        we_hour_0 = int(data.get("we_hour-0", 0))
        we_hour_1 = int(data.get("we_hour-1", 0))
        we_hour_2 = int(data.get("we_hour-2", 0))
        we_hour_3 = int(data.get("we_hour-3", 0))
        we_hour_4 = int(data.get("we_hour-4", 0))
        we_hour_5 = int(data.get("we_hour-5", 0))
        we_hour_6 = int(data.get("we_hour-6", 0))
        we_hour_7 = int(data.get("we_hour-7", 0))
        we_hour_8 = int(data.get("we_hour-8", 0))
        we_hour_9 = int(data.get("we_hour-9", 0))
        we_hour_10 = int(data.get("we_hour-10", 0))
        we_hour_11 = int(data.get("we_hour-11", 0))
        we_hour_12 = int(data.get("we_hour-12", 0))
        we_hour_13 = int(data.get("we_hour-13", 0))
        we_hour_14 = int(data.get("we_hour-14", 0))
        we_hour_15 = int(data.get("we_hour-15", 0))
        we_hour_16 = int(data.get("we_hour-16", 0))
        we_hour_17 = int(data.get("we_hour-17", 0))
        we_hour_18 = int(data.get("we_hour-18", 0))
        we_hour_19 = int(data.get("we_hour-19", 0))
        we_hour_20 = int(data.get("we_hour-20", 0))
        we_hour_21 = int(data.get("we_hour-21", 0))
        we_hour_22 = int(data.get("we_hour-22", 0))
        we_hour_23 = int(data.get("we_hour-23", 0))
        weedDays = [hour_0, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23]
        weekend = [we_hour_0, we_hour_1, we_hour_2, we_hour_3, we_hour_4, we_hour_5, we_hour_6, we_hour_7, we_hour_8, we_hour_9, we_hour_10, we_hour_11, we_hour_12, we_hour_13, we_hour_14, we_hour_15, we_hour_16, we_hour_17, we_hour_18, we_hour_19, we_hour_20, we_hour_21, we_hour_22, we_hour_23]
        print(f"userID: {userID}, userType: {userType}")
        thisUser = user.User.getUserObject(userType, userID)
        print(thisUser)
        thisUser.addCourts(courtType, location, pricePerHour, weekend, weedDays)
    
        return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return "Invalid request."        


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Bem-vindo, {session["username"]} ({session["user_type"]})! Este é o painel de controle.'
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_type', None)
    
    return redirect('/')

@app.route('/user_created')
def user_created():
    return render_template('user_created.html')


if __name__ == '__main__':
    app.run(debug=True, port='8080')
