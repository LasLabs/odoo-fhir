# -*- coding: utf-8 -*-
from openerp import http

# class HcSpecimen(http.Controller):
#     @http.route('/hc_specimen/hc_specimen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_specimen/hc_specimen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_specimen.listing', {
#             'root': '/hc_specimen/hc_specimen',
#             'objects': http.request.env['hc_specimen.hc_specimen'].search([]),
#         })

#     @http.route('/hc_specimen/hc_specimen/objects/<model("hc_specimen.hc_specimen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_specimen.object', {
#             'object': obj
#         })