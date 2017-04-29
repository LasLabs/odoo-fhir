# -*- coding: utf-8 -*-
from openerp import http

# class HcPaymentReconciliation(http.Controller):
#     @http.route('/hc_payment_reconciliation/hc_payment_reconciliation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_payment_reconciliation/hc_payment_reconciliation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_payment_reconciliation.listing', {
#             'root': '/hc_payment_reconciliation/hc_payment_reconciliation',
#             'objects': http.request.env['hc_payment_reconciliation.hc_payment_reconciliation'].search([]),
#         })

#     @http.route('/hc_payment_reconciliation/hc_payment_reconciliation/objects/<model("hc_payment_reconciliation.hc_payment_reconciliation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_payment_reconciliation.object', {
#             'object': obj
#         })