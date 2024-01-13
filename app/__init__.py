from flask import Flask,render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from os import path
from flask_babel import Babel


# Uygulama ve Veritabanı Yapılandırması
app = Flask(__name__)
babel = Babel(app)
basedir = path.abspath(path.dirname(__file__))
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, 'site.db')

# Uygulama Eklentileri
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.init_app(app)

# Model ve View İçe Aktarmaları
from app.models import User
from app.auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')

from app import views, models
from app.models import User

from app import app, db
from app.models import User

from app import app, db
from app.models import Contact
from app import app, db
from app.models import Subscriber

"""with app.app_context():
    # Uygulama bağlamı içinde işlemler
    user = User.query.filter_by(username="admin").first()
    if user:
        user.set_password("1234567890")
        # Şifre ve diğer ayarlar
        db.session.commit()"""


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

"""@babel.localeselector
def get_locale():
    # Kullanıcıya ait dil tercihini döndürür
    # Örnek: 'en' veya 'de'
    return 'en'"""

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['Name']
        phonenumber = request.form['Phone Number']
        email = request.form['Email Address']
        metin = request.form['Massage']

        # Create a new Contact object
        new_contact = Contact(name=name, phonenumber=phonenumber, email=email, metin=metin)

        # Add the new contact to the database
        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('success_page'))

    return render_template('contact.html')


@app.route('/subscribe', methods=['POST'])
def subscribe():
    if request.method == 'POST':
        phonenumber = request.form['phonenumber']
        email = request.form['email']

        # Create a new Subscriber object
        new_subscriber = Subscriber(phonenumber=phonenumber, email=email)

        try:
            # Add the new subscriber to the database
            db.session.add(new_subscriber)
            db.session.commit()
            return redirect(url_for('index'))  # 'index' yerine uygun sayfa adını belirtin
        except:
            db.session.rollback()
            return 'Veritabanına kayıt sırasında bir hata oluştu.'

    return render_template('subscribe.html')  # 'subscribe.html' dosyanızın adını belirtin