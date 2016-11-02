# -*- coding: utf-8 -*-
{
    'name': "Operation Outcome",

    'summary': """
        Collection of error, warning or information messages
        """,

    'description': """
        A collection of error, warning or information messages that result from a system action.

        **Scope and Usage**

        Operation Outcomes are sets of error, warning and information messages that provide detailed information about the outcome of some attempted system operation. 
        They are provided as a direct system response, or component of one, where they provide information about the outcome of the operation.

        OperationOutcomes are used in the following circumstances:

        * When an RESTful operation fails
        * As the response on a validation operation, to provide information about the outcomes
        * As part of a message response, usually when the message has not been processed correctly
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/operationoutcome.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_operation_outcome_views.xml',
        'views/hc_res_operation_outcome_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}