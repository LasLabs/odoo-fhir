# -*- coding: utf-8 -*-
from openerp import http

# class HcPaymentNotice(http.Controller):
#     @http.route('/hc_payment_notice/hc_payment_notice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_payment_notice/hc_payment_notice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_payment_notice.listing', {
#             'root': '/hc_payment_notice/hc_payment_notice',
#             'objects': http.request.env['hc_payment_notice.hc_payment_notice'].search([]),
#         })

#     @http.route('/hc_payment_notice/hc_payment_notice/objects/<model("hc_payment_notice.hc_payment_notice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_payment_notice.object', {
#             'object': obj
#         })