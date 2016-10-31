# -*- coding: utf-8 -*-
{
    'name': "Slot",

    'summary': """
        Time slot
        """,

    'description': """
        A slot of time on a schedule that may be available for booking appointments.

        **Scope and Usage** 
        
        Slot resources are used to provide time-slots that can be booked using an appointment. They do not provide any information about appointments that are available, 
        just the time, and optionally what the time can be used for. These are effectively spaces of free/busy time.
        
        Slots can also be marked as busy without having appointments associated.

        A slot can have more than one appointment allocated to it. A scheduling system may permit multiple allocations up to a specific number of places. 
        An example of this type of usage could be where the slot is being used for a group service that permits 5 participants at the same time.
    """,

    'author': "Luigi Sison",
    'website': "http://build.fhir.org/slot.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_schedule'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_slot_views.xml',
        'views/hc_res_slot_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}