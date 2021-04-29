import jinja2
import aiohttp_jinja2
from aiohttp import web
import asyncio

from routes import routes
from setup import setup


#create a loop for the db
loop = asyncio.get_event_loop()
db = loop.run_until_complete(setup())

app = web.Application()

app['db'] = db


#setting up the jinja template
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

#adding the routes
routes(app)

#run the web app
web.run_app(app)