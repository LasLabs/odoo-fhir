# -*- coding: utf-8 -*-
from openerp import http

# class HcMeasure(http.Controller):
#     @http.route('/hc_measure/hc_measure/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_measure/hc_measure/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_measure.listing', {
#             'root': '/hc_measure/hc_measure',
#             'objects': http.request.env['hc_measure.hc_measure'].search([]),
#         })

#     @http.route('/hc_measure/hc_measure/objects/<model("hc_measure.hc_measure"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_measure.object', {
#             'object': obj
#         })