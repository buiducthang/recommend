from views import index

def setup_routes(app):
    app.router.add_post('/', index)
    #app.router.add_post('/comment', comment, name='comment')