import os
class CONFIG:
      def __init__(self):
        self.endpoint = os.getenv('END_POINT', 'END_POINT')
        self.key = os.getenv('KEY', 'KEY')
        self.database_name = os.getenv('DATABASE_NAME', 'END_POINT')
        self.container_name = os.getenv('CONTAINER_NAME', 'END_POINT')
        pass
