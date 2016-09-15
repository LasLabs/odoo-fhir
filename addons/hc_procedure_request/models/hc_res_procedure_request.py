# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ProcedureRequest(models.Model):    
    _name = "hc.res.procedure.request"    
    _description = "Procedure Request"            

    identifier_ids = fields.One2many(
        comodel_name="hc.procedure.request.identifier", 
        inverse_name="procedure_request_id", 
        string="Identifiers", 
        help="Identifier.")                    
    subject_type = fields.Selection(
        string="Subject Type", 
        required="True", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group")], 
        help="Type of who the procedure should be done to.")
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Who the procedure should be done to.")  
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        required="True", 
        help="Who the procedure should be done to.")                    
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        required="True", 
        help="The reference to the group.")                    
    type_id = fields.Many2one(
        comodel_name="hc.vs.procedure.code", 
        string="Type", 
        required="True", 
        help="What procedure to perform.")                    
    body_site_ids = fields.One2many(
        comodel_name="hc.procedure.request.body.site", 
        inverse_name="procedure_request_id", 
        string="Body Sites", 
        help="What part of body to perform on.")                    
    reason_type = fields.Selection(
        string="Reason Type", 
        selection=[
            ("Codeable Concept", "Codeable Concept"), 
            ("Condition", "Condition")], 
        help="Type of why procedure should occur.")
    reason_name = fields.Char(
        string="Reason", 
        compute="_compute_reason_name", 
        store="True", 
        help="Why procedure should occur.")
    reason_codeable_concept_id = fields.Many2one(
        comodel_name="hc.vs.procedure.reason", 
        string="Reason Codeable Concept", 
        help="Codeable Concept why procedure should occur.")
    reason_condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Reason Condition", 
        help="The reference to the condition.")                    
    scheduled_type = fields.Selection(
        string="Scheduled Type", 
        selection=[
            ("datetime", "Datetime"), 
            ("period", "Period"), 
            ("timing", "Timing")], 
        help="Type of when procedure should occur.")
    scheduled_name = fields.Char(
        string="Scheduled", 
        compute="_compute_scheduled_name", 
        store="True", 
        help="When procedure should occur.")
    scheduled_datetime = fields.Datetime(
        string="Scheduled Datetime", 
        help="dateTime when procedure should occur.")            
    scheduled_start_date = fields.Datetime(
        string="Scheduled Start Date", 
        help="Start of the when procedure should occur.")
    scheduled_end_date = fields.Datetime(
        string="Scheduled End Date", 
        help="End of the when procedure should occur.")
    scheduled_timing_id = fields.Many2one(
        comodel_name="hc.procedure.request.scheduled.timing", 
        string="Scheduled Timing", 
        help="Timing when procedure should occur.")                    
    encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Encounter", 
        help="Encounter.")                    
    performer_type = fields.Selection(
        string="Performer Type", 
        selection=[
            ("practitioner", "Practitioner"), 
            ("organization", "Organization"), 
            ("patient", "Patient"), 
            ("related person", "Related Person")], 
        help="Type of who should perform the procedure.")
    performer_name = fields.Char(
        string="Performer", 
        compute="_compute_performer_name", 
        store="True", 
        help="Who should perform the procedure.")
    performer_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Performer Practitioner", 
        help="Practitioner who should perform the procedure.")                    
    performer_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Performer Organization", 
        help="The reference to the organization.")                    
    performer_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Performer Patient", 
        help="The reference to the patient.")                    
    performer_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Performer Related Person", 
        help="The reference to the related person.")                    
    status = fields.Selection(
        string="Procedure Request Status", 
        selection=[
            ("proposed", "Proposed"), 
            ("draft", "Draft"), 
            ("requested", "Requested"), 
            ("received", "Received"), 
            ("accepted", "Accepted"), 
            ("in-progress", "In-Progress"), 
            ("completed", "Completed"), 
            ("suspended", "Suspended"), 
            ("rejected", "Rejected"), 
            ("aborted", "Aborted")], 
        help="The status of the order.")                    
    note_ids = fields.One2many(
        comodel_name="hc.procedure.request.note", 
        inverse_name="procedure_request_id", 
        string="Note", 
        help="Additional information about desired procedure.")                    
    as_needed_type = fields.Selection(
        string="As Needed Type", 
        selection=[
            ("boolean", "Boolean"), 
            ("Codeable Concept", "Codeable Concept")], 
        help="Type of preconditions for procedure.")
    as_needed_name = fields.Char(
        string="As Needed", 
        compute="_compute_as_needed_name", 
        store="True", 
        help="Preconditions for procedure.")  
    is_as_needed = fields.Boolean(
        string="As Needed", 
        help="boolean preconditions for procedure.")                    
    as_needed_codeable_concept_id = fields.Many2one(
        comodel_name="hc.vs.procedure.request.as.needed", 
        string="As Needed Codeable Concept", 
        help="The reference to the codeable concept.")                    
    ordered_on = fields.Datetime(
        string="Ordered On Date", 
        help="When Requested.")                    
    orderer_type = fields.Selection(
        string="Orderer Type", 
        selection=[
            ("practitioner", "Practitioner"), 
            ("patient", "Patient"), 
            ("related person", "Related Person"), 
            ("device", "Device")], 
        help="Type of Ordering Party.")
    orderer_name = fields.Char(
        string="Orderer", 
        compute="_compute_orderer_name", 
        store="True", 
        help="Ordering Party.")
    orderer_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Orderer Practitioner", 
        help="Practitioner ordering party.")                    
    orderer_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Orderer Patient", 
        help="The reference to the patient.")                    
    orderer_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Orderer Related Person", 
        help="The reference to the related person.")                    
    orderer_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Orderer Device", 
        help="The reference to the device.")                    
    priority = fields.Selection(
        string="Procedure Request Priority", 
        selection=[
            ("routine", "Routine"), 
            ("urgent", "Urgent"), 
            ("stat", "Stat"), 
            ("asap", "Asap")], 
        help="The clinical priority associated with this order.")                    

    @api.multi          
    def _compute_subject_name(self):            
        for hc_res_procedure in self:       
            if hc_res_procedure.subject_type == 'Patient':  
                hc_res_procedure.subject_name = hc_res_procedure.subject_patient_id.name
            elif hc_res_procedure.subject_type == 'Group':  
                hc_res_procedure.subject_name = hc_res_procedure.subject_group_id.name

    @api.multi          
    def _compute_reason_name(self):         
        for hc_res_procedure in self:       
            if hc_res_procedure.reason_type == 'Codeable Concept':  
                hc_res_procedure.reason_name = hc_res_procedure.reason_codeable_concept_id.name
            elif hc_res_procedure.reason_type == 'Condition':   
                hc_res_procedure.reason_name = hc_res_procedure.reason_condition_id.name

    @api.multi          
    def _compute_scheduled_name(self):          
        for hc_procedure_used_request in self:      
            if hc_procedure_used_request.scheduled_type == 'datetime':  
                hc_procedure_used_request.scheduled_name = hc_procedure_used_request.scheduled_datetime_id.name
            elif hc_procedure_used_request.scheduled_type == 'period':  
                hc_procedure_used_request.scheduled_name = hc_procedure_used_request.scheduled_period_id.name
            elif hc_procedure_used_request.scheduled_type == 'timing':  
                hc_procedure_used_request.scheduled_name = hc_procedure_used_request.scheduled_timing_id.name

    @api.multi          
    def _compute_performer_name(self):          
        for hc_res_procedure in self:       
            if hc_res_procedure.performer_type == 'practitioner':   
                hc_res_procedure.performer_name = hc_res_procedure.performer_practitioner_id.name
            elif hc_res_procedure.performer_type == 'organization': 
                hc_res_procedure.performer_name = hc_res_procedure.performer_organization_id.name
            elif hc_res_procedure.performer_type == 'patient':  
                hc_res_procedure.performer_name = hc_res_procedure.performer_patient_id.name
            elif hc_res_procedure.performer_type == 'related person':   
                hc_res_procedure.performer_name = hc_res_procedure.performer_related_person_id.name

    @api.multi          
    def _compute_as_needed_name(self):          
        for hc_res_procedure in self:       
            if hc_res_procedure.as_needed_type == 'boolean':    
                hc_res_procedure.as_needed_name = hc_res_procedure.as_needed_boolean_id.name
            elif hc_res_procedure.as_needed_type == 'Codeable Concept': 
                hc_res_procedure.as_needed_name = hc_res_procedure.as_needed_codeable_concept_id.name

    @api.multi          
    def _compute_orderer_name(self):            
        for hc_res_procedure in self:       
            if hc_res_procedure.orderer_type == 'practitioner': 
                hc_res_procedure.orderer_name = hc_res_procedure.orderer_practitioner_id.name
            elif hc_res_procedure.orderer_type == 'patient':    
                hc_res_procedure.orderer_name = hc_res_procedure.orderer_patient_id.name
            elif hc_res_procedure.orderer_type == 'related person': 
                hc_res_procedure.orderer_name = hc_res_procedure.orderer_related_person_id.name
            elif hc_res_procedure.orderer_type == 'device': 
                hc_res_procedure.orderer_name = hc_res_procedure.orderer_device_id.name

