"""
Routing configuration.
"""

import tornado.web
from handlers.login_handler import LoginHandler
from handlers.logout_handler import LogoutHandler
from handlers.index_handler import IndexHandler
from handlers.register_handler import RegisterHandler
from services.survey import Survey

settings = {
    'cookie_secret': '8goWPH9uTyO+9e2NzuaW6pbR6WKH1EbmrXIfxttXq00=',
    'xsrf_cookies': True,
}

# Tornado pro-tip: regex routing is optimized by putting more frequently
# accessed routes and simpler regexes before other routes.
routes = [
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/login", LoginHandler),
    (r"/login", LogoutHandler),
    (r"/register/(\w+)", RegisterHandler),
    (r"/register", RegisterHandler),

    (r"/api/survey/(\d+)", Survey),
    (r"/api/survey", Survey),
]
