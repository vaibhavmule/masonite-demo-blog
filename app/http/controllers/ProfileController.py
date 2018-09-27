''' A Controller for Dashboard Profiles '''
from app.Post import Post
from app.User import User
from masonite.facades.Auth import Auth
from masonite.helpers import password as bcrypt_password

from helpers.DashboardHelper import remove_whitespaces

	
class ProfileController(object):

	def __init__(self):
		pass

	def show(self, Request):
		""" Controller to show user profile page """

		if not Auth(Request).user():
			Request.redirect('dashboard')

		return view('dashboard/profile', {'Auth': Auth(Request)})
	
	def store(self, Request, Upload):
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

		# Save image
		try:
			image = Upload.driver('s3').store(Request.input(
				'file_upload'), location='storage/user/img')
			user[0].image = image
		except AttributeError:
			# If user did not pick image, check and see if there was a previous image. 
			if user[0].image != "":
				pass


		# Change password
		# if Request.input('password'):
		# 	user[0].password = bcrypt_password(Request.input('password'))


		# Update user info
		user[0].save()

		return view('dashboard/profile', {'Auth': Auth(Request)})

