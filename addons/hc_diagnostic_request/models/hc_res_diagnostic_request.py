# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DiagnosticRequest(models.Model):    
    _name = "hc.res.diagnostic.request"    
    _description = "Diagnostic Request"

    identifier_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.identifier", 
        inverse_name="diagnostic_request_id", 
        string="Identifiers", 
        help="Identifiers assigned to this order.")                    
    definition_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.definition", 
        inverse_name="diagnostic_request_id", 
        string="Definitions", 
        help="Protocol or definition.")                    
    based_on_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.based.on", 
        inverse_name="diagnostic_request_id", 
        string="Based On", 
        help="What request fulfills.")                    
    replaces_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.replaces", 
        inverse_name="diagnostic_request_id", 
        string="Replaces", 
        help="What request replaces.")                    
    requisition_identifier_id = fields.Many2one(
        comodel_name="hc.diagnostic.request.requisition.identifier", 
        string="Diagnostic Request Requisition Identifier", 
        help="Identifier of composite request.")                    
    status = fields.Selection(
        string="Diagnostic Request Status", 
        selection=[
            ("requested", "Requested"), 
            ("received", "Received"), 
            ("accepted", "Accepted"), 
            ("in progress", "In Progress"), 
            ("review", "Review"), 
            ("completed", "Completed"), 
            ("suspended", "Suspended"), 
            ("rejected", "Rejected"), 
            ("failed", "Failed")], 
        help="The status of the order.")                    
    stage_id = fields.Many2one(
        comodel_name="hc.vs.diagnostic.request.stage", 
        string="Diagnostic Request Stage", 
        required="True", 
        help="Whether the request is a proposal, plan, an original order or a reflex order.")
    # stage = fields.Selection(string="Diagnostic Request Stage", required="True", selection=[("proposal", "Proposal"), ("plan", "Plan"), ("original-order", "Original-Order"), ("reflex-order", "Reflex-Order")], help="proposal | plan | original-order | reflex-order.")                    
    code_id = fields.Many2one(
        comodel_name="hc.vs.diagnostic.request", 
        string="Code", 
        required="True", 
        help="What's being requested/ordered.")                    
    subject_type = fields.Selection(
        string="Subject Type", 
        required="True", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group"), 
            ("Location", "Location"), 
            ("Device", "Device")],
        help="Type of who and/or what test is about.")                    
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Who and/or what test is about.")                 
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient who and/or what test is about.")
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group who and/or what test is about.")
    subject_location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Subject Location", 
        help="Location who and/or what test is about.")
    subject_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Subject Device", 
        help="Device who and/or what test is about.")                  
    context_type = fields.Selection(
        string="Context Type", 
        selection=[
            ("Encounter", "Encounter"), 
            ("Episode Of Care", "Episode of Care")], 
        help="Encounter or Episode during which request was created.")                    
    context_name = fields.Char(
        string="Context", 
        compute="_compute_context_name", 
        store="True", 
        help="Encounter or Episode during which request was created.")
    context_encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Context Encounter", 
        help="Encounter during which request was created.")                    
    context_episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Context Episode Of Care", 
        help="Episode Of Care during which request was created.")                                       
    occurence_type = fields.Selection(
        string="Occurence Type", 
        selection=[
            ("datetime", "Datetime"), 
            ("period", "Period"), 
            ("timing", "Timing")], 
        help="Type of when testing should occur.")                     
    occurrence_name = fields.Char(
        string="Occurrence", 
        compute="_compute_occurrence_name", 
        store="True", 
        help="When testing should occur.")
    occurrence_datetime = fields.Datetime(
        string="Occurrence Datetime", 
        help="dateTime when testing should occur.")                    
    occurence_start_date = fields.Datetime(
        string="Occurrence Start Date", 
        help="Start of the when testing should occur.")                    
    occurence_end_date = fields.Datetime(
        string="Occurence End Date", 
        help="End of the when testing should occur.")                    
    occurrence_timing_id = fields.Many2one(
        comodel_name="hc.diagnostic.request.occurrence.timing", 
        string="Occurrence Timing", 
        help="Timing when testing should occur.")             
    authored = fields.Datetime(string="Authored Date", 
        help="Request signed.")                            
    requester_type = fields.Selection(
        string="Requester Type", 
        selection=[
            ("Device", "Device"), 
            ("Practitioner", "Practitioner"), 
            ("Organization", "Organization")],
        help="Type of who/what is requesting diagnostics.")                    
    requester_name = fields.Char(
        string="Requester", 
        compute="_compute_requester_name", 
        store="True",
        help="Who/what is requesting diagnostics.")
    requester_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Requester Device", 
        help="Device who/what is requesting diagnostics.")
    requester_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Requester Practitioner", 
        help="Practitioner who/what is requesting diagnostics.")                    
    requester_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Requester Organization", 
        help="Organization who/what is requesting diagnostics.")                     
    performer_type_id = fields.Many2one(
        comodel_name="hc.vs.participant.role", 
        string="Performer Type", 
        help="Performer role.")                    
    requested_performer_type = fields.Selection(
        string="Requested Performer Type", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Organization", "Organization"), 
            ("Patient", "Patient"), 
            ("Device", "Device"), 
            ("Related Person", "Related Person")], 
        help="Type of requested perfomer.")
    requested_performer_name = fields.Char(
        string="Requested Performer", 
        compute="_compute_requested_performer_name", 
        store="True", 
        help="Requested perfomer.")
    requested_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Requested Practitioner", 
        help="Practitioner requested perfomer.")
    requested_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Requested Organization", 
        help="Organization requested perfomer.")
    requested_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Requested Patient", 
        help="Patient requested perfomer.")
    requested_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Requested Device", 
        help="Device requested perfomer.")
    requested_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Requested Related Person", 
        help="Related Person requested perfomer.")
    reason_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.reason", 
        inverse_name="diagnostic_request_id", 
        string="Reasons", 
        help="Explanation/Justification for test.")                    
    supporting_info_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.supporting.info", 
        inverse_name="diagnostic_request_id", 
        string="Supporting Info", 
        help="Additional clinical information.")     
    note_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.note", 
        inverse_name="diagnostic_request_id", 
        string="Notes", 
        help="Comments.")                    
    relevant_history_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.relevant.history", 
        inverse_name="diagnostic_request_id", 
        string="Relevant Histories", 
        help="Request provenance.")

    @api.multi          
    def _compute_subject_name(self):            
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.subject_type == 'Practitioner':    
                hc_res_diagnostic_request.subject_name = hc_res_diagnostic_request.subject_practitioner_id.name
            elif hc_res_diagnostic_request.subject_type == 'Patient':   
                hc_res_diagnostic_request.subject_name = hc_res_diagnostic_request.subject_patient_id.name
            elif hc_res_diagnostic_request.subject_type == 'Related Person':    
                hc_res_diagnostic_request.subject_name = hc_res_diagnostic_request.subject_related_person_id.name
            elif hc_res_diagnostic_request.subject_type == 'Device':    
                hc_res_diagnostic_request.subject_name = hc_res_diagnostic_request.subject_device_id.name

    @api.multi          
    def _compute_context_name(self):            
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.context_type == 'Encounter':   
                hc_res_diagnostic_request.context_name = hc_res_diagnostic_request.context_encounter_id.name
            elif hc_res_diagnostic_request.context_type == 'Episode Of Care':   
                hc_res_diagnostic_request.context_name = hc_res_diagnostic_request.context_episode_of_care_id.name
    
    @api.multi          
    def _compute_occurence_name(self):          
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.occurence_type == 'datetime':  
                hc_res_diagnostic_request.occurence_name = hc_res_diagnostic_request.occurence_datetime_id.name
            elif hc_res_diagnostic_request.occurence_type == 'period':  
                hc_res_diagnostic_request.occurence_name = hc_res_diagnostic_request.occurence_period_id.name
            elif hc_res_diagnostic_request.occurence_type == 'timing':  
                hc_res_diagnostic_request.occurence_name = hc_res_diagnostic_request.occurence_timing_id.name
    
    @api.multi          
    def _compute_requester_name(self):          
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.requester_type == 'Device':    
                hc_res_diagnostic_request.requester_name = hc_res_diagnostic_request.requester_device_id.name
            elif hc_res_diagnostic_request.requester_type == 'Practitioner':    
                hc_res_diagnostic_request.requester_name = hc_res_diagnostic_request.requester_practitioner_id.name
            elif hc_res_diagnostic_request.requester_type == 'Organization':    
                hc_res_diagnostic_request.requester_name = hc_res_diagnostic_request.requester_organization_id.name
 
    @api.multi          
    def _compute_requested_performer_name(self):            
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.requested_performer_type == 'Practitioner':    
                hc_res_diagnostic_request.requested_performer_name = hc_res_diagnostic_request.requested_performer_practitioner_id.name
            elif hc_res_diagnostic_request.requested_performer_type == 'Organization':  
                hc_res_diagnostic_request.requested_performer_name = hc_res_diagnostic_request.requested_performer_organization_id.name
            elif hc_res_diagnostic_request.requested_performer_type == 'Patient':   
                hc_res_diagnostic_request.requested_performer_name = hc_res_diagnostic_request.requested_performer_patient_id.name
            elif hc_res_diagnostic_request.requested_performer_type == 'Device':    
                hc_res_diagnostic_request.requested_performer_name = hc_res_diagnostic_request.requested_performer_device_id.name
            elif hc_res_diagnostic_request.requested_performer_type == 'Related Person': 
                hc_res_diagnostic_request.requested_performer_name = hc_res_diagnostic_request.requested_performer_related_person_id.name

