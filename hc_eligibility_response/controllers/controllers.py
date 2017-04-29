# -*- coding: utf-8 -*-
from openerp import http

# class HcEligibilityResponse(http.Controller):
#     @http.route('/hc_eligibility_response/hc_eligibility_response/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_eligibility_response/hc_eligibility_response/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_eligibility_response.listing', {
#             'root': '/hc_eligibility_response/hc_eligibility_response',
#             'objects': http.request.env['hc_eligibility_response.hc_eligibility_response'].search([]),
#         })

#     @http.route('/hc_eligibility_response/hc_eligibility_response/objects/<model("hc_eligibility_response.hc_eligibility_response"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_eligibility_response.object', {
#             'object': obj
#         })