
import tweepy
import time

credentials = []
recoveryData = []
# Eskeetit
# Function: Reads the contents of a text file that contains the twitter API
#           OAuth credentials to the credentials list. If i was less lazy
#           I would make this used for all file reading and writing
#           but im  Australian and not German
def ReadFile():
    credentialsDoc = open("credentialsTextDocument.txt", "r")
    for line in credentialsDoc:
        credentials.append(line)
    credentialsDoc.close()
    
# Function: Takes the credentials from the ReadFile Function and uses them for OAuth
def AssignAuthValues():
    consumer_key = credentials[0].rstrip()
    consumer_secret = credentials[1].rstrip()
    access_token = credentials[2].rstrip()
    access_token_secret = credentials[3].rstrip()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    global numOfTweets
    api = tweepy.API(auth)
def LastInstance(lst,thing):
    i = 1
    mostWanted = 0
    print (lst)
    while i < len(lst):
        if lst[i] == thing:
            if lst[i+1] == ' ':
                mostWanted = i
        i += 1
    return mostWanted
def FirstInstance(lst,thing):
    i = 1
    found = 0
    mostWanted = 0
    while i < len(lst) and found < 3:
        if lst[i] == thing:
            mostWanted = i
            found += 1
        i += 1
    return mostWanted
def ShrekRead(start=0):
    charLimit = 280
    shrekDoc = open("theRoom.txt",'r')
    shrekLines = []
    for line in shrekDoc:
        shrekLines.append(line)
    outLines = []
    lengthOfLine = len(shrekLines[start])
    if  lengthOfLine > charLimit:
        pre = shrekLines[start]
        outLine = list(pre)
        lstInst = LastInstance(outLine,".")
        inst = lstInst
        if lstInst >= charLimit - 1:
            fstInst = FirstInstance(outLine,".")
            inst = fstInst
        i = 0
        outLines = []
        while i <= inst:
            outLines.append(outLine[i])
            i += 1
        frontHalf = "".join(outLines)
        outLines = []
        while i < lengthOfLine:
            outLines.append(outLine[i])
            i += 1
        backHalf = "".join(outLines)
        output = [frontHalf,backHalf]
    else:
        output = shrekLines[start]
    return output
# Function: Tweets to the account
# Variable: String
def PostTweet(x):
    api.update_status(x)
