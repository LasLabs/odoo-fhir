# -*- coding: utf-8 -*-
from openerp import http

# class HcServiceDefinition(http.Controller):
#     @http.route('/hc_service_definition/hc_service_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_service_definition/hc_service_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_service_definition.listing', {
#             'root': '/hc_service_definition/hc_service_definition',
#             'objects': http.request.env['hc_service_definition.hc_service_definition'].search([]),
#         })

#     @http.route('/hc_service_definition/hc_service_definition/objects/<model("hc_service_definition.hc_service_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_service_definition.object', {
#             'object': obj
#         })