from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

#Use python run.py to start the server.
#sample http://127.0.0.1:5000/jsonify/hello  or /user/logout 