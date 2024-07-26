import os
import json
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


@app.route('/about')
def about():
    data = []
    # opens company.json as 'read-only' ('r'), and assigns content to json_data variable
    # assigns json_data to 'data' list variable
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # assigning new variable 'company', which will be set thru to html file, the content of 'data'
    return render_template('about.html', page_title="About", company=data) 


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            # matches the link clicked to the correct member data
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member) # 1st member refers to member.html, second is member object defined above


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title="Contact")


@app.route('/careers')
def careers():
    return render_template('careers.html', page_title="Careers")


if __name__ == '__main__': # '__main__' is default module in python
    app.run(
        host=os.environ.get('IP' , '0.0.0.0'), # get IP from os, but if IP variable does not exist the default of '0.0.0.0' used
        port=int(os.environ.get('PORT', '5000')), # same as for IP with default of '5000'
        debug=True # allows us to debug app during development. must be changed to False for proj submission (security issue if left)
    )