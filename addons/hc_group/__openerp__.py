# -*- coding: utf-8 -*-
{
    'name': "Group",

    'summary': """
        Non-organization group of people, animals, devices, etc.
        """,

    'description': """
        Represents a defined collection of entities that may be discussed or acted upon collectively 
        but which are not expected to act collectively and are not formally or legally recognized; 
        i.e. a collection of entities that isn't an Organization.

        **Scope and Usage**

        The group resource is used in one of two ways:

        * To define a group of specific people, animals, devices, etc. that is being tracked, examined or otherwise referenced as part of healthcare-related activities
        * To define a set of *possible* people, animals, devices, etc. that are of interest for some intended future healthcare-related activities
        
        Examples of the former could include group therapy or treatment sessions, exposed entities tracked as part of public health, etc. 
        The latter might be used to define expected subjects for a clinical study.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/group.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_organization'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_group_views.xml',
        'views/hc_res_group_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}