# -*- coding: utf-8 -*-
from openerp import http

# class HcActivityDefinition(http.Controller):
#     @http.route('/hc_activity_definition/hc_activity_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_activity_definition/hc_activity_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_activity_definition.listing', {
#             'root': '/hc_activity_definition/hc_activity_definition',
#             'objects': http.request.env['hc_activity_definition.hc_activity_definition'].search([]),
#         })

#     @http.route('/hc_activity_definition/hc_activity_definition/objects/<model("hc_activity_definition.hc_activity_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_activity_definition.object', {
#             'object': obj
#         })