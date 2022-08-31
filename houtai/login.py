import base64
import hashlib
import hmac
import json
import time

import requests
from flask import jsonify, Flask
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

import jwt
import time
# def create_token(name, extime=36000):
#     ts_str = str(str(time.time()) + str(extime))
#     ts_byte = ts_str.encode("utf-8")
#     sha1_tshexstr = hmac.new(name.encode("utf-8"),  ts_byte, 'sha1').hexdigest()
#     print(sha1_tshexstr.encode("utf-8"))
#     token = ts_str + ':' + sha1_tshexstr
#     print(token.encode("utf-8"))
#     b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
#     print(" b64_token",b64_token)
#     print(b64_token.decode("utf-8"))
#     return b64_token.decode("utf-8")



#写一个反向解码token的方法，获取用户的name值，传给前端

import jwt
import time

from flask_login import UserMixin
from werkzeug.security import check_password_hash


def create_token(data):
 d = {
    # 公共声明
    'exp': time.time() + 3000,  # (Expiration Time) 此token的过期时间的时间戳
    'iat': time.time(),  # (Issued At) 指明此创建时间的时间戳
    'iss': 'Issuer',  # (Issuer) 指明此token的签发者

    # 私有声明
    'data': data
}
 jwt_encode = jwt.encode(d, data['password'], algorithm='HS256')
 return jwt_encode
 print(jwt_encode)










