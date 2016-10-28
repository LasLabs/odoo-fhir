# -*- coding: utf-8 -*-
{
    'name': "Questionnaire Response",

    'summary': """
        Completed Questionnaire
        """,

    'description': """
        A structured set of questions and their answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the 
        grouping of the underlying questions.

        **Scope and Usage**

        QuestionnaireResponse provides a complete or partial list of answers to a set of questions filled when responding to a questionnaire. 
        The questions may be included directly or by reference to a Questionnaire resource that defines the questions as well as the constraints on the allowed answers. 
        In some cases, both formal rules for editing the questionnaire (via link to Questionnaire) as well as sufficient local information to allow rendering of the 
        questionnaire may be provided.

        Each time a questionnaire is completed for a different subject or at a different time, a distinct QuestionnaireResponse is generated, though it may be possible 
        for a previously entered set of answers to be edited or updated.

        Questionnaires cover the need to communicate data originating from forms used in medical history examinations, research questionnaires and 
        sometimes full clinical specialty records. In many systems this data is collected using user-defined screens and forms. 
        Questionnaires record specifics about data capture - exactly what questions were asked, in what order, what choices for answers were, etc. 
        Each of these questions is part of the Questionnaire, and as such the Questionnaire is a separately identifiable Resource, 
        whereas the individual questions are not.

        Examples of Questionnaires include:

        * Past medical history (PMH)
        * Family diseases
        * Social history
        * Research questionnaires and Case report forms (CRFs)
        * Quality and evaluation forms
        * Patient intake form (e.g. clipboard)
        * Insurance claim form
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/questionnaireresponse.html",

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
        'views/hc_res_questionnaire_response_views.xml',
        'views/hc_res_questionnaire_response_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}