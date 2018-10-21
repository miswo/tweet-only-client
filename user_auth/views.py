from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.http import HttpResponse
from djangoworks.settings import isDebug
import tweepy, os

if isDebug() == True:
    try:
        from djangoworks.configs import twitter
        SOCIAL_AUTH_TWITTER_KEY = twitter.SOCIAL_AUTH_TWITTER_KEY
        SOCIAL_AUTH_TWITTER_SECRET = twitter.SOCIAL_AUTH_TWITTER_SECRET
    except:
        pass
else:
    SOCIAL_AUTH_TWITTER_KEY = os.environ['SOCIAL_AUTH_TWITTER_KEY']
    SOCIAL_AUTH_TWITTER_SECRET = os.environ['SOCIAL_AUTH_TWITTER_SECRET']


@login_required
def top(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)

    if 'words' in request.GET:
        try:
            auth = UserSocialAuth.objects.filter(user=request.user).get()
            handler = tweepy.OAuthHandler(SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET)
            handler.set_access_token(auth.tokens["oauth_token"],auth.tokens["oauth_token_secret"])
            api = tweepy.API(auth_handler=handler)

            
            Message = {
                'words': request.GET.get('words'),
            }

            msg = Message['words']

            print(msg)
            api.update_status(msg)
            
            return render(request, 'top.html', Message)

        except:
            ErrorMessage = {
                'words': "Couldn't tweet because you said the same thing again.",
            }
            return render(request, 'top.html', ErrorMessage)
    else: 

        return render(request,'top.html',{'user': user})

