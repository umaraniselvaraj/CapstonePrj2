"""Main application file"""
from flask import Flask
app=Flask(_name_)

@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    return "Breaking the unit test...."
if _name_=='_main_':
    app.run(host='0.0.0.0',port=8080)
