# -*- coding: utf-8 -*-
from openerp import http

# class HcImagingStudy(http.Controller):
#     @http.route('/hc_imaging_study/hc_imaging_study/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_imaging_study/hc_imaging_study/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_imaging_study.listing', {
#             'root': '/hc_imaging_study/hc_imaging_study',
#             'objects': http.request.env['hc_imaging_study.hc_imaging_study'].search([]),
#         })

#     @http.route('/hc_imaging_study/hc_imaging_study/objects/<model("hc_imaging_study.hc_imaging_study"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_imaging_study.object', {
#             'object': obj
#         })