# -*- coding: utf-8 -*-
{
    'name': "Payment Reconciliation",

    'summary': """
        Payment details, claim references
        """,

    'description': """
        This resource provides payment details and claim references supporting a bulk payment.

        **Scope and Usage** 
        The PaymentReconciliation resource provides the bulk payment details associated with a payment by the payor for goods and services 
        rendered by a provider to patients covered by insurance plans offered by that payor. These are the payment reconciliation details which 
        align to the individual payment amounts indicated on discrete ClaimResponses.

        Bulk payments need to provide a means to associate the amounts paid again specific Claims, and other financial exchanges and adjustments, 
        to the bulk payment itself in order to reconcile provider accounts receivable.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/paymentreconciliation.html",

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
        'views/hc_res_payment_reconciliation_views.xml',
        'views/hc_res_payment_reconciliation_templates.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}