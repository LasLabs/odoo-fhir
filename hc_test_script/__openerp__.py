# -*- coding: utf-8 -*-
{
    'name': "Test Script",

    'summary': """
        FHIR server tests
        """,

    'description': """
        TestScript is a resource that specifies a suite of tests against a FHIR server implementation to determine compliance against the FHIR specification.

        **Scope and Usage** 
        
        The TestScript resource is used to define tests that can be executed on one or more FHIR servers. The TestScript resource would typically contain

        * a list of fixtures (required resources used in the tests)
        * setup procedures
        * a suite of thematically related tests
        * teardown procedures

    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/testscript.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_capability_statement'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_test_script_views.xml',
        'views/hc_res_test_script_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}