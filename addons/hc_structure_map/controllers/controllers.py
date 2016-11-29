# -*- coding: utf-8 -*-
from openerp import http

# class HcStructureMap(http.Controller):
#     @http.route('/hc_structure_map/hc_structure_map/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_structure_map/hc_structure_map/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_structure_map.listing', {
#             'root': '/hc_structure_map/hc_structure_map',
#             'objects': http.request.env['hc_structure_map.hc_structure_map'].search([]),
#         })

#     @http.route('/hc_structure_map/hc_structure_map/objects/<model("hc_structure_map.hc_structure_map"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_structure_map.object', {
#             'object': obj
#         })