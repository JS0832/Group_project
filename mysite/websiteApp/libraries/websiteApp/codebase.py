# Use "import libraries.websiteApp.codebase as game" on views!

# This is the functions used for the games within the websiteApp
# All functions used by website are included here. This should decrease repeated
# code and also improve readability of views.
# Add functions as necessary!

def stringComparison(stringA, stringB):
        # Compares two strings, if they are the same when all unnecessary characters
        # Are removed, this returs true. Else false.

    characterToRemove = [" ", "-", ",", "."]
        #Any character that may cause discrepancies between correct inputs.

    for character in characterToRemove:
        # Remove the unnecessary characters by replacing them with nothing
        stringA = stringA.replace(character, '')
        stringB = stringB.replace(character, '')
    
    if stringA.lower() == stringB.lower():
        return True
    else:
        return False
    