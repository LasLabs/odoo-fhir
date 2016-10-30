# -*- coding: utf-8 -*-
{
    'name': "Diagnostic Report",

    'summary': """
        Diagnostic test findings and interpretations
        """,

    'description': """
        The findings and interpretation of diagnostic tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. 
        The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, 
        and formatted representation of diagnostic reports.

        **Scope and Usage** 
    
        A diagnostic report is the set of information that is typically provided by a diagnostic service when investigations are complete. 
        The information includes a mix of atomic results, text reports, images, and codes. The mix varies depending on the nature of the diagnostic procedure, 
        and sometimes on the nature of the outcomes for a particular investigation.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/diagnosticreport.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_media', 'hc_imaging_manifest'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_diagnostic_report_views.xml',
        'views/hc_res_diagnostic_report_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}