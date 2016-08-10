# -*- coding: utf-8 -*-
from openerp import http

# class HcProtocol(http.Controller):
#     @http.route('/hc_protocol/hc_protocol/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_protocol/hc_protocol/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_protocol.listing', {
#             'root': '/hc_protocol/hc_protocol',
#             'objects': http.request.env['hc_protocol.hc_protocol'].search([]),
#         })

#     @http.route('/hc_protocol/hc_protocol/objects/<model("hc_protocol.hc_protocol"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_protocol.object', {
#             'object': obj
#         })