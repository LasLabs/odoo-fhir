# -*- coding: utf-8 -*-
from openerp import http

# class HcTask(http.Controller):
#     @http.route('/hc_task/hc_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_task/hc_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_task.listing', {
#             'root': '/hc_task/hc_task',
#             'objects': http.request.env['hc_task.hc_task'].search([]),
#         })

#     @http.route('/hc_task/hc_task/objects/<model("hc_task.hc_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_task.object', {
#             'object': obj
#         })