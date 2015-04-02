from twython import Twython, TwythonError

def main():
    APP_KEY = input('App Key: ')
    APP_SECRET = input('App Secret: ')
    OAUTH_TOKEN = input('OAuth Token: ')
    OAUTH_TOKEN_SECRET = input('OAuth Token Secret: ')
    screen_name = input('Screen Name: ')
    
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    user_timeline = twitter.get_user_timeline(screen_name=screen_name)
    twitter.update_status(status= input( 'Tweet: '))

if __name__ == "__main__":
	main()