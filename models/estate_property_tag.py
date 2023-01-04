from odoo import models, fields, api


class estatePropertyTag(models.Model):
    _name = 'estate.property.tag'

    name = fields.Char("Name", required=True)