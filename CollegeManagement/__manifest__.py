{
    'name': 'College Management',
    'version': '1.1',
    'sequence': 1,
    'author': 'Planet Odoo',
    'description': """Module Of College""",
    'category': '',
    'website': '',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/student_wizard_view.xml',
        'reports/report.xml',
        'reports/custom_report.xml',
        'reports/library_report.xml',
        'reports/custom_library_report.xml',
        'views/student_info_view.xml',
        'views/library_info_view.xml',
        'views/books_info_view.xml',

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
