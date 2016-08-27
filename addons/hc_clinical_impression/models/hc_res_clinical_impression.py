# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ClinicalImpression(models.Model):    
    _name = "hc.res.clinical.impression"    
    _description = "Clinical Impression"        

    identifier_ids = fields.One2many(
        comodel_name="hc.clinical.impression.identifier", 
        inverse_name="clinical_impression_id", 
        string="Identifiers", 
        help="Business identifier.")                
    status = fields.Selection(string="Clinical Impression Status", required="True", selection=[("in-progress", "In-Progress"), ("completed", "Completed"), ("entered-in-error", "Entered-In-Error")], help="Identifies the workflow status of the assessment.")                
    code_id = fields.Many2one(comodel_name="hc.vs.clinical.impression.kind", string="Code", help="Kind of impression performed.")                
    description = fields.Char(string="Description", help="Why/how the assessment was performed.")                
    subject_type = fields.Selection(string="Clinical Impression Subject Type", selection=[("Patient", "Patient"), ("Group", "Group")], help="Type of entity assessed.")                
    subject_name = fields.Char(string="Subject", compute="compute_subject_name", required="True", help="Patient or group assessed.")                
    subject_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject Patient", required="True", help="Patient assessed.")                
    subject_group_id = fields.Many2one(comodel_name="hc.res.group", string="Subject Group", required="True", help="Group assessed.")                
    assessor_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Assessor Practitioner", help="The clinician performing the assessment.")                
    date = fields.Datetime(string="Date", help="When the assessment occurred.")                
    context_type = fields.Selection(string="Clinical Impression Context Type", selection=[("Encounter", "Encounter"), ("Episode Of Care", "Episode Of Care")], help="Type of Encounter or Episode created from.")                
    context_name = fields.Char(string="Context", compute="compute_context_name", help="Encounter or Episode created from.")                
    # context_encounter_id = fields.Many2one(
    #     comodel_name="hc.res.encounter", 
    #     string="Context Encounter", 
    #     help="Encounter created from.")                
    # context_episode_of_care_id = fields.Many2one(
    #     comodel_name="hc.res.episode of care", 
    #     string="Context Episode Of Care", 
    #     help="Episode Of Care created from.")                
    previous_clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Previous Clinical Impression", help="Reference to last assessment.")                
    problem_ids = fields.One2many(comodel_name="hc.clinical.impression.problem", inverse_name="clinical_impression_id", string="Problems", help="General assessment of patient state.")                
    trigger_id = fields.Many2one(comodel_name="hc.vs.clinical.impression.trigger", string="Trigger", help="CodeableConcept request or event that necessitated this assessment.")                
    trigger = fields.Char(string="Trigger Any", help="string request or event that necessitated this assessment.")                
    protocol = fields.Char(string="Protocol", help="Clinical Protocol followed.")                
    summary = fields.Char(string="Summary", help="Summary of the assessment.")                
    resolved_ids = fields.One2many(comodel_name="hc.clinical.impression.resolved", inverse_name="clinical_impression_id", string="Resolved", help="Diagnosies/conditions resolved since previous assessment.")                
    prognosis_ids = fields.One2many(comodel_name="hc.clinical.impression.prognosis", inverse_name="clinical_impression_id", string="Prognosis", help="Estimate of likely outcome.")                
    prognosis_reference_ids = fields.One2many(comodel_name="hc.clinical.impression.prognosis.reference", inverse_name="clinical_impression_id", string="Prognosis References", help="RiskAssessment expressing likely outcome.")                
    plan_ids = fields.One2many(comodel_name="hc.clinical.impression.plan", inverse_name="clinical_impression_id", string="Plans", help="Plan of action after assessment.")                
    action_ids = fields.One2many(comodel_name="hc.clinical.impression.action", inverse_name="clinical_impression_id", string="Actions", help="Actions taken during assessment.")                
    note_ids = fields.One2many(comodel_name="hc.clinical.impression.note", inverse_name="clinical_impression_id", string="Notes", help="Comments made about the Clinical Impression.")                
    investigation_ids = fields.One2many(comodel_name="hc.clinical.impression.investigation", inverse_name="clinical_impression_id", string="Investigations", help="One or more sets of investigations (signs, symptions, etc).")                
    finding_ids = fields.One2many(comodel_name="hc.clinical.impression.finding", inverse_name="clinical_impression_id", string="Findings", help="Possible or likely findings and diagnoses.")                
    ruled_out_ids = fields.One2many(comodel_name="hc.clinical.impression.ruled.out", inverse_name="clinical_impression_id", string="Ruled Outs", help="Diagnosis considered not possible.")                

