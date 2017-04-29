# -*- coding: utf-8 -*-
{
    'name': "Test Report",

    'summary': """
        Results of a Test Script
        """,

    'description': """
        TestReport is a resource that includes summary information on the results of executing a TestScript.

        **Scope and Usage**

        The TestScript resource is used to define tests that can be executed on one or more FHIR servers. The TestReport resource defines how systems should encode the summarized results of executing a TestScript.

        The TestReport structure mirrors the TestScript concepts of having sections for setup, tests, and teardown. If present, these ordered lists should mirror the actions (either operations or assertions) of the referenced TestScript with a result code: pass, skip, fail, warning, or error.
    """,

    'author': "Luigi Sison",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_test_script'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_test_report_views.xml',
        'views/hc_res_test_report_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}