# -*- coding: utf-8 -*-
{
    'name': "Medication Administration",

    'summary': """
        Consumption or administration of medication, vaccines, etc.""",

    'description': """
        Describes the event of a patient consuming or otherwise being administered a medication. This may be as simple as swallowing a tablet or 
        it may be a long running infusion. Related resources tie this event to the authorizing prescription, and the specific encounter between patient 
        and health care practitioner.

        **Scope and Usage**

        This resource covers the administration of all medications and vaccines. Please refer to the Immunization Resource/Profile for the treatment of vaccines. 
        It will principally be used within care settings (including inpatient) to record the capture of medication administrations, including self-administrations 
        of oral medications, injections, intra-venous adjustments, etc. It can also be used in out-patient settings to record allergy shots and other non-immunization 
        administrations. In some cases it might be used for home-health reporting, such as recording self-administered or even device-administered insulin.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/medicationadministration.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_medication_order'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_medication_administration_views.xml',
        'views/hc_res_medication_administration_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}