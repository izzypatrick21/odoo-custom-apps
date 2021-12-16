from odoo import fields, api, models, _


class Transactions(models.Model):
    _name = 'bank.transaction'
    
    customer_id = fields.Many2one('res.partner', string='Customer', required = True)
    bank_id = fields.Many2one('bank.bank', string='Bank', required = True)
    balance = fields.Float(string='Balance')
    remarks = fields.Char(string='Remarks')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], default='draft')
    
    
    
    