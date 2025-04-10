# 1. 创建 Flask 工程
# 在终端运行以下命令
# pip install flask flask-sqlalchemy flask-migrate flask-wtf flask-login

from flaskr import create_app

# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# import os
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'your_secret_key'
#
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
#
#
# # 2. 数据库模型
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#
#
# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     organization = db.Column(db.String(255), nullable=True)
#     deadline = db.Column(db.Date, nullable=True)
#     creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     status = db.Column(db.String(20), default='pending')
#     approval_comment = db.Column(db.Text, nullable=True)
#
#
# class Metadata(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
#     data = db.Column(db.Text, nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     approved = db.Column(db.Boolean, default=False)
#
#
# class DataProcessAgreement(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), unique=True, nullable=False)
#     file_path = db.Column(db.String(255), nullable=False)
#
#
# # 3. 视图和路由
# @app.route('/projects')
# def project_list():
#     projects = Project.query.all()
#     return render_template('project_list.html', projects=projects)
#
#
# @app.route('/metadata')
# def metadata_list():
#     metadata = Metadata.query.all()
#     return render_template('metadata_list.html', metadata=metadata)
#
#
# @app.route('/agreements')
# def agreements_list():
#     agreements = DataProcessAgreement.query.all()
#     return render_template('agreements_list.html', agreements=agreements)
#
#
# # 4. 运行应用
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
