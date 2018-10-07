from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from djangoworks.configs import twitter

import tweepy


@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)

    return render(request,'user_auth/top.html',{'user': user})




@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    auth = UserSocialAuth.objects.filter(user=request.user).get()
    #auth = tweepy.OAuthHandler(request.oauth_token, request.oauth_token_secret)
    handler = tweepy.OAuthHandler(twitter.SOCIAL_AUTH_TWITTER_KEY, twitter.SOCIAL_AUTH_TWITTER_SECRET)
    handler.set_access_token(auth.tokens["oauth_token"],auth.tokens["oauth_token_secret"])
    api = tweepy.API(auth_handler=handler)

    

    Message = {
        'words': request.GET.get('words'),
    }

    msg = Message['words']
    #api.update_status(msg)
    
    return render(request, 'user_auth/top.html', Message)
