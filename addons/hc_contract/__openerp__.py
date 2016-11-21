# -*- coding: utf-8 -*-
{
    'name': "Contract",

    'summary': """
        Formal agreements like insurance policies, supply contracts, consent directives
        """,

    'description': """
        A formal agreement between parties regarding the conduct of business, exchange of information or other matters.

        **Scope and Usage**

        The Contract resource is the basal resource to convey information of all manner of contracts for financial (e.g. Insurance policies), 
        business arrangements (eg. supply contracts) and privacy and security (e.g. consent directives).
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/contract.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_document_reference', 'hc_questionnaire_response', 'hc_composition'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_contract_views.xml',
        'views/hc_res_contract_templates.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}