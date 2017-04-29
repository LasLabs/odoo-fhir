# -*- coding: utf-8 -*-
{
    'name': "Process Request",

    'summary': """
        Action specifications
        """,

    'description': """
        This resource provides the target, request and response, and action details for an action to be performed by the target on or about existing resources. 

        **Scope and Usage**

        The ProcessRequest resource allows for the specification of an action to be performed on an existing resource or resources and then provides the additional 
        supporting information to support that action. The actions currently defined are: cancel, poll, reprocess, and status.  

    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/processrequest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_practitioner'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_process_request_views.xml',
        'views/hc_res_process_request_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}