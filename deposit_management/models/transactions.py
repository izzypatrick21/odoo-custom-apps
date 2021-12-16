from odoo import fields, api, models, _


class Transactions(models.Model):
    _name = 'bank.transaction'
    _description = 'bank transactions'
    
    name = fields.Many2one('res.partner', string='Customer', required = True)
    bank_id = fields.Many2one('bank.bank',string='Bank', required = True, default=lambda self: self.env.user.bank_id.id)
    balance = fields.Float(string='Balance')
    remarks = fields.Char(string='Remarks')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], default='draft')
    type = fields.Selection([('withdrawal', 'Withdrawal'), ('deposit', 'Deposit')],
                            string='Transaction Type', default='withdrawal', required=True)
    
    def transaction_done(self):
        self.state = 'done'
    
    
    
    