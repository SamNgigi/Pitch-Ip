#!/usr/bin/env python3.6
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Pitch, Comment


# Creating the app instance
app = create_app('production')
# app = create_app('test')
# app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """
    Running the unit tests.
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    # , User=User, Review=Review


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitch=Pitch, Comment=Comment)


if __name__ == '__main__':
    manager.run()
