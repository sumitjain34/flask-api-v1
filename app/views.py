from app import app
from flask import request, jsonify,make_response,abort
from models import User
from utils import dbhelper
import json
import traceback
from utils import request_validator
import time

@app.route('/home')
def home():
    return "This is home page"

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        try:
            # jsondata=request.form.get('data')
            # data=json.loads(jsondata)
            # email=data.get("email",None)
            # password=data.get("password",None)
            email=request.form.get('email',None)
            password=request.form.get('password',None)
            if email and password:
                response_body=dbhelper.create_user(email,password)
            else:
                response_body={'message':'Email or password is empty','error_code':1}
        except Exception as e:
            print "Exception in fetching email and password"
            print traceback.format_exc(e)
            response_body={'message':'Please Try again','error_code':1}
    else:
      response_body={'message':'wrong request type','error_code':1}
    time.sleep(5)
    return make_response(jsonify(response_body))

@app.route('/user/profile/<user_id>',methods=['GET','POST'])
def get_profile(user_id):
    if request.method=='GET':
        response_body=dbhelper.get_user(user_id)
    else:
        response_body={'message':'wrong request type','error_code':1}
    return make_response(jsonify(response_body))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        try:
            email=request.form.get('email',None)
            password=request.form.get('password',None)
            # jsondata=request.form.get('data',None)
            # data=json.loads(jsondata)
            # email=data.get('email',None)
            # password=data.get('password',None)
            if email and password:
                response_body=dbhelper.user_login(email,password)
            else:
                response_body={'message':'email or password is empty','error_code':1}
        except Exception as e:
            print "Error in fetching email or password"
            response_body={'message':'Please Try again','error_code':1}
    else:
        response_body={'message':'wrong request type','error_code':1}
    return make_response(jsonify(response_body))

# @app.route('/user/friend/',methods=['GET','POST'])
# def add_friend():
#     if request.method=='POST':
#         j
        