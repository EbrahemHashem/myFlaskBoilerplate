from flask_restx import Namespace ,fields

class TestDto:
    api = Namespace("test",description="test file")
    test = api.model(
        "test object",
        {
                # "title":fields.String,
                "instruction":fields.String,
                "attached":fields.boolean,
                "signed":fields.boolean,
                "voice_attached":fields.boolean,
                "description":fields.String,
                "status":fields.String
        }
    )
    data_resp = api.model(
        "Test Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
        },
    )

    data_update = api.model(
        "update object",
        {       "id":fields.String(required = True),
                "title":fields.String,
                "instruction":fields.String,
                "attached":fields.boolean,
                "signed":fields.boolean,
                "voice_attached":fields.boolean,
                "description":fields.String,
                "status":fields.String
        }
    )
