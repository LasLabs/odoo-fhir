# -*- coding: utf-8 -*-
{
    'name': "Enrollment Response",

    'summary': """
        Insurance plan details
        """,

    'description': """
        This resource provides enrollment and plan details from the processing of an Enrollment resource.

        **Scope and Usage**

        The EnrollmentResponse resource provides enrollment and plan details from the processing of an Enrollment resource.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/enrollmentresponse.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_enrollment_request'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_enrollment_response_views.xml',
        'views/hc_res_enrollment_response_templates.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}