# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Condition(models.Model):    
    _name = "hc.res.condition"    
    _description = "Condition"            

    identifier_ids = fields.One2many(
        comodel_name="hc.condition.identifier", 
        inverse_name="condition_id", 
        string="Identifiers", 
        help="External Ids for this condition.")                    
    clinical_status = fields.Selection(
        string="Condition Clinical Status", 
        selection=[
            ("active", "Active"), 
            ("relapse", "Relapse"), 
            ("remission", "Remission"), 
            ("resolved", "Resolved")], 
        help="The clinical status of the condition.")                    
    verification_status = fields.Selection(
        string="Condition Verification Status", 
        required="True", 
        selection=[
            ("provisional", "Provisional"), 
            ("differential", "Differential"), 
            ("confirmed", "Confirmed"), 
            ("refuted", "Refuted"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("unknown", "Unknown")], 
        help="The verification status to support the clinical status of the condition.")                    
    category = fields.Selection(
        string="Condition Category", 
        selection=[
            ("complaint", "Complaint"), 
            ("symptom", "Symptom"), 
            ("finding", "Finding"), 
            ("diagnosis", "Diagnosis")], 
        help="A category assigned to the condition.")                    
    severity_id = fields.Many2one(
        comodel_name="hc.vs.condition.severity", 
        string="Severity", 
        help="A category assigned to the condition.")                    
    code_id = fields.Many2one(
        comodel_name="hc.vs.condition.code", 
        string="Code", 
        required="True", 
        help="Identification of the condition, problem or diagnosis.")                       
    body_site_ids = fields.One2many(
        comodel_name="hc.condition.body.site", 
        inverse_name="condition_id", 
        string="Body Sites", 
        help="Anatomical location, if relevant.")               
    subject_type = fields.Selection(
        string="Condition Subject Type",
        required="True", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group")], 
        help="Type of who has the condition.")
    subject_name = fields.Char(
        string="Subject", 
        compute="compute_subject_name",  
        help="Who has the condition?")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        required="True", 
        help="Patient who has the condition.")                    
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        required="True", 
        help="Group who has the condition.")                
    context_type = fields.Selection(
        string="Condition Context Type",
        selection=[
            ("Encounter", "Encounter"), 
            ("Episode Of Care", "Episode of Care")], 
        help="Type of encounter when condition first asserted.")                    
    context_name = fields.Char(
        string="Context", 
        compute="compute_context_name", 
        help="Encounter when condition first asserted.")                
    # context_encounter_id = fields.Many2one(
    #     comodel_name="hc.res.encounter", 
    #     string="Context Encounter", 
    #     help="Encounter when condition first asserted.")                    
    context_episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Context Episode Of Care", 
        help="Episode Of Care when condition first asserted.")                    
    onset_type = fields.Selection(
        string="Condition Onset Type",
        selection=[
            ("dateTime", "Datetime"), 
            ("Age", "Age"), 
            ("Period", "Period"), 
            ("Range", "Range"), 
            ("string", "String")], 
        help="Type of onset.")
    onset_name = fields.Char(
        string="Onset", 
        compute="compute_onset_name", 
        help="Estimated or actual date, date-time, or age.")             
    onset_datetime = fields.Datetime(
        string="Onset", 
        help="Estimated or actual date, date-time, or age.")                    
    onset_age = fields.Integer(
        string="Onset Age", 
        size=3, 
        help="Estimated or actual date, date-time, or age.")                    
    onset_age_uom = fields.Many2one(
        comodel_name="hc.vs.uom", 
        string="Onset Age UOM", 
        default="year", 
        help="Age unit of measure. Default = year.")                    
    onset_start_date = fields.Datetime(
        string="Onset Start Date", 
        help="Start of the estimated or actual date, date-time, or age.")                    
    onset_end_date = fields.Datetime(
        string="Onset End Date", 
        help="End of the estimated or actual date, date-time, or age.")                    
    onset_range_low = fields.Float(
        string="Onset Range Low", 
        help="Low limit of estimated or actual date, date-time, or age.")                    
    onset_range_high = fields.Float(
        string="Onset Range High", 
        help="High limit of estimated or actual date, date-time, or age.")                    
    abatement_type = fields.Selection(
        string="Condition Abatement Type",
        selection=[
            ("date", "Date"), 
            ("Age", "Age"), 
            ("boolean", "Boolean"), 
            ("Period", "Period"), 
            ("Range", "Range"), 
            ("string", "String")], 
        help="Type of abatement.")                    
    abatement_name = fields.Char(
        string="Abatement", 
        compute="compute_abatement_name", 
        help="If/when in resolution/remission .")                   
    abatement_date = fields.Date(
        string="Abatement Date", 
        help="date if/when in resolution/remission.")                    
    abatement_age = fields.Integer(
        string="Abatement Age", 
        size=3, 
        help="If/when in resolution/remission.")                    
    abatement_age_uom = fields.Many2one(
        comodel_name="hc.vs.uom", 
        string="Abatement Age UOM", 
        default="year", 
        help="Age unit of measure. Default = year.")                    
    is_abatement = fields.Boolean(
        string="Abatement", 
        help="boolean if/when in resolution/remission.")                    
    abatement_start_date = fields.Datetime(
        string="Abatement Start Date", 
        help="Start of the if/when in resolution/remission.")
    abatement_end_date = fields.Datetime(
        string="Abatement End Date", 
        help="End of the if/when in resolution/remission.")                 
    abatement_range_low = fields.Float(
        string="Abatement Range Low", 
        help="Low limit of if/when in resolution/remission.")                    
    abatement_range_high = fields.Float(
        string="Abatement Range High", 
        help="High limit of if/when in resolution/remission.")                    
    abatement = fields.Char(
        string="Abatement", 
        help="string if/when in resolution/remission.")                    
    date_asserted = fields.Date(
        string="Date Asserted",
        help="When first entered.")                    
    asserter_type = fields.Selection(
        string="Condition Asserter Type",
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Patient", "Patient")], 
        help="Type of asserter.")                    
    asserter_name = fields.Char(
        string="Asserter", 
        compute="compute_asserter_name", 
        help="Person who asserts this condition.")                  
    asserter_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Asserter Practitioner", 
        help="Practitioner person who asserts this condition.")                    
    asserter_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Asserter Patient", 
        help="Patient person who asserts this condition.")                    
    note_ids = fields.One2many(
        comodel_name="hc.condition.note", 
        inverse_name="condition_id", 
        string="Note", 
        help="Additional information about the Condition.")                    
    stage_ids = fields.One2many(
        comodel_name="hc.condition.stage", 
        inverse_name="condition_id", 
        string="Stage", 
        help="Stage/grade, usually assessed formally.")                    
    evidence_ids = fields.One2many(
        comodel_name="hc.condition.evidence", 
        inverse_name="condition_id", 
        string="Evidence", 
        help="Supporting evidence.")                    

