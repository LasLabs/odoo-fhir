# -*- coding: utf-8 -*-
{
    'name': "Charge Item",

    'summary': """
        Provision of product for a patient
        """,

    'description': """
        The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, 
        but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. 
        Main Usage of the ChargeItem is to enable the billing process and internal cost allocation. 

        **Scope and Usage** 

        Tracking Financial information is vital in Patient Administration and Finance systems in most Healthcare Organizations. 
        The resource ChargeItem describes the charge for provision of healthcare provider products for a certain patient, therefore referring not only to the product, 
        but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem 
        is to enable the billing process and internal cost allocation. They are created as soon as the products are planned or provisioned, references to Encounters 
        and/or Accounts can be maintained in a later process step.

        The target of ChargeItem.definition may provide information on the Charge code such as pricing and inclusion/exclusion rules as well as factors that apply 
        under certain conditions. In many cases however this information may been drawn from sources outside of FHIR depending on the distribution format of the code catalogue. 
        The ChargeItem assumes that such information is either implicitly known by the communicating systems or explicitly shared through the ChargeItem.definition. 
        Therefore explicit pricing information is not shared within the ChargeItem resource. Also, the systems posting the ChargeItems are not expected to apply the 
        rules associated with the charge codes as they may not know the whole context of the patient/encounter to evaluate such rules. It lies within the responsibity 
        of a billing engine, to collect the ChargeItems in the context of an Account or Encounter at a certain point in time (e.g. discharge of the patient) and to 
        evaluate the associated rules resulting in some of the ChargeItems to be set to the status "not billable" in case the rules exclude them from being billed, 
        or to create financial transactions according to base price and factors. Additional references to Encounter/EpisodeOfCare, Patient/Group and Services provide 
        further context to help billing systems determine the appropriate account and establish the clinical/financial context to evaluate the rules associated with 
        the charge codes. 
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/chargeitem.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_immunization', 'hc_diagnostic_report', 'hc_supply_delivery'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_charge_item_views.xml',
        'views/hc_res_charge_item_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}