import sys
from src.logger import logging
'''
import logging
from logger import logger
'''
def error_msg_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg,error_details:sys):
        super().__init__(error_msg)
        self.error_message=error_msg_details(error_msg,error_details=error_details)
        #logger.error(self.error_message)
    
    def __str__(self):
         return self.error_message

'''
if __name__=="__main__":
    logging.basicConfig(level=logging.INFO) 
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
'''