# define simple flask app
from flask import Flask,render_template, session
from flask_session import Session
from flask import request
from models.code_breaker import CodeBreaker

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save_secret_code', methods=['post'])
def save_secret_code():
    secret_code = request.form.get('secret_code')
    session['secret_code'] = secret_code
    code_breaker = CodeBreaker(secret_code)
    result = 'The secret was config correctly' if code_breaker.is_valid else 'The secret was NOT config correctly'

    return render_template('game.html', result = result)

@app.route('/guess', methods=['post'])
def guess():
    guess_code = request.form.get('your_guess')
    secret_code = session['secret_code']
    
    code_breaker = CodeBreaker(secret_code)
    
    result = code_breaker.guess(guess_code)

    if not result:
        result = 'Invalid number, the number must have 4 digits'

    return render_template('game.html', result = result)

if __name__ == "__main__":
    app.run(debug=True)
