import praw, threading, ujson, time

try:
    with open('deleteData.json', 'r') as outfile:
        data = ujson.load(outfile)
    outfile.close()
except:
    data = []


r2 = praw.Reddit(username = "",
                        password = "",
                        client_id = "",
                        client_secret = "",
                        user_agent = "Deletes crap")



def autoDelete():
    while True:
        try:
            for comment in r2.redditor('yuvalhad12').comments.new(limit=100):
                t = threading.Thread(target= _autoDelete, args=(comment , ))
                t.start()
            time.sleep(60)
        except:
            print('reddit server must have crashed. Will restart in 1 minutes')
            time.sleep(60)



def _autoDelete(comment):
    global data
    print(comment)
    if comment.score <= -2:
        to_append = {
        'comment_body': comment.body,
        'submission_link':'https://reddit.com'+comment.submission.permalink
        }
        comment.delete()
        print('Comment deleted')
        data.append(to_append)
        with open('deleteData.json', 'w') as outfile:
            ujson.dump(data, outfile,sort_keys=True, indent=4)
        outfile.close()


autoDelete()