# errors.py

class Error(Exception):
    """Base class for other execptions"""
    pass

class ResponseNot200(Error):
    """Exception raised for when request response is not 200

    Attributes:
        response_code -- response code that caused the error
        message -- explanation of the error
    """
    def __init__(self, response_code: int, message:str="Page reached, but not crawlable:"):
        self.response_code = response_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} Error code {self.response_code}'

class NoScheduleFound(Error):
    """Exception raise for when a schedule for a title is not found

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message:str="Unfortunately, rezka.ag does not have a schedule for this title"):
        self.message = message
        super().__init__(self.message)

    def __str___(self):
        return f'{self.message}'