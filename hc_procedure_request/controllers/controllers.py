# -*- coding: utf-8 -*-
from openerp import http

# class HcProcedureRequest(http.Controller):
#     @http.route('/hc_procedure_request/hc_procedure_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_procedure_request/hc_procedure_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_procedure_request.listing', {
#             'root': '/hc_procedure_request/hc_procedure_request',
#             'objects': http.request.env['hc_procedure_request.hc_procedure_request'].search([]),
#         })

#     @http.route('/hc_procedure_request/hc_procedure_request/objects/<model("hc_procedure_request.hc_procedure_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_procedure_request.object', {
#             'object': obj
#         })