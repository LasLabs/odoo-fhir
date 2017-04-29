# -*- coding: utf-8 -*-
from openerp import http

# class HcOperationOutcome(http.Controller):
#     @http.route('/hc_operation_outcome/hc_operation_outcome/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_operation_outcome/hc_operation_outcome/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_operation_outcome.listing', {
#             'root': '/hc_operation_outcome/hc_operation_outcome',
#             'objects': http.request.env['hc_operation_outcome.hc_operation_outcome'].search([]),
#         })

#     @http.route('/hc_operation_outcome/hc_operation_outcome/objects/<model("hc_operation_outcome.hc_operation_outcome"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_operation_outcome.object', {
#             'object': obj
#         })