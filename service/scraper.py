from facebook_scraper import get_posts

# Scrape a facebook page and return a list of posts
def facebook_scraper(pagename):
    posts = []
    for post in get_posts(pagename, pages=1, extra_info=True):
        if post is not None:
            posts.append(post)
    return posts
