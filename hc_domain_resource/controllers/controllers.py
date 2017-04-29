# -*- coding: utf-8 -*-
from openerp import http

# class HcDomainResource(http.Controller):
#     @http.route('/hc_domain_resource/hc_domain_resource/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_domain_resource/hc_domain_resource/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_domain_resource.listing', {
#             'root': '/hc_domain_resource/hc_domain_resource',
#             'objects': http.request.env['hc_domain_resource.hc_domain_resource'].search([]),
#         })

#     @http.route('/hc_domain_resource/hc_domain_resource/objects/<model("hc_domain_resource.hc_domain_resource"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_domain_resource.object', {
#             'object': obj
#         })