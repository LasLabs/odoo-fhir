# -*- coding: utf-8 -*-
from openerp import http

# class HcBundle(http.Controller):
#     @http.route('/hc_bundle/hc_bundle/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_bundle/hc_bundle/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_bundle.listing', {
#             'root': '/hc_bundle/hc_bundle',
#             'objects': http.request.env['hc_bundle.hc_bundle'].search([]),
#         })

#     @http.route('/hc_bundle/hc_bundle/objects/<model("hc_bundle.hc_bundle"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_bundle.object', {
#             'object': obj
#         })