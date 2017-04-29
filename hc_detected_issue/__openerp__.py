# -*- coding: utf-8 -*-
{
    'name': "Detected Issue",

    'summary': """
        Clinical issue
        """,

    'description': """
        Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions 
        for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.

        **Scope and Usage**

        This resource applies to various circumstances where there is a concern about an existing or proposed set of 
        clinical activity. The issue could relate to single, proposed, or multiple actions. It does not apply to 
        technical issues (e.g. lack of user permissions) but could relate to violation of patient consent limitations. 
        Examples include:

        * Drug-drug interactions
        * Inappropriate therapy (wrong dose, frequency, body site)
        * Duplicate therapy
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/detectedissue.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_device'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_detected_issue_views.xml',
        'views/hc_res_detected_issue_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}