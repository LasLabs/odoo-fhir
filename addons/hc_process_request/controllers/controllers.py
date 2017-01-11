# -*- coding: utf-8 -*-
from openerp import http

# class HcProcessRequest(http.Controller):
#     @http.route('/hc_process_request/hc_process_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_process_request/hc_process_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_process_request.listing', {
#             'root': '/hc_process_request/hc_process_request',
#             'objects': http.request.env['hc_process_request.hc_process_request'].search([]),
#         })

#     @http.route('/hc_process_request/hc_process_request/objects/<model("hc_process_request.hc_process_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_process_request.object', {
#             'object': obj
#         })