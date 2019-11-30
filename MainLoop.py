import time
from TwitterBot import *

ReadFile()
AssignAuthValues()
Tweet = ShrekRead()
i = 0
day = 86400
while True:
    if isinstance(Tweet, str) == True:
        PostTweet(Tweet)
        time.sleep(day) 
    else:
        PostTweet(Tweet[0])
        time.sleep(day) 
        PostTweet(Tweet[1])
        
    time.sleep(day)
    i+=1
    Tweet = ShrekRead(i)
