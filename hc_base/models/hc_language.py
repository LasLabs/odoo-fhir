# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Language(models.Model): 
    _name = "hc.vs.language"    
    _description = "Language"
    _inherit = ["hc.value.set.contains"]
    _inherits = {"res.lang": "language_id"}

    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language",
        required=True,
        ondelete="restrict", 
        help="Human Language based on ISO-639.")

class LanguageProficiency(models.Model): 
    _name = "hc.vs.language.proficiency"   
    _description = "Language Proficiency"
    _inherit = ["hc.value.set.contains"]

class LanguageSkill(models.Model): 
    _name = "hc.vs.language.skill"   
    _description = "Language Skill"
    _inherit = ["hc.value.set.contains"]

# External Reference

class lang(models.Model):
    _inherit = ["res.lang"]

    iso3_code = fields.Char(
        string="ISO3 code",
        size=16, 
        help="A 3-character representation of the ISO language code.")
    country_id = fields.Many2one(
        comodel_name="res.country", 
        string="Country", 
        help="Country that the ISO language belongs to.")
    language = fields.Char(
        string="Language",
        help="A human language.")