class ClinicalImpressionPlan(models.Model):    
    _name = "hc.clinical.impression.plan"    
    _description = "Clinical Impression Plan"        
    _inherit = ["hc.basic.association"]

    clinical_impression_id = fields.Many2one(
        comodel_name="hc.res.clinical.impression", 
        string="Clinical Impression", 
        help="Clinical impression associated with this clinical impression plan.")                
    plan_type = fields.Selection(string="Clinical Impression Plan Plan Type", selection=[("care plan", "Care Plan"), ("appointment", "Appointment"),("communication request", "Communication Request"),("device use request", "Device Use Request"),("diagnostic order", "Diagnostic Order"),("medication order", "Medication Order"),("nutrition order", "Nutrition Order"), ("order", "Order"),("procedure request", "Procedure Request"),("process request", "Process Request"),("referral request", "Referral Request"),("supply request", "Supply Request"),("vision prescription", "Vision Prescription")], help="Type of plan of action after assessment.")              
    plan_name = fields.Char(string="Plan", compute="compute_plan_name", help="Plan of action after assessment.")               
    # plan_appointment_id = fields.Many2one(
    #     comodel_name="hc.res.appointment", 
    #     string="Plan Appointment", 
    #     help="Appointment plan of action after assessment.")                
    # plan_communication_request_id = fields.Many2one(
    #     comodel_name="hc.res.communication.request", 
    #     string="Plan Communication Request", 
    #     help="Communication Request plan of action after assessment.")                
    # plan_device_use_request_id = fields.Many2one(
    #     comodel_name="hc.res.device.use.request", 
    #     string="Plan Device Use Request", 
    #     help="Device Use Request plan of action after assessment.")                
    # plan_diagnostic_order_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.order", 
    #     string="Plan Diagnostic Order", 
    #     help="Diagnostic Order plan of action after assessment.")                
    # plan_medication_order_id = fields.Many2one(
    #     comodel_name="hc.res.medication.order", 
    #     string="Plan Medication Order", 
    #     help="Medication Order plan of action after assessment.")                
    # plan_nutrition_order_id = fields.Many2one(
    #     comodel_name="hc.res.nutrition.order", 
    #     string="Plan Nutrition Order", 
    #     help="Nutrition Order plan of action after assessment.")                
    # plan_order_id = fields.Many2one(
    #     comodel_name="hc.res.order", 
    #     string="Plan Order", 
    #     help="Order plan of action after assessment.")                
    # plan_procedure_request_id = fields.Many2one(
    #     comodel_name="hc.res.procedure.request", 
    #     string="Plan Procedure Request", 
    #     help="Procedure Request plan of action after assessment.")                
    # plan_process_request_id = fields.Many2one(
    #     comodel_name="hc.res.process.request", 
    #     string="Plan Process Request", 
    #     help="Process Request plan of action after assessment.")                
    # plan_referral_request_id = fields.Many2one(
    #     comodel_name="hc.res.referral.request", 
    #     string="Plan Referral Request", 
    #     help="Referral Request plan of action after assessment.")                
    # plan_supply_request_id = fields.Many2one(
    #     comodel_name="hc.res.supply.request", 
    #     string="Plan Supply Request", 
    #     help="Supply Request plan of action after assessment.")                
    # plan_vision_prescription_id = fields.Many2one(
    #     comodel_name="hc.res.vision.prescription", 
    #     string="Plan Vision Prescription", 
    #     help="Vision Prescription of the plan of action after assessment.")             

