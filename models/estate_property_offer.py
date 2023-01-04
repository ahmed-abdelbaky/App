from odoo import models, fields, api


class estatePropertyOffer(models.Model):
    _name = 'estate.property.offer'

    price = fields.Float("Price")
    status = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ], string="Status", copy=False
      )
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")