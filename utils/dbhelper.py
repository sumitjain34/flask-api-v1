from mongoengine import *
from app.models import User
from utils import user_helper
import traceback


def db_connected():
    try:
        DATABASE_NAME='test_database'
        connect(DATABASE_NAME)
        return True
    except Exception as e:
        print "Database not connected"
        print traceback.format_exc(e)
        return False

# def fetch_user_from_db(user_id=None,email=None):
#     if db_connected():
#         try:
#             if user_id:
#                 cursor=User.objects(user_id=user_id)
#             else:
#                 cursor=User.objects(email=email)
#             if cursor:
#                 user=cursor[0]
#         except Exception as e:
#             response={'message':'no data in database','error_code':1}
#             print traceback.format_exc(e)

def get_user(user_id):
    try:
        if db_connected():
            cursor=User.objects(user_id=user_id)
            if cursor:
                user=cursor[0]
                user_json=user_helper.generate_user_json(user)
                response={'message':'Cool Profile','error_code':0,'user':user_json}
            else:
                response={'message':'No user with this id','error_code':1}
        else:
            response={'message':'Some error.. Please Try again','error_code':1}
    except Exception as e:
        response={'message':'no data in database','error_code':1}
        print traceback.format_exc(e)
    return response

def save_user(email,password,user_id,access_token):
    try:
        if db_connected():
            User(email=email,password=password,user_id=user_id,access_token=access_token).save()
            response={'message':'You are registered','error_code':0,'access_token':access_token,'user_id':user_id}
        else:
            response={'message':'Some error.. Please Try again','error_code':1}
    except NotUniqueError as e:
        if 'user.$user_id' in traceback.format_exc(e):
            response={'message':'Please try again','error_code':1}
        else:
            response={'message':'This email already exists','error_code':1}
        print traceback.format_exc(e)
    except ValidationError as e:
        response={'message':'Invalid Email format','error_code':1}
        print traceback.format_exc(e)
    return response

def create_user(email,password):
    user_id=user_helper.generate_user_id()
    access_token=user_helper.generate_access_token()
    response=save_user(email,password,user_id,access_token)
    return response

def user_login(email,password):
    if db_connected():
        try:
            cursor=User.objects(email=email)
            if cursor:
                user=cursor[0]
                if user.password==password:
                    response={'message':'You are logged in','error_code':0,'access_token':user.access_token,'user_id':user.user_id}
                else:
                    response={'message':'wrong password','error_code':1}
            else:
                response={'message':'wrong email','error_code':1}
        except Exception as e:
            response={'message':'no data in database','error_code':1}
        return response
    

    


    
