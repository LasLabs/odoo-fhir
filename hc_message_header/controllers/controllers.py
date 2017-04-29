# -*- coding: utf-8 -*-
from openerp import http

# class HcMessageHeader(http.Controller):
#     @http.route('/hc_message_header/hc_message_header/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_message_header/hc_message_header/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_message_header.listing', {
#             'root': '/hc_message_header/hc_message_header',
#             'objects': http.request.env['hc_message_header.hc_message_header'].search([]),
#         })

#     @http.route('/hc_message_header/hc_message_header/objects/<model("hc_message_header.hc_message_header"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_message_header.object', {
#             'object': obj
#         })