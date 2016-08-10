# -*- coding: utf-8 -*-
{
    'name': "Condition",

    'summary': """
        Conditions, problems or diagnoses
    """,

    'description': """
        Detailed information about conditions, problems or diagnoses recognized by a clinician. 
        There are many uses including: recording a diagnosis during an encounter; 
        populating a problem list or a summary statement, such as a discharge summary.

        **Scope and Usage**

        Used to record detailed information pertinent to a clinician's assessment and assertion 
        of a particular aspect of a person's state of health. Examples of condition include problems, 
        diagnoses, concerns, issues. There are many uses of condition which include:
        
        * recording a problem, diagnosis, health concern or health issue during an encounter
        * the use of such information to populate a problem list of a summary statement such as a discharge summary
        
        This resource is used to record detailed information about a clinician's assessment and assertion 
        of a particular aspect of a patient's state of health. It is intended for use to record information 
        about a disease/illness identified from application of clinical reasoning over the pathologic 
        and pathophysiologic findings (diagnosis), or identification of health issues/situations that 
        require ongoing monitoring and/or management (health issue/concern), or identification of 
        health issues/situations considered harmful, potentially harmful and required to be investigated 
        and managed (problems).

        The condition resource may also be used to record certain health state of a patient 
        which does not normally present negative outcome (until complications are predicted or detected), 
        e.g. pregnancy. Examples of complications of pregnancy include: hyperemesis gravidarum, 
        preeclampsia, eclampsia - which are captured as problems/diagnoses.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/condition.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_procedure'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_condition_views.xml',
        'views/hc_res_condition_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}