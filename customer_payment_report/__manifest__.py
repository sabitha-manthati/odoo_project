{
    'name': 'Customer Payment Report',
    'version': '16.0.0.1',
    'category': 'Project',
    'author': 'RDP',
    'summary': 'Customer Payment Report',
    'website': 'www.rdp.in',
    'sequence': '10',
    'description': """
     
    """,
    'depends': ['base', 'sale','portal'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/customer_payment_report.xml',
        'wizards/customer_payment_report_wizard.xml',
        'views/customer_payment_report_view.xml',
        'report/payment_report.xml',
    ],

    # 'license': 'OPL-1',
    'application': True,
    'installable': True,


}