from odoo import fields, api, models, _

class Banks(models.Model):
    _name = 'bank.bank'
    _description = 'Banks'
    
    name = fields.Char(string="Bank Name", required=True)
    code = fields.Char(string='Code', default='New', readonly=True)
    balance = fields.Float(string='Balance')
    partner_id = fields.Many2one('res.partner', string='Address')
    
    _sql_constraints = [
        ('unique_bank_name', 'unique(name)', 'Bank Name already exist, please provide another')
    ]
    
    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('bank.bank')
        res = super(Banks, self).create(vals)
        return res



