# -*- coding: utf-8 -*-
from openerp import http

# class HcLocation(http.Controller):
#     @http.route('/hc_location/hc_location/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_location/hc_location/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_location.listing', {
#             'root': '/hc_location/hc_location',
#             'objects': http.request.env['hc_location.hc_location'].search([]),
#         })

#     @http.route('/hc_location/hc_location/objects/<model("hc_location.hc_location"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_location.object', {
#             'object': obj
#         })