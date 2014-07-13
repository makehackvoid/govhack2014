from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')

import govhack2014.routes   # noqa
