# -*- coding: utf-8 -*-
from openerp import http

# class HcParameter(http.Controller):
#     @http.route('/hc_parameter/hc_parameter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_parameter/hc_parameter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_parameter.listing', {
#             'root': '/hc_parameter/hc_parameter',
#             'objects': http.request.env['hc_parameter.hc_parameter'].search([]),
#         })

#     @http.route('/hc_parameter/hc_parameter/objects/<model("hc_parameter.hc_parameter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_parameter.object', {
#             'object': obj
#         })