import tweepy
from Other import keys

#Authetication
def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path= list):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_with(message)

        print('Tweeted successfully!')


if __name__ == '__main__':
    api = api()
    tweet(api, 'This was tweeted from Python', 'chess.jpg')
