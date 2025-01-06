from flask import Flask, request,jsonify, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
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
    print(request)
    name = request.args.get('name', 'Guest')  # Default value 'Guest' if 'name' is not provided
    age = request.args.get('age','none')
    return jsonify(f'Hello {name}{user_id} of age {age}')
#Extend the previous example to accept two query parameters: name and age. You will return a message that includes both the name and the age.
# combine query parameters with URL parameters http://10.0.0.215:5555/greet/10?name=jenry&age=12

#request.args is a dictionary 

#multiple variables in a route
#made comment_id optional that route will default to 1
@app.route('/post/<int:post_id>/comment/', methods=['GET'])
@app.route('/post/<int:post_id>/comment/<int:comment_id>', methods=['GET'])
def show_comment(post_id, comment_id=None):
    # Check for query parameters or use default value for comment_id
    comment_id = request.args.get('comment_id', comment_id or 1, type=int)
    
    return f'Post ID: {post_id}, Comment ID: {comment_id}'
"""
/post/10/comment/5?comment_id=20
#comment_id = 20 (from query string).

#/post/10/comment/5
#comment_id = 5 (from path).

#/post/10/comment/5?comment_id=
#comment_id = 5 (from path; query string is empty).

#/post/10/comment/5?comment_id=0
#comment_id = 0 (from query string).

#/post/10/comment/0
#Post ID: 10, Comment ID: 1
"""

#You can also define default values for variables if needed    
@app.route('/product/<int:product_id>', defaults={'comment_id': 0})
@app.route('/product/<int:product_id>/comment/<int:comment_id>')
def show_product(product_id, comment_id): #this is the endpoint?
    return f'product ID: {product_id}, Comment ID: {comment_id}'

#jsonify
@app.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

#Create a Flask route that accepts a POST request and stores the received data in a Python dictionary.
#Create a route @app.route('/submit', methods=['POST'])
#Accept the data as JSON
#Return a JSON response indicating success.
#Test using Postman by sending a JSON payload
data_store = []
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()#convert the JSON into a Python dictionary. request contains the data sent by the client
    data_store.append(data)#will add this dictionary to the data_store list
    #Before: data_store = []
    #After: data_store = [{"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"}]
    return jsonify({"message": "Data submitted successfully", "data": data}), 201


#Create an API endpoint that allows users to submit their profile information (name, age, email). The data should be stored in a list, 
# and when a user sends a POST request with their profile, return a confirmation message along with the data.


#Create an endpoint /profile that accepts a POST request with user profile data (name, age, email).
# A global list to store the profiles
profiles = []

# Route to handle POST request and store profiles
@app.route('/profile', methods=['POST'])
def submit_profile():
    # Get JSON data from the request
    profile_data = request.get_json()
    
    # Store the profile data in the global list
    profiles.append(profile_data)
    
    # Return a success message with the stored profile
    return jsonify({"message": "Profile added successfully", "profile": profile_data}), 201

#Create a GET endpoint that returns all the profiles submitted so far
# Route to handle GET request and return all profiles
@app.route('/profiles', methods=['GET'])
def get_profiles():
    # Return all stored profiles
    return jsonify({"profiles": profiles}), 200

#Create an API endpoint /profile/<id> that allows updating a user's profile using their ID. 
# The user ID should be included in the request URL, and the data should be updated in the list.
@app.route('/profile/<int:id>', methods=['PUT'])
def profile_update(id):
    updated_data = request.get_json()
    if id < len(profiles):
        profiles[id] = updated_data
        return jsonify({"message": "Profile updated", "profile": updated_data}), 200
    else:
        return jsonify({"message": "Profile not found"}), 404

#Accept the user ID as part of the URL.
#Check if the user exists and remove them from the list if found.
#Return a confirmation message.

@app.route('/profile/<int:id>', methods=['DELETE'])
def delete_profile(id):
    if id < len(profiles):
        deleted_data = profiles.pop(id)
        return jsonify({"message":"profile deleted"})
    else:
        return jsonify({"message": "Profile not found"}), 404

USER_CREDENTIALS = {'username': 'admin', 'password': 'password123'}
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
        session['logged_in'] = True
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5555, debug = True)