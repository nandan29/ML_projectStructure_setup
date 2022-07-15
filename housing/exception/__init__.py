import Exception
import sys

class housing_exception(Exception):
    def __init__(self,error_msg:Exception,error_details:sys):
        super().__init__(error_msg)











@staticmethod
def get_detailed_error_msg(error_msg:Exception,error_details:sys):
    pass