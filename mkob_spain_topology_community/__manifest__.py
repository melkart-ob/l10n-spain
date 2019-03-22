# -*- coding: utf-8 -*-
{
    'name': "Spain Topology Community",
    'summary': """
        Spain Topology Community""",

    'description': """
       Spain Topology Community
    """,
    "category": "Website",
    "website": "https://melkart-ob.com/",
    "author": "Melkart",
    "license": "LGPL-3",
    'depends': [
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/autonomous_community.xml',
        'views/base_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'qweb': [
    ],
    'application': True,
    "installable": True,
}
