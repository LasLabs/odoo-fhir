# -*- coding: utf-8 -*-
{
    'name': "Message Header",

    'summary': """
        Header of a message exchange
        """,

    'description': """
        The header for a message exchange that is either requesting or responding to an action. The reference(s) that are the subject of the action as well 
        as other information related to the action are typically transmitted in a bundle in which the MessageHeader resource instance is the first resource in the bundle.

        **Scope and Usage**

        The MessageHeader resource is defined in order to support Messaging using FHIR resources. The principle usage of the MessageHeader resource is when messages are exchanged. 
        However, as a resource that can be used with the RESTful framework, the MessageHeader resource has the normal resource end-point ([base-url]/MessageHeader), 
        which is used to manage a set of static messages resources. This could be used to make an archive of past messages available. 
        Creating or updating Message resources in this fashion does not represent the actual occurrence of any event, nor can it trigger any logic associated with the actual event. 
        It is just for managing a set of message resources.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/messageheader.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_device', 'hc_operation_outcome'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_message_header_views.xml',
        'views/hc_res_message_header_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}