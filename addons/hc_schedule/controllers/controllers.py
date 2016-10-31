# -*- coding: utf-8 -*-
from openerp import http

# class HcSchedule(http.Controller):
#     @http.route('/hc_schedule/hc_schedule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_schedule/hc_schedule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_schedule.listing', {
#             'root': '/hc_schedule/hc_schedule',
#             'objects': http.request.env['hc_schedule.hc_schedule'].search([]),
#         })

#     @http.route('/hc_schedule/hc_schedule/objects/<model("hc_schedule.hc_schedule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_schedule.object', {
#             'object': obj
#         })