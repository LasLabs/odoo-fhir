# -*- coding: utf-8 -*-
{
    'name': "Clinical Impression",

    'summary': """
        Assessment, impression, diagnosis
        """,

    'description': """
        A record of a clinical assessment performed to determine what problem(s) may affect the patient 
        and before planning the treatments or management strategies that are best to manage a patient's condition. 
        Assessments are often 1:1 with a clinical consultation / encounter, but this varies greatly depending on the 
        clinical workflow. This resource is called "ClinicalImpression" rather than "ClinicalAssessment" to avoid 
        confusion with the recording of assessment tools such as Apgar score.

        **Scope and Usage**
         
        Performing a clinical assessment is a fundamental part of a clinician's workflow, performed repeatedly throughout 
        the day. In spite of this - or perhaps, because of it - there is wide variance in how clinical impressions 
        are recorded. Some clinical assessments simply result in an impression recorded as a single text note in the patient 'record' 
        (e.g. "Progress satisfactory, continue with treatment"), while others are associated with careful, detailed record keeping of the 
        evidence gathered, the reasoning leading to a differential diagnosis, and the actions taken during or planned as a result of the 
        clinical assessment, and there is a continuum between these. This resource is intended to be used to cover all these use cases.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/clinicalimpression.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_family_member_history','hc_questionnaire_response', 'hc_diagnostic_report'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_clinical_impression_views.xml',
        'views/hc_res_clinical_impression_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}