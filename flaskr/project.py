from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from flaskr.auth import login_required
from flaskr.db import get_db
import os

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


bp = Blueprint('project', __name__, url_prefix='/project')


@bp.route('/')
def index():
    # db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()
    return render_template('project/index.html')


@bp.route('/create', methods=['get', 'post'])
def create():
    if request.method == 'post':
        return redirect('/project/aggrement')
    else:
        return render_template('project/create.html')


@bp.route('/aggrement', methods=['get', 'post'])
def aggrement():
    if request.method == 'post':
        return redirect('/project/upload')
    else:
        return render_template('project/aggrement.html')


@bp.route('/metadata', methods=['get', 'post'])
def metadata():
    return render_template('project/metadata.html')



@bp.route('/upolad', methods=['get', 'post'])
def upload():
    if request.method == 'POST':
        print('file check')
        if 'file' in request.files:
            print('have file')
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            upload_path = os.path.join(basepath, 'static/uploads', f.filename)
            f.save(upload_path)
            print('uploading ...')
            return redirect('/project/metadata')
        else:
            print('3')
            return render_template('project/upload.html')
            #return '没有文件部分'




