# -*- coding: utf-8 -*-
from openerp import http

# class HcSearchParameter(http.Controller):
#     @http.route('/hc_search_parameter/hc_search_parameter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_search_parameter/hc_search_parameter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_search_parameter.listing', {
#             'root': '/hc_search_parameter/hc_search_parameter',
#             'objects': http.request.env['hc_search_parameter.hc_search_parameter'].search([]),
#         })

#     @http.route('/hc_search_parameter/hc_search_parameter/objects/<model("hc_search_parameter.hc_search_parameter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_search_parameter.object', {
#             'object': obj
#         })