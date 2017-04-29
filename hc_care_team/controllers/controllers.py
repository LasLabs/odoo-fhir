# -*- coding: utf-8 -*-
from openerp import http

# class HcCareTeam(http.Controller):
#     @http.route('/hc_care_team/hc_care_team/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_care_team/hc_care_team/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_care_team.listing', {
#             'root': '/hc_care_team/hc_care_team',
#             'objects': http.request.env['hc_care_team.hc_care_team'].search([]),
#         })

#     @http.route('/hc_care_team/hc_care_team/objects/<model("hc_care_team.hc_care_team"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_care_team.object', {
#             'object': obj
#         })