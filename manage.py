import os
# 
import click
from flask_migrate import Migrate
from app import create_app, db, socketio
from flask_cors import CORS
# 
from app.models.order_services import OrderService
from app.models.services_order import ServiceOrder
from app.models.requests import Requests
from app.models.user import User
from app.models.roles import Role
from app.models.clients import Client
from app.models.permissions import Permissions
from app.models.projects import Projects
from app.models.units import Units
from app.models.developer import Developer
from app.models.villages import Villages
from app.models.user_roles import UserProjectRoles
from app.models.client_roles import ClientRoles
from app.models.qr_codes_requests import Qr_codes
from app.models.notes import Notes
from app.models.types import Types
from app.models.images import Image
from app.models.services import Services
from app.models.services_schedules import ServiceSchedule
from app.models.black_list import BlackList
from app.models.white_list import WhiteList
from app.models.invoices import Invoice
from app.models.quota import Quota
from app.models.gates import Gates
from app.models.gate_schedule import GateSchedule
from app.models.types import Types
from app.models.cards import Cards
from app.models.schedule_controller import Scheduler
from app.models.building import Buildings
from app.models.gate_quota import GateQuota
from app.models.client_units import ClientUnits
from app.models.blocks import Blocks
from app.models.ratings import Ratings
from app.models.promo_codes import PromoCodes
from app.models.attendee import Attendee
from app.models.event import Event
from app.models.host import Host
from app.models.ticket import Ticket
from app.models.waiting_list import WaitingList
from app.models.event_tickets import EventTicketType
from app.models.utilities import Utilities
from app.models.utilities_section import UtilitiesٍSections
from app.models.notifications import Notifications
from app.models.client_notifications import Client_notifications
from app.models.field_booking import FieldBooking
from app.models.club import Club
from app.models.field import Field
from app.models.field_schedule import FieldSchedule
from app.models.field_time_slots import TimeSlot
from app.models.sport import Sport
from app.models.subscription import Subscription
from app.models.unit_details import UnitDetails
from app.models.amenities import Amenity
from app.models.unit_booking import UnitBooking
from app.models.location import Location
from app.models.user_cards import UserCards
from app.models.news import News
from app.models.user_access_configuration import AccessConfiguration
from app.models.invoice_items import Item
from app.models.services_timeline_ticket import ServiceOrderTicket
from app.models.unit_rental_booking import UnitRentalBooking

# 

from dotenv import load_dotenv
# from flask_marshmallow import Marshmallow

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

##

import click
from flask_migrate import Migrate
from app import create_app, db

# Import models
# from app.models.user import User, Role, Permission


app = create_app(os.getenv("FLASK_CONFIG") or "development")
migrate = Migrate(app, db)

def run():
    app.run(app, host='0.0.0.0', port=5000, debug=True)
    
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,
                User=User,
                Role=Role,
                Permissions=Permissions,
                Client=Client,
                Projects=Projects,
                Units=Units,
                AccessConfiguration=AccessConfiguration,
                Developer=Developer,
                Villages=Villages,
                UserProjectRoles=UserProjectRoles,
                Qr_codes=Qr_codes,
                News=News,
                Notes=Notes,
                Types=Types,
                Image=Image,
                Gates=Gates,
                GateSchedule=GateSchedule,
                WhiteList=WhiteList,
                BlackList=BlackList,
                Invoice=Invoice,
                Cards=Cards,
                Scheduler=Scheduler,
                Buildings=Buildings,
                GateQuota=GateQuota,
                ClientUnits=ClientUnits,
                Blocks=Blocks,
                Services=Services,
                ServiceSchedule=ServiceSchedule,
                PromoCodes=PromoCodes,
                Ratings=Ratings,
                Attendee=Attendee,
                Event=Event,
                Host=Host,
                Ticket=Ticket,
                WaitingList=WaitingList,
                EventTicketType=EventTicketType,
                UtilitiesٍSections=UtilitiesٍSections,
                Utilities=Utilities,
                ClientRoles=ClientRoles,
                Notifications=Notifications,
                Client_notifications=Client_notifications,
                # 
                FieldBooking=FieldBooking,
                Item = Item,
                ServiceOrderTicket = ServiceOrderTicket,
                UnitRentalBooking = UnitRentalBooking,
                # 
                Club=Club,
                ServiceOrder=ServiceOrder,
                Requests=Requests,
                Field=Field,
                FieldSchedule=FieldSchedule,
                TimeSlot=TimeSlot,
                Sport=Sport,
                Subscription=Subscription,
                Amenity=Amenity,
                UnitDetails=UnitDetails,
                UnitBooking=UnitBooking,
                Location=Location,
                OrderService=OrderService,
                UserCards=UserCards,
                Quota=Quota)


@app.cli.command()
@click.argument("test_names", nargs=-1)
def test(test_names):
    """ Run unit tests """
    import unittest

    if test_names:
        """ Run specific unit tests.

        Example:
        $ flask test tests.test_auth_api tests.test_user_model ...
        """
        tests = unittest.TestLoader().loadTestsFromNames(test_names)

    else:
        tests = unittest.TestLoader().discover("tests", pattern="test*.py")

    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0

    # Return 1 if tests failed, won't reach here if succeeded.
    return 1
