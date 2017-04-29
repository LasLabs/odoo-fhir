# -*- coding: utf-8 -*-
from openerp import http

# class HcDeviceComponent(http.Controller):
#     @http.route('/hc_device_component/hc_device_component/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_device_component/hc_device_component/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_device_component.listing', {
#             'root': '/hc_device_component/hc_device_component',
#             'objects': http.request.env['hc_device_component.hc_device_component'].search([]),
#         })

#     @http.route('/hc_device_component/hc_device_component/objects/<model("hc_device_component.hc_device_component"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_device_component.object', {
#             'object': obj
#         })