class ClinicalImpressionAction(models.Model):    
    _name = "hc.clinical.impression.action"    
    _description = "Clinical Impression Action"        
    _inherit = ["hc.basic.association"]

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this clinical impression action.")
    action_type = fields.Selection(string="Clinical Impression Action Action Type", selection=[("Referral Request", "Referral Request"), ("Procedure Request|Procedure|Medication Order|Diagnostic Order|Nutrition Order|Supply Request|Appointment", "Procedure Request|Procedure|Medication Order|Diagnostic Order|Nutrition Order|Supply Request|Appointment")], help="Type of actions taken during assessment.")
    action_name = fields.Char(string="Action", compute="compute_action_name", help="Actions taken during assessment.")
    # action_diagnostic_order_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.order", 
    #     string="Action Diagnostic Order", 
    #     help="Diagnostic Order actions taken during assessment.")
    # action_procedure_request_id = fields.Many2one(
    #     comodel_name="hc.res.procedure.request", 
    #     string="Action Procedure Request", 
    #     help="Procedure Request actions taken during assessment.")
    action_procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Action Procedure", 
        help="Procedure actions taken during assessment.")
    # action_medication_order_id = fields.Many2one(
    #     comodel_name="hc.res.medication.order", 
    #     string="Action Medication Order", 
    #     help="Medication Order actions taken during assessment.")
    # action_diagnostic_order_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.order", 
    #     string="Action Diagnostic Order", 
    #     help="Diagnostic Order actions taken during assessment.")
    # action_nutrition_order_id = fields.Many2one(
    #     comodel_name="hc.res.nutrition.order", 
    #     string="Action Nutrition Order", 
    #     help="Nutrition Order actions taken during assessment.")
    # action_supply_request_id = fields.Many2one(
    #     comodel_name="hc.res.supply.request", 
    #     string="Action Supply Request", 
    #     help="Supply Request actions taken during assessment.")
    # action_appointment_id = fields.Many2one(
    #     comodel_name="hc.res.appointment", 
    #     string="Action Appointment", 
    #     help="Appointment actions taken during assessment.")


class ClinicalImpressionInvestigation(models.Model):    
    _name = "hc.clinical.impression.investigation"    
    _description = "Clinical Impression Investigation"

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this investigation.")
    code_id = fields.Many2one(comodel_name="hc.vs.investigation.set", string="Code", required="True", help="A name/code for the set.")
    item_type = fields.Selection(string="Investigation Item Type", selection=[("observation", "Observation"), ("questionnaire response", "Questionnaire Response"), ("family member history", "Family Member History"), ("diagnostic report", "Diagnostic Report"), ("risk assessment", "Risk Assessment"), ("imaging study", "Imaging Study")], help="Type of record of a specific investigation.")
    item_name = fields.Char(string="Item", compute="compute_item_name", help="Record of a specific investigation.")
    # item_observation_id = fields.Many2one(
    #     comodel_name="hc.res.observation", 
    #     string="Item Observation", 
    #     help="Observation record of a specific investigation.")
    # item_questionnaire_response_id = fields.Many2one(
    #     comodel_name="hc.res.questionnaire.response", 
    #     string="Item Questionnaire Response", 
    #     help="Questionnaire Response record of a specific investigation.")
    item_family_member_history_id = fields.Many2one(
        comodel_name="hc.res.family.member.history", 
        string="Item Family Member History", 
        help="Family Member History record of a specific investigation.")
    # item_diagnostic_report_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.report", 
    #     string="Item Diagnostic Report", 
    #     elp="Diagnostic Report record of a specific investigation.")
    # item_risk_assessment_id = fields.Many2one(
    #     comodel_name="hc.res.risk.assessment", 
    #     string="Item Risk Assessment", 
    #     help="Risk Assessment record of a specific investigation.")
    # item_imaging_study_id = fields.Many2one(
    #     comodel_name="hc.res.imaging.study", 
    #     string="Item Imaging Study", 
    #     help="Imaging Study record of a specific investigation.")

class ClinicalImpressionFinding(models.Model):    
    _name = "hc.clinical.impression.finding"    
    _description = "Clinical Impression Finding"        

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this finding.")                
    item_type = fields.Selection(
        string="Finding Item Type",
        required="True",  
        selection=[
            ("code", "Code"),
            ("Condition", "Condition"), 
            ("Observation", "Observation")], 
        help="Type of what was found.")                
    item_name = fields.Char(string="Item", compute="compute_item_name", required="True", help="What was found.")                
    item_code_id = fields.Many2one(comodel_name="hc.vs.condition.code", string="Item Code", required="True", help="What was found")                
    item_condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Item Condition", 
        required="True", 
        help="Condition what was found.")                
    # item_observation_id = fields.Many2one(
    #     comodel_name="hc.res.observation", 
    #     string="Item Observation", 
    #     help="Observation what was found.")                
    cause = fields.Char(
        string="Cause", 
        help="Which investigations support finding.")                

class ClinicalImpressionRuledOut(models.Model): 
    _name = "hc.clinical.impression.ruled.out"  
    _description = "Clinical Impression Ruled Out"       

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this ruled out.")                
    item_id = fields.Many2one(comodel_name="hc.vs.condition.code", string="Item", required="True", help="Specific text of code for diagnosis.")                
    reason = fields.Char(string="Reason", help="Grounds for elimination.")                

