# -*- coding: utf-8 -*-
{
    'name': "Binary",

    'summary': """
        Any binary resource like text, image, CDA Document, PDF Document
        """,

    'description': """
        
        A binary resource can contain any content, whether text, image, pdf, zip archive, etc.

        **Scope and Usage**
         
        There are situations where it is useful or required to handle pure binary content using the same framework as other resources. 
        Typically, this is when the binary content is referred to from other FHIR Resources. Using the same framework means that the existing servers, 
        security arrangements, code libraries etc. can handle additional related content. Typically, Binary resources are used for handling content such as:

        * CDA  Documents (i.e. with XDS)
        * PDF Documents
        * Images (the Media resource is preferred for handling images, but not possible when the content is already binary - XDS)
        
        A binary resource can contain any content, whether text, image, pdf, zip archive, etc. These resources are served in their native form on the rest interface, 
        but can also be represented in XML or JSON, such as when including these resources in a bundle (used when it is convenient to include these in the feed directly 
        rather than leaving them by reference).
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/binary.html",

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
        'views/hc_res_binary_views.xml',
        'views/hc_res_binary_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}