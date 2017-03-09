# -*- coding: utf-8 -*-
{
    'name': "Domain Resource",

    'summary': """
    Extended base resource
        """,

    'description': """
    **Scope and Usage**
    
    A domain resource is a resource that:

    * has a human-readable XHTML representation of the content of the resource
    * can contain additional related resources inside the resource
    * can have additional extensions and modifierExtensions as well as the defined data
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/domain_resource.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_domain_resource_views.xml',
        'views/hc_res_domain_resource_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}