""" Contains plugins for the worldtimes_extension """

import datetime

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint, render_template, make_response

import pytz # pip install pytz


def index():
    """ view function for the worldtimes_exxtension plugin """
    return make_response(render_template('worldtimes.html',
                                         current_date_time=datetime.\
                                             datetime.now(pytz.utc),
                                         pytz=pytz))


# Plugin class for the extension
class Worldtimes_ExtensionPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    
    # method implementation for the IConfigurer interface
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'worldtimes_extension')
    
    # method implementation for IBlueprint
    def get_blueprint(self):
        u'''Return a Flask Blueprint object to be registered by the app.'''
        # Create Blueprint for plugin
        blueprint = Blueprint('worldtimes', self.__module__)
        blueprint.template_folder = u'templates'
        # Add plugin url rules to Blueprint object
        blueprint.add_url_rule('/worldtimes', 'index', index)
        return blueprint
