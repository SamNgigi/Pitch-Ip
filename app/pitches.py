from .models import Pitch


def get_pitches():
    pitch_list = []
    pitch_one = Pitch(0, 'Elevator Pitch Example for an Professional Accountant',
                      """
     A plumber approached me because while he’s a very good plumber he had no idea how to improve the profitability of his business.

     I set up a simple reporting system for him so his numbers are always up to date, and he can do future forecasting for his business.

     I’m happy to report that based on this information he was able to increase his profit by 17% last year.

     A great lead for me is a trade professional.
     """,
                      'Improv Andy',
                      'Business')
    pitch_two = Pitch(1, 'Research Job Pitch',
                      """
                    Hi, my name is Samantha Atcheson, and I am a senior Environmental Sciences major. I’m looking for a
position that will allow me to use my research and analysis skills. Over the past few years, I’ve been
strengthening these skills through my work with a local watershed council on conservation strategies to
support water quality and habitats. Eventually, I’d like develop education programs on water
conservation awareness. I read that your organization is involved in water quality projects. Can you tell
me how someone with my experience may fit into your organization?
                    """,
                      'Samantha Atcheson',
                      'Science')

    pitch_list.extend((pitch_one, pitch_two))
    return pitch_list
