# -*- coding:utf-8 -*-
import os
from glob_app import create_app ,db
from glob_app.models import User
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
@manager.command
def test ():
    """ run your unit tests """
    pass

if __name__=='__main__':
    manager.run()