class ConditionStage(models.Model):    
    _name = "hc.condition.stage"    
    _description = "Condition Stage"
    _inherit = ["hc.basic.association"]            

    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        required="True", 
        help="Condition associated with this stage.")                    
    assessment_ids = fields.One2many(
        comodel_name="hc.condition.stage.assessment", 
        inverse_name="condition_stage_id", 
        string="Assessment", 
        help="Formal record of assessment.")                    
    summary_id = fields.Many2one(
        comodel_name="hc.vs.condition.stage", 
        string="Summary", 
        help="Simple summary (disease specific).")                    

class ConditionEvidence(models.Model):    
    _name = "hc.condition.evidence"    
    _description = "Condition Evidence"
    _inherit = ["hc.basic.association"]            

    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        required="True", 
        help="Condition associated with this evidence.")                    
    detail_ids = fields.One2many(
        comodel_name="hc.condition.evidence.detail", 
        inverse_name="condition_evidence_id", 
        string="Detail", 
        help="Supporting information found elsewhere.")                    
    code_id = fields.Many2one(
        comodel_name="hc.vs.condition.evidence.code", 
        string="Code", 
        help="Manifestation/symptom.")                    

class ConditionIdentifier(models.Model):    
    _name = "hc.condition.identifier"    
    _description = "Condition Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        help="Condition associated with this identifier.")                    

