import os
from app import create_app, db
from app.models import Comment
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def turn_eval(*args, **kwargs):
    result = eval(*args, **kwargs)
    return result


def turn_type(*args, **kwargs):
    result = type(*args, **kwargs)
    return result


env = app.jinja_env
env.filters['turn_eval'] = turn_eval
env.filters['turn_type'] = turn_type


def make_shell_context():
    return dict(app=app, db=db, Comment=Comment)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
