# -*- coding: utf-8 -*-
{
    'name': "Device Component",

    'summary': """
        Device characteristics, operational status and capabilities
        """,

    'description': """
        Describes the characteristics, operational status and capabilities of a medical-related component of a medical device.

        **Scope and Usage** 
        
        The DeviceComponent resource is used to describe the characteristics, operational status and capabilities of a medical-related component of a medical device. 
        It can be a physical component that is integrated inside the device, a removable physical component, or a non-physical component that allows 
        physiological measurement data and its derived data to be grouped in a hierarchical information organization.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/devicecomponent.html",

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
        'views/hc_res_device_component_views.xml',
        'views/hc_res_device_component_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}