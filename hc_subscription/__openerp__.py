# -*- coding: utf-8 -*-
{
    'name': "Subscription",

    'summary': """
        Push-based subscription""",

    'description': """
        
        The subscription resource is used to define a push based subscription from a server to another system. Once a subscription is registered with the server, 
        the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" 
        so that another system is able to take an appropriate action.

        **Scope and Usage** 
        
        The subscription resource is used to define a push based subscription from a server to another system. Once a subscription is registered with the server, 
        the server checks every resource that is created or updated, and if the resource matches the given criteria, it sends a message on the defined "channel" 
        so that another system is able to take an appropriate action. The server is able to send notifications without any information about the matching resource, 
        or with the entire resource.

        Several different types of channels are supported:

        * rest-hook: A post is made to the URL. If the subscription requests that the whole resource is included, the URL is interpreted as the service base
        * websocket: An PING message is sent to the designated URI
        * email/sms: A notification is send to nominated email address or SMS number
        * message: The resource is sent to the application identified in the URI as a message
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/subscription.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_subscription_views.xml',
        'views/hc_res_subscription_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}