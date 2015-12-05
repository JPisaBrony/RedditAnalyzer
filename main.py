import sys
import praw

user_agent = "Reddit Analayzer 1.0 by JP, Josh, and Gabby"

def main():
    if len(sys.argv) < 2:
        print "Not Enough Arguments"
        print "Usage: python2 %s subreddit_name" % sys.argv[0]
        exit(0)

    subreddit = sys.argv[1]
    r = praw.Reddit(user_agent=user_agent)
    submissions = r.get_subreddit(subreddit).get_hot(limit=5)
    print [str(x) for x in submissions]

if __name__ == "__main__":
    main()
