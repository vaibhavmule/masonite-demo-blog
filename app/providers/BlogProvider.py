from masonite.provider import ServiceProvider
from dashboard.Link import BaseLink

class BlogEditorLink(BaseLink):
    display = 'Blog Editor'
    url = '/dashboard/blog'

# class BlogEditorLink(BaseLink):
#     display = 'Blog Create'
#     url = '/dashboard/blog/create'

class BlogProvider(ServiceProvider):

    def register(self):
        self.app.bind('BlogEditor', BlogEditorLink)

    def boot(self):
        pass