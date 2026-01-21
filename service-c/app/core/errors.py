class MySQLError(Exception):
    def __init__(self, msg: str):
        self.msg = f'error trying to interact to mysql server: {msg}'
        super().__init__(self.msg)
        