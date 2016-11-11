# -*- coding: utf-8 -*-
{
    'name': "Activity Definition",

    'summary': """
        Activity to be performed
        """,

    'description': """
        This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.

        **Scope and Usage** 
        
        An activity definition is a shareable, consumable description of some activity to be performed. It may be used to specify actions to be taken as part of an order set or protocol, 
        or it may be used independently as part of a catalog of activities such as orderables.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/activitydefinition.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_location', 'hc_medication'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_activity_definition_views.xml',
        'views/hc_res_activity_definition_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}