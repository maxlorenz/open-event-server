from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship
from flask_rest_jsonapi import ResourceList

from app.api.bootstrap import api
from app.api.helpers.utilities import dasherize
from app.models import db
from app.models.permission import Permission


class AdminPermissionsSchema(Schema):
    """
    Permissions schema

    Sample information: `organizer`
    """

    class Meta:
        type_ = 'admin-permissions'
        self_view = 'v1.admin_permissions'
        inflect = dasherize

    id = fields.String()
    role = fields.Dict()
    title_name = fields.String()
    can_create = fields.Boolean()
    service_name = fields.String()

class AdminPermissionsList(ResourceList):
    """
    Resource
    """

    methods = ['GET', 'POST']
    decorators = (api.has_permission('is_admin'), )
    schema = AdminPermissionsSchema
    data_layer = {'model': Permission, 'session': db.session}
