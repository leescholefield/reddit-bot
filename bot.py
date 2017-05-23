"""
Creates a new Reddit connection and then polls each subreddit in the config.yml file for the last 10 submissions.
"""
import yaml
import praw

# contains login details for creating a new Reddit instance
with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

reddit = praw.Reddit(client_id=cfg['oauth']['client_id'],
                     client_secret=cfg['oauth']['client_secret'],
                     user_agent=cfg['oauth']['user_agent'])

for sub in cfg['subreddits']:
    for submission in reddit.subreddit(sub).new(limit=10):
        print(submission.title)
    print('\n')
