import unittest
from app.models import Pitch, User
from flask_login import current_user
from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_James = User(
            username='James', password='potato', email='james@ms.com')
        self.new_pitch = Pitch(title='Elevator Pitch Example for an Professional Accountant',
                               body="""
         A plumber approached me because while he’s a very good plumber he had no idea how to improve the profitability of his business.

         I set up a simple reporting system for him so his numbers are always up to date, and he can do future forecasting for his business.

         I’m happy to report that based on this information he was able to increase his profit by 17% last year.

         A great lead for me is a trade professional.
         """,
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
        self.assertEquals(self.new_pitch.movie_id, 12345)
        self.assertEquals(self.new_pitch.movie_title, 'Pitch for movies')
        self.assertEquals(self.new_pitch.image_path,
                          "https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_pitch.movie_pitch,
                          'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_pitch.user, self.user_James)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitchs = Pitch.get_pitchs(12345)
        self.assertTrue(len(got_pitchs) == 1)
