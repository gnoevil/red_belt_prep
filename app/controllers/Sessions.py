from system.core.controller import *

class Sessions(Controller):
	def __init__(self, action):
		super(Sessions, self).__init__(action)
		self.load_model('User')

	def index(self):
		return self.load_view('new.html')

	def new(self):
		return self.load_view('new.html')

	def login(self):
		our_user = self.models['User'].login(request.form)
		try:
			our_user
			session['user'] = {'name':our_user['alias'], 'id':our_user['id']}
		except:
			return redirect ('/')
		return redirect ('/books')

	def register(self):
		our_user = self.models['User'].create(request.form)
		try:
			print '-' * 100
			print our_user
			our_user
			session['user'] = {'name':our_user[0]['alias'], 'id':our_user[0]['id']}
			print session['user']
		except:
			return redirect ('/')
		return redirect ('/books')
