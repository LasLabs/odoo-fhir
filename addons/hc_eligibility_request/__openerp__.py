# -*- coding: utf-8 -*-
{
    'name': "Eligibility Request",

    'summary': """
        Query about insurance coverage
        """,

    'description': """
        This resource provides the insurance eligibility details from the insurer regarding a specified coverage and optionally some class of service.

        **Scope and Usage** 
        
        The EligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an 
        Eligibility Response, with information regarding whether the stated coverage is valid and in-force, and potentially the amount of 
        coverage which may be available to any services classes identified in this request.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/eligibilityrequest.html",

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
        'views/hc_res_eligibility_request_views.xml',
        'views/hc_res_eligibility_request_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}