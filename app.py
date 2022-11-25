import imgkit

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


@app.route('/set_web', methods=['POST'])
def set_web():
    pass
@app.route('/test2', methods=['GET', 'POST'])
def test2():
    path_wk = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
    config = imgkit.config(wkhtmltoimage=path_wk)
    options = {
        'crop-w': 1024,  # 需要截图的宽高位置，这里可以进行调整
        'crop-h': 645,
        'crop-x': 10,
        'crop-y': 150,
        'encoding': 'UTF-8',
    }
    # 转换HTML文件为图片
    html1 = imgkit.from_file(filename="./web/python requests库中的post详解 - 简书.html", config=config,
                             options=options, output_path="out1.jpg")

    print(html1)

    # 转换HTML网址为图片
    # html2 = imgkit.from_url(url="https://www.baidu.com", config=config, output_path="out2.png")
    # print(html2)
    return "0"

# -----------------------------------------------
app.run(port=12369, host='0.0.0.0', debug=True)
