from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/hello')
def get_location_names():
    response = jsonify({
        'location': util
    })
    return 'hi'


if __name__ == '__main__':
    print('starting flask server')
    app.run()