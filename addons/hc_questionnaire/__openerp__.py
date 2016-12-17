# -*- coding: utf-8 -*-
{
    'name': "Questionnaire",

    'summary': """
        Collection of questions like forms
        """,

    'description': """
        A structured set of questions intended to guide the collection of answers. The questions are ordered and grouped into coherent subsets, corresponding to the structure of the grouping of the underlying questions.

        **Scope and Usage** 
        
        A Questionnaire is an organized collection of questions intended to solicit information from patients, providers or other individuals involved in the healthcare domain. 
        They may be simple flat lists of questions or can be hierarchically organized in groups and sub-groups, each containing questions. 
        The Questionnaire defines the questions to be asked, how they are ordered and grouped, any intervening instructional text and what the constraints are on the 
        allowed answers. The results of a Questionnaire can be communicated using the QuestionnaireResponse resource.

        Questionnaires cover the need to communicate data originating from forms used in medical history examinations, research questionnaires and sometimes 
        full clinical specialty records. In many systems this data is collected using user-defined screens and forms. Questionnaires define specifics 
        about data capture - exactly what questions were asked, in what order, what choices for answers were, etc. 
        Each of these questions is part of the Questionnaire, and as such the Questionnaire is a separately identifiable Resource, 
        whereas the individual questions are not.

        Examples of Questionnaires include:

        * Past medical history (PMH)
        * Family diseases
        * Social history
        * Research questionnaires/Clinical research forms (CRFs)
        * Quality and evaluation forms
        * Patient intake form (e.g. clipboard)
        * Insurance claim form
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/questionnaire.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_value_set'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_questionnaire_views.xml',
        'views/hc_res_questionnaire_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}