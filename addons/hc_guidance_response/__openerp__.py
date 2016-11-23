# -*- coding: utf-8 -*-
{
    'name': "Guidance Response",

    'summary': """
        Response to a guidance request
        """,

    'description': """
        A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken. 

        **Scope and Usage** 
         
        The GuidanceResponse resource is used to represent the result of invoking a decision support service. It provides a container for the status of the response, any warnings or messages returned 
        by the service, as well as the output data of the module and any suggested actions to be performed.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/guidanceresponse.html",

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
        'views/hc_res_guidance_response_views.xml',
        'views/hc_res_guidance_response_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}