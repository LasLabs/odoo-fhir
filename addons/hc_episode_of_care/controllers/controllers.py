# -*- coding: utf-8 -*-
from openerp import http

# class HcEpisodeOfCare(http.Controller):
#     @http.route('/hc_episode_of_care/hc_episode_of_care/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_episode_of_care/hc_episode_of_care/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_episode_of_care.listing', {
#             'root': '/hc_episode_of_care/hc_episode_of_care',
#             'objects': http.request.env['hc_episode_of_care.hc_episode_of_care'].search([]),
#         })

#     @http.route('/hc_episode_of_care/hc_episode_of_care/objects/<model("hc_episode_of_care.hc_episode_of_care"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_episode_of_care.object', {
#             'object': obj
#         })