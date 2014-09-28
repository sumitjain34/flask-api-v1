#!/usr/bin/python
from app import app

port=8000
host='0.0.0.0'
app.run(host=host,port=port,debug=True)