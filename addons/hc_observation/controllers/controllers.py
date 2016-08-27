# -*- coding: utf-8 -*-
from openerp import http

# class HcObservation(http.Controller):
#     @http.route('/hc_observation/hc_observation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_observation/hc_observation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_observation.listing', {
#             'root': '/hc_observation/hc_observation',
#             'objects': http.request.env['hc_observation.hc_observation'].search([]),
#         })

#     @http.route('/hc_observation/hc_observation/objects/<model("hc_observation.hc_observation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_observation.object', {
#             'object': obj
#         })