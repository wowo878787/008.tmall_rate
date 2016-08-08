# coding:utf-8

import sys
from flask import render_template, redirect, request, flash, session, current_app, url_for
from . import main
from .. import db
from ..models import Comment
from config import colors

reload(sys)
sys.setdefaultencoding('utf8')

good_colors = colors.good_colors  # 直接在视图函数里面调用colors.good_colors会报AttributeError,说colors里没有good_colors属性


@main.route('/', methods=['GET', 'POST'])
def index():
    session['past_path'] = request.path
    session['past_endpoint']=request.endpoint
    session['past_sth']=unicode(request.url_rule)
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.order_by(Comment.com_time.desc()).paginate(
        page, per_page=current_app.config['FLASKY_RATE_PER_PAGE'],
        error_out=False)
    comments = pagination.items
    return render_template('index.html', pagination=pagination, comments=comments, colors=good_colors)


@main.route('/colors/<color>')
def colors(color):
    session['past_path'] = request.path
    session['past_endpoint']=request.endpoint
    session['past_sth']=unicode(request.url_rule)
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.filter_by(good=color).paginate(
        page, per_page=current_app.config['FLASKY_RATE_PER_PAGE'],
        error_out=False)
    comments = pagination.items
    return render_template('index.html', pagination=pagination, comments=comments, colors=good_colors,
                           current_color=color)


@main.route('/delete/<id>')
def delete_rate(id):
    flash('id : %s 已删除.' % id,'alert alert-success')
    delete_id = Comment.query.filter_by(com_id=id).first()
    db.session.delete(delete_id)
    db.session.commit()
    # return render_template('test.html',target=delete_id)
    return redirect(session['past_path'])


@main.route('/refresh_data')
def refresh_data():
    flash('data已刷新.', 'alert alert-info')
    Comment.generate_data()
    return redirect(url_for('.index'))


@main.route('/delete_data')
def delete_data():
    flash('data已删除.', 'alert alert-danger')
    Comment.query.delete()
    return redirect(url_for('.index'))


@main.route('/test')
def test():
    return render_template('test.html')
