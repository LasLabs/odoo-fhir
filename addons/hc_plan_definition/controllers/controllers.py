# -*- coding: utf-8 -*-
from openerp import http

# class HcPlanDefinition(http.Controller):
#     @http.route('/hc_plan_definition/hc_plan_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_plan_definition/hc_plan_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_plan_definition.listing', {
#             'root': '/hc_plan_definition/hc_plan_definition',
#             'objects': http.request.env['hc_plan_definition.hc_plan_definition'].search([]),
#         })

#     @http.route('/hc_plan_definition/hc_plan_definition/objects/<model("hc_plan_definition.hc_plan_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_plan_definition.object', {
#             'object': obj
#         })