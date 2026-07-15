import wikipedia

def search(query):

    try:
        return wikipedia.summary(query, sentences=3)

    except:
        return "No information found."