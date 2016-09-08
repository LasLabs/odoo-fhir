# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DiagnosticReport(models.Model):    
    _name = "hc.res.diagnostic.report"    
    _description = "Diagnostic Report"        

    identifier_ids = fields.One2many(comodel_name="hc.diagnostic.report.identifier", inverse_name="diagnostic_report_id", string="Identifiers", help="Id for external references to this report.")                
    name = fields.Char(string="Name", required="True", help="Name for this diagnostic report.")                
    status = fields.Selection(string="Diagnostic Report Status", required="True", selection=[("registered", "Registered"), ("partial", "Partial"), ("final", "Final"), ("corrected", "Corrected"), ("appended", "Appended"), ("cancelled", "Cancelled"), ("entered-in-error", "Entered-In-Error")], help="The status of the diagnostic report as a whole.")                
    category_id = fields.Many2one(comodel_name="hc.vs.diagnostic.report.category", string="Category", help="Service category")                
    code_id = fields.Many2one(comodel_name="hc.vs.diagnostic.report.code", string="Code", required="True", help="Name/Code for this diagnostic report")                
    subject_type = fields.Selection(string="Subject Type", required="True", selection=[("patient", "Patient"), ("group", "Group"), ("device", "Device"), ("location", "Location")], help="Type of plan or agreement issuer.")                
    subject_name = fields.Char(string="Subject", compute="compute_subject_name", help="The subject of the report, usually, but not always, the patient.")                
    subject_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject Patient", required="True", help="Patient subject of the report, usually, but not always, the patient.")                
    subject_group_id = fields.Many2one(comodel_name="hc.res.group", string="Subject Group", help="Group subject of the report, usually, but not always, the patient.")                
    subject_location_id = fields.Many2one(comodel_name="hc.res.location", string="Subject Location", help="Location subject of the report, usually, but not always, the patient.")                
    subject_device_id = fields.Many2one(comodel_name="hc.res.device", string="Subject Device", help="Device subject of the report, usually, but not always, the patient.")                
    encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Encounter", help="Health care event when test ordered.")                
    effective_type = fields.Selection(string="Effective Type", required="True", selection=[("dateTime", "Datetime"), ("Period", "Period")], help="Type of plan or agreement issuer.")                
    effective_name = fields.Char(string="Effective", compute="compute_effective_name", required="True", help="Clinically Relevant time/time-period for report.")                
    effective_datetime = fields.Datetime(string="Effective Datetime", required="True", help="dateTime clinically relevant time/time-period for report.")                
    effective_start_date = fields.Datetime(string="Effective Start Date", help="Start of the clinically relevant time/time-period for report.")                
    effective_end_date = fields.Datetime(string="Effective End Date", help="End of the clinically relevant time/time-period for report.")                
    issued = fields.Datetime(string="Issued Date", required="True", help="DateTime this version was released.")                
    performer_type = fields.Selection(string="Performer Type", required="True", selection=[("Practitioner", "Practitioner"), ("Organization", "Organization")], help="Type of plan or agreement issuer.")                
    performer_name = fields.Char(string="Performer", compute="compute_performer_name", help="Responsible Diagnostic Service.")                
    performer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Performer Practitioner", required="True", help="Practitioner responsible diagnostic service.")                
    performer_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Performer Organization", help="Organization responsible diagnostic service.")                
    request_ids = fields.One2many(comodel_name="hc.diagnostic.report.request", inverse_name="diagnostic_report_id", string="Requests", help="What was requested.")                
    specimen_ids = fields.One2many(comodel_name="hc.diagnostic.report.specimen", inverse_name="diagnostic_report_id", string="Specimens", help="Specimens this report is based on.")                
    result_ids = fields.One2many(comodel_name="hc.diagnostic.report.result", inverse_name="diagnostic_report_id", string="Results", help="Observations - simple, or complex nested groups.")                
    imaging_study_ids = fields.One2many(comodel_name="hc.diagnostic.report.imaging.study", inverse_name="diagnostic_report_id", string="Imaging Supplies", help="Reference to full details of imaging associated with the diagnostic report.")                
    conclusion = fields.Text(string="Conclusion", help="Clinical Interpretation of test results.")                
    coded_diagnosis_ids = fields.One2many(comodel_name="hc.diagnostic.report.coded.diagnosis", inverse_name="diagnostic_report_id", string="Coded Diagnosis", help="Codes for the conclusion.")                
    presented_form_ids = fields.One2many(comodel_name="hc.diagnostic.report.presented.form", inverse_name="diagnostic_report_id", string="Presented Forms", help="Entire Report as issued.")                
    image_ids = fields.One2many(comodel_name="hc.diagnostic.report.image", inverse_name="diagnostic_report_id", string="Images", help="Key images associated with this report.")                

