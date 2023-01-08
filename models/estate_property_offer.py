from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


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
    validity = fields.Integer("Validity", default='7')
    date_deadline = fields.Date('Date Deadline', compute="_compute_date", inverse='_inverse_date')

    @api.depends('validity')
    def _compute_date(self):
        for record in self:
            record.date_deadline = self.env.user.create_date + relativedelta(days=record.validity)
           # print('record.date_deadline', record.date_deadline)

    def _inverse_date(self):
        for record in self:
            record.date_deadline = record.datetime()
