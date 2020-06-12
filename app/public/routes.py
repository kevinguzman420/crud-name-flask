
from flask import render_template

from . forms import FormName
from . import public_bp

@public_bp.route("/", methods=["GET", "POST"])
def index():
    form = FormName()
    return render_template('public/index.html', form=form)