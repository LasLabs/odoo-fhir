# -*- coding: utf-8 -*-
from openerp import http

# class HcClaim(http.Controller):
#     @http.route('/hc_claim/hc_claim/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_claim/hc_claim/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_claim.listing', {
#             'root': '/hc_claim/hc_claim',
#             'objects': http.request.env['hc_claim.hc_claim'].search([]),
#         })

#     @http.route('/hc_claim/hc_claim/objects/<model("hc_claim.hc_claim"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_claim.object', {
#             'object': obj
#         })