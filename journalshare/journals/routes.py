from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from journalshare import db
from journalshare.models import Journal
from journalshare.journals.forms import JournalForm

journals = Blueprint('journals', __name__)

@journals.route("/journal/new", methods=['GET', 'POST'])
@login_required
def new_journal():
	form = JournalForm()
	if form.validate_on_submit():
		journal = Journal(title=form.title.data, content=form.content.data, private=True if request.form['privacy_setting']=='on' else False, author=current_user)
		db.session.add(journal)
		db.session.commit()
		flash('Your journal entry has been created!', 'success')
		return redirect(url_for('main.home'))
	return render_template('create_journal.html', title='New Journal Entry', form=form, legend='New Journal Entry')

@journals.route("/journal/<int:journal_id>")
def journal(journal_id):
	journal = Journal.query.get_or_404(journal_id)
	return render_template('journal.html', title=journal.title, journal=journal)

@journals.route("/journal/<int:journal_id>/update", methods=['GET', 'POST'])
@login_required
def update_journal(journal_id):
	journal = Journal.query.get_or_404(journal_id)
	if journal.author != current_user:
		abort(403)
	form = JournalForm()
	if form.validate_on_submit():
		journal.title = form.title.data
		journal.content = form.content.data
		db.session.commit()
		flash('Your journal entry has been updated!', 'success')
		return redirect(url_for('journals.journal', journal_id=journal.id))
	elif request.method == 'GET':
		form.title.data = journal.title
		form.content.data = journal.content
	return render_template('create_journal.html', title='Update Journal Entry', form=form, legend='Update Journal Entry')

@journals.route("/journal/<int:journal_id>/delete", methods=['POST'])
@login_required
def delete_journal(journal_id):
	journal = journal.query.get_or_404(journal_id)
	if journal.author != current_user:
		abort(403)
	db.session.delete(journal)
	db.session.commit()
	flash('Your journal entry has been deleted!', 'success')
	return redirect(url_for('main.home'))