# -*- coding: utf-8 -*-
{
    'name': "Observation",

    'summary': """
        Meaurements, assertions
        """,

    'description': """
        Measurements and simple assertions made about a patient, device or other subject.

        **Scope and Usage** 

        Observations are a central element in healthcare, used to support diagnosis, monitor progress, 
        determine baselines and patterns and even capture demographic characteristics. 
        Most observations are simple name/value pair assertions with some metadata, 
        but some observations group other observations together logically, or even are multi-component observations. 
        Note that the DiagnosticReport resource provides a clinical or workflow context for a set of observations.

        Uses for the Observation resource include:

        * Vital signs such as body weight, blood pressure, and temperature
        * Laboratory Data llike blood glucose, or an estimated GFR
        * Imaging results like bone density or fetal measurements
        * Devices Measurements such as EKG data or Pulse Oximetry data
        * Clinical assessment tools such as APGAR or a Glasgow Coma Score
        * Personal characteristics: such as eye-color
        * Social history like tobacco use, family support, or cognitive status
        * Core characteristics like pregnancy status, or a death assertion

    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/observation.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_sequence'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_observation_views.xml',
        'views/hc_res_observation_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}