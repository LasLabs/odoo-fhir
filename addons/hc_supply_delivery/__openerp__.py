# -*- coding: utf-8 -*-
{
    'name': "Supply Delivery",

    'summary': """
        Supply movement
        """,

    'description': """
        Record of delivery of what is supplied.

        **Scope and Usage** 
    
        The scope of the supply resource is for supplies used in the healthcare process. 
        This includes supplies specifically used in the treatment of patients as well as supply movement within an institution 
        (transport a set of supplies from materials management to a service unit (nurse station). 
        This resource does not include the provisioning of transportation services.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/supplydelivery.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_supply_request'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_supply_delivery_views.xml',
        'views/hc_res_supply_delivery_templates.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}