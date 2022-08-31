from flask_cors import *
from houtai.json_flask import JsonFlask
from houtai.json_response import JsonResponse
from houtai.config import *

# 创建视图应用
app = JsonFlask(__name__)

# 解决跨域
CORS(app, supports_credentials=True)

db = SQLManager()



@app.route("/all_old", methods=["GET"])  # 查询（全部）
def all():
    sql = f'select * from test'
    # result = db.get_list(sql='select * from test')
    result = db.get_list(sql)
    return JsonResponse.success(msg='查询成功', data=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=667, debug=True)
