# Model Schemas
from app import ma

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "is_admin")

class RoleSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name")

class TypeSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name")

class CardSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "card_id", "type", "license_plate")
    type = ma.Nested(TypeSchema)

class ClientRatingSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ( "id", "first_name", "last_name", "email")


class VillageSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name")

class SimpleRatingSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "rating", "review", "joined_date")

class RatingSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "rating", "review", "joined_date", "client")
    client = ma.Nested(ClientRatingSchema)


class PermissionsSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "path", "edit", "view", "add", 'delete')

class PojectSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "description")

class VillageSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name")

class NoteSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "note", "timestamp", 'action', 'unit_id')

class ImageSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "image", "image_type")

class NamedUnitSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name")

class GateSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name")

class UnitSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "ext_id", "village")
    village = ma.Nested(VillageSchema)

class BlockSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "gates", "units")
    units = ma.List(ma.Nested(UnitSchema))
    gates = ma.List(ma.Nested(GateSchema))

class SimpleBlockSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "name", "gates")
    gates = ma.List(ma.Nested(GateSchema))

class ClientSchema(ma.Schema):
    class Meta:
        
        # Fields to expose, add more if needed.
        fields =("id", 
                "name",
                "phone_number",
                "birth_date",
                "email",
                "national_id",
                "verified", 
                "printed_id",
                "printed",
                "arabic_name",
                "cancelled",
                "gender",
                "activated",
                "ext_id",
                "valid_from",
                "valid_to",
                "cancelled",
                "national_id",
                "cards",
                "notes",
                "images",
                "type",
                "unit"
                )
    cards = ma.List(ma.Nested(CardSchema))
    images = ma.List(ma.Nested(ImageSchema))
    notes = ma.List(ma.Nested(NoteSchema))
    unit = ma.List(ma.Nested(UnitSchema))
    type = ma.Nested(TypeSchema)

class ListClientSchema(ma.Schema):
    class Meta:
        
        # Fields to expose, add more if needed.
        fields =("id", 
                "name",
                "phone_number",
                "birth_date",
                "email",
                "national_id",
                "verified", 
                "printed_id",
                "printed",
                "arabic_name",
                "cancelled",
                "gender",
                "activated",
                "ext_id",
                "valid_from",
                "valid_to",
                "cancelled",
                "national_id",
                "cards",
                "notes",
                "images",
                "type",
                )
    cards = ma.List(ma.Nested(CardSchema))
    images = ma.List(ma.Nested(ImageSchema))
    notes = ma.List(ma.Nested(NoteSchema))
    type = ma.Nested(TypeSchema)

class DeletedClientSchema(ma.Schema):
    class Meta:
        
        # Fields to expose, add more if needed.
        fields =("id", 
                "name",
                "phone_number",
                "birth_date",
                "email",
                "national_id",
                "verified", 
                "printed_id",
                "printed",
                "arabic_name",
                "cancelled",
                "gender",
                "activated",
                "deleted",
                "ext_id",
                "valid_from",
                "valid_to",
                "cancelled",
                "national_id",
                "type",
                )
    type = ma.Nested(TypeSchema)

class ClientLoginSchema(ma.Schema):
    class Meta:
        
        # Fields to expose, add more if needed.
        fields =("id", 
                "name",
                "phone_number",
                "birth_date",
                "email",
                "national_id",
                "verified", 
                "printed_id",
                "arabic_name",
                "cancelled",
                "gender",
                "activated",
                "ext_id",
                "valid_from",
                "valid_to",
                "cancelled",
                "national_id",
                "images",
                "type",
                "unit"
                )
    images = ma.List(ma.Nested(ImageSchema))
    unit = ma.List(ma.Nested(UnitSchema))
    type = ma.Nested(TypeSchema)

class QRSchema(ma.Schema):
    class Meta:
        
        # Fields to expose, add more if needed.
        fields =("id", 
                "customer_name",
                "birth_date",
                "phone_number",
                "email",
                "national_id",
                "relation",
                "verified",
                "printed_id",
                "printed",
                "arabic_name",
                "cancelled",
                "gender",
                "activated",
                "ext_id",
                "valid_from",
                "valid_to",
                "cancelled",
                "national_id",
                "cards",
                "notes",
                "images",
                "type",
                "unit"
                )
    cards = ma.List(ma.Nested(CardSchema))
    images = ma.List(ma.Nested(ImageSchema))
    notes = ma.List(ma.Nested(NoteSchema))
    unit = ma.List(ma.Nested(UnitSchema))
    type = ma.Nested(TypeSchema)
#
class ClientSimpleSchema(ma.Schema):
    class Meta:
        
        # Fields to expose, add more if needed.
        fields =("id", 
                "name",
                "phone_number",
                "birth_date",
                "email",
                "national_id",
                "verified",
                "printed_id",
                "printed",
                "arabic_name",
                "cancelled",
                "gender",
                "activated",
                "ext_id",
                "valid_from",
                "valid_to",
                "cancelled",
                "national_id"
                )

class GateSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id",
               "name",
               "face_rec_ip",
               "anpr_ip",
               "cctv_ip",
               "type",
               "ext_id")
    type = ma.Nested(TypeSchema)

class DeveloperSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id","name")

class CardSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id","card_id", "license_plate")

class BlackSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("id", "gate", 'client')
    
    gate = ma.Nested(GateSchema)
    client = ma.Nested(ClientSchema)
 