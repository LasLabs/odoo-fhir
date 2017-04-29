# -*- coding: utf-8 -*-
from openerp import http

# class HcDeviceMetric(http.Controller):
#     @http.route('/hc_device_metric/hc_device_metric/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_device_metric/hc_device_metric/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_device_metric.listing', {
#             'root': '/hc_device_metric/hc_device_metric',
#             'objects': http.request.env['hc_device_metric.hc_device_metric'].search([]),
#         })

#     @http.route('/hc_device_metric/hc_device_metric/objects/<model("hc_device_metric.hc_device_metric"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_device_metric.object', {
#             'object': obj
#         })