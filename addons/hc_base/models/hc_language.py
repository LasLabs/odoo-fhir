# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Language(models.Model): 
    _name = "hc.language"    
    _description = "Language"
    _inherits = {"res.lang": "language_id"}

    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language",
        help="Language associated with this patient.")

class LanguageProficiency(models.Model): 
    _name = "hc.vs.language.proficiency"   
    _description = "Language Proficiency of the Language"
    _inherit = ["hc.value.set.contains"]

class LanguageSkill(models.Model): 
    _name = "hc.vs.language.skill"   
    _description = "Language Skill of the Language"
    _inherit = ["hc.value.set.contains"]