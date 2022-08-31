import datetime
from werkzeug.utils import secure_filename
import os
import uuid
from flask import request
from flask_cors import *
from houtai.head import allowed_file
from houtai.login import create_token
from json_flask import JsonFlask
from json_response import JsonResponse
from config import *
import json
from flask import session,escape

# 创建视图应用


app = JsonFlask(__name__)
app.secret_key = os.urandom(16)

# 设置允许上传的文件格式
ALLOW_EXTENSIONS = ['png', 'jpg']

# 设置图片保存文件夹
app.config['UPLOAD_FOLDER'] = 'D:/project/qianduan/vue_element/houtai/src/images'
# 设置图片返回的域名前缀
# 设置图片压缩尺寸
image_c = 1000

# 解决跨域
CORS(app, supports_credentials=True)

db = SQLManager()


# 编写视图函数，绑定路由
@app.route("/all", methods=["GET","POST"])  # 查询（全部）

def all():
    data = json.loads(request.data)
    sql = f'select * from test limit %s,10'% int((data['currentPage']-1)*10)
    result = db.get_list(sql)
    return JsonResponse.success(msg='查询成功',data=result)if result else JsonResponse.fail(msg='添加失败')

@app.route("/all_user", methods=["GET","POST"])  # 查询（全部）
def all_user():

    sql = f'select * from login_user '
    result = db.get_list(sql)
    print(result)
    return JsonResponse.success(msg='查询成功', data=result)



@app.route("/add", methods=["POST"])  # 添加（单个）
def add():
    data = json.loads(request.data)  # 将json字符串转为dict
    isOk = db.modify(sql='insert into test(name,user,password) values(%s,%s,%s)',
                      args=[data['name'], data['user'], data['password']])
    return JsonResponse.success(msg='添加成功') if isOk else JsonResponse.fail(msg='添加失败')


@app.route("/update", methods=["PUT"])  # 修改（单个）
def update():
    data = json.loads(request.data)  # 将json字符串转为dict
    if 'id' not in data:
        return JsonResponse.fail(msg='需要传入name')
    isOk = db.modify(sql='update test set name=%s,user=%s,password=%s where id=%s',
                      args=[data['name'], data['user'], data['password'], str(data['id'])])
    return JsonResponse.success(msg='修改成功') if isOk else JsonResponse.fail(msg='修改失败')


@app.route("/delete", methods=["DELETE"])  # 删除（单个）
def delete():
    if 'id' not in request.args:
        return JsonResponse.fail(msg='需要传入id')
    isOk = db.modify(sql='delete from test where id=%s', args=[request.args['id']])
    return JsonResponse.success(msg='删除成功') if isOk else JsonResponse.fail(msg='删除失败')

#用户登录
@app.route("/login", methods=["GET","POST"])  # 查询（全部）
def loginuser():
    data = json.loads(request.data)
    print(data)
    print(data['name'],data['password'])
    sql = f"select * from login_user where name='%s' and password='%s'"%(data['name'],data['password'])
    result = db.get_list(sql)
    # 数据库有无token,判断是否第一次登录，是则加一个token，否就验证token，再直接进入
    for i in result:
        if  not i['token']:
         new_token= create_token(data)
         print("new",new_token)
         isOk = db.modify(sql='update login_user set token = %s where name=%s',
                          args=([new_token],i['name']))

    return JsonResponse.success(msg='查询成功', data=result) if result else JsonResponse.fail(msg="该用户没有注册")
@app.route("/login_out", methods=["GET","POST"])  # 退出登录
def login_out():
  token = request.headers['Token']
  print(token)
  isOk = db.modify(sql='update login_user set token = "" where token=%s',args = [token])
  return JsonResponse.success(msg='成功退出',) if isOk else JsonResponse.fail(msg="该用户未成功退出")

# @app.route("/public", methods=["GET","POST"])
# def public():
#     token = request.data
#     print(token)
#     sql='select name from token = "" where token=%s'
#     args=[token]
#     result =db.get_one(sql,args)
#     return JsonResponse.success(msg='已获取当前用户信息',data=result ) if result else JsonResponse.fail(msg="获取用户信息失败")


