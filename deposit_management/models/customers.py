from odoo import fields, api, models, _

class Customers(models.Model):
    _inherit = 'res.partner'
    
    bank_id = fields.Many2one('bank.bank', string='Bank ID')