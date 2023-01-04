from odoo import models, fields, api


class estatePropertyType(models.Model):
    _name = "estate.property.type"

    name = fields.Char('Name', required=True)
