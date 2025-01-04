from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/notes')
def index(): #view function
    return "hello"

 #will throw value error if theres a gap between int: and notes_id
 #called url processors?   
@app.route('/notes/<int:notes_id>')
def note(notes_id):
    return f"hello id number {notes_id} "



@app.route('/handling_url_parameters')
def handling_parameters():
    return str(request.args)
#http://10.0.0.215:5555/handling_url_parameters?name=mike&greeting=hello
#ImmutableMultiDict([('name', 'mike'), ('greeting', 'hello')])


@app.route('/handle_url_parameters')
def handle_parameters():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting} {name}'
    #http://10.0.0.215:5555/handle_url_parameters?name=mike&greeting=hello
    #hello mike
    
    else:
        return 'Some parameters are missing'
    #http://10.0.0.215:5555/handle_url_parameters?name=mike
    #Some parameters are missing


#Create a route that accepts a query parameter called name and returns a greeting message based on that parameter.
@app.route('/greet/<int:user_id>')
def greeting(user_id):
    name = request.args.get('name', 'Guest')  # Default value 'Guest' if 'name' is not provided
    age = request.args.get('age','none')
    return f'Hello {name}{user_id} of age {age}'
#Extend the previous example to accept two query parameters: name and age. You will return a message that includes both the name and the age.
# combine query parameters with URL parameters http://10.0.0.215:5555/greet/10?name=jenry&age=12

#request.args is a dictionary 



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5555, debug = True)