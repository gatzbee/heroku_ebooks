'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'm5Yo5cA0Wz6jXFKe2aLEhTLiI'
MY_CONSUMER_SECRET = 'badSbsc7lhAlp7diGEsX41XFWm8UXiVz7EsnidOUQbBLcrOk0k'
MY_ACCESS_TOKEN_KEY = '67645636-O0faN878wJoWb4P1jqXtJRghHlHntDl1p5SLeugk6'
MY_ACCESS_TOKEN_SECRET = '	ECIh0sYhvNc5KqZmhXCJFmfOhVJfTLGTVuqGpv0mU9CR4'

SOURCE_ACCOUNTS = ["gatzby_, theoddestbrain, haishidao"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "theoddestbrain" #The name of the account you're tweeting to.
