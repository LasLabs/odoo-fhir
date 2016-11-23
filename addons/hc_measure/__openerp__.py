# -*- coding: utf-8 -*-
{
    'name': "Measure",

    'summary': """
        Quality measurement definition
        """,

    'description': """
        The Measure resource provides the definition of a quality measure. 
        
        **Scope and Usage** 
        
        The Measure resource represents a structured computable definition of a clinical quality measure. 
        A quality measure is a quantitative tool to assess the performance of an individual or organization with respect to a specified process or outcome 
        via the measurement of actions, processes, or outcomes of clinical care. Quality measures are often derived from clinical quidelines 
        and are designed to determine whether the appropriate care has been provided given a set of clinical criteria and an evidence base.
        
        Note that the Measure itself does not contain any logic; rather a Library resource is referenced that contains the logic required by the measure, 
        and the various expression elements, such as poulation criteria, reference named expressions within that library (or libraries). 
        In addition, if the Measure references multiple libraries, then any expression references within the resource must be qualified with the 
        name of the library that contains the referenced expression.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/measure.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_measure_views.xml',
        'views/hc_res_measure_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}