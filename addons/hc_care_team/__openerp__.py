# -*- coding: utf-8 -*-
{
    'name': "Care Team",

    'summary': """
        Practitioners, caregivers, patients
        """,

    'description': """
        The Care Team includes all the people and organizations who plan to participate in the coordination and 
        delivery of care for a patient.

        **Scope and Usage** 
        
        The Care Team resource includes all the people and/or organizations who plan to participate in the coordination 
        and delivery of care for a patient. This is not limited to practitioners, but may include other caregivers such as 
        family members, guardians, the patient themself, or others. The Care Team, depending on where used, may include 
        care team members specific to a particular care plan, an episode, an encounter, or may reflect all known team members 
        across these perspectives.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/careteam.html",

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
        'views/hc_res_care_team_views.xml',
        'views/hc_res_care_team_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}