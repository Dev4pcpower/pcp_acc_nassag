from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    account_commission_debit = fields.Many2one('account.account', string='Account', ondelete='cascade',
                                 help="Select an accounting account which will use analytic account specified in analytic default (e.g. create new customer invoice or Sales order if we select this account, it will automatically take this as an analytic account)")
    account_commission_credit = fields.Many2one('account.account', string='Account', ondelete='cascade',
                                 help="Select an accounting account which will use analytic account specified in analytic default (e.g. create new customer invoice or Sales order if we select this account, it will automatically take this as an analytic account)")