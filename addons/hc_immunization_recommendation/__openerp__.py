# -*- coding: utf-8 -*-
{
    'name': "Immunization Recommendation",

    'summary': """
        Immunization recommendation and status
        """,

    'description': """
        A patient's point-in-time immunization and recommendation 
        (i.e. forecasting a patient's immunization eligibility according to a 
        published schedule) with optional supporting justification.

        **Scope and Usage**
         
        The ImmunizationRecommendation resource is intended to cover communication of a 
        specified patient's immunization recommendations and status across all healthcare 
        disciplines in all care settings and all regions.


    """,

    'author': "Luigi Sison",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_allergy_intolerance', 'hc_observation'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_immunization_recommendation_views.xml',
        'views/hc_res_immunization_recommendation_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}