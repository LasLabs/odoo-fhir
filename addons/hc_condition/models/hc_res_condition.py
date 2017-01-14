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
    body_site_ids = fields.Many2many(
        comodel_name="hc.vs.body.site", 
        relation="condition_body_site_rel", 
        string="Body Sites", 
        help="Anatomical location, if relevant.")              
    subject_type = fields.Selection(
        string="Subject Type",
        required="True", 
        selection=[
            ("patient", "Patient"), 
            ("group", "Group")], 
        help="Type of who has the condition.")
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
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
    # context_type = fields.Selection(
    #     string="Context Type",
    #     selection=[
    #         ("encounter", "Encounter"), 
    #         ("episode_of_care", "Episode of Care")], 
    #     help="Type of encounter when condition first asserted.")                    
    # context_name = fields.Char(
    #     string="Context", 
    #     compute="_compute_context_name",
    #     store="True", 
    #     help="Encounter when condition first asserted.")                
    # context_encounter_id = fields.Many2one(
    #     comodel_name="hc.res.encounter", 
    #     string="Context Encounter", 
    #     help="Encounter when condition first asserted.")                    
    # context_episode_of_care_id = fields.Many2one(
    #     comodel_name="hc.res.episode.of.care", 
    #     string="Context Episode Of Care", 
    #     help="Episode Of Care when condition first asserted.")                    
    onset_type = fields.Selection(
        string="Onset Type",
        selection=[
            ("dateTime", "Datetime"), 
            ("Age", "Age"), 
            ("Period", "Period"), 
            ("Range", "Range"), 
            ("string", "String")], 
        help="Type of onset.")
    onset_name = fields.Char(
        string="Onset", 
        compute="_compute_onset_name",
        store="True", 
        help="Estimated or actual date, date-time, or age.")             
    onset_datetime = fields.Datetime(
        string="Onset Datetime", 
        help="Estimated or actual date, date-time, or age.")                    
    onset_age = fields.Integer(
        string="Onset Age", 
        size=3, 
        help="Estimated or actual date, date-time, or age.")
    onset_age_uom_id = fields.Many2one(
        comodel_name="hc.vs.time.uom", 
        string="Onset Age UOM", 
        default="a", 
        help="Onset age unit of measure.")                    
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
        string="Abatement Type",
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
        compute="_compute_abatement_name",
        store="True", 
        help="If/when in resolution/remission .")                   
    abatement_date = fields.Date(
        string="Abatement Date", 
        help="date if/when in resolution/remission.")                    
    abatement_age = fields.Integer(
        string="Abatement Age", 
        size=3, 
        help="If/when in resolution/remission.")                    
    abatement_age_uom_id = fields.Many2one(
        comodel_name="hc.vs.time.uom", 
        string="Abatement Age UOM", 
        default="a",
        help="Abatement age unit of measure.")                
    is_abatement = fields.Boolean(
        string="Abatement", 
        help="Boolean of if/when in resolution/remission.")                    
    abatement_start_date = fields.Datetime(
        string="Abatement Start Date", 
        help="Start of period of the if/when in resolution/remission.")
    abatement_end_date = fields.Datetime(
        string="Abatement End Date", 
        help="End of period of the if/when in resolution/remission.")                 
    abatement_range_low = fields.Float(
        string="Abatement Range Low", 
        help="Low limit of if/when in resolution/remission.")                    
    abatement_range_high = fields.Float(
        string="Abatement Range High", 
        help="High limit of if/when in resolution/remission.")                    
    abatement_string = fields.Char(
        string="Abatement", 
        help="String of if/when in resolution/remission.")                    
    date_asserted = fields.Date(
        string="Date Asserted",
        help="When first entered.")                    
    asserter_type = fields.Selection(
        string="Asserter Type",
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Patient", "Patient")], 
        help="Type of asserter.")                    
    asserter_name = fields.Char(
        string="Asserter", 
        compute="_compute_asserter_name",
        store="True",  
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
        string="Notes", 
        help="Additional information about the Condition.")                    
    stage_ids = fields.One2many(
        comodel_name="hc.condition.stage", 
        inverse_name="condition_id", 
        string="Stages", 
        help="Stage/grade, usually assessed formally.")                    
    evidence_ids = fields.One2many(
        comodel_name="hc.condition.evidence", 
        inverse_name="condition_id", 
        string="Evidence", 
        help="Supporting evidence.")                    

    @api.multi          
    def _compute_subject_name(self):            
        for hc_res_condition in self:       
            if hc_res_condition.subject_type == 'patient':  
                hc_res_condition.subject_name = hc_res_condition.subject_patient_id.name
            elif hc_res_condition.subject_type == 'group':  
                hc_res_condition.subject_name = hc_res_condition.subject_group_id.name

    # @api.multi          
    # def _compute_context_name(self):            
    #     for hc_res_condition in self:       
    #         if hc_res_condition.context_type == 'encounter':
    #             hc_res_condition.context_name = hc_res_condition.context_encounter_id.name
    #         elif hc_res_condition.context_type == 'episode_of_care':  
    #             hc_res_condition.context_name = hc_res_condition.context_episode_of_care_id.name


    @api.multi          
    def _compute_onset_name(self):          
        for hc_res_condition in self:       
            if hc_res_condition.onset_type == 'date_time':   
                hc_res_condition.onset_name = hc_res_condition.onset_datetime
            elif hc_res_condition.onset_type == 'age':  
                hc_res_condition.onset_name = hc_res_condition.onset_age_id.name
            elif hc_res_condition.onset_type == 'period':   
                hc_res_condition.onset_name = hc_res_condition.onset_period_id.name
            elif hc_res_condition.onset_type == 'range':    
                hc_res_condition.onset_name = hc_res_condition.onset_range_id.name
            elif hc_res_condition.onset_type == 'string':   
                hc_res_condition.onset_name = hc_res_condition.onset_string

    @api.multi          
    def _compute_abatement_name(self):          
        for hc_res_condition in self:       
            if hc_res_condition.abatement_type == 'date':   
                hc_res_condition.abatement_name = hc_res_condition.abatement_date
            elif hc_res_condition.abatement_type == 'age':  
                hc_res_condition.abatement_name = hc_res_condition.abatement_age_id.name
            elif hc_res_condition.abatement_type == 'boolean':  
                hc_res_condition.abatement_name = hc_res_condition.abatement_boolean
            elif hc_res_condition.abatement_type == 'period':   
                hc_res_condition.abatement_name = hc_res_condition.abatement_period_id.name
            elif hc_res_condition.abatement_type == 'range':    
                hc_res_condition.abatement_name = hc_res_condition.abatement_range_id.name
            elif hc_res_condition.abatement_type == 'string':   
                hc_res_condition.abatement_name = hc_res_condition.abatement_string

    @api.multi          
    def _compute_asserter_name(self):           
        for hc_res_condition in self:       
            if hc_res_condition.asserter_type == 'practitioner':    
                hc_res_condition.asserter_name = hc_res_condition.asserter_practitioner_id.name
            elif hc_res_condition.asserter_type == 'patient':   
                hc_res_condition.asserter_name = hc_res_condition.asserter_patient_id.name

