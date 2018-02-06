import unittest
from app.models import Pitch, User
# from flask_login import current_user
# from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_James = User(
            username='James', password='potato', email='james@ms.com')
        self.new_pitch = Pitch(title='Elevator Pitch Example for an Professional Accountant',
                               body="Test Pitch",
                               author='Improv Andy',
                               category='business',
                               upvotes=1,
                               downvotes=0,
                               user=self.user_James)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(
            self.new_pitch.title, 'Elevator Pitch Example for an Professional Accountant')
        self.assertEquals(self.new_pitch.body, "Test Pitch")
        self.assertEquals(self.new_pitch.author,
                          'Improv Andy')
        self.assertEquals(self.new_pitch.category,
                          'business')
        self.assertEquals(self.new_pitch.upvotes,
                          1)
        self.assertEquals(self.new_pitch.downvotes,
                          0)
        self.assertEquals(self.new_pitch.user, self.user_James)

    def test_save_pitch(self):
        self.new_pitch.save_pitches()
        self.assertTrue(len(Pitch.query.all()) > 0)

    # def test_get_pitch_by_cat(self):
    #
    #     self.new_pitch.save_pitches()
    #     got_pitchs = Pitch.get_categories('business')
    #     self.assertTrue(len(got_pitchs) == 1)
