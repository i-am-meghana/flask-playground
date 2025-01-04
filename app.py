from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/notes')
def index():
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
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    return f'{greeting} {name}'
#http://10.0.0.215:5555/handle_url_parameters?name=mike&greeting=hello
#hello mike



#return jsonify({"msg": "Friend created succesfully"}), 201

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5555, debug = True)