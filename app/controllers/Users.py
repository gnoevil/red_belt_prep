from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')


	def show(self,id):
		user = self.models['User'].show(id)
		return self.load_view('users/show.html', user=user)