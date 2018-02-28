Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "B2eEMkKdZsssb3I6Q6gc4viZE",
    "consumer_secret"     : "blNDmFc0n3iOrp71QpKcrQT8X6jCbK6uvmf6XiPE1oJnINKqw9",
    "access_token"        : "966152934881972225-FUA14bZzjDWMN8WgUvw2Yba289HJBPH",
    "access_token_secret" : "NMWTyHAvODvizYXXPt7l7nNkeRfpiiRBDQYK1LDP2XnKC" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
