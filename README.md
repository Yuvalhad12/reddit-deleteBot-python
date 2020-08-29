# reddit-deleteBot-python
basically deletes all comments of the user if comment score is lower than (-2).

That's the first ever python script I have had ever developed, and looking at the code brought up so many memories.
I decided to improve it just a little with eveyrthing I have learned since:

1. added support for json indentation
2. added threading
3. decided to utilize the power of the cpu im running the script on, and now it runs every 60 seconds instead of 1800 seconds (30 minutes)
4. implemented try\except approach for finding the json file, instead if's and elses.
5. changed from praw's STREAM function to a function of fetching the latest 100 comments every 60 seconds. REASON: I found praw's STREAM function unreliable: new comments often arrive late which lets te comment to get downvoted to oblivion before getting deleted.


I have no intention to keep working on this script. I know it's not perfect and that OOP may have been more suitable here, but it's a basic script and it dets the job done fast enough.
