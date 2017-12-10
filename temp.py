from flask import Flask,request,render_template,make_response,redirect,url_for,jsonify,send_file
import requests
import json
app=Flask(__name__)



#---------Question 1-------------------------
@app.route('/')
def index():
    return "Hello Varun"


#--------------Question 2a---------------------
@app.route('/authors')
def authors():
    data=requests.get('https://jsonplaceholder.typicode.com/users') #Send GET request
    jsonresp=data.text #get response data
    jsondata=json.loads(jsonresp)   #convert json
    #print(jsondata)
    for details in jsondata:
        print(details['name']) #loop through the list and display names only
    return jsonresp #display the data


#----------------Question 2b-------------------
@app.route('/posts')
def posts():
    data=requests.get('https://jsonplaceholder.typicode.com/posts')
    jsonresp=data.text
    jsondata=json.loads(jsonresp)
    #print(jsondata)
    for details in jsondata:
        print(details['title'])
    return jsonresp


#----------------Question 2c-------------------
@app.route('/count')
def users():
    adata=requests.get('https://jsonplaceholder.typicode.com/users')
    aresp=adata.text #get author data
    authordata=json.loads(aresp)
    #print(jsondata)
    templist=list()
    tempdict=dict()
    '''for details in authordata:
        print(details['name'])'''
    pdata = requests.get('https://jsonplaceholder.typicode.com/posts')
    presp = pdata.text #get post data
    postdata = json.loads(presp)
    ct=0
    for author in authordata:
        ct=0
        tempdict=dict()
        for posts in postdata:
            if author['id']==posts['userId']:
                ct=ct+1
        tempdict['name']=author['name'] #create dictionary with name value pairs
        tempdict['ct']=ct
        templist.append(tempdict) #append to a list to create list of dicts
    #print(templist)
    return render_template("authors.html",auth=templist) #open authors.html and send list


#----------------Question 3-------------------
@app.route('/setcookie/<username>')
def profile(username):
    resp=make_response(render_template('welcome.html')) #open welcome.html and create response object
    resp.set_cookie('name',username) #set cookie called name
    resp.set_cookie('age','19') #set cookie called age
    return resp

#----------------Question 4-------------------
@app.route('/getcookie')
def getcook():
    cook=request.cookies #get cookies
    print(cook)
    return jsonify(cook)

#----------------Question 5-------------------
@app.route('/robots.txt')
def deny():
    return redirect('http://httpbin.org/deny',code=302) #redirect to error message



##----------------Question 6-------------------
@app.route('/html')
def welcome():
    return render_template('welcome.html',error=None) #open welcome.html

@app.route('/image')
def img():
    return send_file('static\Penguins.jpg',mimetype='image/gif') #send image file



#----------------Question 7-------------------
@app.route('/input/',methods=["GET","POST"])
def login():
    if request.method=="POST": #check if POST request
        username=request.form['username'] #get value from textbox in form
        return redirect('/authenticate/'+username,code=302) #redirect to /authenticate/ with username

    return render_template("form.html",error=None) #open form.html

@app.route('/authenticate/<username>')
def auth(username):
    print(username)
    return "hello"

#---------------------------------------------------


if __name__=='__main__':
    app.run(debug=True)
