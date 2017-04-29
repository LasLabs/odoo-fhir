# -*- coding: utf-8 -*-
{
    'name': "Consent",

    'summary': """
        Healthcare consumer's policy choices like Privacy Consent, Advance Care Directive
        """,

    'description': """
        A record of a healthcare consumer’s policy choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.

        **Scope and Usage**

        The purpose of this Resource is to be used to express a Consent regarding Healthcare. There are 3 possible uses for consent:

        * Privacy Consent: consent to share information
        * Treatment Consent: consent to undergo a specific treatment (or record of refusal to consent)
        * Research Consent: privacy and medical consent to participate in clinical trial, translational medicine, or to permit collection, use, or disclosure of health information and specimen to registries or directly to research projects for use in e.g., biomedical research and population origins or ancestry research
        * Advance Care Directives (e.g. DNR)
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/consent.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_care_team', 'hc_contract'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_consent_views.xml',
        'views/hc_res_consent_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}