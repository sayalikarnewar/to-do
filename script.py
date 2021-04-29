import aiohttp_jinja2

@aiohttp_jinja2.template('list.html')
async def get_list(request):

    db = request.app['db']
    _list = []
    async for document in db.to_do.find():
        _list.append(document['item'])
    
    return {'list': _list}


@aiohttp_jinja2.template('list.html')
async def add_item(request):
    form = await request.post()
    item = str(form['item'])


    db = request.app['db']
    
    db.to_do.insert_one({'item':item})
    
    return {'response':'item added'}

