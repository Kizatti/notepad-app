from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/health', methods=['GET'])
def health():
    # Health endpoint: verifies app is running and DB connection
    try:
        # Try a lightweight DB call
        db.session.execute('SELECT 1')
        return jsonify({'status': 'ok', 'database': 'connected'}), 200
    except Exception as e:
        # Return error details (stringified) so you can see what failed in the browser
        return jsonify({'status': 'error', 'database': 'disconnected', 'error': str(e)}), 500


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')  # Gets the note from the HTML

        # Validate input safely (note can be None)
        if not note or len(note.strip()) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note.strip(), user_id=getattr(current_user, 'id', None))
            db.session.add(new_note)
            try:
                db.session.commit()
                flash('Note added!', category='success')
            except Exception as e:
                # Rollback on error and log
                db.session.rollback()
                print(f"Error saving note: {e}")
                flash('Error saving note. Please try again.', category='error')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
