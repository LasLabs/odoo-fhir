# -*- coding: utf-8 -*-
from openerp import http

# class HcEndpoint(http.Controller):
#     @http.route('/hc_endpoint/hc_endpoint/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_endpoint/hc_endpoint/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_endpoint.listing', {
#             'root': '/hc_endpoint/hc_endpoint',
#             'objects': http.request.env['hc_endpoint.hc_endpoint'].search([]),
#         })

#     @http.route('/hc_endpoint/hc_endpoint/objects/<model("hc_endpoint.hc_endpoint"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_endpoint.object', {
#             'object': obj
#         })