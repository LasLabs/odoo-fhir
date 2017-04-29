# -*- coding: utf-8 -*-
from openerp import http

# class HcPractitionerRole(http.Controller):
#     @http.route('/hc_practitioner_role/hc_practitioner_role/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_practitioner_role/hc_practitioner_role/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_practitioner_role.listing', {
#             'root': '/hc_practitioner_role/hc_practitioner_role',
#             'objects': http.request.env['hc_practitioner_role.hc_practitioner_role'].search([]),
#         })

#     @http.route('/hc_practitioner_role/hc_practitioner_role/objects/<model("hc_practitioner_role.hc_practitioner_role"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_practitioner_role.object', {
#             'object': obj
#         })