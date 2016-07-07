# -*- coding: utf-8 -*-
{
    'name': "Value Set",

    'summary': """
        A value set specifies a set of codes drawn from one or more code systems.
        """,

    'description': """
        The FHIR terminology specification is based two key concepts, originally defined in HL7 v3 Core Principles :

        * code system - defines a set of codes with meanings (also known as enumeration, terminology, classification, and/or ontology)
        * value set - selects a set of codes from those defined by one or more code systems

        Code systems define which codes (symbols and/or expressions) exist, and how they are understood. 
        Value sets select a set of codes from one or more code systems to specify which codes can be used in a particular context.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/valueset.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hc_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}