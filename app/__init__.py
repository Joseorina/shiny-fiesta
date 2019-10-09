"""
App module init file
"""
from flask import  Flask, Blueprint, jsonify
from flask import  make_response
from flask_cors import CORS
from instance.config import APP_CONFIG
from app.db_config import create_tables,create_super_user

from app.api.v1.routes import  VERSION_ONE as v1

import uuid
import os

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))

def url_not_found(error):
	return make_response(jsonify({
		"status": 404,
		"error":"page not found"
	}), 404)
	
def create_app(config_name='development'):
	"""
	Method that creates app and initialize the app configurations
	
	Keyword Arguments:
		config_name {str} -- [description] (default: {'development'})
	"""
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object(APP_CONFIG[config_name])

	url = app.config.get('DATABASE_URL')
	url = app.config.get('DATABASE_URL')
	CORS(app, resources={r"/api/*": {"origins": "*"}})

	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

	create_tables(url)
	public_id = str(uuid.uuid4())
	if config_name == 'testing':
		public_id = "f3b8a1c3-f775-49e1-991c-5bfb963eb419"
	create_super_user(url, public_id)

	app.register_error_handler(404, url_not_found)
	app.url_map.strict_slashes = False


	app.register_blueprint(v1)
	app.register_blueprint(v2)
	return app


