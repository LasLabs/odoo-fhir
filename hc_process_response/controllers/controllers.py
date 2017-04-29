# -*- coding: utf-8 -*-
from openerp import http

# class HcProcessResponse(http.Controller):
#     @http.route('/hc_process_response/hc_process_response/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_process_response/hc_process_response/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_process_response.listing', {
#             'root': '/hc_process_response/hc_process_response',
#             'objects': http.request.env['hc_process_response.hc_process_response'].search([]),
#         })

#     @http.route('/hc_process_response/hc_process_response/objects/<model("hc_process_response.hc_process_response"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_process_response.object', {
#             'object': obj
#         })