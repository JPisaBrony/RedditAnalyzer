import os
import sys
import praw
from scipy.stats.vonmises_cython import numpy
from __builtin__ import file
#from numpy.distutils.from_template import outfile

user_agent = "Reddit Analayzer 1.0 by JP, Josh, and Gabie"
#outfile = open("output.txt", 'w')

def main():
    for path,dir,file in os.walk("./data"):
        if len(sys.argv) < 3:
            print "Not Enough Arguments"
            print "Usage: python2 %s subreddit_name #_of_posts" % sys.argv[0]
            exit(0)
        for x in file:
            if x == "output.txt":
                pass
            else:
                os.remove("./data/" + x)

    subreddit = sys.argv[1]
    r = praw.Reddit(user_agent=user_agent)
    posts = r.get_subreddit(subreddit).get_hot(limit=sys.argv[2])
    users = {}
    users_to_post = {}
    run_times = 0
    for x in posts:
        flat = praw.helpers.flatten_tree(x.comments)
        for c in flat:
            try:
                u = str(c.author).lower()
                if u in users:
                    users[u] += 1
                else:
                    users[u] = 1
                users_to_post[u] = x.title
            except AttributeError:
                pass
        write_to_file(users_to_post)
        users_to_post = {}
        run_times += 1
        if run_times >= int(sys.argv[2]):
            break
    combine()
    os.system("Rscript comment_miner.R")

def write_to_file(post):
    for x in post:
        try:
            outfile = open("./data/%s" % post[x].encode("UTF-8", "ignore"), "a")
            outfile.write(x.encode("UTF-8", "ignore") + " ", )
            outfile.close()
        except:
            pass

def combine():
    outfile = open("./data/dataset.txt", "w")
    for path,dir,file in os.walk("./data"):
        for x in file:
            if x == "dataset.txt" or x == "output.txt":
                pass
            else:
                outfile.write(open("./data/" + x).readline() + "\n")
        for x in file:
            if x == "dataset.txt" or x == "output.txt":
                pass
            else:
                os.remove("./data/" + x)
    outfile.close()

if __name__ == "__main__":
    main()
