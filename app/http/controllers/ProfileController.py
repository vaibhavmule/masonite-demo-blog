''' A Controller for Dashboard Profiles '''
from app.Post import Post
from app.User import User
from masonite.facades.Auth import Auth

    
class ProfileController(object):

	def __init__(self):
		pass

	def show(self, Request):
		return view('dashboard/profile', {'Auth': Auth(Request)})
	