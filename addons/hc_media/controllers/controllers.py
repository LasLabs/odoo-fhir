# -*- coding: utf-8 -*-
from openerp import http

# class HcMedia(http.Controller):
#     @http.route('/hc_media/hc_media/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_media/hc_media/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_media.listing', {
#             'root': '/hc_media/hc_media',
#             'objects': http.request.env['hc_media.hc_media'].search([]),
#         })

#     @http.route('/hc_media/hc_media/objects/<model("hc_media.hc_media"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_media.object', {
#             'object': obj
#         })