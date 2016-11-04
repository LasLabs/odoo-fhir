# -*- coding: utf-8 -*-
from openerp import http

# class HcClaimResponse(http.Controller):
#     @http.route('/hc_claim_response/hc_claim_response/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_claim_response/hc_claim_response/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_claim_response.listing', {
#             'root': '/hc_claim_response/hc_claim_response',
#             'objects': http.request.env['hc_claim_response.hc_claim_response'].search([]),
#         })

#     @http.route('/hc_claim_response/hc_claim_response/objects/<model("hc_claim_response.hc_claim_response"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_claim_response.object', {
#             'object': obj
#         })