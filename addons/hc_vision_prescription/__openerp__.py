# -*- coding: utf-8 -*-
{
    'name': "Vision Prescription",

    'summary': """
        Prescription for glasses and contact lenses
        """,

    'description': """
        An authorization for the supply of glasses and/or contact lenses to a patient.

        **Scope and Usage** 
        This resource covers all prescriptions for glasses and contact lenses for a patient.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/visionprescription.html",

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
        'views/hc_res_vision_prescription_views.xml',
        'views/hc_res_vision_prescription_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}