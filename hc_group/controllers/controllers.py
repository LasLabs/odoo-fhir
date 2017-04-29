# -*- coding: utf-8 -*-
from openerp import http

# class HcGroup(http.Controller):
#     @http.route('/hc_group/hc_group/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_group/hc_group/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_group.listing', {
#             'root': '/hc_group/hc_group',
#             'objects': http.request.env['hc_group.hc_group'].search([]),
#         })

#     @http.route('/hc_group/hc_group/objects/<model("hc_group.hc_group"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_group.object', {
#             'object': obj
#         })