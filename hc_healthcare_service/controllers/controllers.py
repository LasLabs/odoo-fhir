# -*- coding: utf-8 -*-
from openerp import http

# class HcHealthcareService(http.Controller):
#     @http.route('/hc_healthcare_service/hc_healthcare_service/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_healthcare_service/hc_healthcare_service/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_healthcare_service.listing', {
#             'root': '/hc_healthcare_service/hc_healthcare_service',
#             'objects': http.request.env['hc_healthcare_service.hc_healthcare_service'].search([]),
#         })

#     @http.route('/hc_healthcare_service/hc_healthcare_service/objects/<model("hc_healthcare_service.hc_healthcare_service"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_healthcare_service.object', {
#             'object': obj
#         })