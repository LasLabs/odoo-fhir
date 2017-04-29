# -*- coding: utf-8 -*-
from openerp import http

# class HcEligibilityRequest(http.Controller):
#     @http.route('/hc_eligibility_request/hc_eligibility_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_eligibility_request/hc_eligibility_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_eligibility_request.listing', {
#             'root': '/hc_eligibility_request/hc_eligibility_request',
#             'objects': http.request.env['hc_eligibility_request.hc_eligibility_request'].search([]),
#         })

#     @http.route('/hc_eligibility_request/hc_eligibility_request/objects/<model("hc_eligibility_request.hc_eligibility_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_eligibility_request.object', {
#             'object': obj
#         })