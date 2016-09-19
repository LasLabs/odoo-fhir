# -*- coding: utf-8 -*-
from openerp import http

# class HcComposition(http.Controller):
#     @http.route('/hc_composition/hc_composition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_composition/hc_composition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_composition.listing', {
#             'root': '/hc_composition/hc_composition',
#             'objects': http.request.env['hc_composition.hc_composition'].search([]),
#         })

#     @http.route('/hc_composition/hc_composition/objects/<model("hc_composition.hc_composition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_composition.object', {
#             'object': obj
#         })