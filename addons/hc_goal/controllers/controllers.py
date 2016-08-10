# -*- coding: utf-8 -*-
from openerp import http

# class HcGoal(http.Controller):
#     @http.route('/hc_goal/hc_goal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_goal/hc_goal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_goal.listing', {
#             'root': '/hc_goal/hc_goal',
#             'objects': http.request.env['hc_goal.hc_goal'].search([]),
#         })

#     @http.route('/hc_goal/hc_goal/objects/<model("hc_goal.hc_goal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_goal.object', {
#             'object': obj
#         })