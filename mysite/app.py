from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')


@app.route("/contato")
def contato():
  return render_template('contato.html')

@app.route("/informações")
def inf_basica():
  return render_template('inf_basica.html')

@app.route("/sobre")
def sobre():
  return render_template('sobre.html')


if __name__ == "__main__":
  app.run(debug=True)