from odoo import models, fields
# from datetime import datetime
from dateutil.relativedelta import relativedelta


class estateProperty(models.Model):
    _name = 'estate.property'
    _description = 'estate property'

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date( 'Available From', default=lambda self: fields.Datetime.now() + relativedelta(months=+3), copy=False)
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default='2')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ], string="Garden Orientation"
     )
    active = fields.Boolean('Active')
    state = fields.Selection(
        [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold_and_cancel', 'Sold and Cancel')
        ],
        default='new', required=True, copy=False, string='Status'
        )
