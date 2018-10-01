from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm

import tweepy

consumer_key = '1ajVPYtNS09p27YPq8SLo54y7'
consumer_secret = 'DP7VOUXFd7sLWRWsJnhMIthxHac4MgCETUA2KSvxzVXAOfw4xl'
access_token = '142843393-tITe8g8Z3DsqZKXFoqRHGXjJwvwui1GG0pRYrLRk'
access_token_secret = 'yufRfuVQ05VYEBqsPqUbXsai9a2QF2q6Lk1cDX2U1g2ZS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#APIインスタンスを作成
api = tweepy.API(auth)


def index(request):
    Message = {
        'words': request.GET.get('words'),
    }

    msg = Message['words']
    #api.update_status(msg)
    
    return render(request, 'tweets/index.html', Message)
