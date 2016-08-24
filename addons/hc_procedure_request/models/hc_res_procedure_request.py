# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ProcedureRequest(models.Model):    
    _name = "hc.res.procedure.request"    
    _description = "Procedure Request"            

    identifier_ids = fields.One2many(comodel_name="hc.procedure.request.identifier", inverse_name="procedure_request_id", string="Identifiers", help="Identifier.")                    
    subject_type = fields.Selection(string="Procedure Request Subject Type", help="Type of who the procedure should be done to.")                    
    subject_name = fields.Char(string="Subject", compute="compute_subject_name", required="True", help="Patient|Group.")                    
    subject_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject Patient", required="True", help="Who the procedure should be done to.")                    
    subject_group_id = fields.Many2one(comodel_name="hc.res.group", string="Subject Group", required="True", help="The reference to the group.")                    
    type_id = fields.Many2one(comodel_name="hc.vs.procedure.code", string="Type", required="True", help="What procedure to perform.")                    
    body_site_ids = fields.One2many(comodel_name="hc.procedure.request.body.site", inverse_name="procedure_request_id", string="Body Sites", help="What part of body to perform on.")                    
    subject_type = fields.Selection(string="Procedure Request Subject Type", help="Type of why procedure should occur.")                    
    reason_name = fields.Char(string="Reason", compute="compute_reason_name", help="Why procedure should occur.")                    
    site_id = fields.Many2one(comodel_name="hc.vs.procedure.reason", string="Site", help="CodeableConcept why procedure should occur.")                    
    reason_condition_id = fields.Many2one(comodel_name="hc.res.condition", string="Reason Condition", help="The reference to the condition.")                    
    subject_type = fields.Selection(string="Procedure Request Subject Type", help="Type of when procedure should occur.")                    
    scheduled_name = fields.Char(string="Scheduled", compute="compute_scheduled_name", help="When procedure should occur.")                    
    timing = fields.Datetime(string="Timing Date", help="dateTime when procedure should occur.")                    
    start_date = fields.Datetime(string="Start Date", help="Start of the when procedure should occur.")                    
    end_date = fields.Datetime(string="End Date", help="End of the when procedure should occur.")                    
    scheduled_timing_id = fields.Many2one(comodel_name="hc.procedure.request.scheduled.timing", string="Scheduled Timing", help="Timing when procedure should occur.")                    
    encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Encounter", help="Encounter.")                    
    subject_type = fields.Selection(string="Procedure Request Subject Type", help="Type of who should perform the procedure.")                    
    subject_name = fields.Char(string="Performer", compute="compute_subject_name", help="Practitioner|Organization|Patient|RelatedPerson.")                    
    performer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Performer Practitioner", help="Practitioner who should perform the procedure.")                    
    performer_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Performer Organization", help="The reference to the organization.")                    
    performer_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Performer Patient", help="The reference to the patient.")                    
    performer_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Performer Related Person", help="The reference to the related person.")                    
    status = fields.Selection(string="Procedure Request Status", selection=[("proposed", "Proposed"), ("draft", "Draft"), ("requested", "Requested"), ("received", "Received"), ("accepted", "Accepted"), ("in-progress", "In-Progress"), ("completed", "Completed"), ("suspended", "Suspended"), ("rejected", "Rejected"), ("aborted", "Aborted")], help="The status of the order.")                    
    note_ids = fields.One2many(comodel_name="hc.procedure.request.note", inverse_name="procedure_request_id", string="Note", help="Additional information about desired procedure.")                    
    subject_type = fields.Selection(string="Procedure Request Subject Type", help="Type of preconditions for procedure.")                    
    as_needed_name = fields.Char(string="As Needed", compute="compute_as_needed_name", help="Preconditions for procedure.")                    
    is_as_needed = fields.Boolean(string="As Needed", help="boolean preconditions for procedure.")                    
    as_needed_codeable_concept_id = fields.Many2one(comodel_name="hc.vs.procedure.request.as.needed", string="As Needed Codeable Concept", help="The reference to the codeableconcept.")                    
    ordered_on = fields.Datetime(string="Ordered On Date", help="When Requested.")                    
    subject_type = fields.Selection(string="Procedure Request Subject Type", help="Type of Ordering Party.")                    
    subject_name = fields.Char(string="Orderer", compute="compute_subject_name", help="Practitioner|Patient|RelatedPerson|Device.")                    
    orderer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Orderer Practitioner", help="Practitioner ordering party.")                    
    orderer_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Orderer Patient", help="The reference to the patient.")                    
    orderer_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Orderer Related Person", help="The reference to the related person.")                    
    orderer_device_id = fields.Many2one(comodel_name="hc.res.device", string="Orderer Device", help="The reference to the device.")                    
    priority = fields.Selection(string="Procedure Request Priority", selection=[("routine", "Routine"), ("urgent", "Urgent"), ("stat", "Stat"), ("asap", "Asap")], help="The clinical priority associated with this order.")                    

class ProcedureRequestBodySite(models.Model):    
    _name = "hc.procedure.request.body.site"    
    _description = "Procedure Request Body Site"        
    _inherit = ["hc.basic.association"]    

    procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Procedure Request", help="Procedure request associated with this procedure request body site.")                    
    body_site_id = fields.Many2one(comodel_name="hc.vs.body.site", string="Body Site", help="What part of body to perform on.")                    

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

class ProcedureRequestAsNeeded(models.Model):    
    _name = "hc.vs.procedure.request.as.needed"    
    _description = "Procedure Request As Needed"        
    _inherit = ["hc.value.set.contains"]    
