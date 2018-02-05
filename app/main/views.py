from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import PitchForm  # CommentForm  UpdateProfile,
from ..models import User, Pitch  # Comment,
from flask_login import login_required
from .. import db, photos
# from ..pitches import get_pitches, get_pitch


@main.route('/')
def index():
    """
    Function that renders the index.html and its content
    """
    pitches = Pitch.query.all()

    return render_template('index.html', pitches=pitches)


@main.route('/business')
def business():
    """
    Function that renders the business category pitches and its content
    """
    business_pitch = Pitch.query.filter_by(category='business').all()

    return render_template('business.html', business=business_pitch)


@main.route('/jobs')
def jobs():
    """
    Function that renders the job category pitches and its content
    """

    jobs_pitch = Pitch.query.filter_by(category='jobs').all()

    return render_template('jobs.html', jobs=jobs_pitch)


@main.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        body = pitch_form.body.data
        author = pitch_form.author.data
        category = pitch_form.category.data
        # category=category
        new_pitch = Pitch(title=title, body=body,
                          author=author, category=category, upvotes=0, downvotes=0)
        new_pitch.save_pitches()
        return redirect(url_for('main.index'))

    return render_template('new.html', pitch_form=pitch_form)


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    pass


@main.route('/user/<uname>')
@login_required
def profile(uname):
    """
    Function that renders the profile page of our user
    """
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
