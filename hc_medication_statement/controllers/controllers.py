# -*- coding: utf-8 -*-
from openerp import http

# class HcMedicationStatement(http.Controller):
#     @http.route('/hc_medication_statement/hc_medication_statement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_medication_statement/hc_medication_statement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_medication_statement.listing', {
#             'root': '/hc_medication_statement/hc_medication_statement',
#             'objects': http.request.env['hc_medication_statement.hc_medication_statement'].search([]),
#         })

#     @http.route('/hc_medication_statement/hc_medication_statement/objects/<model("hc_medication_statement.hc_medication_statement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_medication_statement.object', {
#             'object': obj
#         })