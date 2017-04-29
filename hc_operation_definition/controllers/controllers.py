# -*- coding: utf-8 -*-
from openerp import http

# class HcOperationDefinition(http.Controller):
#     @http.route('/hc_operation_definition/hc_operation_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_operation_definition/hc_operation_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_operation_definition.listing', {
#             'root': '/hc_operation_definition/hc_operation_definition',
#             'objects': http.request.env['hc_operation_definition.hc_operation_definition'].search([]),
#         })

#     @http.route('/hc_operation_definition/hc_operation_definition/objects/<model("hc_operation_definition.hc_operation_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_operation_definition.object', {
#             'object': obj
#         })