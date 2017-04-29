# -*- coding: utf-8 -*-
{
    'name': "Claim Response",

    'summary': """
        Response for claims, re-adjudication and reversals
        """,

    'description': """
        This resource provides the adjudication details from the processing of a Claim resource.

        **Scope and Usage** 
        
        The ClaimResponse resource provides application level error or application level adjudication results which are the result of processing a submitted Claim resource where that Claim may 
        be which is the functional corollary of a Claim, Pre-Determination or a Pre-Authorization.

        This is the adjudicated response to a Claim, Pre-determination or Pre-Authorization. The strength of the payment aspect of the response is matching to the strength of the original request.

        * For a Claim, the adjudication indicates payment which is intended to be made.
        * For Pre-Authorization and Pre-Determination, no payment will actually be made. However funds may be reserved to settle a claim submitted later.
        
        Only an actual claim may be expected to result in actual payment.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/claimresponse.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_claim'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_claim_response_views.xml',
        'views/hc_res_claim_response_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}