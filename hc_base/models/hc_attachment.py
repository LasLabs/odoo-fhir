# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AttachmentType(models.Model): 
    _name = "hc.vs.attachment.type"    
    _description = "Attachment Type"
    _inherit = ["hc.value.set.contains"]

class MimeType(models.Model): 
    _name = "hc.vs.mime.type"    
    _description = "MIME Type"
    _inherit = ["hc.value.set.contains"]

class Attachment(models.Model): 
    _name = "hc.attachment" 
    _description = "Attachment"
    _inherit = ["ir.attachment"]

    attachment_type_id = fields.Many2one(
        comodel_name="hc.vs.attachment.type", 
        string="Attachment Type", 
        help="Type of attachment (e.g. ADT Form)")
    mimetype = fields.Many2one(
        comodel_name="hc.vs.mime.type", 
        string="MIME Type", 
        help="Mime type of the content, with charset etc.")
    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language", 
        help="Human language of the content (BCP-47).")
    datas = fields.Binary(
        string="Data", 
        help="Data inline, base64ed.")
    hash_attachment = fields.Binary(
        string="Hash", 
        help="Hash of the data (sha-1, base64ed ).")
    creation_date = fields.Datetime(
        string="Creation Date", 
        help="Date attachment was first created.")

# Constraints

# If the Attachment has datas, it SHALL have a mimetype