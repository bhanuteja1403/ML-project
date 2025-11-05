import sys
import logging


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
        # ✅ Fixed: pass the actual error object, not just message text
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    logging.basicConfig(
        filename="error.log",
        level=logging.INFO,
        format="[%(asctime)s] %(name)s %(levelname)s: %(message)s"
    )
