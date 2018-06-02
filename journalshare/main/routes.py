from flask import render_template, request, Blueprint
from journalshare.models import Journal

main = Blueprint('main', __name__)

@main.route("/home")
def home():
	return render_template('home.html')

@main.route("/alljournals")
def alljournals():
	page = request.args.get('page', 1, type=int)
	journals = Journal.query.filter_by(private=False).order_by(Journal.date_posted.desc()).paginate(page=page, per_page=3)
	journals = Journal.query.filter_by(private=False).order_by(Journal.date_posted.desc()).paginate(page=page, per_page=3)
	return render_template('alljournals.html', journals=journals)

@main.route("/about")
def about():
	return render_template('about.html', title='About')