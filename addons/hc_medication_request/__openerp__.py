# -*- coding: utf-8 -*-
{
    'name': "Medication Request",

    'summary': """
        Medication supply order, medication administration instruction
        """,

    'description': """
        An order for both supply of the medication and the instructions for administration of the medication to a patient. 
        The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across 
        inpatient and outpatient settings as well as for care plans, etc and to harmonize with workflow patterns.

        **Scope and Usage**

        This resource covers all orders for medications for a patient. This includes in-patient medication orders as well as community orders 
        (whether filled by the prescriber or by a pharmacy). It also includes orders for over-the-counter medications (e.g. Aspirin), 
        total parenteral nutrition and diet/ vitamin supplements. It may be used to support the order of medication-related devices. 
        It is not intended for use in prescribing particular diets, or for ordering non-medication-related items (eye-glasses, supplies, etc.).
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/medicationrequest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_observation', 'hc_referral_request', 'hc_procedure_request','hc_plan_definition'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_medication_request_views.xml',
        'views/hc_res_medication_request_templates.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}