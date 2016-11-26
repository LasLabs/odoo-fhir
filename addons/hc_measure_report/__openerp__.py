# -*- coding: utf-8 -*-
{
    'name': "Measure Report",

    'summary': """
        Measure results
        """,

    'description': """
        The MeasureReport resource contains the results of evaluating a measure. 

        **Scope and Usage** 

        The _evaluate_ operation of the Measure resource is defined to return a MeasureReport. The resource is capable of representing 
        three different levels of report: patient-level, patient-list, and summary. 
        The resource is based on the HL7 CDA R2 Implementation Guide: Quality Reporting Document Architecture - Category 1 (QRDA I) DSTU Release 3 (US Realm) 
        and the HL7 Implementation Guide for CDA Release 2: Quality Reporting Document Architecture - Category III (QRDA III), DSTU Release 1 implementation guides. 

        Note that this resource is a special case of the more general notion of a query evaluation result. 
        However, because the general case requires the ability to represent arbitrary content, this resource uses a simple indicator structure to describe population 
        sizes for each population type defined in the measure. The intent is to be able to represent the more general case as well, either by generalizing this resource, 
        or by making this structure a profile of a more general resource, and we are actively seeking comments about what approaches might be taken to achieve that aim.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/measurereport.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_list', 'hc_bundle', 'hc_measure'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_measure_report_views.xml',
        'views/hc_res_measure_report_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}