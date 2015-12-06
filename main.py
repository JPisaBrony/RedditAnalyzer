import sys
import praw

user_agent = "Reddit Analayzer 1.0 by JP, Josh, and Gabie"
chars_to_ignore = ",.:;?[]{}_+=\\/|0123456789<>!@#$%^&*()-~"

def read_file(file):
    word_list = []
    with open(file) as f:
        word_list = f.read().splitlines()
    return word_list

def main():
    if len(sys.argv) < 4:
        print "Not Enough Arguments"
        print "Usage: python2 %s subreddit_name #_of_posts words_to_exclude_file" % sys.argv[0]
        exit(0)

    exclude_words = read_file(sys.argv[3])

    subreddit = sys.argv[1]
    r = praw.Reddit(user_agent=user_agent)
    posts = r.get_subreddit(subreddit).get_hot(limit=sys.argv[2])
    for x in posts:
        print parse_post(x, exclude_words)[2:]
        flat = praw.helpers.flatten_tree(x.comments)
        for comment in flat:
            try:
                print parse_post(comment.body.encode("ascii", "ignore"), exclude_words)
            except AttributeError:
                pass

def parse_post(post, words):
    parsed_list = []
    cur_words = str(post)
    cur_words = cur_words.lower().split(" ")
    for x in cur_words:
        x = x.strip(chars_to_ignore)
        if x not in words:
            parsed_list.append(x)
    return parsed_list

if __name__ == "__main__":
    main()
