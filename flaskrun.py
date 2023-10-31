from flask import Flask, render_template, request, redirect, session
import user

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Defina uma chave secreta para a sessão

# Dados de usuários (para fins de demonstração)
usuarios = {
    'locador': {'username': 'locador', 'password': 'senha_locador'},
    'locatario': {'username': 'locatario', 'password': 'senha_locatario'}
}


@app.route('/', methods=['GET', 'POST'])
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
        ownedCourtsNum = int(request.form['ownedCourtsNum'])

        user.Locator(name, username, password, email, phone_number)

        for _ in range(ownedCourtsNum):
            return render_template('add_courts.html')

    return render_template('add_user_locator.html')


@app.route('/add_courts', methods=['GET', 'POST'])
def add_courts(): ## PRECISA CONSERTAR REQUESTS DOS HORÁRIOS --> DAR REQUEST NO 'value'
    if request.method == 'POST':
        courtType = request.form['courtType'] 
        location = request.form['location'] 
        pricePerHour = request.form['pricePerHour']
        hour_0 = int(request.form.get("hour-0"))
        hour_1 = int(request.form.get("hour-1"))
        hour_2 = int(request.form.get("hour-2"))
        hour_3 = int(request.form.get("hour-3"))
        hour_4 = int(request.form.get("hour-4"))
        hour_5 = int(request.form.get("hour-5"))
        hour_6 = int(request.form.get("hour-6"))
        hour_7 = int(request.form.get("hour-7"))
        hour_8 = int(request.form.get("hour-8"))
        hour_9 = int(request.form.get("hour-9"))
        hour_10 = int(request.form.get("hour-10"))
        hour_11 = int(request.form.get("hour-11"))
        hour_12 = int(request.form.get("hour-12"))
        hour_13 = int(request.form.get("hour-13"))
        hour_14 = int(request.form.get("hour-14"))
        hour_15 = int(request.form.get("hour-15"))
        hour_16 = int(request.form.get("hour-16"))
        hour_17 = int(request.form.get("hour-17"))
        hour_18 = int(request.form.get("hour-18"))
        hour_19 = int(request.form.get("hour-19"))
        hour_20 = int(request.form.get("hour-20"))
        hour_21 = int(request.form.get("hour-21"))
        hour_22 = int(request.form.get("hour-22"))
        hour_23 = int(request.form.get("hour-23"))
        we_hour_0 = int(request.form.get("we_hour-0"))
        we_hour_1 = int(request.form.get("we_hour-1"))
        we_hour_2 = int(request.form.get("we_hour-2"))
        we_hour_3 = int(request.form.get("we_hour-3"))
        we_hour_4 = int(request.form.get("we_hour-4"))
        we_hour_5 = int(request.form.get("we_hour-5"))
        we_hour_6 = int(request.form.get("we_hour-6"))
        we_hour_7 = int(request.form.get("we_hour-7"))
        we_hour_8 = int(request.form.get("we_hour-8"))
        we_hour_9 = int(request.form.get("we_hour-9"))
        we_hour_10 = int(request.form.get("we_hour-10"))
        we_hour_11 = int(request.form.get("we_hour-11"))
        we_hour_12 = int(request.form.get("we_hour-12"))
        we_hour_13 = int(request.form.get("we_hour-13"))
        we_hour_14 = int(request.form.get("we_hour-14"))
        we_hour_15 = int(request.form.get("we_hour-15"))
        we_hour_16 = int(request.form.get("we_hour-16"))
        we_hour_17 = int(request.form.get("we_hour-17"))
        we_hour_18 = int(request.form.get("we_hour-18"))
        we_hour_19 = int(request.form.get("we_hour-19"))
        we_hour_20 = int(request.form.get("we_hour-20"))
        we_hour_21 = int(request.form.get("we_hour-21"))
        we_hour_22 = int(request.form.get("we_hour-22"))
        we_hour_23 = int(request.form.get("we_hour-23"))
        weedDays = [hour_0, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23]
        weekend = [we_hour_0, we_hour_1, we_hour_2, we_hour_3, we_hour_4, we_hour_5, we_hour_6, we_hour_7, we_hour_8, we_hour_9, we_hour_10, we_hour_11, we_hour_12, we_hour_13, we_hour_14, we_hour_15, we_hour_16, we_hour_17, we_hour_18, we_hour_19, we_hour_20, we_hour_21, we_hour_22, we_hour_23]
    return render_template('add_courts.html')

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


if __name__ == '__main__':
    app.run(debug=True, port='8080')
