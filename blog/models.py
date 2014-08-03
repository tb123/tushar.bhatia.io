from google.appengine.ext import ndb


class BlogPost(ndb.Model):
    """ Models an individual blog post entry. """
    author = ndb.UserProperty()
    title = ndb.StringProperty(indexed=False)
    content = ndb.TextProperty()
    is_published = ndb.BooleanProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
