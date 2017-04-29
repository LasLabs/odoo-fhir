# -*- coding: utf-8 -*-
from openerp import http

# class HcOrganization(http.Controller):
#     @http.route('/hc_organization/hc_organization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_organization/hc_organization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_organization.listing', {
#             'root': '/hc_organization/hc_organization',
#             'objects': http.request.env['hc_organization.hc_organization'].search([]),
#         })

#     @http.route('/hc_organization/hc_organization/objects/<model("hc_organization.hc_organization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_organization.object', {
#             'object': obj
#         })