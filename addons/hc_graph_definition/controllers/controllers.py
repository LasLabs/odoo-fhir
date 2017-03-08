# -*- coding: utf-8 -*-
from openerp import http

# class HcGraphDefinition(http.Controller):
#     @http.route('/hc_graph_definition/hc_graph_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_graph_definition/hc_graph_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_graph_definition.listing', {
#             'root': '/hc_graph_definition/hc_graph_definition',
#             'objects': http.request.env['hc_graph_definition.hc_graph_definition'].search([]),
#         })

#     @http.route('/hc_graph_definition/hc_graph_definition/objects/<model("hc_graph_definition.hc_graph_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_graph_definition.object', {
#             'object': obj
#         })