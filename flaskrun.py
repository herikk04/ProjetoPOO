from flask import Flask, render_template, request, redirect, session

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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['userType']

        # Check if the username already exists
        if username in usuarios:
            error = 'Username already exists. Choose a different username.'
            
        else:
            usuarios[username] = {'username': username, 'password': password}
            return redirect('/')
    
        if user_type == "Locator":
            return redirect('/add_locator_page')
        
        elif user_type == "Renter":
            # Redirect to the dashboard or any other page for locatarios
            return redirect('/dashboard')
        
        else:
            error = 'Tipo de usuário inválido. Por favor, selecione Locador ou Locatário.'

    return render_template('add_user.html', error=None)



@app.route('/add_locator', methods=['POST'])
def add_locator():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone_number = request.form['phoneNumber']
    owned_courts_num = int(request.form['ownedCourtsNum'])

    locator_data = {
        'name': name,
        'username': username,
        'password': password,
        'email': email,
        'phone_number': phone_number,
        'owned_courts_num': owned_courts_num
    }

    return redirect('/')


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
