# -*- coding: utf-8 -*-
{
    'name': "Message Definition",

    'summary': """
        Messages between systems
        """,

    'description': """
        Defines the characteristics of a message that can be shared between systems, including the type of event that initiates the message, 
        the content to be transmitted and what response(s), if any, are permitted. 
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/messagedefinition.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_plan_definition'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_message_definition_views.xml',
        'views/hc_res_message_definition_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}