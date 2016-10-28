# -*- coding: utf-8 -*-
{
    'name': "Basic",

    'summary': """
        Concepts not yet defined in FHIR
        """,

    'description': """
        Basic is used for handling concepts not yet defined in FHIR, narrative-only resources that don't map to an existing resource, and custom resources 
        not appropriate for inclusion in the FHIR specification.

        **Scope and Usage**

        Basic is a special type of resource. Unlike all other resources, it doesn't correspond to a specific pre-defined HL7 concept. 
        Instead, it's a placeholder for any resource-like concept that isn't already defined in the HL7 specification.

        The Basic resource is intended for use in three circumstances:

        When an implementer needs a resource concept that is likely to be defined by HL7 in the future but they have not yet done so (due to bandwidth issues, lack of sufficient requirements, lower prioritization, etc.)
        When there's a need to convey a narrative-only construct that doesn't neatly correspond to one of the other resources, either because it combines aspects of several resources (e.g. Assessment + Plan) or because the allowed content is flexible such that the system can't be totally sure what sort of content might have been included in the narrative text.
        Other than the circumstances above, this resource will see minimal use. To keep the FHIR specification manageable, it cannot incorporate every site-specific requirement that might be needed in some implementation somewhere. This set of resources likely won't ever be officially defined in HL7.
        There's also a fourth circumstance: An implementer wishes to convey information that could/should be conveyed using a standard resource, however they want to represent the information in a custom format that isn't aligned with the official resource's elements. While this resource would be the preferred way of meeting that use-case because it will at least be wire-format compatible, such a use would not be conformant because making use of the Basic resource would prevent the healthcare-related information from being safely processed, queried and analyzed by other conformant systems.

        Implementers don't need to be concerned with which of the three categories their desired resource fits within. If they need a resource and it clearly doesn't fit one of the ones currently defined, they should use Basic.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/basic.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['hc_any'],
    'depends': ['hc_device'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_basic_views.xml',
        'views/hc_res_basic_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}