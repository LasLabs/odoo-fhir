# -*- coding: utf-8 -*-
from openerp import http

# class HcRequestGroup(http.Controller):
#     @http.route('/hc_request_group/hc_request_group/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_request_group/hc_request_group/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_request_group.listing', {
#             'root': '/hc_request_group/hc_request_group',
#             'objects': http.request.env['hc_request_group.hc_request_group'].search([]),
#         })

#     @http.route('/hc_request_group/hc_request_group/objects/<model("hc_request_group.hc_request_group"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_request_group.object', {
#             'object': obj
#         })