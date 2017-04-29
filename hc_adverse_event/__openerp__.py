# -*- coding: utf-8 -*-
{
    'name': "Adverse Event",

    'summary': """
        Events causing unintended physical injury
        """,

    'description': """
    Actual or potential/avoided event causing unintended physical injury resulting from or contributed to by medical care, a research study or other healthcare 
    setting factors that requires additional monitoring, treatment, or hospitalization, or that results in death. 

    **Scope and Usage**

    AdverseEvent applies to events that occur during the course of medical care or medical research which may impact an individual as the recipient of care or the participant 
    in a research study. There are also events that occur within a care setting that may or may not impact an individual but had the potential to cause an adverse event. 
    Health care organizations monitor and report both adverse events as well as events that had the potential to cause patient harm. Data are often aggregated for reporting purposes. 
    
    An adverse event is the result of an intervention that caused unintentional harm to a specific subject or group of subjects. 
    Examples of adverse events include the administration of an incorrect drug or an incorrect dose of a drug causing an adverse reaction, 
    the use of an implanted device that causes an infection, or a biologic used during a research study that causes unanticipated renal failure. 
    These events are characterized by the need to capture cause and effect (although they may not be known at the time of the event), severity, and outcome. 
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/adverse_event.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_practitioner_role', 'hc_family_member_history', 'hc_document_reference', 'hc_procedure', 'hc_medication_statement', 'hc_research_study', 'hc_immunization'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_adverse_event_views.xml',
        'views/hc_res_adverse_event_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}