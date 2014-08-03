import webapp2
from tushar.settings import JINJA_ENVIRONMENT
from google.appengine.api import users

# Utils
from blog.utils import (
    get_blog_post,
    update_blog_post,
    get_all_blog_posts,
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        posts = get_all_blog_posts()
        template_values = {
            'posts': posts, # A list of blog posts
            'post_count': posts.count(),
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class BlogEditPage(webapp2.RequestHandler):
    def get(self, blog_post_id=None):
        """ Render the edit blog post form and pass the blog post data if
        an existing blog post is going to be edited.
        """
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        if users.is_current_user_admin():
            return webapp2.redirect('/')

        blog_post = None
        if blog_post_id:
            blog_post = get_blog_post(blog_post_id)
        template_values = {
            'blog_post': blog_post,
            'blog_post_id': blog_post_id,
        }
        template = JINJA_ENVIRONMENT.get_template('edit-post.html')
        self.response.write(template.render(template_values))

    def post(self, blog_post_id=None):
        """
        """
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        if users.is_current_user_admin():
            return webapp2.redirect('/')

        if self.request.get('submit'):
            blog_post = update_blog_post(
                title=self.request.get('title'),
                content=self.request.get('content'),
                is_published=self.request.get('is_published'),
                blog_post_id=blog_post_id,
            )
        return webapp2.redirect('/blog/edit/%d/' % (blog_post.key.id()))
