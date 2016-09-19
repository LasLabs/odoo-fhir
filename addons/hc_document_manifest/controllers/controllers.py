# -*- coding: utf-8 -*-
from openerp import http

# class HcDocumentManifest(http.Controller):
#     @http.route('/hc_document_manifest/hc_document_manifest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_document_manifest/hc_document_manifest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_document_manifest.listing', {
#             'root': '/hc_document_manifest/hc_document_manifest',
#             'objects': http.request.env['hc_document_manifest.hc_document_manifest'].search([]),
#         })

#     @http.route('/hc_document_manifest/hc_document_manifest/objects/<model("hc_document_manifest.hc_document_manifest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_document_manifest.object', {
#             'object': obj
#         })