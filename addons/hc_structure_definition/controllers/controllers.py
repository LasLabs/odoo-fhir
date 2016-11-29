# -*- coding: utf-8 -*-
from openerp import http

# class HcStructureDefinition(http.Controller):
#     @http.route('/hc_structure_definition/hc_structure_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_structure_definition/hc_structure_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_structure_definition.listing', {
#             'root': '/hc_structure_definition/hc_structure_definition',
#             'objects': http.request.env['hc_structure_definition.hc_structure_definition'].search([]),
#         })

#     @http.route('/hc_structure_definition/hc_structure_definition/objects/<model("hc_structure_definition.hc_structure_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_structure_definition.object', {
#             'object': obj
#         })