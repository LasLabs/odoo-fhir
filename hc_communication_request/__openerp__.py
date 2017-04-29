# -*- coding: utf-8 -*-
{
    'name': "Communication Request",

    'summary': """
        Request by a person, organization or device to convey information
        """,

    'description': """
        A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes 
        that the public health agency be notified about a reportable condition.

        **Scope and Usage** 

        This resource is a record of a request for a communication to be performed. A communication is a conveyance of information from one entity, a sender, 
        to another entity, a receiver. The sender and receivers may be patients, practitioners, related persons, organizations, and devices. 
        Uses of communication request include:

        * A computer-based decision-support system requesting a reminder or alert be delivered to a responsible provider
        * A physician requesting notification from the nurse if a patient's temperature exceeds a value
        * A monitoring system or a provider requesting a staff member or department to notify a public health agency of a patient presenting with a communicable disease reportable to the public health agency
        * A computer-based decision-support system proposes to send educational material to a patient
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/communicationrequest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_care_team', 'hc_encounter'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_communication_request_views.xml',
        'views/hc_res_communication_request_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}