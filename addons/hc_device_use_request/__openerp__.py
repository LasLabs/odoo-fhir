# -*- coding: utf-8 -*-
{
    'name': "Device Use Request",

    'summary': """
        Request to use a medical device
        """,

    'description': """
        Represents a request for a patient to employ a medical device. The device may be an implantable device, 
        or an external assistive device, such as a walker.

        **Scope and Usage**

        This resource describes the request for the use of a device by a patient. 
        The device may be any pertinent device specified in the Device resource. 
        Examples of devices that may be requested include wheelchair, hearing aids, or an insulin pump. 
        The request may lead to the dispensing of the device to the patient or for use by the patient.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/deviceuserequest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_encounter'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_device_use_request_views.xml',
        'views/hc_res_device_use_request_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}