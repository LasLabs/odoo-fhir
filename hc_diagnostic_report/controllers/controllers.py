# -*- coding: utf-8 -*-
from openerp import http

# class HcDiagnosticReport(http.Controller):
#     @http.route('/hc_diagnostic_report/hc_diagnostic_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_diagnostic_report/hc_diagnostic_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_diagnostic_report.listing', {
#             'root': '/hc_diagnostic_report/hc_diagnostic_report',
#             'objects': http.request.env['hc_diagnostic_report.hc_diagnostic_report'].search([]),
#         })

#     @http.route('/hc_diagnostic_report/hc_diagnostic_report/objects/<model("hc_diagnostic_report.hc_diagnostic_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_diagnostic_report.object', {
#             'object': obj
#         })