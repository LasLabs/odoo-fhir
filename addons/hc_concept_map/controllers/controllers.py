# -*- coding: utf-8 -*-
from openerp import http

# class HcConceptMap(http.Controller):
#     @http.route('/hc_concept_map/hc_concept_map/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_concept_map/hc_concept_map/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_concept_map.listing', {
#             'root': '/hc_concept_map/hc_concept_map',
#             'objects': http.request.env['hc_concept_map.hc_concept_map'].search([]),
#         })

#     @http.route('/hc_concept_map/hc_concept_map/objects/<model("hc_concept_map.hc_concept_map"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_concept_map.object', {
#             'object': obj
#         })