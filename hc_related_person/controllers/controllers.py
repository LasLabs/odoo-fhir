# -*- coding: utf-8 -*-
from openerp import http

# class HcRelatedPerson(http.Controller):
#     @http.route('/hc_related_person/hc_related_person/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_related_person/hc_related_person/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_related_person.listing', {
#             'root': '/hc_related_person/hc_related_person',
#             'objects': http.request.env['hc_related_person.hc_related_person'].search([]),
#         })

#     @http.route('/hc_related_person/hc_related_person/objects/<model("hc_related_person.hc_related_person"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_related_person.object', {
#             'object': obj
#         })