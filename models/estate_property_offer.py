from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class estatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _order = "price desc"

    price = fields.Float("Price")
    state = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused')
        ], string="Status", copy=False
      )
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", string="Property")
    validity = fields.Integer("Validity", default='7')
    date_deadline = fields.Date('Deadline', compute="_compute_date", inverse='_inverse_date')

    @api.depends('validity')
    def _compute_date(self):
        for record in self:
            record.date_deadline = datetime.now().date() + relativedelta(days=record.validity)
           # print('record.date_deadline', record.date_deadline)

    def _inverse_date(self):
        for record in self:
            record.date_deadline = datetime.now().date()

    def button_accept(self):
        for record in self:
            record.property_id.selling_price = record.price
            record.property_id.partner_id = record.partner_id
            record.state = 'accepted'
            record.property_id.state = 'offer_accepted'

    def button_refuse(self):
        for record in self:
            record.state = 'refused'
            record.property_id = False

    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'THE VALUE OF PRICE MUST BE POSITIVE')
    ]




