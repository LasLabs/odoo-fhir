# -*- coding: utf-8 -*-
{
    'name': "Supply Request",

    'summary': """
        Inventory request for medication, substance, or device
        """,

    'description': """
        A record of a request for a medication, substance or device used in the healthcare setting.

        **Scope and Usage** 
        
        The scope of the SupplyRequest resource is for recording the request of supplies used in the healthcare process. 
        This includes supplies specifically used in the treatment of patients as well as supply movement within an institution 
        (transport a set of supplies from materials management to a service unit (nurse station). This resource does not include 
        the provisioning of transportation services.

        The SupplyRequest resource is used for inventory management. When requesting medication, substances and devices when 
        there is a patient focus or instructions regarding their use, DeviceUseRequest or MedicationRequest should be used instead.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/supplyrequest.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_medication', 'hc_device'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_supply_request_views.xml',
        'views/hc_res_supply_request_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}