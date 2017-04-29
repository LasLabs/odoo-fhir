# -*- coding: utf-8 -*-
{
    'name': "Appointment Response",

    'summary': """
        Appointment confirmation or rejection
        """,

    'description': """
        A reply to an appointment request for a patient and/or practitioner(s), such as a confirmation or rejection.

        **Scope and Usage** 
        
        Appointment resources are used to provide information about a planned meeting that may be in the future or past. 
        They may be for a single meeting or for a series of repeating visits. Examples include a scheduled surgery, a follow-up for a clinical visit, 
        a scheduled conference call between clinicians to discuss a case, the reservation of a piece of diagnostic equipment for a particular use, etc. 
        The visit scheduled by an appointment may be in person or remote (by phone, video conference, etc.) All that matters is that the time and usage of one or more individuals, locations and/or pieces of equipment is being fully or partially reserved for a designated period of time.

        This definition takes the concepts of appointments in a clinical setting and also extends them to be relevant in the community healthcare space, 
        and also ease exposure to other appointment / calendar standards widely used outside of Healthcare.
    """,

    'author': "Luigi Sison",
    'website': "http://build.fhir.org/appointmentresponse.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_appointment'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_appointment_response_views.xml',
        'views/hc_res_appointment_response_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}