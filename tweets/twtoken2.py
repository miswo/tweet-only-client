from django.http import HttpResponse
import twitter
from requests_oauthlib import OAuth1Session
     
KEY = "1ajVPYtNS09p27YPq8SLo54y7"
SECRET = "DP7VOUXFd7sLWRWsJnhMIthxHac4MgCETUA2KSvxzVXAOfw4xl"


     
_CONSUMER_KEY = KEY
_CONSUMER_SECRET = SECRET
     
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
     
def twitter_auth(request):
    '''
    Twitter認証を行う
    '''
    oauth_token = request.GET["oauth_token"]
    oauth_verifier = request.GET["oauth_verifier"]
     
    oauth = OAuthTokenTemp.objects.get(oauth_token=oauth_token)
    oauth_token_secret =  oauth.oauth_token_secret
        
    oauth_client = OAuth1Session(_CONSUMER_KEY, client_secret=_CONSUMER_SECRET,
                                resource_owner_key=oauth_token,
                                resource_owner_secret=oauth_token_secret,
                                verifier=oauth_verifier)
    try:
        resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    except ValueError as e:
        return
                                     
    api = twitter.Api(consumer_key=_CONSUMER_KEY,
                        consumer_secret=_CONSUMER_SECRET,
                        access_token_key=resp.get('oauth_token'),
                        access_token_secret=resp.get('oauth_token_secret'))
     
    tw_user = api.VerifyCredentials()
    oauth.delete()
