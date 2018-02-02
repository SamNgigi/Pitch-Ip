#!/usr/bin/env python3.6
from app import create_app, db
# f/rom app.models import User, Review
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
# , User=User, Review=Review
# Creating the app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
