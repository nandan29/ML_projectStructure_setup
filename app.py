from flask import Flask
from housing.logger import logging

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info("testing the logging module")
    return "CI CD pipeline has been established and application is containerised"


if __name__=="__main__":
    app.run(debug=True)
