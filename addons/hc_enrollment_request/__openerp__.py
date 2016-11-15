# -*- coding: utf-8 -*-
{
    'name': "Enrollment Request",

    'summary': """
        Insurance enrollment
        """,

    'description': """
        This resource provides the insurance enrollment details to the insurer regarding a specified coverage.

        **Scope and Usage** 
    
        The EnrollmentRequest resource allows for the addition and removal of plan subscribers and their dependents 
        to health insurance coverage.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/enrollmentrequest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_eligibility_request'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_enrollment_request_views.xml',
        'views/hc_res_enrollment_request_templates.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}