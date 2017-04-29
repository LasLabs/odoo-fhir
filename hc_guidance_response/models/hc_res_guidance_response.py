# -*- coding: utf-8 -*-

from openerp import models, fields, api

class GuidanceResponse(models.Model):    
    _name = "hc.res.guidance.response"    
    _description = "Guidance Response"        

    request_id = fields.Char(
        string="Request Id", 
        help="The id of the request associated with this response, if any.")                
    identifier_id = fields.Many2one(
        comodel_name="hc.guidance.response.identifier", 
        string="Identifier", 
        help="Business identifier.")                
    module_id = fields.Many2one(
        comodel_name="hc.res.service.definition", 
        string="Module", 
        required="True", 
        help="A reference to a knowledge module.")                
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("success", "Success"), 
            ("data-requested", "Data-Requested"), 
            ("data-required", "Data-Required"), 
            ("in-progress", "In-Progress"), 
            ("failure", "Failure")], 
        help="The status of the response.")
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group")], 
        help="Type of patient or group the request was performed for.")                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Patient or group the request was performed for.")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient the request was performed for.")                
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group the request was performed for.")                
    context_type = fields.Selection(
        string="Context Type", 
        selection=[
            ("Encounter", "Encounter"), 
            ("Episode Of Care", "Episode Of Care")], 
        help="Type of Encounter or Episode during which the response was returned.")                
    context_name = fields.Char(
        string="Context", 
        compute="_compute_context_name", 
        store="True", 
        help="Encounter or Episode during which the response was returned.")                
    context_encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Context Encounter", 
        help="Encounter during which the response was returned.")                
    context_episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Context Episode Of Care", 
        help="Episode Of Care during which the response was returned.")                
    occurrence_datetime = fields.Datetime(
        string="Occurrence Datetime", 
        help="When the guidance response was processed.")                
    performer_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Performer", 
        help="Device returning the guidance.")                
    reason_type = fields.Selection(
        string="Reason Type", 
        selection=[
            ("code", "Code"), 
            ("string", "String"), 
            ("Resource Type", "Resource Type")], 
        help="Type of reason for the response.")                
    reason_name = fields.Char(
        string="Reason", 
        compute="_compute_reason_name", 
        store="True", 
        help="Reason for the response.")                
    reason_code_id = fields.Many2one(
        comodel_name="hc.vs.guidance.response.reason", 
        string="Reason Code", 
        help="Code of reason for the response.")                
    reason_string = fields.Char(
        string="Reason String", 
        help="String of reason for the response.")                
    reason_resource_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Reason Resource", 
        help="Resource type of reason for the response.")                
    note_ids = fields.One2many(
        comodel_name="hc.guidance.response.note", 
        inverse_name="guidance_response_id", 
        string="Notes", 
        help="Additional notes about the response." )                
    evaluation_message_ids = fields.One2many(
        comodel_name="hc.guidance.response.evaluation.message", 
        inverse_name="guidance_response_id", 
        string="Evaluation Messages", 
        help="Messages resulting from the evaluation of the artifact or artifacts.")                
    output_parameter_id = fields.Many2one(
        comodel_name="hc.res.parameters", 
        string="Output Parameter", 
        help="The output parameters of the evaluation, if any.")                
    request_group_id = fields.Many2one(
        comodel_name="hc.res.request.group", 
        string="Request Group", 
        help="Proposed actions, if any.")                
    data_requirement_ids = fields.One2many(
        comodel_name="hc.guidance.response.data.requirement", 
        inverse_name="guidance_response_id", 
        string="Data Requirements", 
        help="Additional required data." )                

class GuidanceResponseIdentifier(models.Model):    
    _name = "hc.guidance.response.identifier"    
    _description = "Guidance Response Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class GuidanceResponseNote(models.Model):    
    _name = "hc.guidance.response.note"    
    _description = "Guidance Response Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    guidance_response_id = fields.Many2one(
        comodel_name="hc.res.guidance.response", 
        string="Guidance Response", 
        help="Guidance Response associated with this Guidance Response Note.")                

class GuidanceResponseEvaluationMessage(models.Model):    
    _name = "hc.guidance.response.evaluation.message"    
    _description = "Guidance Response Evaluation Message"        
    _inherit = ["hc.basic.association"]

    guidance_response_id = fields.Many2one(
        comodel_name="hc.res.guidance.response", 
        string="Guidance Response", 
        help="Guidance Response associated with this Guidance Response Evaluation Message.")                
    # evaluation_message_id = fields.Many2one(
    #     comodel_name="hc.res.operation.outcome", 
    #     string="Evaluation Message", 
    #     help="Operation Outcome associated with this Guidance Response Evaluation Message.")                

class GuidanceResponseDataRequirement(models.Model):    
    _name = "hc.guidance.response.data.requirement"    
    _description = "Guidance Response Data Requirement"        
    _inherit = ["hc.basic.association", "hc.data.requirement"]

    guidance_response_id = fields.Many2one(
        comodel_name="hc.res.guidance.response", 
        string="Guidance Response", 
        help="Guidance Response associated with this Guidance Response Data Requirement.")                

class GuidanceResponseReason(models.Model):    
    _name = "hc.vs.guidance.response.reason"    
    _description = "Guidance Response Reason"        
    _inherit = ["hc.value.set.contains"]
