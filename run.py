import os
from flask import Flask, render_template #use capital F as is a class name


# Storing an instance of class 'Flask' in variable called app
# First argument of FLask class is the name of module
# As only using one module for app can use built in python variable: __name__
app = Flask(__name__) 

# @ is a decorator in python, allows wrapping of functions
# when browse the root directory (indicated by '/') the index function is run
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__': # '__main__' is default module in python
    app.run(
        host=os.environ.get('IP' , '0.0.0.0'), # get IP from os, but if IP variable does not exist the default of '0.0.0.0' used
        port=int(os.environ.get('PORT', '5000')), # same as for IP with default of '5000'
        debug=True # allows us to debug app during development. must be changed to False for proj submission (security issue if left)
    )