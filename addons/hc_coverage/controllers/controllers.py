# -*- coding: utf-8 -*-
from openerp import http

# class HcCoverage(http.Controller):
#     @http.route('/hc_coverage/hc_coverage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_coverage/hc_coverage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_coverage.listing', {
#             'root': '/hc_coverage/hc_coverage',
#             'objects': http.request.env['hc_coverage.hc_coverage'].search([]),
#         })

#     @http.route('/hc_coverage/hc_coverage/objects/<model("hc_coverage.hc_coverage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_coverage.object', {
#             'object': obj
#         })