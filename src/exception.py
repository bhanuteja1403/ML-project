import sys
from src.logger import logging  # ✅ Use global logger setup

def error_message_details(error, error_detail: sys):
    """
    Captures detailed error information including file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_detail=error_detail)
        logging.error(self.error_message)  # ✅ Automatically log the error message

    def __str__(self):
        return self.error_message


