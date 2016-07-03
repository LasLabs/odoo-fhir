# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Language(models.Model): 
    _name = "hc.vs.language"    
    _description = "Language"
    # _inherit = ["hc.value.set.contains"]
    _inherits = {"res.lang": "language_id"}

    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language",
        required=True,
        ondelete="restrict", 
        help="Human Language based on ISO-639.")


class lang(models.Model):

    direction = fields.Selection(
        selection=[
            ("ltr", "Left-to-Right"), 
            ("rtl", "Right-to-Left"),
            ("ttd", "Top-to-Down")], 
        string ='Direction', 
        required=True)

class LanguageProficiency(models.Model): 
    _name = "hc.vs.language.proficiency"   
    _description = "Language Proficiency"
    _inherit = ["hc.value.set.contains"]

class LanguageSkill(models.Model): 
    _name = "hc.vs.language.skill"   
    _description = "Language Skill"
    _inherit = ["hc.value.set.contains"]

