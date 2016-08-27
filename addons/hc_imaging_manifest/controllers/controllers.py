# -*- coding: utf-8 -*-
from openerp import http

# class HcImagingManifest(http.Controller):
#     @http.route('/hc_imaging_manifest/hc_imaging_manifest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_imaging_manifest/hc_imaging_manifest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_imaging_manifest.listing', {
#             'root': '/hc_imaging_manifest/hc_imaging_manifest',
#             'objects': http.request.env['hc_imaging_manifest.hc_imaging_manifest'].search([]),
#         })

#     @http.route('/hc_imaging_manifest/hc_imaging_manifest/objects/<model("hc_imaging_manifest.hc_imaging_manifest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_imaging_manifest.object', {
#             'object': obj
#         })