class ConditionStage(models.Model):    
    _name = "hc.condition.stage"    
    _description = "Condition Stage"
    _inherit = ["hc.basic.association"]            

    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        help="Condition associated with this Condition Stage.") 
    stage_type = fields.Selection(
        string="Abatement Type",
        required="True", 
        selection=[
            ("summary", "Summary"), 
            ("assessment", "Assessment")], 
        help="Summary or assessment.")
    stage_name = fields.Char(
        string="Stage", 
        compute="_compute_stage_name",
        store="True",  
        help="Summary or assessment.")                   
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
        help="Condition associated with this Condition Evidence.")                    
    detail_ids = fields.One2many(
        comodel_name="hc.condition.evidence.detail", 
        inverse_name="evidence_id", 
        string="Details", 
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
        help="Condition associated with this Condition Identifier.")                                  

class ConditionStageAssessment(models.Model):    
    _name = "hc.condition.stage.assessment"    
    _description = "Condition Stage Assessment"        
    _inherit = ["hc.basic.association"]    

    condition_stage_id = fields.Many2one(
        comodel_name="hc.condition.stage", 
        string="Stage", 
        help="Stage associated with this Condition Stage Assessment.")                    
    assessment_type = fields.Selection(
        string="Assessment Type", 
        selection=[
            ("clinical_impression", "Clinical Impression"), 
            ("diagnostic_report", "Diagnostic Report"), 
            ("observation", "Observation")], 
        help="Type of assessment.")                    
    assessment_name = fields.Char(
        string="Assessment", 
        compute="_compute_assessment_name",
        store="True",  
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

    # @api.multi          
    # def _compute_assessment_name(self):         
    #     for hc_res_condition in self:       
    #         if hc_res_condition.assessment_type == 'clinical_impression':   
    #             hc_res_condition.assessment_name = hc_res_condition.assessment_clinical_impression_id.name
    #         elif hc_res_condition.assessment_type == 'observation': 
    #             hc_res_condition.assessment_name = hc_res_condition.assessment_observation_id.name
            # elif hc_res_condition.assessment_type == 'diagnostic_report':   
            #     hc_res_condition.assessment_name = hc_res_condition.assessment_diagnostic_report_id.name
            
class ConditionEvidenceDetail(models.Model):    
    _name = "hc.condition.evidence.detail"    
    _description = "Condition Evidence Detail"        
    _inherit = ["hc.basic.association"]    

    evidence_id = fields.Many2one(
        comodel_name="hc.condition.evidence", 
        string="Evidence", 
        help="Evidence associated with this Condition Evidence Detail.")                    
    reference = fields.Reference(
        string="Reference",
        selection="_records_models")
    # detail_type = fields.Selection(
    #     string="Detail Type", 
    #     selection=[
    #         ("string", "String"), 
    #         ("reference", "Reference")], 
    #     help="Type of supporting information found elsewhere.")                 
    detail_name = fields.Char(
        string="Details", 
        compute="_compute_detail_name",
        store="True",  
        help="Supporting information found elsewhere.")                
    detail = fields.Char(
        string="Details", 
        help="Supporting information found elsewhere.")
    detail_string = fields.Char(
        string="Detail String", 
        help="String supporting information found elsewhere.")
    detail_condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Detail Condition", 
        help="Condition supporting information found elsewhere.")                   
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

    @api.model
    def _records_models(self):
        #type manual is used to display custom models only
        models = self.env['ir.model'].search([('state', '=', 'manual')])
        return [(model.model, model.name)
                for model in models
                if model.model.startswith('hc.res')]

    @api.multi          
    def _compute_detail_name(self):         
        for hc_res_condition in self:       
            if hc_res_condition.detail_type == 'string':    
                hc_res_condition.detail_name = hc_res_condition.detail_string_
            elif hc_res_condition.detail_type == 'condition':   
                hc_res_condition.detail_name = hc_res_condition.detail_condition_id.name
            # elif hc_res_condition.detail_type == 'observation': 
            #     hc_res_condition.detail_name = hc_res_condition.detail_observation_id.name
            # elif hc_res_condition.detail_type == 'clinical_impression': 
            #     hc_res_condition.detail_name = hc_res_condition.detail_clinical_impression_id.name
            # elif hc_res_condition.detail_type == 'diagnostic_report':   
            #     hc_res_condition.detail_name = hc_res_condition.detail_diagnostic_report_id.name

class ConditionNote(models.Model):  
    _name = "hc.condition.note" 
    _description = "Condition Note"     
    _inherit = ["hc.basic.association", "hc.annotation"]

    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        help="Condition associated with this Condition Note.")              

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