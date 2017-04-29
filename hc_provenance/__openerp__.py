# -*- coding: utf-8 -*-
{
    'name': "Provenance",

    'summary': """
        Contextual metadata
        """,

    'description': """
        Provenance of a resource is a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource. 
        Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. Provenance assertions are a form of 
        contextual metadata and can themselves become important records with their own provenance. Provenance statement indicates clinical significance in terms 
        of confidence in authenticity, reliability, and trustworthiness, integrity, and stage in lifecycle (e.g. Document Completion - has the artifact been legally authenticated), all of which may impact security, privacy, and trust policies.

        **Scope and Usage**

        The Provenance resource tracks information about the activity that created a version of a resource, including the entities, and agents involved in producing a resource. 
        This information can be used to form assessments about its quality, reliability or trustworthiness, or to provide pointers for where to go to further investigate 
        the origins of the resource and the information in it.

        Provenance resources are a record-keeping assertion that gathers information about the context in which the information in a resource was obtained. 
        Provenance resources are prepared by the application that initiates the create/update etc. of the resource. An AuditEvent resource contains overlapping information, 
        but is created as events occur, to track and audit the events. AuditEvent resources are often (though not exclusively) created by the application 
        responding to the read/query/create/update, etc., event.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/provenance.html",

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
        'views/hc_res_provenance_views.xml',
        'views/hc_res_provenance_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}