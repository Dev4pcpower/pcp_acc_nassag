from collections import defaultdict
from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class CommissionLine(models.Model):
    _inherit = 'commission.line'

    validity_status = fields.Selection([
        ('invoice', 'Invoice'),
        ('tobe', 'To be Invoiced'),
    ], 'Status', sort=False, readonly=True, default='tobe')
    is_invoiced = fields.Boolean(copy=False, default=False)


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_commission = fields.Boolean(default=False)

    def action_claim(self):
        active_id = self.id
        commission_lines = self.env['invoice.commission.line'].search([('invoice_sale_order_id', '=', active_id)])
        account_debit = self.env['res.config.settings'].search([])[-1]
        account_invoice_obj = self.env['account.move.line']
        total = 0
        for rec in commission_lines:
            total += rec.total_commission_per_line
        self.env['account.move.line'].create([
            {
                'name': 'claim commission',
                'move_id': active_id,
                'account_id': account_debit.account_commission_debit.id,
                'debit': total,
                'credit': 0,
            },
            {
                'name': 'claim commission',
                'move_id': active_id,
                'account_id': account_debit.account_commission_credit.id,
                'debit': 0,
                'credit': total,
            }
        ])