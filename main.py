import tweepy
import data
import time as t
from data import horas,horas_2
from keys import consumer_key,consumer_secret,key,secret
print('This is UBI BOT, do you copy?', flush=True)



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)



api = tweepy.API(auth)


horas = horas
horas_2 = horas_2
while True:
    time = data.get_time()
    try:
        if time in horas:
            price = str(round(data.get_price(),2))
            variation = str(round(data.get_24hs_variation(),2))

            api.update_status("The actual price of UBI💧 is " + price + " USD. (" +
                                variation + "%)")
            print("Tweeting price...")
            t.sleep(3)
            if time in horas_2:
                humans = str(data.get_humans())
                pending_humans = str(data.get_pending_humans())

                api.update_status("Currently " + humans + " humans are earning UBI💧.\n\n" + "And " +
                                pending_humans + " are pending registration.")
                print("Tweeting abot humans...")
        print("Im running...")
        t.sleep(30)
    except Exception as e:
	    print("ERROR : "+str(e))