@app.route("/search", methods=["GET","POST"])  # 查询（全部）
def search():
    print(request.data)
    data = json.loads(request.data)
    sql = f"select * from login_user where name like %s"
    args = ['%'+data['search']+'%']
    result = db.get_list(sql,args)
    print(result)
    return JsonResponse.success(msg='查询成功', data=result) if result else JsonResponse.fail(msg="查询失败")

@app.route("/update_user",methods=["GET","POST"])
def update_user():
    data = json.loads(request.data)  # 将json字符串转为dict
    if 'id' not in data:
        return JsonResponse.fail(msg='需要传入name')
    isOk = db.modify(sql='update login_user set name=%s,email=%s,sex=%s where id=%s',
                     args=[data['name'], data['email'], data['sex'], str(data['id'])])
    return JsonResponse.success(msg='修改成功') if isOk else JsonResponse.fail(msg='修改失败')

@app.route("/add_user", methods=["POST"])  # 添加（单个）
def add_user():
    data = json.loads(request.data)  # 将json字符串转为dict
    isOk = db.modify(sql='insert into login_user(name,password,email,sex,c_time) values(%s,%s,%s,%s,%s)',
                      args=[data['name'], data['name'],data['email'], data['sex'],datetime.datetime.now()])
    return JsonResponse.success(msg='添加成功') if isOk else JsonResponse.fail(msg='添加失败')

@app.route("/add_login", methods=["POST"])  # 添加（单个）
def add_login():
    data = json.loads(request.data)  # 将json字符串转为dict
    isOk = db.modify(sql='insert into login_user(name,password,email,sex,c_time) values(%s,%s,%s,%s,%s)',
                      args=[data['name'], data['pass'],data['name'],'male',datetime.datetime.now()])
    return JsonResponse.success(msg='注册成功') if isOk else JsonResponse.fail(msg='注册失败')



@app.route("/add_blog", methods=["POST"])  # 添加（单个）
def add_blog():
    data = json.loads(request.data)
    print(request.headers['Token'])
    print(data)
    token = request.headers['Token']
    sql = f"select name from login_user where token=%s"
    args = [token]
    result = db.get_list(sql, args)
    # name = db.modify(sql='select name from login_user where token=%s',
    #                  args=[token])
    name = result[0]['name']
    print(result[0]['name'])
    isOk = db.modify(sql='insert into blog(name,context,createTime) values(%s,%s,%s)',
                      args=[name,data['message'],datetime.datetime.now()])
    return JsonResponse.success(msg='添加成功',data = result) if isOk else JsonResponse.fail(msg='添加失败')

@app.route("/all_msg", methods=["GET","POST"])  # 查询（全部）
def all_msg():
    sql = f'select * from blog'
    result = db.get_list(sql)
    return JsonResponse.success(msg='查询成功', data=result)


@app.route("/delete_user", methods=["DELETE"])  # 删除（单个）
def delete_user():
    if 'id' not in request.args:
        return JsonResponse.fail(msg='需要传入id')
    isOk = db.modify(sql='delete from login_user where id=%s', args=[request.args['id']])
    return JsonResponse.success(msg='删除成功') if isOk else JsonResponse.fail(msg='删除失败')


@app.route("/upload_image", methods=['POST', "GET"])
def uploads():
    if request.method == 'POST':
        # 获取文件
        file = request.files['file']
        print(file)
        print(file.filename)
        # 检测文件格式
        if file and allowed_file(file.filename):
            # secure_filename方法会去掉文件名中的中文，获取文件的后缀名
            file_name_hz = secure_filename(file.filename).split('.')[-1]
            # 使用uuid生成唯一图片名
            first_name = str(uuid.uuid4())
            # 将 uuid和后缀拼接为 完整的文件名
            file_name = first_name + '.' + file_name_hz
            # 保存原图
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            print(file_name)
            return {"code": '200', "image_url": file_name,
                    "message": "上传成功"}
        else:
            return "格式错误，仅支持jpg、png、jpeg格式文件"
    return {"code": '503', "data": "", "message": "仅支持post方法"}





# 运行flask：默认是5000端口，此处设置端口为666
if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
