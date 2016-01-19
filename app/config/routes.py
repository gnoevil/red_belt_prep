from system.core.router import routes

routes['default_controller'] = 'Sessions'
routes['POST']['/register'] = 'Sessions#register'
routes['POST']['/login'] = 'Sessions#login'
routes['GET']['/books'] = 'Books#index'
routes['GET']['/books/<id>'] = 'Books#show'
routes['GET']['/users/<id>'] = 'Users#show'
routes['POST']['/reviews'] = 'Books#create_review'
routes['POST']['/reviews/<id>/delete'] = 'Books#delete'

routes['POST']['/books/add'] = 'Books#add'