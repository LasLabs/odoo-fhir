# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Media(models.Model):    
    _name = "hc.res.media"    
    _description = "Media"        

    identifier_ids = fields.One2many(
        comodel_name="hc.media.identifier", 
        inverse_name="media_id", 
        string="Identifiers", 
        help="Identifier(s) for the image.")                
    type = fields.Selection(string="Media Type", 
        required="True", 
        selection=[
            ("photo", "Photo"), 
            ("video", "Video"), 
            ("audio", "Audio")], 
        help="Whether the media is a photo (still image), an audio recording, or a video recording.")                
    subtype_id = fields.Many2one(
        comodel_name="hc.vs.digital.media.subtype", 
        string="Subtype", 
        help="The type of acquisition equipment/process.")
    view_id = fields.Many2one(
        comodel_name="hc.vs.media.view", 
        string="View", 
        help="Imaging view e.g Lateral or Antero-posterior.")                
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Practitioner", "Practitioner"), 
            ("Group", "Group"), 
            ("Device", "Device"), 
            ("Specimen", "Specimen")], 
        help="Type of patient observations supporting recommendation.")                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Who/What this Media is a record of.")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient this media is a record of.")                
    subject_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Subject Practitioner", 
        help="Practitioner this media is a record of.")                
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group this media is a record of.")                
    subject_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Subject Device", 
        help="Device this media is a record of.")                
    subject_specimen_id = fields.Many2one(
        comodel_name="hc.res.specimen", 
        string="Subject Specimen", 
        help="Specimen this media is a record of.")                
    operator_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Operator", 
        help="The person who generated the image.")                
    device_name = fields.Char(
        string="Device Name", 
        help="Name of the device/manufacturer.")                
    height = fields.Integer(
        string="Height", 
        help="Height of the image in pixels(photo/video).")                
    width = fields.Integer(
        string="Width", 
        help="Width of the image in pixels (photo/video).")                
    frames = fields.Integer(
        string="Frames", 
        help="Number of frames if > 1 (photo).")                
    duration = fields.Integer(
        string="Duration", 
        help="Length in seconds (audio / video).")                
    duration_uom_id = fields.Many2one(
        comodel_name="hc.vs.time.uom", 
        string="Duration UOM",
        default="s",
        help="Duration unit of measure." )                
    content_attachment_id = fields.Many2one(
        comodel_name="hc.media.content.attachment", 
        string="Content Attachment", 
        required="True", 
        help="Actual Media - reference or data.")                

    @api.multi          
    def _compute_subject_name(self):            
        for hc_res_media in self:       
            if hc_res_media.subject_type == 'Patient':  
                hc_res_media.subject_name = hc_res_media.subject_patient_id.name
            elif hc_res_media.subject_type == 'Practitioner':   
                hc_res_media.subject_name = hc_res_media.subject_practitioner_id.name
            elif hc_res_media.subject_type == 'Group':  
                hc_res_media.subject_name = hc_res_media.subject_group_id.name
            elif hc_res_media.subject_type == 'Device': 
                hc_res_media.subject_name = hc_res_media.subject_device_id.name
            elif hc_res_media.subject_type == 'Specimen':   
                hc_res_media.subject_name = hc_res_media.subject_specimen_id.name

class MediaIdentifier(models.Model):    
    _name = "hc.media.identifier"   
    _description = "Media Identifier"       
    _inherit = ["hc.basic.association", "hc.identifier"]

    media_id = fields.Many2one(
        comodel_name="hc.res.media", 
        string="Media", 
        help="Media associated with this media content identifier.")                

class MediaContentAttachment(models.Model):    
    _name = "hc.media.content.attachment"   
    _description = "Media Content Attachment"       
    _inherit = ["hc.basic.association", "hc.attachment"]

class DigitalMediaSubtype(models.Model):    
    _name = "hc.vs.digital.media.subtype"    
    _description = "Digital Media Subtype"        
    _inherit = ["hc.value.set.contains"]

class MediaView(models.Model):    
    _name = "hc.vs.media.view"    
    _description = "Media View"        
    _inherit = ["hc.value.set.contains"]
