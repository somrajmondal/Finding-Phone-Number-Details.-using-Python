from instabot import Bot

bot=Bot()
bot.login(username="myselfsomraj",password='')
bot.unfollow('white_chilis')
bot.send_message('i love python',['userid','userid'])

followers=bot.get_user_followers("myselfsomraj")
for Follower in followers:
    print(bot.get_user_followers(Follower))

photo=bot.upload_photo("pywhatkit.png",caption='This is py image')