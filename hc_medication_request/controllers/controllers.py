# -*- coding: utf-8 -*-
from openerp import http

# class HcMedicationRequest(http.Controller):
#     @http.route('/hc_medication_request/hc_medication_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_medication_request/hc_medication_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_medication_request.listing', {
#             'root': '/hc_medication_request/hc_medication_request',
#             'objects': http.request.env['hc_medication_request.hc_medication_request'].search([]),
#         })

#     @http.route('/hc_medication_request/hc_medication_request/objects/<model("hc_medication_request.hc_medication_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_medication_request.object', {
#             'object': obj
#         })