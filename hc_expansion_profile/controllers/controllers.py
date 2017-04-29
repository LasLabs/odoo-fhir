# -*- coding: utf-8 -*-
from openerp import http

# class HcExpansionProfile(http.Controller):
#     @http.route('/hc_expansion_profile/hc_expansion_profile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_expansion_profile/hc_expansion_profile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_expansion_profile.listing', {
#             'root': '/hc_expansion_profile/hc_expansion_profile',
#             'objects': http.request.env['hc_expansion_profile.hc_expansion_profile'].search([]),
#         })

#     @http.route('/hc_expansion_profile/hc_expansion_profile/objects/<model("hc_expansion_profile.hc_expansion_profile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_expansion_profile.object', {
#             'object': obj
#         })