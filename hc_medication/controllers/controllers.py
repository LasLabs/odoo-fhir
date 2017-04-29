# -*- coding: utf-8 -*-
from openerp import http

# class HcMedication(http.Controller):
#     @http.route('/hc_medication/hc_medication/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_medication/hc_medication/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_medication.listing', {
#             'root': '/hc_medication/hc_medication',
#             'objects': http.request.env['hc_medication.hc_medication'].search([]),
#         })

#     @http.route('/hc_medication/hc_medication/objects/<model("hc_medication.hc_medication"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_medication.object', {
#             'object': obj
#         })