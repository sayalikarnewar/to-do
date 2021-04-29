from script import add_item, get_list

def routes(app):

    #home page
    app.router.add_get('/', add_item)
    app.router.add_post('/', get_list, name='list')

   