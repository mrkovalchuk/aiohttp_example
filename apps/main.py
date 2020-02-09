import asyncio
from aiohttp import web

from apps.db import init_pg, close_pg
from apps.users.routers import setup_routes
from aiohttp_example.settings import config


async def init_app():
    """Initialize the application server."""
    app = web.Application()

    # Configure project
    app['config'] = config

    # Configure service routes
    setup_routes(app)

    # Configure signals for db
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    return app


loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_app())

if __name__ == '__main__':
    web.run_app(app)

