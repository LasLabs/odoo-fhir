# -*- coding: utf-8 -*-
{
    'name': "Communication",

    'summary': """
        Information exchange between people, organizations, and devices
        """,

    'description': """
        An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency was notified about a reportable condition.

        **Scope and Usage**

        This resource is a record of a communication. A communication is a conveyance of information from one entity, a sender, to another entity, a receiver. 
        The sender and receivers may be patients, practitioners, related persons, organizations, or devices. Communication use cases include:

        * A reminder or alert delivered to a responsible provider
        * A recorded notification from the nurse that a patient's temperature exceeds a value
        * A notification to a public health agency of a patient presenting with a communicable disease reportable to the public health agency
        * Patient educational material sent by a provider to a patient
        
        Non-patient specific communication use cases may include:

        * A nurse call from a hall bathroom
        * Advisory for battery service from a pump
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/communication.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_device', 'hc_encounter'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_communication_views.xml',
        'views/hc_res_communication_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}