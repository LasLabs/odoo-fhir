# -*- coding: utf-8 -*-
{
    'name': "Schedule",

    'summary': """
        Container for appointment slots
        """,

    'description': """
        A container for slot(s) of time that may be available for booking appointments.

        **Scope and Usage**

        Schedule resources provide a container for time-slots that can be booked using an appointment. 
        It provides the window of time (period) that slots are defined for and what type of appointments can be booked.
        
        The schedule does not provide any information about actual appointments. 
        This separation also greatly assists where access to the appointments would not be permitted for security or privacy reasons, 
        and still being able to determine if an appointment might be available.
    """,

    'author': "Luigi Sison",
    'website': "http://build.fhir.org/schedule.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_device'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_schedule_views.xml',
        'views/hc_res_schedule_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}