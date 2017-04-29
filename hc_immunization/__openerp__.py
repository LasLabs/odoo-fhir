# -*- coding: utf-8 -*-
{
    'name': "Immunization",

    'summary': """
        Vaccination, vaccine reaction and protocol
        """,

    'description': """
        Describes the event of a patient being administered a vaccination or a record of a vaccination 
        as reported by a patient, a clinician or another party and may include vaccine reaction information 
        and what vaccination protocol was followed.

        **Scope and Usage** 
        
        The Immunization resource is intended to cover the recording of current and historical administration 
        of vaccines to patients across all healthcare disciplines in all care settings and all regions. 
        This includes immunization of both humans and animals, but does not include the administration of 
        non-vaccine agents, even those that may have or claim to have immunological effects.

    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/immunization.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_observation'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_immunization_views.xml',
        'views/hc_res_immunization_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}