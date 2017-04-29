# -*- coding: utf-8 -*-
from openerp import http

# class HcAdverseEvent(http.Controller):
#     @http.route('/hc_adverse_event/hc_adverse_event/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_adverse_event/hc_adverse_event/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_adverse_event.listing', {
#             'root': '/hc_adverse_event/hc_adverse_event',
#             'objects': http.request.env['hc_adverse_event.hc_adverse_event'].search([]),
#         })

#     @http.route('/hc_adverse_event/hc_adverse_event/objects/<model("hc_adverse_event.hc_adverse_event"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_adverse_event.object', {
#             'object': obj
#         })