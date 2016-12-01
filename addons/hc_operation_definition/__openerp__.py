# -*- coding: utf-8 -*-
{
    'name': "Operation Definition",

    'summary': """
        Computable definition of an operation, named query
        """,

    'description': """
        A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction). 
        
        **Scope and Usage** 
        
        The OperationDefinition resource provides a formal computable definition of an operation or a named query. 
        The OperationDefinition serves two principal purposes: 
        
        * To allow for automatic determination of system compatibility
        * To allow for dynamic generation of forms to drive the operations
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/operationdefinition.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['hc_value_set'],
    'depends': ['hc_structure_definition'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_operation_definition_views.xml',
        'views/hc_res_operation_definition_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}