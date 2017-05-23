import yaml
import praw

with open('config.yml', 'r') as ymlfile:
    auth = yaml.load(ymlfile)

reddit = praw.Reddit(client_id=auth['client_id'],
                     client_secret=auth['client_secret'],
                     user_agent=auth['user_agent'])

for submission in reddit.subreddit('ukpolitics').new(limit=10):
    print(submission.title)
