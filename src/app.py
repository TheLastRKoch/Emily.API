from src.resources.player.controller import add_player_resource_table
from src.resources.basic.controller import add_basic_resource_table
from dotenv import load_dotenv
from flask_restful import Api
from flask import Flask
import os

# Load .env file
load_dotenv()

# Init app
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
api = Api(app)


# End Points Routes
# add_product_resource_table(api)
add_basic_resource_table(api)
add_player_resource_table(api)
