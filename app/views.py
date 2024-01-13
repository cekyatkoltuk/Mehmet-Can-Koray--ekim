from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Client, Blog, About, Services, Contact
from app.forms import ContactForm
from sqlalchemy.exc import IntegrityError


@app.route("/")
def index():
    clients_data = Client.query.all()
    blogs_data = Blog.query.all()
    abouts_data = About.query.all()
    servis_data = Services.query.all()
    return render_template(
        "index.html",
        blogs=blogs_data,
        about=abouts_data,
        servis=servis_data,
        clients=clients_data,
    )


@app.route("/whatwedo")
def whatwedo():
    blogs_data = Blog.query.all()
    return render_template("whatwedo.html", blogs=blogs_data)


@app.route("/about")
def about():
    abouts_data = About.query.all()
    return render_template("about.html", about=abouts_data)


@app.route("/client")
def client():
    clients_data = Client.query.all()
    return render_template("client.html", clients=clients_data)


def add_contact(name, phonenumber, email, message):
    try:
        new_contact = Contact(
            name=name, phonenumber=phonenumber, email=email, metin=message
        )
        db.session.add(new_contact)
        db.session.commit()
        flash("Talebiniz alınmıştır. Teşekkür ederiz!", "success")
    except IntegrityError:
        db.session.rollback()
        flash(
            "Bu isim veya telefon numarası zaten kayıtlıdır. Lütfen farklı bir isim veya telefon numarası deneyin.",
            "error",
        )
    except Exception as e:
        db.session.rollback()
        flash("Bir hata oluştu. Lütfen daha sonra tekrar deneyin.", "error")
    finally:
        db.session.close()


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        add_contact(
            form.name.data, form.phonenumber.data, form.email.data, form.message.data
        )
        flash("Talebiniz alınmıştır. Teşekkür ederiz!", "success")
        return redirect(url_for("contact"))  # Başarı sayfasına yönlendirme

    return render_template("contact.html", form=form)


@app.route("/services")
def services():
    servis_data = Services.query.all()
    return render_template("services.html", servis=servis_data)


@app.route("/login")
def login():
    return render_template("login.html")
