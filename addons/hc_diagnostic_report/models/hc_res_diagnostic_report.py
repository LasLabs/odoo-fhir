# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DiagnosticReport(models.Model):    
    _name = "hc.res.diagnostic.report"    
    _description = "Diagnostic Report"        

    identifier_ids = fields.One2many(
        comodel_name="hc.diagnostic.report.identifier", 
        inverse_name="diagnostic_report_id", 
        string="Identifiers", 
        help="Id for external references to this report.")                
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Name for this diagnostic report.")                
    status = fields.Selection(
        string="Diagnostic Report Status", 
        required="True", 
        selection=[
            ("registered", "Registered"), 
            ("partial", "Partial"), 
            ("final", "Final"), 
            ("corrected", "Corrected"), 
            ("appended", "Appended"), 
            ("cancelled", "Cancelled"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the diagnostic report as a whole.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.diagnostic.report.category", 
        string="Category", 
        help="Service category")                
    code_id = fields.Many2one(
        comodel_name="hc.vs.diagnostic.report.code", 
        string="Code", 
        required="True", 
        help="Name/Code for this diagnostic report")                
    subject_type = fields.Selection(
        string="Subject Type", 
        required="True", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group"), 
            ("Device", "Device"), 
            ("Location", "Location")], 
        help="Type of plan or agreement issuer.")                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        help="The subject of the report, usually, but not always, the patient.")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        required="True", 
        help="Patient subject of the report, usually, but not always, the patient.")                
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group subject of the report, usually, but not always, the patient.")                
    subject_location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Subject Location", 
        help="Location subject of the report, usually, but not always, the patient.")                
    subject_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Subject Device", 
        help="Device subject of the report, usually, but not always, the patient.")                
    encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Encounter", 
        help="Health care event when test ordered.")                
    effective_type = fields.Selection(
        string="Effective Type", 
        required="True", 
        selection=[
            ("dateTime", "Datetime"), 
            ("Period", "Period")], 
        help="Type of plan or agreement issuer.")                
    effective_name = fields.Char(
        string="Effective", 
        compute="_compute_effective_name", 
        required="True", 
        help="Clinically Relevant time/time-period for report.")                
    effective_datetime = fields.Datetime(
        string="Effective Datetime", 
        required="True", 
        help="DateTime clinically relevant time/time-period for report.")                
    effective_start_date = fields.Datetime(
        string="Effective Start Date", 
        help="Start of the clinically relevant time/time-period for report.")                
    effective_end_date = fields.Datetime(
        string="Effective End Date", 
        help="End of the clinically relevant time/time-period for report.")                
    issued = fields.Datetime(
        string="Issued Date", 
        required="True", 
        help="DateTime this version was released.")                
    performer_type = fields.Selection(
        string="Performer Type", 
        required="True", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Organization", "Organization")], 
        help="Type of plan or agreement issuer.")                
    performer_name = fields.Char(
        string="Performer", 
        compute="_compute_performer_name", 
        help="Responsible Diagnostic Service.")                
    performer_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Performer Practitioner",
        help="Practitioner responsible diagnostic service.")                
    performer_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Performer Organization", 
        help="Organization responsible diagnostic service.")                
    request_ids = fields.One2many(
        comodel_name="hc.diagnostic.report.request", 
        inverse_name="diagnostic_report_id", 
        string="Requests", 
        help="What was requested.")                
    specimen_ids = fields.One2many(
        comodel_name="hc.diagnostic.report.specimen", 
        inverse_name="diagnostic_report_id", 
        string="Specimens", 
        help="Specimens this report is based on.")                
    result_ids = fields.One2many(
        comodel_name="hc.diagnostic.report.result", 
        inverse_name="diagnostic_report_id", 
        string="Results", 
        help="Observations - simple, or complex nested groups.")                
    imaging_study_ids = fields.One2many(
        comodel_name="hc.diagnostic.report.imaging.study", 
        inverse_name="diagnostic_report_id", 
        string="Imaging Supplies", 
        help="Reference to full details of imaging associated with the diagnostic report.")                
    conclusion = fields.Text(
        string="Conclusion", 
        help="Clinical Interpretation of test results.")                
    coded_diagnosis_ids = fields.Many2many(
        comodel_name="hc.vs.clinical.finding", 
        string="Coded Diagnosis", 
        help="Codes for the conclusion.")          
    presented_form_ids = fields.One2many(
        comodel_name="hc.diagnostic.report.presented.form", 
        inverse_name="diagnostic_report_id", 
        string="Presented Forms", 
        help="Entire Report as issued.")                
    image_ids = fields.One2many(
        comodel_name="hc.diagnostic.report.image", 
        inverse_name="diagnostic_report_id", 
        string="Images", 
        help="Key images associated with this report.")                

class DiagnosticReportImage(models.Model):    
    _name = "hc.diagnostic.report.image"    
    _description = "Diagnostic Report Image"        

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this image.")                
    comment = fields.Text(
        string="Comment", 
        help="Comment about the image (e.g. explanation).")                
    link_id = fields.Many2one(
        comodel_name="hc.res.media", 
        string="Link", 
        required="True", 
        help="Reference to the image source.")                           