class DiagnosticRequestIdentifier(models.Model):    
    _name = "hc.diagnostic.request.identifier"    
    _description = "Diagnostic Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request identifier.")                    

class DiagnosticRequestRequisitionIdentifier(models.Model): 
    _name = "hc.diagnostic.request.requisition.identifier"  
    _description = "Diagnostic Request Requisition Identifier"      
    _inherit = ["hc.basic.association", "hc.identifier"]

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request requisition identifier." )              

class DiagnosticRequestBasedOn(models.Model):    
    _name = "hc.diagnostic.request.based.on"    
    _description = "Diagnostic Request Based On"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request based on.")                    
    based_on_type = fields.Selection(
        string="Based On Type", 
        selection=[
            ("string", "String"), 
            ("Diagnostic Request", "Diagnostic Request")], 
        help="Type of what request fulfills.")                  
    based_on_name = fields.Char(
        string="Based On", 
        compute="_compute_based_on_name", 
        store="True", 
        help="What request fulfills.")                  
    based_on_string = fields.Char(
        string="Based On String", 
        help="String what request fulfills.")                    
    based_on_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Based On Diagnostic Request", 
        help="Diagnostic Request what request fulfills.")                    

    @api.multi          
    def _compute_based_on_name(self):           
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.based_on_type == 'string': 
                hc_res_diagnostic_request.based_on_name = hc_res_diagnostic_request.based_on_string_id.name
            elif hc_res_diagnostic_request.based_on_type == 'Diagnostic Request':   
                hc_res_diagnostic_request.based_on_name = hc_res_diagnostic_request.based_on_diagnostic_request_id.name

