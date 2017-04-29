# -*- coding: utf-8 -*-
from openerp import http

# class HcFamilyMemberHistory(http.Controller):
#     @http.route('/hc_family_member_history/hc_family_member_history/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_family_member_history/hc_family_member_history/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_family_member_history.listing', {
#             'root': '/hc_family_member_history/hc_family_member_history',
#             'objects': http.request.env['hc_family_member_history.hc_family_member_history'].search([]),
#         })

#     @http.route('/hc_family_member_history/hc_family_member_history/objects/<model("hc_family_member_history.hc_family_member_history"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_family_member_history.object', {
#             'object': obj
#         })