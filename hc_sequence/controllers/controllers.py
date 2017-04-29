# -*- coding: utf-8 -*-
from openerp import http

# class HcSequence(http.Controller):
#     @http.route('/hc_sequence/hc_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_sequence/hc_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_sequence.listing', {
#             'root': '/hc_sequence/hc_sequence',
#             'objects': http.request.env['hc_sequence.hc_sequence'].search([]),
#         })

#     @http.route('/hc_sequence/hc_sequence/objects/<model("hc_sequence.hc_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_sequence.object', {
#             'object': obj
#         })