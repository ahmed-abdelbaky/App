from odoo import models, fields, api


class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _order = "name"

    name = fields.Char('Name', required=True)
    property_ids = fields.One2many('estate.property', 'type_id')

    _sql_constraints = [
        ('check_unique_type_name', 'unique(name)', 'Name of type already found')
    ]