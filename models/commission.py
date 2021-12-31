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
