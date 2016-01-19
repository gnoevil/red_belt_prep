from system.core.controller import *

class Books(Controller):
	def __init__(self, action):
		super(Books, self).__init__(action)
		self.load_model('Book')
		self.load_model('Review')

	def index(self):
		recent_books = self.models['Book'].index_recent()
		remaining_books = self.models['Book'].index_remaining()

		return self.load_view('books/index.html', recent=recent_books, remaining=remaining_books)

	def show(self, id):
		book = self.models['Book'].show(id)
		return self.load_view('books/show.html', book=book)

	def create_review(self):
		print request.form
		self.models['Review'].create(request.form)
		return redirect('/books/'+request.form['book_id'])

	def delete_review(self, id):
		self.models['Review'].delete(id)
		return redirect ('/books/'+request.form['book_id'])


