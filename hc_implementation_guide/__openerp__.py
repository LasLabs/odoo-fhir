# -*- coding: utf-8 -*-
{
    'name': "Implementation Guide",

    'summary': """
        FHIR rules
        """,

    'description': """
        A set of rules or how FHIR is used to solve a particular problem. This resource is used to gather all the parts of an implementation guide 
        into a logical whole, and to publish a computable definition of all the parts. 

        **Scope and Usage**

        An "implementation guide" defines a particular scope of usage for FHIR, and sets a bounded set of expectations for implementations to comply to. 
        
        The significant conformance expectation introduced by the ImplementationGuide resource is the idea of Default Profiles. 
        Implementations may conform to multiple implementation guides at once, but this requires that the implementation guides are compatible.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/implementationguide.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_structure_definition'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_implementation_guide_views.xml',
        'views/hc_res_implementation_guide_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}
