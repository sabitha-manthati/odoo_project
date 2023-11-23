# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'Purchase Dashboard',
    'version': '16.0.0.1',
    'category': 'Purchase',
    'author': 'sabitha',
    'summary': 'CRM. ',
    'website': 'www.rdp.in',
    'sequence': '10',
    'description': """
     
    """,
    'depends': ['base','purchase','sale'],
    'data': [

       'views/purchase_dashboard.xml',
       'views/purchase_order_view.xml',

    ],

    # 'license': 'OPL-1',
    # 'application': True,
    'installable': True,


}
