from odoo import models, fields, api


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('sourth', 'Sourth'),
            ('east', 'East'),
            ('west', 'West')
        ]
    )
