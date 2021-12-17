from app import app as application
from os import environ as env

if __name__ == "__main__":
    application.run(host=env["HOST"], port=env['API_PORT'],
                    debug=env['DEBUG_MODE_ON'])
