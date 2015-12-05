import sys
import praw

user_agent = "Reddit Analayzer 1.0 by JP, Josh, and Gabie"

def main():
    if len(sys.argv) < 3:
        print "Not Enough Arguments"
        print "Usage: python2 %s subreddit_name #_of_posts" % sys.argv[0]
        exit(0)

    subreddit = sys.argv[1]
    r = praw.Reddit(user_agent=user_agent)
    posts = r.get_subreddit(subreddit).get_hot(limit=sys.argv[2])
    for x in posts:
        flat = praw.helpers.flatten_tree(x.comments)
        for comment in flat:
            print comment

if __name__ == "__main__":
    main()
