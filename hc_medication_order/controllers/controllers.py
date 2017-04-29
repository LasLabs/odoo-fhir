# -*- coding: utf-8 -*-
from openerp import http

# class HcMedicationOrder(http.Controller):
#     @http.route('/hc_medication_order/hc_medication_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_medication_order/hc_medication_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_medication_order.listing', {
#             'root': '/hc_medication_order/hc_medication_order',
#             'objects': http.request.env['hc_medication_order.hc_medication_order'].search([]),
#         })

#     @http.route('/hc_medication_order/hc_medication_order/objects/<model("hc_medication_order.hc_medication_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_medication_order.object', {
#             'object': obj
#         })