class DiagnosticReportImage(models.Model):    
    _name = "hc.diagnostic.report.image"    
    _description = "Diagnostic Report Image"        

    diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Diagnostic Report", help="Diagnostic Report associated with this image.")                
    comment = fields.Text(string="Comment", help="Comment about the image (e.g. explanation).")                
    # link_id = fields.Many2one(
    #     comodel_name="hc.res.media", 
    #     string="Link", 
    #     required="True", 
    #     help="Reference to the image source.")                

class DiagnosticReportCodedDiagnosis(models.Model):    
    _name = "hc.diagnostic.report.coded.diagnosis"    
    _description = "Diagnostic Report Coded Diagnosis"        
    _inherit = ["hc.basic.association"]

    diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Diagnostic Report", help="Diagnostic Report associated with this diagnostic report coded diagnosis.")                
    coded_diagnosis_id = fields.Many2one(comodel_name="hc.vs.clinical.finding", string="Coded Diagnosis", help="Codes for the conclusion.")                

class DiagnosticReportRequest(models.Model):    
    _name = "hc.diagnostic.report.request"    
    _description = "Diagnostic Report Request"        

    diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Diagnostic Report", help="Diagnostic Report associated with this diagnostic report diagnostic request.")                
    request_type = fields.Selection(string="Request Type", selection=[("Diagnostic Request", "Diagnostic Request"), ("Procedure Request|Referral Request", "Procedure Request|Referral Request")], help="Type of what was requested.")                
    request_name = fields.Char(string="Request", compute="compute_request_name", help="What was requested.")                
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Report", 
        help="Diagnostic Request associated with this diagnostic report diagnostic request.")                
    # procedure_request_id = fields.Many2one(
    #     comodel_name="hc.res.procedure.request", 
    #     string="Procedure Request", 
    #     help="ProcedureRequest request associated with this diagnostic report diagnostic request.")                
    # referral_request_id = fields.Many2one(
    #     comodel_name="hc.res.referral.request", 
    #     string="Referral Request", 
    #     help="ReferralRequest request associated with this diagnostic report diagnostic request.")                

class DiagnosticReportIdentifier(models.Model):    
    _name = "hc.diagnostic.report.identifier"    
    _description = "Diagnostic Report Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Diagnostic Report", help="Diagnostic Report associated with this diagnostic report identifier.")                

class DiagnosticReportImagingStudy(models.Model):    
    _name = "hc.diagnostic.report.imaging.study"    
    _description = "Diagnostic Report Imaging Study"        

    diagnostic_report_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.report",  
        string="Diagnostic Report", 
        help="Diagnostic Report associated with this diagnostic report imaging study.")                
    imaging_study_type = fields.Selection(string="Imaging Study Type", 
        selection=[("Imaging Study", "Imaging Study"), ("Imaging Manifest", "Imaging Manifest")], 
        help="Type of reference to full details of imaging associated with the diagnostic report.")                
    imaging_study_name = fields.Char(string="Imaging Study", compute="compute_imaging_study_name", help="Reference to full details of imaging associated with the diagnostic report.")                
    # imaging_study_id = fields.Many2one(
    #     comodel_name="hc.res.imaging.study", 
    #     string="Imaging Study", 
    #     help="Imaging Study associated with this diagnostic report imaging study.")                
    # imaging_manifest_id = fields.Many2one(
    #     comodel_name="hc.res.imaging.manifest", 
    #     string="Imaging Manifest", 
    #     help="ImagingManifest study associated with this diagnostic report imaging study.")                

class DiagnosticReportResult(models.Model):    
    _name = "hc.diagnostic.report.result"    
    _description = "Diagnostic Report Result"        

    diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Diagnostic Report", help="Diagnostic Report associated with this diagnostic report observation.")                
    result_id = fields.Many2one(comodel_name="hc.res.observation", string="Result", help="Observation associated with this diagnostic report observation.")                

class DiagnosticReportPresentedForm(models.Model):    
    _name = "hc.diagnostic.report.presented.form"    
    _description = "Diagnostic Report Presented Form"        
    _inherit = ["hc.basic.association", "hc.attachment"]

    diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Diagnostic Report", help="Diagnostic Report associated with this diagnostic report presented form.")                

class DiagnosticReportSpecimen(models.Model):    
    _name = "hc.diagnostic.report.specimen"    
    _description = "Diagnostic Report Specimen"        

    diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Diagnostic Report", help="Diagnostic Report associated with this diagnostic report specimen.")                
    # specimen_id = fields.Many2one(
    #     comodel_name="hc.res.specimen", 
    #     string="Specimen", 
    #     help="Specimen associated with this diagnostic report specimen.")                

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
