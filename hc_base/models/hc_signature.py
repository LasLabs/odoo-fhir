# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Signature(models.AbstractModel):    
    _name = "hc.signature"    
    _description = "Signature"        

                   
    type_ids = fields.Many2many(
        comodel_name="hc.vs.commitment.type.indication", 
        relation="signature_type_rel", 
        string="Types", 
        required="True", 
        help="Indication of the reason the entity signed the object(s).")
    when = fields.Datetime(
        string="When Date", 
        required="True", 
        help="When the signature was created.")                
    who_type = fields.Selection(
        string="Who Type", 
        required="True", 
        selection=[
            ("uri", "URI"), 
            ("Practitioner", "Practitioner"), 
            ("Related Person", "Related Person"), 
            ("Patient", "Patient"), 
            ("Device", "Device"), 
            ("Organization", "Organization")], 
        help="Type of who signed.")                
    who_name = fields.Char(
        string="Who", 
        compute="compute_who_name", 
        help="Who signed.")                
    who_uri = fields.Char(
        string="Who URI", 
        help="URI of who signed.")                
    # who_practitioner_id = fields.Many2one(
    #     comodel_name="hc.res.practitioner", 
    #     string="Who Practitioner", 
    #     help="Practitioner who signed.")                
    # who_related_person_id = fields.Many2one(
    #     comodel_name="hc.res.related.person", 
    #     string="Who Related Person", 
    #     help="Related Person who signed.")                
    # who_patient_id = fields.Many2one(
    #     comodel_name="hc.res.patient", 
    #     string="Who Patient", 
    #     help="Patient who signed.")                
    # who_device_id = fields.Many2one(
    #     comodel_name="hc.res.device", 
    #     string="Who Device", 
    #     help="Device who signed.")                
    # who_organization_id = fields.Many2one(
    #     comodel_name="hc.res.organization", 
    #     string="Who Organization", 
    #     help="Organization who signed.")                
    on_behalf_of_type = fields.Selection(
        string="On Behalf Of Type", 
        selection=[
            ("uri", "URI"), 
            ("practitioner", "Practitioner"), 
            ("related person", "Related Person"), 
            ("patient", "Patient"), 
            ("device", "Device"), 
            ("organization", "Organization")], 
        help="Type of the party represented.")                
    on_behalf_of_name = fields.Char(
        string="On Behalf Of", 
        compute="compute_on_behalf_of_name", 
        help="The party represented.")                
    on_behalf_of_uri = fields.Char(
        string="On Behalf Of URI", 
        help="URI of the party represented.")                
    # on_behalf_of_practitioner_id = fields.Many2one(
    #     comodel_name="hc.res.practitioner", 
    #     string="On Behalf Of Practitioner", 
    #     help="Practitioner the party represented.")                
    # on_behalf_of_related_person_id = fields.Many2one(
    #     comodel_name="hc.res.related.person", 
    #     string="On Behalf Of Related Person", 
    #     help="Related Person the party represented.")                
    # on_behalf_of_patient_id = fields.Many2one(
    #     comodel_name="hc.res.patient", 
    #     string="On Behalf Of Patient", 
    #     help="Patient the party represented.")                
    # on_behalf_of_device_id = fields.Many2one(
    #     comodel_name="hc.res.device", 
    #     string="On Behalf Of Device", 
    #     help="Device the party represented.")                
    # on_behalf_of_organization_id = fields.Many2one(
    #     comodel_name="hc.res.organization", 
    #     string="On Behalf Of Organization", 
    #     help="Organization the party represented.")                
    content_type_id = fields.Many2one(
        comodel_name="hc.vs.mime.type", 
        string="Content Type", 
        help="The technical format of the signature.")                
    blob = fields.Binary(
        string="Blob", 
        help="The actual signature content (XML DigSig. JWT, picture, etc.).")                

class CommitmentTypeIndication(models.Model):    
    _name = "hc.vs.commitment.type.indication"    
    _description = "Commitment Type Indication"        
    _inherit = ["hc.value.set.contains"]
