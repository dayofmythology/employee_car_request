# -*- coding: utf-8 -*-
{
    'name': "Employee Car Request",

    'summary': """
        Request a car and get the approval""",

    'description': """
        This app allows the employee to request a car and get an approval from a designated approver within the company
    """,

    'author': "Mohamed Ait",
    'website': "http://www.mediadesk.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','fleet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}