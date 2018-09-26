''' A Controller for Dashboard Profiles '''
from app.Post import Post
from app.User import User
from masonite.facades.Auth import Auth
from helpers.DashboardHelper import remove_whitespaces

	
class ProfileController(object):

	def __init__(self):
		pass

	def show(self, Request):
		""" Controller to show user profile page """

		if not Auth(Request).user():
			Request.redirect('dashboard')

		return view('dashboard/profile', {'Auth': Auth(Request)})
	
	def store(self, Request):
		""" Store user profile information """

		if not Auth(Request).user():
			Request.redirect('dashboard')

		user_name = Auth(Request).user().user_name
		user = User.where('user_name', user_name).get()

		# Get new user info
		user[0].name = remove_whitespaces(Request.input('name'))
		user[0].website = remove_whitespaces(Request.input('website'))
		user[0].twitter = remove_whitespaces(Request.input('twitter'))
		user[0].facebook = remove_whitespaces(Request.input('facebook'))
		user[0].github = remove_whitespaces(Request.input('github'))
		user[0].gitlab = remove_whitespaces(Request.input('gitlab'))
		user[0].bio = remove_whitespaces(Request.input('bio'))

		# Update user info
		user[0].save()

		return view('dashboard/profile', {'Auth': Auth(Request)})

