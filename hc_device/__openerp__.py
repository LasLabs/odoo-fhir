# -*- coding: utf-8 -*-
{
    'name': "Device",

    'summary': """
        Medical and non-medical devices, reusable or disposable
        """,

    'description': """
        This resource identifies an instance or a type of a manufactured item that is used in the provision of healthcare 
        without being substantially changed through that activity. The device may be a medical or non-medical device. 
        Medical devices includes durable (reusable) medical equipment, implantable devices, as well as disposable equipment 
        used for diagnostic, treatment, and research for healthcare and public health. Non-medical devices may include items 
        such as a machine, cellphone, computer, application, etc.

        **Scope and Usage**
         
        This resource an administrative resource that tracks individual device types or instances of a device and their location. 
        It is referenced by other resource for recording which device performed an action such as a procedure or an observation. 
        It is also referenced when prescribing and dispensing devices for patient use or for ordering supplies. It is used to record 
        and transmit Unique Device Identifer (UDI) information about a device such as a patient's implant.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/device.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_patient'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_device_views.xml',
        'views/hc_res_device_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}