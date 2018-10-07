from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests_oauthlib import OAuth1Session
 
from tweets.models import *
from .forms import TestForm

import tweepy


consumer_key = '1ajVPYtNS09p27YPq8SLo54y7'
consumer_secret = 'DP7VOUXFd7sLWRWsJnhMIthxHac4MgCETUA2KSvxzVXAOfw4xl'
access_token = '142843393-tITe8g8Z3DsqZKXFoqRHGXjJwvwui1GG0pRYrLRk'
access_token_secret = 'yufRfuVQ05VYEBqsPqUbXsai9a2QF2q6Lk1cDX2U1g2ZS'

CONSUMER_KEY = consumer_key
CONSUMER_SECRET = consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


# トップページ（認証へのリンクを設置するページ）
def index(request):
    return render(request, 'tweets/index.html')


# 認証リンク
def signin(request):
    # request token取得
    callback_uri = "https://tweet-only.herokuapp.com"
    oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            callback_uri=callback_uri)
    request_token_url = "https://api.twitter.com/oauth/request_token"
    response = oauth.fetch_request_token(request_token_url)
 
    # 認証用URL作成
    redirect_url = "https://api.twitter.com/oauth/authenticate?oauth_token=" + response["oauth_token"]
 
    # 認証へリダイレクト
    return redirect(redirect_url)
 
 
# ユーザーが認証完了後にtwitterからリダイレクトされるURL
def callback(request):
    request_token = request.GET["oauth_token"]; # リクエストトークンは以前と同じもの
    verifier = request.GET["oauth_verifier"];
    oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=request_token,
            verifier=verifier)
    access_token_url = "https://api.twitter.com/oauth/access_token"
    # アクセストークン取得
    response = oauth.fetch_request_token(access_token_url)
 
    # DBに追加or更新
    try:
        # レコードが存在するか確認
        user = User.objects.get(id=response["user_id"])
        if user.access_token != response["oauth_token"]:
            # アクセストークンが変わった場合更新
            user.access_token = response["oauth_token"]
            user.access_token_secret = response["oauth_token_secret"]
            user.save()
    except User.DoesNotExist:
        # 存在しなかったら追加
        user = User()
        user.id = response["user_id"]
        user.access_token = response["oauth_token"]
        user.access_token_secret = response["oauth_token_secret"]
        user.save()
 
    # セッションにトークンを保存
    request.session["access_token"] = response["oauth_token"]
 
    # リダイレクト
    return redirect("tweets.views.tweet")
 
# アクセストークンを使って機能を提供するページ
def tweet(request):


    access_token = request.session.get("access_token", None)
    if not access_token:
        # セッションにアクセストークンが無ければサインインに移行
        return redirect("tweets.views.signin")
 
    user = User.objects.get(access_token=access_token)
 
    # 以下、consumer key/secret、access token/secretの4つを使ってAPIを叩く
 
    print ("access_token_key: " + user.access_token)
    print ("access_token_secret: " + user.access_token_secret)


    auth.set_access_token(user.access_token, user.access_token_secret)
    #APIインスタンスを作成
    api = tweepy.API(auth)

    Message = {
        'words': request.GET.get('words'),
    }

    msg = Message['words']
    #api.update_status(msg)
    return HttpResponse("access_token_secret: " + user.access_token_secret)
    #return render(request, 'tweets/tweet.html', Message)    

'''
def tweet(request):
    Message = {
        'words': request.GET.get('words'),
    }

    msg = Message['words']
    #api.update_status(msg)
    
    return render(request, 'tweets/tweet.html', Message)
'''