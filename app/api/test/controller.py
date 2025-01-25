from flask import request, jsonify
from flask_restx import Resource
from .dto import TestDto
from app.api.test.service import TestService
request_dto = TestDto.test

api = TestDto.api
data_resp = TestDto.data_resp
data_update = TestDto.data_update
@api.route("/test")
class CreateRequest(Resource):
    @api.doc(
        "test requests",
        responses={
            200:("request success",data_resp),
            400:"Missing required fields",
            500:"Exception"
        }                           
    )
    def post(self):
        data = request.json
        return TestService.create_service(data)
    # get1
    @api.doc(
        "get all requests",
        responses = {
            200:("request success",data_resp),
            500:"Exception"
        }
    )
    def get(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=1, type=int)
        response, status = TestService.get_all_requests(page, per_page)
        return response, status


    
    
    
    # get2
@api.route("/detailed/")
class GetById(Resource):
    @api.marshal_with(request_dto, envelope='resource')
    @api.doc("get data by id",
            responses = {
            200: ("Request success", data_resp),
            400: "Missing ID",
            404: "Request not found",
            500: "Exception"
        }   )
    def get(self): 
        id = request.args.get("id", type=str)
        
        response = TestService.get_by_id()
        return response
    
#put
@api.route("/update")
class UpdateById(Resource):
    @api.doc("update data by id",
            responses={
            200: ("Request success",data_update),
            400: "Missing ID",
            404: "Request not found",
            500: "Exception"
             })
    @api.expect(data_update)
    def put(self):

        return TestService.update_by_id(self)
        