class DiagnosticRequestDefinition(models.Model):    
    _name = "hc.diagnostic.request.definition"    
    _description = "Diagnostic Request Definition"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request definition.")                    
    definition_type = fields.Selection(
        string="Definition Type", 
        selection=[
            ("string", "String"), 
            ("Diagnostic Request", "Diagnostic Request")], 
        help="Type of protocol or definition.")                    
    definition_name = fields.Char(
        string="Definition", 
        compute="_compute_definition_name", 
        store="True", 
        help="Protocol or definition.")               
    definition_string = fields.Char(
        string="Definition String", 
        help="String protocol or definition.")                    
    definition_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Definition Diagnostic Request", 
        help="Diagnostic Request protocol or definition.")     

    @api.multi          
    def _compute_definition_name(self):         
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.definition_type == 'string':   
                hc_res_diagnostic_request.definition_name = hc_res_diagnostic_request.definition_string_id.name
            elif hc_res_diagnostic_request.definition_type == 'Diagnostic Request': 
                hc_res_diagnostic_request.definition_name = hc_res_diagnostic_request.definition_diagnostic_request_id.name

class DiagnosticRequestNote(models.Model):    
    _name = "hc.diagnostic.request.note"    
    _description = "Diagnostic Request Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request note.")                    

class DiagnosticRequestRelevantHistory(models.Model):    
    _name = "hc.diagnostic.request.relevant.history"   
    _description = "Diagnostic Request Relevant History"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request relevant history.")                    
    # relevant_history_id = fields.Many2one(
    #     comodel_name="hc.res.provenance", 
    #     string="Relevant History", 
    #     help="Provenance associated with this diagnostic request relevant history.")                    

