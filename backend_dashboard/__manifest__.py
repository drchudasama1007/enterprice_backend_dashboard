# Copyright 2021 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Backend Dashboard',
    'category': 'hidden',
    'version': '13.0.1',

    'summary': 'Enterprice Backend Dashboard',

    'description': """
   Enterprice Backend Dashboard
        """,

    'author': 'Odoo Helper',

    'depends': ['web_enterprise','base',],
     # templates
    'data': [
        'views/assets.xml'
    ],

    'qweb': [
        "static/src/xml/*.xml",
    ],

    'images': ['images/OdooHelper.jpg'],

    'price': 18.17,
    'currency': 'USD',

    'installable': True,
    'application': False
}



