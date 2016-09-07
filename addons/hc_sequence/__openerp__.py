# -*- coding: utf-8 -*-
{
    'name': "Sequence",

    'summary': """
        Biological sequence
        """,

    'description': """
        Raw data describing a biological sequence.

        **Scope and Usage**

        The Sequence resource is designed to describe an atomic sequence which contains more than one bases but 
        has at most one variation. Atomic sequences can be connected by link element and they will lead to sequence 
        graph. By this method, a sequence can be reported. Complete genetic sequence information, of which specific 
        genetic variations are a part, is reported by reference to the GA4GH repository. Thus, the FHIR Sequence 
        resource avoids large genomic payloads in a manner analogous to how the FHIR ImagingStudy resource references 
        large images maintained in other systems. This resource contextualizes well established standards from the 
        field of clinical genetics into the standards of healthcare (e.g. HGNC - HUGO Gene Nomenclature Committee's 
        international standard for gene names, symbols, and identifiers).
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/sequence.html",

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
        'views/hc_res_sequence_views.xml',
        'views/hc_res_sequence_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}