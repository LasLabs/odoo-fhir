# -*- coding: utf-8 -*-
{
    'name': "Research Subject",

    'summary': """
        Human or animal subject
        """,

    'description': """
        A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge. 
        This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional 
        and investigative techniques. ResearchStudies involve the gathering of information about human or animal subjects. 
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/researchsubject.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_research_study', 'hc_consent'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_research_subject_views.xml',
        'views/hc_res_research_subject_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}