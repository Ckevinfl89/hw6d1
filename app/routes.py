# from app import app
# from flask import render_template

# # Add a route
# @app.route('/')
# def index():
#     colors = [{"name":"Blue", "pic_url":"https://media.architecturaldigest.com/photos/5ba551bb44966b64d8d5fc2b/16:9/w_2560%2Cc_limit/hyper-blue-4.jpg"}, {"name":"Red", "pic_url":"https://images.unsplash.com/photo-1568535904307-f48b760a39f3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cmVkJTIwdGV4dHVyZXxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80"}, {"name":"Black", "pic_url":"https://www.al.com/resizer/KsZaj46Thx9ARTCiYaMEfX6kHiw=/1280x0/smart/cloudfront-us-east-1.images.arcpublishing.com/advancelocal/NSDL77J3KJFZXCK3MFWAV7HMUE.JPG"}, {"name":"Green", "pic_url":"https://htmlcolorcodes.com/assets/images/colors/dark-green-color-solid-background-1920x1080.png"}, {"name":"Pink", "pic_url":"https://img.freepik.com/premium-photo/sunset-sky-shot-clouds-generative-ai_384720-686.jpg"}]
#     return render_template('index.html', first_name='Peeps', colors=colors)

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/favorite')
# def favorite():
#     colors = [{"name":"Blue", "pic_url":"https://media.architecturaldigest.com/photos/5ba551bb44966b64d8d5fc2b/16:9/w_2560%2Cc_limit/hyper-blue-4.jpg"}]
#     return render_template('favorite.html', colors=colors)

from flask import render_template, redirect, url_for
from app import app, db
from app.models import Contact
from app.forms import ContactForm
from datetime import datetime

@app.route('/')
def home():
    contacts = Contact.query.all()
    last_loaded_date = datetime.utcnow()
    return render_template('home.html', contacts=contacts, last_loaded_date=last_loaded_date)


@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data,
            address=form.address.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_contact.html', form=form)