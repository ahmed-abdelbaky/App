from odoo import models, fields, api


class estatePropertyTag(models.Model):
    _name = 'estate.property.tag'

    name = fields.Char("Name", required=True)

    _sql_constraints = [
        ('check_unique_tag_name', 'unique(name)', 'Name of Tag already found')
    ]