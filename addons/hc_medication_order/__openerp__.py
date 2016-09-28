# -*- coding: utf-8 -*-
{
    'name': "Medication Order",

    'summary': """
        Orders for medication, nutrition and diet/vitamin supplements, medication-related devices
        """,

    'description': """
        An order for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationOrder" rather than "MedicationPrescription" to generalize the use across inpatient and outpatient settings as well as for care plans, etc.

        **Scope and Usage**
         
        This resource covers all orders for medications for a patient. This includes in-patient medication orders as well as community orders 
        (whether filled by the prescriber or by a pharmacy). It also includes orders for over-the-counter medications (e.g. Aspirin), 
        total parenteral nutrition and diet/ vitamin supplements. It may be used to support the order of medication-related devices. 
        It is not intended for use in prescribing particular diets, or for ordering non-medication-related items (eye-glasses, supplies, etc.).
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/medicationorder.html",

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
        'views/hc_res_medication_order_views.xml',
        'views/hc_res_medication_order_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}