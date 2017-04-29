# -*- coding: utf-8 -*-
{
    'name': "Risk Assessment",

    'summary': """
        Prognosis, prediction, risk assessment
        """,

    'description': """
        An assessment of the likely outcome(s) for a patient or other subject as well as the likelihood of each outcome.

        **Scope and Usage**

        This resource captures predicted outcomes for a patient or population on the basis of source information. 

        Examples include:

        * A prognosis statement for a particular condition
        * Risk of health outcome (heart attack, particular type of cancer) on the basis of lifestyle factors and/or family history
        * List of potential health risks based on a patient's genetic analysis
        * A prediction of outbreak infection rates within a geography based on immunization rates
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/riskassessment.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_encounter'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_risk_assessment_views.xml',
        'views/hc_res_risk_assessment_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}