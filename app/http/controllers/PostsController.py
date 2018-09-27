''' A Controller for Live Posts'''
from app.Post import Post
from app.User import User
from masonite.facades.Auth import Auth


class PostsController(object):
	''' Posts Controller '''

	def __init__(self):
		pass

	def show_all(self):
		""" Controller to show all posts"""

		posts = Post.where('is_live', 1).get()
		return view('blog', {'author': User, 'posts': posts})

	def show_one(self, Request, RenderEngine):
		""" Controller to show single post"""

		# Get post via slug
		slug = Request.param('id')
		posts = Post.where('slug', slug).where('is_live', 1).get()
		post = posts[0]
		post.body = RenderEngine(post.body)

		# Get current author
		user = User.where('id', post.author_id).get()

		# Get recent posts
		recent_posts = Post.where('is_live', 1).order_by('updated_at', 'desc').take(5).get()

		return view('blog/post', {'user': user[0], 'post': post, 'recent': recent_posts })

	def show_category(self, Request):
		""" Controller to show poss by category"""

		category = Request.param('id')

		posts = Post.where('category', category).where('is_live', 1).get()
		return view('blog/category', {'author': User, 'category': category, 'posts': posts})

	def show_author(self, Request):
		""" Controller to show posts by author"""

		user_name = Request.param('id')

		author = User.where('user_name', user_name).get()

		posts = Post.where('author_id', author[0].id).where('is_live', 1).get()

		return view('blog/author', {'author': author[0], 'posts': posts})
