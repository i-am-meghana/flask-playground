from flask import Flask

app = Flask(__name__)

@app.route('/notes')
def index():
    return "hello"
    
@app.route('/notes/<int:notes_id>')
def note(notes_id):
    return f"hello id number {notes_id} "


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5555, debug = True)