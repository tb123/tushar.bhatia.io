from blog.models import BlogPost


def get_blog_post(blog_post_id):
    return BlogPost.get_by_id(int(blog_post_id))


def update_blog_post(title, content, is_published, blog_post_id=None):
    if not blog_post_id:
        p = BlogPost()
    else:
        p = get_blog_post(blog_post_id)
    p.title = title
    p.content = content
    p.is_published = bool(is_published)
    p.put()
    return p


def get_all_blog_posts():
    return BlogPost.query().order(BlogPost.date)
