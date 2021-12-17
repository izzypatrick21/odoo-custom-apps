# -*- coding: utf-8 -*-
{
    'name': "Bank Deposit Management",

    'summary': """
        managing customer deposits and withdrawals""",

    'description': """
        Managing customer deposits and withdrawals
    """,

    'author': "Patrick Isaiah",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/group_security_view.xml',
        'data/ir_sequence_data.xml',
        'views/bank_view.xml',
        'views/transaction_view.xml',
        'views/customer_view.xml',
        'views/user_view.xml',
        'views/templates.xml',
        
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
