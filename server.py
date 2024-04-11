from flask import Flask, request

app = Flask(__name__)

@app.route('/post_endpoint', methods=['POST'])
def post_endpoint():
    req_body = request.get_json()  # Get the JSON body of the request
    print("Received request body:", req_body)
    return "Request received successfully."

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
