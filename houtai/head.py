from flask import Flask, request, Response, render_template
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import uuid
from PIL import Image, ExifTags

app = Flask(__name__)  # 实例Flask应用
CORS(app,supports_credentials=True)
# 设置允许上传的文件格式
ALLOW_EXTENSIONS = ['png', 'jpg']

# 设置图片保存文件夹
app.config['UPLOAD_FOLDER'] = 'D:/project/qianduan/vue_element/houtai/src/images'

# 设置图片返回的域名前缀


# 设置图片压缩尺寸
image_c = 1000




# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.after_request(after_request)


# 判断文件后缀是否在列表中
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1] in ALLOW_EXTENSIONS




# 上传图片
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

            # # 以下是压缩图片的过程，在原图的基础上
            # file_min = Image.open(file)
            # # exif读取原始方位信息 防止图片压缩后发生旋转
            # try:
            #     for orientation in ExifTags.TAGS.keys():
            #         if ExifTags.TAGS[orientation] == 'Orientation': break
            #     exif = dict(file_min._getexif().items())
            #     if exif[orientation] == 3:
            #         file_min = file_min.rotate(180, expand=True)
            #     elif exif[orientation] == 6:
            #         file_min = file_min.rotate(270, expand=True)
            #     elif exif[orientation] == 8:
            #         file_min = file_min.rotate(90, expand=True)
            # except:
            #     pass
            # # 获取原图尺寸
            # w, h = file_min.size
            # # 计算压缩比
            # bili = int(w / image_c)
            # # 按比例对宽高压缩
            #
            # # 生成缩略图的完整文件名
            # file_name_min = first_name + '_min.' + file_name_hz
            # # 保存缩略图
            # file_min.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name_min))
            # # 返回原本和缩略图的 完整浏览链接
            print(file_name)
            return {"code": '200', "image_url": file_name,
                    "message": "上传成功"}
        else:
            return "格式错误，仅支持jpg、png、jpeg格式文件"
    return {"code": '503', "data": "", "message": "仅支持post方法"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=667, debug=True)  # 项目入口