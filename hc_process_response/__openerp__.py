# -*- coding: utf-8 -*-
{
    'name': "Process Response",

    'summary': """
        Processing status, errors and notes
        """,

    'description': """
        This resource provides processing status, errors and notes from the processing of a resource. 

        **Scope and Usage**

        The ProcessResponse resource indicates the resource for which the processing status is requested and provides simple acknowledgement and status 
        information of application level errors. It may also be used to convey additional processing requirements in a text form. 

        This is the formal response to a ProcessRequest and may be used as a application level response to PaymentNotice and SupportingDocumentation resources.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/processresponse.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_communication_request'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_process_response_views.xml',
        'views/hc_res_process_response_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}