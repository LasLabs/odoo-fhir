# -*- coding: utf-8 -*-
{
    'name': "Audit Event",

    'summary': """
        Security logs
        """,

    'description': """
        A record of an event made for purposes of maintaining a security log. Typical uses include detection of intrusion attempts and monitoring for inappropriate usage.

        **Scope and Usage** 
        
        The audit event is based on the IHE-ATNA Audit record definitions, originally from RFC 3881 , and now managed by DICOM (see DICOM Part 15 Annex A5 ).

        * ASTM E2147 – Setup the concept of security audit logs for healthcare including accounting of disclosures
        * IETF RFC 3881 – Defined the Information Model (IETF rule forced this to be informative)
        * DICOM Audit Log Message – Made the information model Normative, defined Vocabulary, Transport Binding, and Schema
        * IHE ATNA – Defines the grouping with secure transport and access controls; and defined specific audit log records for specific IHE transactions.
        * NIST SP800-92 – Shows how to do audit log management and reporting – consistent with our model
        * HL7 PASS – Defined an Audit Service with responsibilities and a query interface for reporting use
        * ISO 27789 – Defined the subset of audit events that an EHR would need
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/auditevent.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_device'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_audit_event_views.xml',
        'views/hc_res_audit_event_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}