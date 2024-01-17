from flask import Flask
from app import views

app = Flask(__name__) # webserver gateway interphase (WSGI)


app.add_url_rule('/', 'index', views.index) # route '/' to index view function
app.add_url_rule('/app/', 'app', views.app)
app.add_url_rule('/app/gender/', 'gender', views.genderapp, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug=True)