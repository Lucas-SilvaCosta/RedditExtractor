import praw
from datetime import datetime, timezone
import json

reddit_read_only = praw.Reddit(client_id="c8lt1yQFIOaDD3NHs7bekg",		 # your client id
							client_secret="cWE6Kf3r1TuNxErJc4arsyt9JnPAEg",	 # your client secret
							user_agent="b0linh0x")	 # your user agent

submissionsInfo = []
searchId = 0

for subreddit in reddit_read_only.subreddits.search("hyperledger"):
    # subreddit = reddit_read_only.random_subreddit()
    searchId = 1
    submissionId = 0
    # for submission in subreddit.search(query="blockchain", sort="new", time_filter="year"):
    for submission in subreddit.search(query="fabric", sort="new", limit=None):
        if submission.created_utc < datetime(2010, 1, 1).replace(tzinfo=timezone.utc).timestamp():
            break
        submissionId += 1
        submissionInfo = {
            'ID': str(searchId)+"_"+str(submissionId),
            'Title': submission.title,
            'Upvotes': submission.score,
            'Comments': submission.num_comments,
            'Date': submission.created_utc,
            'URL': submission.url
        }
        submissionsInfo.append(submissionInfo)
        print("added submission: "+str(searchId)+"_"+str(submissionId))
        # print(submission.title)
        # print(submission.score) # Number of upvotes
        # print(submission.num_comments)
        # # print(submission.created_utc) # Time submission was created
        # print(datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'))
        # print(submission.url)
        # print("===================================")
    break

for subreddit in reddit_read_only.subreddits.search("cryptocurrency"):
    # subreddit = reddit_read_only.random_subreddit()
    searchId = 2
    submissionId = 0
    # for submission in subreddit.search(query="blockchain", sort="new", time_filter="year"):
    for submission in subreddit.search(query="hyperledger", sort="new", limit=None):
        if submission.created_utc < datetime(2010, 1, 1).replace(tzinfo=timezone.utc).timestamp():
            break
        submissionId += 1
        submissionInfo = {
            'ID': str(searchId)+"_"+str(submissionId),
            'Title': submission.title,
            'Upvotes': submission.score,
            'Comments': submission.num_comments,
            'Date': submission.created_utc,
            'URL': submission.url
        }
        submissionsInfo.append(submissionInfo)
        print("added submission: "+str(searchId)+"_"+str(submissionId))
    break

for subreddit in reddit_read_only.subreddits.search("blockchainstartups"):
    # subreddit = reddit_read_only.random_subreddit()
    searchId = 3
    submissionId = 0
    # for submission in subreddit.search(query="blockchain", sort="new", time_filter="year"):
    for submission in subreddit.search(query="hyperledger", sort="new", limit=None):
        if submission.created_utc < datetime(2010, 1, 1).replace(tzinfo=timezone.utc).timestamp():
            break
        submissionId += 1
        submissionInfo = {
            'ID': str(searchId)+"_"+str(submissionId),
            'Title': submission.title,
            'Upvotes': submission.score,
            'Comments': submission.num_comments,
            'Date': submission.created_utc,
            'URL': submission.url
        }
        submissionsInfo.append(submissionInfo)
        print("added submission: "+str(searchId)+"_"+str(submissionId))
    break

with open('hyperledger.json', 'w') as file:
  file.write(str(json.dumps(submissionsInfo, indent=4)))

submissionsInfo = []

for subreddit in reddit_read_only.subreddits.search("news"):
    # subreddit = reddit_read_only.random_subreddit()
    searchId = 1
    submissionId = 0
    # for submission in subreddit.search(query="blockchain", sort="new", time_filter="year"):
    for submission in subreddit.search(query="blockchain", sort="new", limit=None):
        if submission.created_utc < datetime(2015, 1, 1).replace(tzinfo=timezone.utc).timestamp():
            break
        submissionId += 1
        submissionInfo = {
            'ID': str(searchId)+"_"+str(submissionId),
            'Title': submission.title,
            'Upvotes': submission.score,
            'Comments': submission.num_comments,
            'Date': submission.created_utc,
            'URL': submission.url
        }
        submissionsInfo.append(submissionInfo)
        print("added submission: "+str(searchId)+"_"+str(submissionId))
    break

for subreddit in reddit_read_only.subreddits.search("worldnews"):
    # subreddit = reddit_read_only.random_subreddit()
    searchId = 2
    submissionId = 0
    # for submission in subreddit.search(query="blockchain", sort="new", time_filter="year"):
    for submission in subreddit.search(query="blockchain", sort="new", limit=None):
        if submission.created_utc < datetime(2015, 1, 1).replace(tzinfo=timezone.utc).timestamp():
            break
        submissionId += 1
        submissionInfo = {
            'ID': str(searchId)+"_"+str(submissionId),
            'Title': submission.title,
            'Upvotes': submission.score,
            'Comments': submission.num_comments,
            'Date': submission.created_utc,
            'URL': submission.url
        }
        submissionsInfo.append(submissionInfo)
        print("added submission: "+str(searchId)+"_"+str(submissionId))
    break

for subreddit in reddit_read_only.subreddits.search("technology"):
    # subreddit = reddit_read_only.random_subreddit()
    searchId = 3
    submissionId = 0
    # for submission in subreddit.search(query="blockchain", sort="new", time_filter="year"):
    for submission in subreddit.search(query="blockchain", sort="new", limit=None):
        if submission.created_utc < datetime(2015, 1, 1).replace(tzinfo=timezone.utc).timestamp():
            break
        submissionId += 1
        submissionInfo = {
            'ID': str(searchId)+"_"+str(submissionId),
            'Title': submission.title,
            'Upvotes': submission.score,
            'Comments': submission.num_comments,
            'Date': submission.created_utc,
            'URL': submission.url
        }
        submissionsInfo.append(submissionInfo)
        print("added submission: "+str(searchId)+"_"+str(submissionId))
    break

for subreddit in reddit_read_only.subreddits.search("cryptotechnology"):
    # subreddit = reddit_read_only.random_subreddit()
    searchId = 4
    submissionId = 0
    # for submission in subreddit.search(query="blockchain", sort="new", time_filter="year"):
    for submission in subreddit.search(query="blockchain", sort="new", limit=None):
        if submission.created_utc < datetime(2015, 1, 1).replace(tzinfo=timezone.utc).timestamp():
            break
        submissionId += 1
        submissionInfo = {
            'ID': str(searchId)+"_"+str(submissionId),
            'Title': submission.title,
            'Upvotes': submission.score,
            'Comments': submission.num_comments,
            'Date': submission.created_utc,
            'URL': submission.url
        }
        submissionsInfo.append(submissionInfo)
        print("added submission: "+str(searchId)+"_"+str(submissionId))
    break

with open('blockchain.json', 'w') as file:
  file.write(str(json.dumps(submissionsInfo, indent=4)))