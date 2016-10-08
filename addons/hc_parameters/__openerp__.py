# -*- coding: utf-8 -*-
{
    'name': "Parameters",

    'summary': """
        Operation Request and Response
        """,

    'description': """
        **Scope and Usage**
        
        This special resource type is used to represent the operation request and response.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/parameters.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_parameters_views.xml',
        'views/hc_res_parameters_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}