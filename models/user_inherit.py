from odoo import models, fields, api


class userInherit(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('estate.property', 'user_id')