class DiagnosticReportRequest(models.Model):    
    _name = "hc.diagnostic.report.request"    
    _description = "Diagnostic Report Request"
    _inherit = ["hc.basic.association"]        

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this Diagnostic Report Request.")                
    request_type = fields.Selection(
        string="Request Type", 
        selection=[
            ("Diagnostic Request", "Diagnostic Request"), 
            ("Procedure Request", "Procedure Request"), 
            ("Referral Request", "Referral Request")], 
        help="Type of what was requested.")
    request_name = fields.Char(
        string="Request", 
        compute="_compute_request_name", 
        help="What was requested.")                
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Report", 
        help="Diagnostic Request what was requested.")                
    procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Procedure Request", 
        help="Procedure Request what was requested.")                
    referral_request_id = fields.Many2one(
        comodel_name="hc.res.referral.request", 
        string="Referral Request", 
        help="Referral Request what was requested.")                

class DiagnosticReportIdentifier(models.Model):    
    _name = "hc.diagnostic.report.identifier"    
    _description = "Diagnostic Report Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this Diagnostic Report Identifier.")                

class DiagnosticReportImagingStudy(models.Model):    
    _name = "hc.diagnostic.report.imaging.study"    
    _description = "Diagnostic Report Imaging Study"
    _inherit = ["hc.basic.association"]        

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report",  
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this Diagnostic Report Imaging Study.")                
    imaging_study_type = fields.Selection(
        string="Imaging Study Type", 
        selection=[
            ("Imaging Study", "Imaging Study"), 
            ("Imaging Manifest", "Imaging Manifest")], 
        help="Type of reference to full details of imaging associated with the diagnostic report.")                
    imaging_study_name = fields.Char(
        string="Imaging Study", 
        compute="_compute_imaging_study_name", 
        help="Reference to full details of imaging associated with the diagnostic report.")                
    imaging_study_id = fields.Many2one(
        comodel_name="hc.res.imaging.study", 
        string="Imaging Study", 
        help="Imaging Study reference to full details of imaging associated with the diagnostic report.")                
    imaging_manifest_id = fields.Many2one(
        comodel_name="hc.res.imaging.manifest", 
        string="Imaging Manifest", 
        help="Imaging Manifest reference to full details of imaging associated with the diagnostic report.")                

class DiagnosticReportResult(models.Model):    
    _name = "hc.diagnostic.report.result"    
    _description = "Diagnostic Report Result"
    _inherit = ["hc.basic.association"]        

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this Diagnostic Report Result.")                
    result_id = fields.Many2one(
        comodel_name="hc.res.observation", 
        string="Result", 
        help="Observation associated with this Diagnostic Report Result.")                

class DiagnosticReportPresentedForm(models.Model):    
    _name = "hc.diagnostic.report.presented.form"    
    _description = "Diagnostic Report Presented Form"        
    _inherit = ["hc.basic.association", "hc.attachment"]

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this Diagnostic Report Presented Form.")                

class DiagnosticReportSpecimen(models.Model):    
    _name = "hc.diagnostic.report.specimen"    
    _description = "Diagnostic Report Specimen"
    _inherit = ["hc.basic.association"]        

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this Diagnostic Report Specimen.")                
    specimen_id = fields.Many2one(
        comodel_name="hc.res.specimen", 
        string="Specimen", 
        help="Specimen associated with this Diagnostic Report Specimen.")                

class DiagnosticReportCategory(models.Model):    
    _name = "hc.vs.diagnostic.report.category"    
    _description = "Diagnostic Report Category"        
    _inherit = ["hc.value.set.contains"]

class DiagnosticReportCode(models.Model):    
    _name = "hc.vs.diagnostic.report.code"    
    _description = "Diagnostic Report Code"        
    _inherit = ["hc.value.set.contains"]

class ClinicalFinding(models.Model):    
    _name = "hc.vs.clinical.finding"    
    _description = "Clinical Finding"        
    _inherit = ["hc.value.set.contains"]

# External Reference

class ConditionStageAssessment(models.Model):    
    _inherit = "hc.condition.stage.assessment"

    assessment_diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Assessment Diagnostic Reports", 
        help="Diagnostic Report formal record of assessment.")

    @api.multi          
    def _compute_assessment_name(self):         
        for hc_res_condition in self:       
            if hc_res_condition.assessment_type == 'Clinical Impression':   
                hc_res_condition.assessment_name = hc_res_condition.assessment_clinical_impression_id.name
            elif hc_res_condition.assessment_type == 'Observation': 
                hc_res_condition.assessment_name = hc_res_condition.assessment_observation_id.name
            elif hc_res_condition.assessment_type == 'Diagnostic Report':   
                hc_res_condition.assessment_name = hc_res_condition.assessment_diagnostic_report_id.name

class ConditionEvidenceDetail(models.Model):    
    _inherit = "hc.condition.evidence.detail"

    detail_diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Detail Diagnostic Report", 
        help="Diagnostic Report supporting information found elsewhere.")     

    @api.multi          
    def _compute_detail_name(self):         
        for hc_res_condition in self:       
            if hc_res_condition.detail_type == 'string':    
                hc_res_condition.detail_name = hc_res_condition.detail_string_id.name
            elif hc_res_condition.detail_type == 'Condition':   
                hc_res_condition.detail_name = hc_res_condition.detail_condition_id.name
            elif hc_res_condition.detail_type == 'Observation': 
                hc_res_condition.detail_name = hc_res_condition.detail_observation_id.name
            elif hc_res_condition.detail_type == 'Clinical Impression': 
                hc_res_condition.detail_name = hc_res_condition.detail_clinical_impression_id.name
            elif hc_res_condition.detail_type == 'Diagnostic Report':   
                hc_res_condition.detail_name = hc_res_condition.detail_diagnostic_report_id.name

class ProcedureDiagnosticReport(models.Model):  
    _inherit = "hc.procedure.diagnostic.report"

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report", 
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this Procedure.")