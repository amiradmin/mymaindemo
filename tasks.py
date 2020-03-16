import os
from celeryapp import app
from datetime import datetime

@app.task
def invocer():
    file_name = 'my_file1.txt'
    f = open(file_name, 'a+')  # open file in append mode
    f.write('python rules')
    f.close()


res =invocer.delay()
