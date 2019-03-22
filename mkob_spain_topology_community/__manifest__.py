# -*- coding: utf-8 -*-
{
    'name': "Spain Topology Community",
    'summary': """
        Spain Topology Community""",

    'description': """
       Spain Topology Community
    """,
    "category": "Localisation",
    "website": "https://melkart.io/",
    "author": "Melkart O&B",
    "license": "LGPL-3",
    'depends': [
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/autonomous_community.xml',
        'views/base_menu.xml',
        'data/groups.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'qweb': [
    ],
    'application': True,
    "installable": True,
}
