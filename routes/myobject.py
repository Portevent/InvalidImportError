from flask_restful import Resource


class MyObject(Resource):
    def get(self):
        return {'hello': 'world'}
