# -*- coding: utf-8 -*-
from openerp import http

# class HcMeasureReport(http.Controller):
#     @http.route('/hc_measure_report/hc_measure_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_measure_report/hc_measure_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_measure_report.listing', {
#             'root': '/hc_measure_report/hc_measure_report',
#             'objects': http.request.env['hc_measure_report.hc_measure_report'].search([]),
#         })

#     @http.route('/hc_measure_report/hc_measure_report/objects/<model("hc_measure_report.hc_measure_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_measure_report.object', {
#             'object': obj
#         })