class ConditionBodySite(models.Model):  
    _name = "hc.condition.body.site"    
    _description = "Condition Body Site"        
    _inherit = ["hc.basic.association"]
    
    body_site_id = fields.Many2one(
        comodel_name="hc.vs.body.site", 
        string="Body Site", 
        help="Anatomical location, if relevant.")             
    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        required="True", 
        help="Encounter associated with this condition body site.")                

class ConditionStageAssessment(models.Model):    
    _name = "hc.condition.stage.assessment"    
    _description = "Condition Stage Assessment"        
    _inherit = ["hc.basic.association"]    

    condition_stage_id = fields.Many2one(
        comodel_name="hc.condition.stage", 
        string="Stage", 
        help="Stage associated with this condition stage assessment.")                    
    assessment_type = fields.Selection(
        string="Condition Stage Assessment Assessment Type", 
        selection=[
            ("clinical impression", "Clinical Impression"), 
            ("diagnostic report", "Diagnostic Report"), 
            ("observation", "Observation")], 
        help="Type of assessment.")                    
    assessment_name = fields.Char(
        string="Assessment", 
        compute="compute_assessment_name", 
        help="Formal record of assessment.")                   
    # assessment_clinical_impression_id = fields.Many2one(
    #     comodel_name="hc.res.clinical.impression", 
    #     string="Assessment Clinical Impressions", 
    #     help="Clinical Impression formal record of assessment.")                    
    # assessment_diagnostic_report_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.report", 
    #     string="Assessment Diagnostic Reports", 
    #     help="Diagnostic Report formal record of assessment.")                    
    # assessment_observation_id = fields.Many2one(
    #     comodel_name="hc.res.observation", 
    #     string="Assessment Observations", 
    #     help="Observation formal record of assessment.")                    

class ConditionEvidenceDetail(models.Model):    
    _name = "hc.condition.evidence.detail"    
    _description = "Condition Evidence Detail"        
    _inherit = ["hc.basic.association"]    

    condition_evidence_id = fields.Many2one(
        comodel_name="hc.condition.evidence", 
        string="Evidence", 
        help="Evidence associated with this condition evidence detail.")                    
    detail_type = fields.Selection(
        string="Conditional Evidence Detail Type", 
        selection=[
            ("string", "String"), 
            ("observation", "Observation"), 
            ("clinical impression", "Clinical Impression"), 
            ("diagnostic report", "Diagnostic Report")], 
        help="Type of supporting information found elsewhere.")                    
    detail_name = fields.Char(
        string="Details", 
        compute="compute_detail_name", 
        help="Supporting information found elsewhere.")                
    detail = fields.Char(
        string="Details", 
        help="Supporting information found elsewhere.")                    
    # detail_observation_id = fields.Many2one(
    #     comodel_name="hc.res.observation", 
    #     string="Detail Observation", 
    #     help="Observation supporting information found elsewhere.")                    
    # detail_clinical_impression_id = fields.Many2one(
    #     comodel_name="hc.res.clinical.impression", 
    #     string="Detail Clinical Impression", 
    #     help="Clinical Impression supporting information found elsewhere.")                    
    # detail_diagnostic_report_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.report", 
    #     string="Detail Diagnostic Report", 
    #     help="Diagnostic Report supporting information found elsewhere.")                    

class ConditionNote(models.Model):  
    _name = "hc.condition.note" 
    _description = "Condition Note"     
    _inherit = ["hc.basic.association", "hc.annotation"]

    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        help="Condition associated with this identifier.")              

class ConditionSeverity(models.Model):    
    _name = "hc.vs.condition.severity"    
    _description = "Condition Severity"        
    _inherit = ["hc.value.set.contains"]    

class ConditionEvidenceCode(models.Model):    
    _name = "hc.vs.condition.evidence.code"    
    _description = "Condition Evidence Code"        
    _inherit = ["hc.value.set.contains"]    

class ConditionStage(models.Model):    
    _name = "hc.vs.condition.stage"    
    _description = "Condition Stage"        
    _inherit = ["hc.value.set.contains"]

# External Reference

class EpisodeOfCareCondition(models.Model):    
    _inherit = "hc.episode.of.care.condition"  
              
    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        help="Condition associated with this episode of care condition.")

class ProcedureReasonReference(models.Model):   
    _inherit = "hc.procedure.reason.reference"
                       
    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        help="Condition associated with this Procedure.")