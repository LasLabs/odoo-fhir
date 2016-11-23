# -*- coding: utf-8 -*-
{
    'name': "Plan Definition",

    'summary': """
        Group of actions like order sets, protocols, decision support rules
        """,

    'description': """
        This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. 
        The resource is general enough to support the description of a broad range of clinical artifacts such as clinical decision support rules, order sets and protocols. 

        **Scope and Usage** 

        A plan definition is a pre-defined group of actions to be taken in particular circumstances, often including conditions, options, and other decision points. 

        The resource is flexible enough to be used to represent a variety of clinical decision support and quality improvement assets, including order sets, protocols, and decision support rules.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/plandefinition.html",

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
        'views/hc_res_plan_definition_views.xml',
        'views/hc_res_plan_definition_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}