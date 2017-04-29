# -*- coding: utf-8 -*-
from openerp import http

# class HcGuidanceResponse(http.Controller):
#     @http.route('/hc_guidance_response/hc_guidance_response/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_guidance_response/hc_guidance_response/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_guidance_response.listing', {
#             'root': '/hc_guidance_response/hc_guidance_response',
#             'objects': http.request.env['hc_guidance_response.hc_guidance_response'].search([]),
#         })

#     @http.route('/hc_guidance_response/hc_guidance_response/objects/<model("hc_guidance_response.hc_guidance_response"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_guidance_response.object', {
#             'object': obj
#         })