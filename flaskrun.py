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
        ownedCourtsNum = request.form['ownedCourtsNum']

        user.Locator(name, username, password, email, phone_number)

        for _ in range(ownedCourtsNum):
            return render_template('add_courts.html')

    return render_template('add_user_locator.html')


@app.route('/add_court', methods=['GET', 'POST'])
def add_court():
    if request.method == 'POST':
        type = request.form['type'] 
        location = request.form['location'] 
        pricePerHour = request.form['pricePerHour']
        week_days = request.form['week_days']
        weekend = request.form['weekend']

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
    app.run(debug=True)
