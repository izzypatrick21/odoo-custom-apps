from odoo import fields, api, models, _

class Customers(models.Model):
    _inherit = 'res.partner'
    
    bank_id = fields.Many2one('bank.bank', string='Bank ID', default=lambda self: self.env.user.bank_id.id)
    balance = fields.Float(string='Balance')