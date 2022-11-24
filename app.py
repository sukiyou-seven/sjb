from lib.main_app import app, g, __log__, request

from interface.app_user_inc import *


# main_app 内包含一个 '/' 路由用于测试服务是否启动成功
#				一个 after_request方法, 重新格式化返回值及写流水日志
#
# -----------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    res = AppUserInc().check_user(auth.get('username'), auth.get("password"))
    return res


# -----------------------------------------------
app.run(port=12369, host='0.0.0.0', debug=True)
