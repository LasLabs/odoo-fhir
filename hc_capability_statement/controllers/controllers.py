# -*- coding: utf-8 -*-
from openerp import http

# class HcCapabilityStatement(http.Controller):
#     @http.route('/hc_capability_statement/hc_capability_statement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_capability_statement/hc_capability_statement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_capability_statement.listing', {
#             'root': '/hc_capability_statement/hc_capability_statement',
#             'objects': http.request.env['hc_capability_statement.hc_capability_statement'].search([]),
#         })

#     @http.route('/hc_capability_statement/hc_capability_statement/objects/<model("hc_capability_statement.hc_capability_statement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_capability_statement.object', {
#             'object': obj
#         })