"""Configuration module for the auto recommendation engine."""
import os

class Config:
    """Base configuration class."""
    
    # Model settings
    MODEL_PATH = os.environ.get('MODEL_PATH', 'models/recommender.pkl')
    DATA_PATH = os.environ.get('DATA_PATH', 'data/')
    
    # API settings
    API_HOST = os.environ.get('API_HOST', '0.0.0.0')
    API_PORT = int(os.environ.get('API_PORT', 8000))
    
    # Recommendation settings
    NUM_RECOMMENDATIONS = int(os.environ.get('NUM_RECOMMENDATIONS', 10))
    
    @staticmethod
    def get_config():
        """Return configuration dictionary."""
        return {
            'model_path': Config.MODEL_PATH,
            'data_path': Config.DATA_PATH,
            'api_host': Config.API_HOST,
            'api_port': Config.API_PORT,
            'num_recommendations': Config.NUM_RECOMMENDATIONS,
        }
