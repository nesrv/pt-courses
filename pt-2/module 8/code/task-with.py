class PrimaryKey:
    def __enter__(self):
        print('вход')


    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        return True



with PrimaryKey() as pk:
    raise ValueError





class ConnectionError(Exception): pass


class DatabaseConnection:

    def __init__(self):
        self._fl_connection_open = False

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        
        
        
class ConnectionError(Exception):
    """генерировать исключение"""
    

class DatabaseConnection:
    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False