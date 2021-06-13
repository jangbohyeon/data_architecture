from flask import Flask
from flask import request
import os
from src import user, mylogger, myconfig
import pdb
import datetime
from flask_restx import Api, Resource

app = Flask(__name__)


# create a logger.
project_root_path = os.getenv("DATA_ARCHITECTURE")
cfg = myconfig.get_config('{}/share/project.config'.format(
    project_root_path))
log_directory = cfg['logger'].get('log_directory')
loggers = dict()
loggers['login'] = mylogger.get_logger('login', log_directory)
loggers['Users_tonic'] = mylogger.get_logger('Users_tonic', log_directory)
loggers['Tonic_info'] = mylogger.get_logger('Tonic_info', log_directory)
 
@app.route('/')
def index():
    return 'Welcome index page'

@app.route('/login', methods=["POST"])
def login():
    """login API function.
    Specification can be found in `API.md` file.
    :return: JSON serialzed string containing the login result with session_id
    :rtype: str
    """
    user_id = request.json.get('user_id')
    passwd = request.json.get('passwd')
    loggers['login'].info('{}: login'.format(user_id))

    ret = {"result": None,
        "session_id": None,
        "msg": ""}

    session_key = user.login(user_id, passwd, loggers['login'])
    loggers['login'].info('{}: session_key = {}'.format(user_id, session_key))
    if not session_key:
        ret["result"] = False
        ret["msg"] = "Failed to login"
    else:
        ret["result"] = True
        ret["session_id"] = session_key["session_id"]

    #pdb.set_trace()
    loggers['login'].info('{}: login result = {}'.format(user_id, ret))
    return ret

@app.route('/Tonic_info', methods=["POST"])
def Users_tonic():
    return render_template("home.html")
    


  
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='1234')
