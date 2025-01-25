from flask import jsonify ,request
from app import db
from app.models.requests import Requests

class TestService:
    def create_service(data):
        try:
            title = data.get('title')
            instruction = data.get('instruction')
            attached = data.get('attached')
            signed = data.get('signed')
            voice_attached = data.get('voice_attached')
            description = data.get('description')
            status = data.get('status')

            if not title or not instruction or not description or not status:
                return jsonify({"error": "Missing required fields"}), 400

            new_request = Requests(
                title=title,
                instruction=instruction,
                attached=attached,
                signed=signed,
                voice_attached=voice_attached,
                description=description,
                status=status
            )

            db.session.add(new_request)
            db.session.commit()

            return jsonify({
                "id": new_request.id,
                "title": new_request.title,
                "instruction": new_request.instruction,
                "attached": new_request.attached,
                "signed": new_request.signed,
                "voice_attached": new_request.voice_attached,
                "description": new_request.description,
                "status": new_request.status
            }, 201)

        except Exception as e:
            return jsonify({"error": str(e)}, 500)
    # get all requests
    def get_all_requests(page=1,per_page=10):
        try:
            pagination = Requests.query.paginate(page=page, per_page=per_page, error_out=False)
            
            items = [req.to_json() for req in pagination.items]

            return {
                "items": items,
                "total": pagination.total,
                "page": pagination.page,
                "pages": pagination.pages,
                "per_page": pagination.per_page,
            }, 200 

        except Exception as e:
            return {"error": str(e)}, 500
    # get data by id
    def get_by_id():
        try:
            request_id = request.args.get('id')
            
            if not request_id:
                return {"error": "ID is required"}, 400
            request = Requests.query.filter_by(id=request_id).first()
            if not request :
                return {"error": "Request not found"}, 404
            return request

        except Exception as e:
            return {"error": str(e)}, 500
    #update by id
    def update_by_id(self):
        update_data = request.json
        try:
            print("Received data:", update_data)
            # request_id = request.args.get('id')
            if not update_data['id']:
                return {"error": "ID is required in the body"}, 400
            request_object = Requests.query.filter_by(id=update_data['id']).first()
            if not request_object:
                return {"error": "Request not found"}, 404
            for key, value in update_data.items():
                if hasattr(request_object, key) and key != 'id':
                    setattr(request_object, key, value)

            db.session.commit()
           

            return {"message": "Request updated successfully", "data": update_data}, 200
        except Exception as e:
            return {"error": str(e)}, 500


       