class ProcedureRequestBodySite(models.Model):    
    _name = "hc.procedure.request.body.site"    
    _description = "Procedure Request Body Site"        
    _inherit = ["hc.basic.association"]    

    procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Procedure Request", 
        help="Procedure request associated with this procedure request body site.")                    
    body_site_id = fields.Many2one(
        comodel_name="hc.vs.body.site", 
        string="Body Site", 
        help="What part of body to perform on.")                    

class ProcedureRequestIdentifier(models.Model):    
    _name = "hc.procedure.request.identifier"    
    _description = "Procedure Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Procedure Request", 
        help="Procedure request associated with this procedure request identifier.")                    

class ProcedureRequestNote(models.Model):    
    _name = "hc.procedure.request.note"    
    _description = "Procedure Request Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    

    procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Procedure Request", 
        help="Procedure request associated with this procedure request note.")                    

class ProcedureRequestScheduledTiming(models.Model):    
    _name = "hc.procedure.request.scheduled.timing"    
    _description = "Procedure Request Scheduled Timing"        
    _inherit = ["hc.basic.association", "hc.timing"]    

class ProcedureCode(models.Model):  
    _name = "hc.vs.procedure.code"  
    _description = "Procedure Code"     
    _inherit = ["hc.value.set.contains"]

class ProcedureReasonCode(models.Model):    
    _name = "hc.vs.procedure.reason"   
    _description = "Procedure Reason"      
    _inherit = ["hc.value.set.contains"] 

class ProcedureRequestAsNeeded(models.Model):    
    _name = "hc.vs.procedure.request.as.needed"    
    _description = "Procedure Request As Needed"        
    _inherit = ["hc.value.set.contains"]    
    