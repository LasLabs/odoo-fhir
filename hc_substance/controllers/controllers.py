# -*- coding: utf-8 -*-
from openerp import http

# class HcSubstance(http.Controller):
#     @http.route('/hc_substance/hc_substance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_substance/hc_substance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_substance.listing', {
#             'root': '/hc_substance/hc_substance',
#             'objects': http.request.env['hc_substance.hc_substance'].search([]),
#         })

#     @http.route('/hc_substance/hc_substance/objects/<model("hc_substance.hc_substance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_substance.object', {
#             'object': obj
#         })