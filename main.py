import os
import sys
import praw
from scipy.stats.vonmises_cython import numpy
from __builtin__ import file
#from numpy.distutils.from_template import outfile

user_agent = "Reddit Analayzer 1.0 by JP, Josh, and Gabie"
#outfile = open("output.txt", 'w')

def main():
    if len(sys.argv) < 3:
        print "Not Enough Arguments"
        print "Usage: python2 %s subreddit_name #_of_posts" % sys.argv[0]
        exit(0)

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
    
def write_to_file(post):
    for x in post:
        outfile = open("data/"+post[x], "a")
        outfile.write(x + " ")#post[x].encode("ascii", "ignore") + ";")
        outfile.close()
        
def combine():
    outfile = open("./data/output.txt", "w")
    for path,dir,file in os.walk("./data"):
        for x in file:
            outfile.write(open("./data/" + x).readline() + "\n")
    outfile.close()

if __name__ == "__main__":
    main()