import os
import sys

class housing_exception(Exception):
    def __init__(self,error_msg:Exception,error_details:sys):
        super().__init__(error_msg) #error msg will be send to the parent class
        self.error_msg = self.get_detailed_error_msg(error_msg = error_msg,
                                                        error_details=error_details)



    #lets prepare the detailed error msg in a beautiful way containing all the information.
    @staticmethod
    def get_detailed_error_msg(error_msg:Exception , error_details:sys)->str:

        """
        error_msg :Exception object 
        error_detail:sys object
        
        
        """


        _,_ ,exec_tb = error_details.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_msg}]
        """
        return error_message

    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return housing_exception.__name__.str()