class DiagnosticRequestReplaces(models.Model):    
    _name = "hc.diagnostic.request.replaces"    
    _description = "Diagnostic Request Replaces"        
    _inherit = ["hc.basic.association"]

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request replaces.")                    
    replaces_type = fields.Selection(
        string="Replaces Type", 
        selection=[
            ("string", "String"), 
            ("Diagnostic Request", "Diagnostic Request")], 
        help="Type of what request replaces.")                    
    replaces_name = fields.Char(
        string="Replaces", 
        compute="_compute_replaces_name", 
        store="True", 
        help="What request replaces.")
    replaces_string = fields.Char(
        string="Replaces String", 
        help="String what request replaces.")
    replaces_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Replaces Diagnostic Request", 
        help="Diagnostic Request what request replaces.")
                   
    @api.multi          
    def _compute_replaces_name(self):           
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.replaces_type == 'string': 
                hc_res_diagnostic_request.replaces_name = hc_res_diagnostic_request.replaces_string_id.name
            elif hc_res_diagnostic_request.replaces_type == 'Diagnostic Request':   
                hc_res_diagnostic_request.replaces_name = hc_res_diagnostic_request.replaces_diagnostic_request_id.name

class DiagnosticRequestSupportingInfo(models.Model):    
    _name = "hc.diagnostic.request.supporting.info"    
    _description = "Diagnostic Request Supporting Information"        
    _inherit = ["hc.basic.association"]    

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request supporting information.")                    
    supporting_info_type = fields.Selection(
        string="Supporting Info Type", 
        selection=[
            ("string", "String"), 
            ("Diagnostic Request", "Diagnostic Request")], 
        help="Type of additional clinical information.")                    
    supporting_info_name = fields.Char(
        string="Supporting Info", 
        compute="_compute_supporting_info_name", 
        store="True", 
        help="Additional clinical information.")
    supporting_info_string = fields.Char(
        string="Supporting Info String", 
        help="String additional clinical information.")
    supporting_info_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Supporting Info Diagnostic Request", 
        help="Diagnostic Request additional clinical information.")

    @api.multi          
    def _compute_supporting_info_name(self):            
        for hc_res_diagnostic_request in self:      
            if hc_res_diagnostic_request.supporting_info_type == 'string':  
                hc_res_diagnostic_request.supporting_info_name = hc_res_diagnostic_request.supporting_info_string_id.name
            elif hc_res_diagnostic_request.supporting_info_type == 'Diagnostic Request':    
                hc_res_diagnostic_request.supporting_info_name = hc_res_diagnostic_request.supporting_info_diagnostic_request_id.name
            
class DiagnosticRequestReason(models.Model): 
    _name = "hc.diagnostic.request.reason"  
    _description = "Diagnostic Request Reason"      
    _inherit = ["hc.basic.association"]

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this diagnostic request reason.")                    
    reason_id = fields.Many2one(
        comodel_name="hc.vs.condition.code", 
        string="Reason", 
        help="Explanation/Justification for test.")                    

class DiagnosticRequestOccurrenceTiming(models.Model):  
    _name = "hc.diagnostic.request.occurrence.timing"    
    _description = "Diagnostic Request Occurrence Timing"       
    _inherit = ["hc.basic.association", "hc.timing"]

class DiagnosticRequest(models.Model):    
    _name = "hc.vs.diagnostic.request"    
    _description = "Diagnostic Request"        
    _inherit = ["hc.value.set.contains"]      
  
class DiagnosticRequestStage(models.Model): 
    _name = "hc.vs.diagnostic.request.stage"    
    _description = "Diagnostic Request Stage"       
    _inherit = ["hc.value.set.contains"]

