# -*- coding: utf-8 -*-
{
    'name': "pcp_acc_nassag",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account','branch','branch_accounting_report','sale_management'],

    # always loaded
    'data': [

        'security/analytic_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/menu_item.xml',
        'views/assets.xml',
        'views/res_config_settings_views.xml',
        'views/analytic_branch.xml',
        'views/account_move.xml',
        'views/branch_analytic_line.xml',
        'views/report_financial.xml',
        'views/search_template_view.xml',
        'wizard/commission_invoice_wizard.xml',
        'views/sale_order_commission_invoice.xml',
        'wizard/multicurrency_revaluation.xml',
        'wizard/report_export_wizard.xml',
        'wizard/fiscal_year.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
