# -*- coding: utf-8 -*-
{
    'name': "Account",

    'summary': """
        Financial account
    """,

    'description': """
        A financial tool for tracking value accrued for a particular purpose. 
        In the healthcare field, used to track charges for a patient, cost centres, etc.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/account.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'hc_healthcare_service', 'hc_coverage'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_account_views.xml',
        'views/hc_res_account_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}