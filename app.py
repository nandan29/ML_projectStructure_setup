from flask import Flask
from housing.logger import logging
from housing.exception import housing_exception
import sys

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():

    try:
        raise Exception(" we are testing custom exception")

    except Exception as e:
        housing = housing_exception(e,sys) #creating an object for housing_exception class
        logging.info(housing.error_msg)
        logging.info("we are testing logging module")
    return "CI CD pipeline has been established and application is containerised"


if __name__=="__main__":
    app.run(debug=True)
