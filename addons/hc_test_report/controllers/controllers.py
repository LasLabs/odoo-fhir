# -*- coding: utf-8 -*-
from openerp import http

# class HcTestReport(http.Controller):
#     @http.route('/hc_test_report/hc_test_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_test_report/hc_test_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_test_report.listing', {
#             'root': '/hc_test_report/hc_test_report',
#             'objects': http.request.env['hc_test_report.hc_test_report'].search([]),
#         })

#     @http.route('/hc_test_report/hc_test_report/objects/<model("hc_test_report.hc_test_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_test_report.object', {
#             'object': obj
#         })