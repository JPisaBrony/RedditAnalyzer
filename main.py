import sys
import praw

user_agent = "Reddit Analayzer 1.0 by JP, Josh, and Gabie"
#transition_words = "transition_words.txt"
chars_to_ignore = ",:"

def read_file(file):
    word_list = []
    with open(file) as f:
        word_list = f.read().splitlines()
    return word_list

def main():
    if len(sys.argv) < 4:
        print "Not Enough Arguments"
        print "Usage: python2 %s subreddit_name #_of_posts words_to_exclude" % sys.argv[0]
        exit(0)

    exclude_words = read_file(sys.argv[3])

    subreddit = sys.argv[1]
    r = praw.Reddit(user_agent=user_agent)
    posts = r.get_subreddit(subreddit).get_hot(limit=sys.argv[2])
    for x in posts:
        post = parse_post(x, exclude_words)
        print post
        #flat = praw.helpers.flatten_tree(x.comments)
        #for comment in flat:
        #    print comment

def parse_post(post, words):
    parsed_list = []
    cur_words = str(post).split(" ")
    cur_words = cur_words[2:]
    for x in cur_words:
        x = x.strip(chars_to_ignore)
        if x not in words:
            parsed_list.append(x)
    return parsed_list

if __name__ == "__main__":
    main()
