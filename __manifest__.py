{
    'name': 'QR Code on Invoice',
    'version': '1.0',
    'category': 'Accounting',
    'author':'James',
    'summary': 'Generates QR codes for invoices.',
    'description': 'This module generates a QR code for each invoice using a base URL and invoice number.',
    'depends': ['account'],
    'data': [
         'security/ir.model.access.csv',
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
