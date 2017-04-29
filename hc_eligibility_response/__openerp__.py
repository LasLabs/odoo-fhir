# -*- coding: utf-8 -*-
{
    'name': "Eligibility Response",

    'summary': """
        Eligibility, plan details
        """,

    'description': """
        This resource provides eligibility and plan details from the processing of an Eligibility resource.

        **Scope and Usage** 
        
        The EligibilityResponse resource provides eligibility and plan details from the processing of an EligibilityRequest resource. 
        It combines key information from a payor as to whether a Coverage is in-force, and optionally the nature of the Policy details.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/eligibilityresponse.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'hc_contract'
    'depends': ['hc_eligibility_request'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_eligibility_response_views.xml',
        'views/hc_res_eligibility_response_templates.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}