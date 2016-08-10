# -*- coding: utf-8 -*-
from openerp import http

# class HcVisionPrescription(http.Controller):
#     @http.route('/hc_vision_prescription/hc_vision_prescription/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_vision_prescription/hc_vision_prescription/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_vision_prescription.listing', {
#             'root': '/hc_vision_prescription/hc_vision_prescription',
#             'objects': http.request.env['hc_vision_prescription.hc_vision_prescription'].search([]),
#         })

#     @http.route('/hc_vision_prescription/hc_vision_prescription/objects/<model("hc_vision_prescription.hc_vision_prescription"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_vision_prescription.object', {
#             'object': obj
#         })