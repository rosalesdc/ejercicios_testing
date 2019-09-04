# -*- coding: utf-8 -*-
{
    'name': "formulario_contacto",

    'summary': """
        Contactos web   
        """,

    'description': """
        Contactos wev
    """,

    'author': "Soluciones4g",
    'website': "http:soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/contactos_web_group.xml',
        'security/ir.model.access.csv',
        'views/contactos_web_views.xml',
        'views/templates.xml',
        'views/contactos_view_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}