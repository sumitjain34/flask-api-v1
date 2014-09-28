from mongoengine import *
from datetime import datetime

class User(Document):
	user_id=StringField(unique=True)
	access_token=StringField(unique=True)
	first_name=StringField()
	middle_name=StringField()
	last_name=StringField()
	email=EmailField(unique=True,required=True)
	other_emails=ListField(DictField())
	password=StringField(required=True,min_length=6)
	birth_date=DateTimeField()
	gender=StringField(choices=['m','f'])
	avatar_thumb_url=URLField()
	avatar_url=URLField()
	contact_numbers=ListField(DictField())
	address=ListField(DictField())
	organisation=StringField()
	designation=StringField()
	social_profiles=ListField(DictField())
	created_at=DateTimeField(default=datetime.now)

# class Friend(Document):
# 	sender=ReferenceField(User)
# 	sendee=ReferenceField(User)
# 	timestamp=DateTimeField(default=datetime.now)

	

