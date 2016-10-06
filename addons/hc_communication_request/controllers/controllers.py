# -*- coding: utf-8 -*-
from openerp import http

# class HcCommunicationRequest(http.Controller):
#     @http.route('/hc_communication_request/hc_communication_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_communication_request/hc_communication_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_communication_request.listing', {
#             'root': '/hc_communication_request/hc_communication_request',
#             'objects': http.request.env['hc_communication_request.hc_communication_request'].search([]),
#         })

#     @http.route('/hc_communication_request/hc_communication_request/objects/<model("hc_communication_request.hc_communication_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_communication_request.object', {
#             'object': obj
#         })