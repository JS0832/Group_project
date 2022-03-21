"""Codebase for Group Engineering Software Project"""
# Use "import libraries.websiteApp.codebase as game" on views!

# This is the functions used for the games within the websiteApp
# All functions used by website are included here. This should decrease repeated
# code and also improve readability of views.
# Add functions as necessary!

from websiteApp.models import *

def string_comparison(string_a: str, string_b: str, char_remove: list = [" ","-",",","."]) -> bool:
    """Compares two strings, removing some characters.
    Returns True if the same

    stringA : str
    stringB : str
    charRemove : list (default = [" ","-",",","."])
        A list of characters to remove from both strings
    """
        #Any character that may cause discrepancies between correct inputs.

    for character in char_remove:
        # Remove the unnecessary characters by replacing them with nothing
        string_a = string_a.replace(character, '')
        string_b = string_b.replace(character, '')

    return string_b.lower() == string_a.lower()

def riddle_check(riddle: Riddle,player_response: str) -> bool:
    """Checks if the resonse to a riddle is the correct answer.
    Returns true if correct

    riddle: Riddle
        That the answer is to be checked against
    player_response: str
        The users response to the riddle
    """
    return string_comparison(riddle.answer, player_response)

def award_points(username: str, points: int) -> bool:
    """Awards points to a selected user
    Returns true if applied

    username: str
        The username of the user to add points
    points: int
        the ammount of points awarded
    """
    applied = False
    user = User.objects.get(username=username)
        # get the users database insert

    if user is not None:
        retrieved_points = user.profile.total_points
            # Retrieve points from the database
        user.profile.total_points = retrieved_points + points
            # Add the points given
        user.save()
            # Apply changes
        applied = True
        print("Added points!")
    return applied
