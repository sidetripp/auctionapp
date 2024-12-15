import json

from app.classes.models.config import Config_Methods

from app.classes.helpers.shared_helpers import Helpers

class Config_Helpers:
    @staticmethod
    def get_latest_config():
        return Config_Methods.get_config_by_id(Config_Methods.get_all_configs()[0]["entry_id"])
    
    @staticmethod
    def get_secret_value():
        return Config_Helpers.get_latest_config().secret_value
    
    @staticmethod
    def is_min_bid_percent():
        return Config_Helpers.get_latest_config().min_bid_percent
    
    @staticmethod
    def get_min_bid_amount():
        return Config_Helpers.get_latest_config().min_bid_amount
    
    @staticmethod
    def get_entity_name():
        return Config_Helpers.get_latest_config().entity_name
    
    @staticmethod
    def get_entity_logo():
        return Config_Helpers.get_latest_config().entity_logo
    
    @staticmethod
    def get_primary_color():
        return Config_Helpers.get_latest_config().primary_color
    
    @staticmethod
    def get_secondary_color():
        return Config_Helpers.get_latest_config().secondary_color
    
    @staticmethod
    def get_stripe_api_key():
        return Config_Helpers.get_latest_config().stripe_api_key
    
    @staticmethod
    def get_tax_id():
        return Config_Helpers.get_latest_config().tax_id
    
    @staticmethod
    def get_smtp_user():
        return Config_Helpers.get_latest_config().smtp_user
    
    @staticmethod
    def get_smtp_email():
        return Config_Helpers.get_latest_config().smtp_email
    
    @staticmethod
    def get_smtp_server():
        return Config_Helpers.get_latest_config().smtp_server
    
    @staticmethod
    def get_smtp_port():
        return Config_Helpers.get_latest_config().smtp_port
    
    @staticmethod
    def get_smtp_password():
        return Config_Helpers.get_latest_config().smtp_password
    
    @staticmethod
    def update_secret():
        latest_config = Config_Helpers.get_latest_config()
        latest_config.secret_value = Helpers.generate_secret()
        return Config_Methods.update_config(latest_config)
    
    @staticmethod
    def get_db_config():
        with open('app/config/db_settings.json', 'r') as db_config:
            data = json.load(db_config)
        return data