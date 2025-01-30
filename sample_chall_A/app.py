from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Access environment variable and display it
    my_env_var = os.getenv('FLAG_VALUE', 'Environment variable not set')
    return f"Challenge A's FLAG_VALUE: {my_env_var}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
