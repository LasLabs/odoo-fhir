# -*- coding: utf-8 -*-
from openerp import http

# class HcList(http.Controller):
#     @http.route('/hc_list/hc_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_list/hc_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_list.listing', {
#             'root': '/hc_list/hc_list',
#             'objects': http.request.env['hc_list.hc_list'].search([]),
#         })

#     @http.route('/hc_list/hc_list/objects/<model("hc_list.hc_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_list.object', {
#             'object': obj
#         })