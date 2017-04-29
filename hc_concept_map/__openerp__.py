# -*- coding: utf-8 -*-
{
    'name': "Concept Map",

    'summary': """
        Concept relationships
        """,

    'description': """
        A statement of relationships from one set of concepts to one or more other concepts - either code systems or data elements, or classes in class models. 

        **Scope and Usage** 
        
        A concept map defines a mapping from a set of concepts defined in a code system to one or more concepts defined in other code systems. 
        Mappings are one way - from the source to the destination. In many cases, the reverse mappings are valid, but this cannot be assumed to be the case. 
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/conceptmap.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_structure_definition', 'hc_value_set'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_concept_map_views.xml',
        'views/hc_res_concept_map_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}