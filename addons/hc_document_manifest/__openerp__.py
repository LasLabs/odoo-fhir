# -*- coding: utf-8 -*-
{
    'name': "Document Manifest",

    'summary': """
        Set of documents
        """,

    'description': """
        A manifest that defines a set of documents.

        **Scope and Usage**

        A document manifest gathers a set of DocumentReference resources into a single package that may be the subject of workflow such as access control, auditing, and targeted delivery.

        Typically, DocumentManifest resources are used in document indexing systems, such as IHE XDS.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/documentmanifest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_group'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hc_res_document_manifest_views.xml',
        'views/hc_res_document_manifest_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}