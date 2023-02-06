from odoo import models, fields, api


class estatePropertyType(models.Model):
    _name = "estate.property.type"
    _order = "name"

    name = fields.Char('Name', required=True)
    property_ids = fields.One2many('estate.property', 'type_id')
    sequence = fields.Integer('Sequence')
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    offer_count = fields.Integer('offer count', compute='_compute_count_offer')
    _sql_constraints = [
        ('check_unique_type_name', 'unique(name)', 'Name of type already found')
    ]

    @api.depends('offer_ids')
    def _compute_count_offer(self):
        for record in self:
            if record.offer_ids:
                record.offer_count = len(record.offer_ids)
            else:
                record.offer_count = 0