class ClinicalImpressionIdentifier(models.Model):    
    _name = "hc.clinical.impression.identifier"    
    _description = "Clinical Impression Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this clinical impression identifier.")                

class ClinicalImpressionPrognosisReference(models.Model):    
    _name = "hc.clinical.impression.prognosis.reference"    
    _description = "Clinical Impression Prognosis Reference"        
    _inherit = ["hc.basic.association"]

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this clinical impression prognosis reference.")                
    # risk_assessment_id = fields.Many2one(
    #     comodel_name="hc.res.risk.assessment", 
    #     string="Risk Assessment", 
    #     help="Risk assessment associated with this clinical impression prognosis reference.")                

class ClinicalImpressionNote(models.Model):    
    _name = "hc.clinical.impression.note"    
    _description = "Clinical Impression Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this clinical impression note.")                

class ClinicalImpressionProblem(models.Model):    
    _name = "hc.clinical.impression.problem"    
    _description = "Clinical Impression Problem"        
    _inherit = ["hc.basic.association"]

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this clinical impression problem.")                
    problem_type = fields.Selection(string="Clinical Impression Problem Problem Type", selection=[("Condition", "Condition"), ("Allergy Intolerance", "Allergy Intolerance")], help="Type of general assessment of patient state.")                
    problem_name = fields.Char(string="Problem", compute="compute_problem_name", help="General assessment of patient state.")                
    problem_condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Problem Condition", 
        help="Condition general assessment of patient state.")                
    problem_allergy_intolerance_id = fields.Many2one(
        comodel_name="hc.res.allergy.intolerance", 
        string="Problem Allergy Intolerance", 
        help="Allergy Intolerance general assessment of patient state.")                

class ClinicalImpressionResolved(models.Model):    
    _name = "hc.clinical.impression.resolved"    
    _description = "Clinical Impression Resolved"        
    _inherit = ["hc.basic.association"]

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this clinical impression resolved.")                
    condition_code_id = fields.Many2one(comodel_name="hc.vs.condition.code", string="Condition Code", help="Clinical impression resolved associated with this clinical impression.")                

class ClinicalImpressionPrognosis(models.Model):    
    _name = "hc.clinical.impression.prognosis"    
    _description = "Clinical Impression Prognosis"        
    _inherit = ["hc.basic.association"]

    clinical_impression_id = fields.Many2one(comodel_name="hc.res.clinical.impression", string="Clinical Impression", help="Clinical impression associated with this clinical impression prognosis.")                
    clinical_impression_prognosis_id = fields.Many2one(comodel_name="hc.vs.clinical.impression.prognosis", string="Clinical Impression Prognosis", help="Clinical impression prognosis associated with this clinical impression.")                

class ClinicalImpressionKind(models.Model):    
    _name = "hc.vs.clinical.impression.kind"    
    _description = "Clinical Impression Kind"        
    _inherit = ["hc.value.set.contains"]

class ClinicalImpressionTrigger(models.Model):    
    _name = "hc.vs.clinical.impression.trigger"    
    _description = "Clinical Impression Trigger"        
    _inherit = ["hc.value.set.contains"]

class ClinicalImpressionResolved(models.Model):    
    _name = "hc.vs.clinical.impression.resolved"    
    _description = "Clinical Impression Resolved"        
    _inherit = ["hc.value.set.contains"]

class ClinicalImpressionPrognosis(models.Model):    
    _name = "hc.vs.clinical.impression.prognosis"    
    _description = "Clinical Impression Prognosis"        
    _inherit = ["hc.value.set.contains"]

class InvestigationSet(models.Model):   
    _name = "hc.vs.investigation.set"   
    _description = "Investigation Set"      
    _inherit = ["hc.value.set.contains"]

class ClinicalImpressionCode(models.Model):    
    _name = "hc.vs.clinical.impression.code"    
    _description = "Clinical Impression Code"        
    _inherit = ["hc.value.set.contains"]


class ConditionEvidenceDetail(models.Model):    
    _inherit = ["hc.condition.evidence.detail"]

    detail_clinical_impression_id = fields.Many2one(
        comodel_name="hc.res.clinical.impression", 
        string="Detail Clinical Impression", 
        help="Clinical Impression supporting information found elsewhere.")

class ConditionStageAssessment(models.Model):    
    _inherit = ["hc.condition.stage.assessment"]
    
    assessment_clinical_impression_id = fields.Many2one(
        comodel_name="hc.res.clinical.impression", 
        string="Assessment Clinical Impressions", 
        help="Clinical Impression formal record of assessment.") 