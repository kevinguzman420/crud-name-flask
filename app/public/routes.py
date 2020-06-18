
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_required

from app.models import UserName

from . forms import FormName
from . import public_bp


@public_bp.route("/") #, methods=["GET", "POST"])
def index():
    form = FormName()
    users = UserName()
    users = users.get_all_user()
    # print(users[0])
    return render_template('public/index.html', form=form, users=users)

@public_bp.route("/create/user/", methods=["GET", "POST"])
def create_user():
    form = FormName()
    users = UserName()
    users = users.get_all_user()
    if form.validate_on_submit() and request.method == "POST":
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        user = UserName.get_by_email(email)
        if user is not None:
            flash(f"This account of {email} it\'s already in use. Provide other please.", "error")
        else:
            user = UserName(name=name, email=email, phone=phone)
            user.save()
            flash("User has been saved successfully.", "success")
        return redirect(url_for('public.index'))
    return render_template('public/index.html', form=form, users=users)


@public_bp.route("/modify/user/<int:id>/", methods=["GET", "POST"])
def modify_user(id):
    user = UserName.get_user_by_id(id)
    form = FormName(obj=user)
    if request.method == "POST":
        if form.validate_on_submit():
            user.name = form.name.data
            user.email = form.email.data
            user.phone = form.phone.data
            user.save()
            flash("User has been updated successfully.", "success")
            return redirect(url_for('public.index'))
        # else:
        #     flash("All fields are required.", "error")
    return render_template("public/update_user.html", form=form)

@public_bp.route("/detele/user/<int:id>/", methods=["GET"])
def delete_user(id):
    # session.clear()
    user = UserName.get_user_by_id(id)
    user.delete()
    flash("User has been deleted successfully.", "success")
    return redirect(url_for('public.index'))
    

