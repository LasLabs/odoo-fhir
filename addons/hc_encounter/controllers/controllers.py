# -*- coding: utf-8 -*-
from openerp import http

# class HcEncounter(http.Controller):
#     @http.route('/hc_encounter/hc_encounter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_encounter/hc_encounter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_encounter.listing', {
#             'root': '/hc_encounter/hc_encounter',
#             'objects': http.request.env['hc_encounter.hc_encounter'].search([]),
#         })

#     @http.route('/hc_encounter/hc_encounter/objects/<model("hc_encounter.hc_encounter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_encounter.object', {
#             'object': obj
#         })