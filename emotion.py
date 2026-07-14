from textblob import TextBlob

def detect(text):

    polarity=TextBlob(text).sentiment.polarity

    if polarity>0:
        return "😊 Happy"

    elif polarity<0:
        return "😔 Sad"

    else:
        return "😐 Neutral"