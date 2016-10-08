# -*- coding: utf-8 -*-
{
    'name': "Bundle",

    'summary': """
        Collection of resources
        """,

    'description': """
        A container for a collection of resources.

        **Scope and Usage**

        One common operation performed with resources is to gather a collection of resources into a single instance with containing context. 
        In FHIR this is referred to as "bundling" the resources together. These resource bundles are useful for a variety of different reasons, including:

        * Returning a set of resources that meet some criteria as part of a server operation (see RESTful Search)
        * Returning a set of versions of resources as part of the history operation on a server (see History)
        * Sending a set of resources as part of a message exchange (see Messaging)
        * Grouping a self-contained set of resources to act as an exchangeable and persistable collection with clinical integrity - e.g. a clinical document (see Documents)
        * Creating/updating/deleting a set of resources on a server as a single operation (including doing so as a single atomic transaction) (see Transactions)
        * Storing a collection of resources
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/bundle.html",

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
        'views/hc_res_bundle_views.xml',
        'views/hc_res_bundle_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}