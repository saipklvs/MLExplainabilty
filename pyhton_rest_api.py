from flask import Flask

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world', "test" : "helper"}

class Pillaka(Resource):
    def get(self):
        return {"pillaka": "hello"}

api.add_resource(HelloWorld, '/')
api.add_resource(Pillaka, '/test')

def test_hello():
    print("test")

if __name__ == '__main__':
    # print("Hello")
    # test_hello()
    app.run(debug=True)





