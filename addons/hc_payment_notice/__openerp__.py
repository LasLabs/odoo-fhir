# -*- coding: utf-8 -*-
{
    'name': "Payment Notice",

    'summary': """
        Payment reminders, payment status
        """,

    'description': """
        This resource provides the status of the payment for goods and services rendered, and the request and response resource references.

        **Scope and Usage** 
        
        The PaymentNotice resource indicates the resource for which the payment has been indicated and reports the current status information of that payment. 
        The payment notice may be used by Providers and Payors to advise the Provider or Regulatory bodies of the state of a payment 
        (cheque in the mail/EFT sent, payment cashed, payment cancelled). Employers or Insurance Exchanges may use this to advise Payors of premium payment.

        Payors and /or Providers may have the need to advise Providers and/or regulators of the status of Claim settlement and payment completion. 
        This same resource may be used by employers and insurance exchanges to advise Payors that premium payments have been issued and settled.
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/paymentnotice.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hc_practitioner'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hc_res_payment_notice_views.xml',
        'views/hc_res_payment_notice_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': 'True',
    'auto-install': 'True',
}