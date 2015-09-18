from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


from views import index, ajax_1, ajax_2, path_params

