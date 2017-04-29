# -*- coding: utf-8 -*-
from openerp import http

# class HcLinkage(http.Controller):
#     @http.route('/hc_linkage/hc_linkage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_linkage/hc_linkage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_linkage.listing', {
#             'root': '/hc_linkage/hc_linkage',
#             'objects': http.request.env['hc_linkage.hc_linkage'].search([]),
#         })

#     @http.route('/hc_linkage/hc_linkage/objects/<model("hc_linkage.hc_linkage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_linkage.object', {
#             'object': obj
#         })