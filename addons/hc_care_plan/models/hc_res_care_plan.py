# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CarePlan(models.Model):    
    _name = "hc.res.care.plan"    
    _description = "Care Plan"        

    identifier_ids = fields.One2many(
        comodel_name="hc.care.plan.identifier", 
        inverse_name="care_plan_id", 
        string="Identifiers", 
        help="External Ids for this plan.")                
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group")], 
        help="Type of who care plan is for.")                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Who care plan is for.")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient who care plan is for.")                
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group who care plan is for.")                
    status = fields.Selection(
        string="Care Plan Status", 
        required="True", 
        selection=[
            ("proposed", "Proposed"), 
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("completed", "Completed"), 
            ("cancelled", "Cancelled")], 
        help="Indicates whether the plan is currently being acted upon, represents future intentions or is now a historical record.")                
    context_type = fields.Selection(
        string="Context Type", 
        selection=[
            ("Encounter", "Encounter"), 
            ("Episode Of Care", "Episode Of Care")], 
        help="Type created in context of.")                
    context_name = fields.Char(
        string="Context", 
        compute="_compute_context_name", 
        store="True", 
        help="Created in context of.")                
    context_encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Care Plan Context Encounter", 
        help="Encounter created in context of.")                
    context_episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Care Plan Context Episode Of Care", 
        help="Episode Of Care created in context of.")                
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the time period plan covers.")                
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the time period plan covers.")                
    author_ids = fields.One2many(
        comodel_name="hc.care.plan.author", 
        inverse_name="care_plan_id", 
        string="Authors", 
        help="Who is responsible for plan.")                
    modified = fields.Datetime(
        string="Modified Date", 
        help="When last updated.")                
    category_ids = fields.Many2many(
        comodel_name="hc.vs.care.plan.category", 
        relation="care_plan_category_rel", 
        string="Categories", 
        help="Type of plan.")               
    description = fields.Text(
        string="Description", 
        help="Summary of nature of plan.")                
    addresses_ids = fields.One2many(
        comodel_name="hc.care.plan.addresses", 
        inverse_name="care_plan_id", 
        string="Addresses", 
        help="Health issues this plan addresses.")                
    support_ids = fields.One2many(
        comodel_name="hc.care.plan.support", 
        inverse_name="care_plan_id", 
        string="Supports", 
        help="Information considered as part of plan.")                
    care_team_ids = fields.One2many(
        comodel_name="hc.care.plan.care.team", 
        inverse_name="care_plan_id", 
        string="Care Teams", 
        help="Who's involved in plan?")                
    goal_ids = fields.One2many(
        comodel_name="hc.care.plan.goal", 
        inverse_name="care_plan_id", 
        string="Goals", 
        help="Desired outcome of plan.")                
    note_id = fields.Many2one(
        comodel_name="hc.care.plan.note", 
        string="Note", 
        help="Comments about the plan.")                
    activity_ids = fields.One2many(
        comodel_name="hc.care.plan.activity", 
        inverse_name="care_plan_id", 
        string="Activities", 
        help="Action to occur as part of plan.")                
    related_plan_ids = fields.One2many(
        comodel_name="hc.care.plan.related.plan", 
        inverse_name="care_plan_id", 
        string="Related Plans", 
        help="Plans related to this one.")                

class CarePlanRelatedPlan(models.Model):    
    _name = "hc.care.plan.related.plan"    
    _description = "Care Plan Related Plan"        

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this related plan.")                
    code = fields.Selection(
        string="Related Plan Code", 
        selection=[
            ("includes", "Includes"), 
            ("replaces", "Replaces"), 
            ("fulfills", "Fulfills")], 
        help="Identifies the type of relationship this plan has to the target plan.")                
    plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Plan", 
        required="True", 
        help="Plan relationship exists with.")                

class CarePlanActivity(models.Model):    
    _name = "hc.care.plan.activity"    
    _description = "Care Plan Activity"        

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this activity.")                
    action_resulting_ids = fields.One2many(
        comodel_name="hc.care.plan.activity.action.resulting", 
        inverse_name="activity_id", 
        string="Actions Resulting", 
        help="Appointments, orders, etc.")                
    outcome_id = fields.Many2one(
        comodel_name="hc.vs.care.plan.outcome", 
        string="Outcome", 
        help="Results of the activity.")                
    progress_ids = fields.One2many(
        comodel_name="hc.care.plan.activity.progress", 
        inverse_name="activity_id", 
        string="Progress", 
        help="Comments about the activity status/progress.")                
    reference_type = fields.Selection(
        string="Reference Type", 
        selection=[
            ("Appointment", "Appointment"), 
            ("Communication Request", "Communication Request"), 
            ("Device Use Request", "Device Use Request"), 
            ("Diagnostic Request", "Diagnostic Request"), 
            ("Medication Request", "Medication Request"), 
            ("Nutrition Request", "Nutrition Request"), 
            ("Procedure Request", "Procedure Request"), 
            # ("Process Request", "Process Request"),
            ("Referral Request", "Referral Request"),
            # ("Supply Request", "Supply Request"),
            ("Vision Prescription", "Vision Prescription")], 
        help="Type of entity assessed.")                
    reference_name = fields.Char(
        string="Reference", 
        compute="_compute_reference_name", 
        store="True", 
        help="Activity details defined in specific resource.")                
    reference_appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Reference Appointment", 
        help="Appointment activity details defined in specific resource.")                
    reference_communication_request_id = fields.Many2one(
        comodel_name="hc.res.communication.request", 
        string="Reference Communication Request", 
        help="Communication Request activity details defined in specific resource.")                
    reference_device_use_request_id = fields.Many2one(
        comodel_name="hc.res.device.use.request", 
        string="Reference Device Use Request", 
        help="Device Use Request activity details defined in specific resource.")                
    reference_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Reference Diagnostic Request", 
        help="Diagnostic Request activity details defined in specific resource.")                
    reference_medication_request_id = fields.Many2one(
        comodel_name="hc.res.medication.request", 
        string="Reference Medication Request", 
        help="Medication Request activity details defined in specific resource.")                
    reference_nutrition_request_id = fields.Many2one(
        comodel_name="hc.res.nutrition.request", 
        string="Reference Nutrition Request", 
        help="Nutrition Request activity details defined in specific resource.")                
    reference_procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Reference Procedure Request", 
        help="Procedure Request activity details defined in specific resource.")                
    # reference_process_request_id = fields.Many2one(comodel_name="hc.res.process.request", string="Reference Process Request", help="Process Request activity details defined in specific resource.")                
    reference_referral_request_id = fields.Many2one(
        comodel_name="hc.res.referral.request", 
        string="Reference Referral Request", 
        help="Referral Request activity details defined in specific resource.")                
    # reference_supply_request_id = fields.Many2one(comodel_name="hc.res.supply.request", string="Reference Supply Request", help="Supply Request activity details defined in specific resource.")                
    reference_vision_prescription_id = fields.Many2one(
        comodel_name="hc.res.vision.prescription", 
        string="Reference Vision Prescription", 
        help="Vision Prescription activity details defined in specific resource.")                
    detail_ids = fields.One2many(
        comodel_name="hc.care.plan.activity.detail", 
        inverse_name="activity_id", 
        string="Details", 
        help="In-line definition of activity.")                

class CarePlanActivityDetail(models.Model):    
    _name = "hc.care.plan.activity.detail"    
    _description = "Care Plan Activity Detail"        

    activity_id = fields.Many2one(
        comodel_name="hc.care.plan.activity", 
        string="Activity", 
        help="Action to occur as part of plan.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.care.plan.activity.category", 
        string="Category", 
        required="True", 
        help="High-level categorization of the type of activity in a care plan.")                
    code_id = fields.Many2one(
        comodel_name="hc.vs.care.plan.activity", 
        string="Code", 
        help="Detail type of activity.")                
    reason_code_ids = fields.Many2many(
        comodel_name="hc.vs.care.plan.activity", 
        relation="care_plan_activity_detail_reason_code_rel", 
        string="Reason Codes", 
        help="Why activity should be done.")               
    reason_reference_ids = fields.One2many(
        comodel_name="hc.care.plan.activity.detail.reason.reference", 
        inverse_name="detail_id", 
        string="Reason References", 
        help="Condition why activity should be done.")                
    goal_ids = fields.One2many(
        comodel_name="hc.care.plan.activity.detail.goal", 
        inverse_name="detail_id", 
        string="Goals", 
        help="Goals this activity relates to.")                
    status = fields.Selection(
        string="Detail Status", 
        selection=[
            ("not-started", "Not-Started"), 
            ("scheduled", "Scheduled"), 
            ("in-progress", "In-Progress"), 
            ("on-hold", "On-Hold"), 
            ("completed", "Completed"), 
            ("cancelled", "Cancelled")], 
        help="Identifies what progress is being made for the specific activity.")                
    status_reason_id = fields.Many2one(
        comodel_name="hc.vs.goal.status.reason", 
        string="Status Reason", 
        help="Reason for current status.")                
    is_prohibited = fields.Boolean(
        string="Prohibited", 
        required="True", 
        help="Do NOT do.")                
    scheduled_type = fields.Selection(
        string="Scheduled Type", 
        selection=[
            ("Timing", "Timing"), 
            ("Period", "Period"), 
            ("string", "String")], 
        help="Type of entity assessed.")                
    scheduled_name = fields.Char(
        string="Scheduled", 
        compute="_compute_scheduled_name", 
        store="True", 
        help="When activity is to occur.")                
    scheduled_timing_id = fields.Many2one(
        comodel_name="hc.care.plan.activity.detail.scheduled.timing", 
        string="Scheduled Timing", 
        help="Timing when activity is to occur.")                
    scheduled_start_date = fields.Datetime(
        string="Scheduled Start Date", 
        help="Start of the when activity is to occur.")                
    scheduled_end_date = fields.Datetime(
        string="Scheduled End Date", 
        help="End of the when activity is to occur.")                
    scheduled_string = fields.Char(
        string="Scheduled", 
        help="String of when activity is to occur.")                
    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location", 
        help="Where it should happen.")                
    performer_ids = fields.One2many(
        comodel_name="hc.care.plan.activity.detail.performer", 
        inverse_name="detail_id", 
        string="Performers", 
        help="Who will be responsible?")                
    product_type = fields.Selection(
        string="Product Type", 
        selection=[
            ("Code", "Code"), 
            ("Medication", "Medication"), 
            ("Substance", "Substance")], 
        help="Type of what is to be administered/supplied.")
    product_name = fields.Char(
        string="Product", 
        compute="_compute_product_name", 
        store="True", 
        help="What is to be administered/supplied.")
    product_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.code", 
        string="Product Code", 
        help="What is to be administered/supplied.")
    product_medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Product Medication", 
        help="Medication what is to be administered/supplied.")           
    product_substance_id = fields.Many2one(
        comodel_name="hc.res.substance", 
        string="Product Substance", 
        help="Substance what is to be administered/supplied.")                
    daily_amount = fields.Float(
        string="Daily Amount", 
        help="How to consume/day?")                
    daily_amount_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Daily Amount UOM", 
        help="Daily amount unit of measure.")                
    quantity = fields.Float(
        string="Quantity", 
        help="How much to administer/supply/consume.")                
    quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Quantity UOM", 
        help="Quantity unit of measure.")                
    description = fields.Text(
        string="Description", 
        help="Extra info describing activity to perform.")                

class CarePlanActivityActionResulting(models.Model):    
    _name = "hc.care.plan.activity.action.resulting"    
    _description = "Care Plan Activity Action Resulting"        
    _inherit = ["hc.basic.association"]

    activity_id = fields.Many2one(
        comodel_name="hc.care.plan.activity", 
        string="Activity", 
        help="Action to occur as part of plan.")                
    action_resulting_type = fields.Selection(
        string="Action Resulting Type", 
        selection=[
            ("Appointment", "Appointment"), 
            ("Communication Request", "Communication Request"), 
            ("Device Use Request", "Device Use Request"), 
            ("Diagnostic Request", "Diagnostic Request"), 
            ("Medication Request", "Medication Request"), 
            ("Nutrition Request", "Nutrition Request"), 
            ("Procedure Request", "Procedure Request"), 
            # ("Process Request", "Process Request"),
            ("Referral Request", "Referral Request"),
            # ("Supply Request", "Supply Request"),
            ("Vision Prescription", "Vision Prescription")], 
        help="Type of resource that describes follow-on actions resulting from the plan.")                
    action_resulting_name = fields.Char(
        string="Action Resulting", 
        compute="_compute_action_resulting_name", 
        store="True", 
        help="Resource that describes follow-on actions resulting from the plan.")                
    action_resulting_appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Action Resulting Appointment", 
        help="Resource that describes follow-on actions resulting from the plan.")
    action_resulting_communication_request_id = fields.Many2one(
        comodel_name="hc.res.communication.request", 
        string="Action Resulting Communication Request", 
        help="Communication Request resource that describes follow-on actions resulting from the plan.")
    action_resulting_device_use_request_id = fields.Many2one(
        comodel_name="hc.res.device.use.request", 
        string="Action Resulting Device Use Request", 
        help="Device Use Request resource that describes follow-on actions resulting from the plan.")
    action_resulting_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Action Resulting Diagnostic Request", 
        help="Diagnostic Request resource that describes follow-on actions resulting from the plan.")
    action_resulting_medication_request_id = fields.Many2one(
        comodel_name="hc.res.medication.request", 
        string="Action Resulting Medication Request", 
        help="Medication Request resource that describes follow-on actions resulting from the plan.")
    action_resulting_nutrition_request_id = fields.Many2one(
        comodel_name="hc.res.nutrition.request", 
        string="Action Resulting Nutrition Request", 
        help="Nutrition Request resource that describes follow-on actions resulting from the plan.")
    action_resulting_procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Action Resulting Procedure Request", 
        help="Procedure Request resource that describes follow-on actions resulting from the plan.")
    # action_resulting_process_request_id = fields.Many2one(comodel_name="hc.res.process.request", string="Action Resulting Process Request", help="Process Request resource that describes follow-on actions resulting from the plan.")
    action_resulting_referral_request_id = fields.Many2one(
        comodel_name="hc.res.referral.request", 
        string="Action Resulting Referral Request", 
        help="Referral Request resource that describes follow-on actions resulting from the plan.")
    # action_resulting_supply_request_id = fields.Many2one(comodel_name="hc.res.supply.request", string="Action Resulting Supply Request", help="Supply Request resource that describes follow-on actions resulting from the plan.")
    action_resulting_vision_prescription_id = fields.Many2one(
        comodel_name="hc.res.vision.prescription", 
        string="Action Resulting Vision Prescription", 
        help="Vision Prescription resource that describes follow-on actions resulting from the plan.")

class CarePlanActivityDetailGoal(models.Model):    
    _name = "hc.care.plan.activity.detail.goal"    
    _description = "Care Plan Activity Detail Goal"        
    _inherit = ["hc.basic.association"]

    detail_id = fields.Many2one(
        comodel_name="hc.care.plan.activity.detail", 
        string="Detail", 
        help="In-line definition of activity.")                
    goal_id = fields.Many2one(
        comodel_name="hc.res.goal", 
        string="Goal", 
        help="Goals this activity relates to.")                

class CarePlanActivityDetailPerformer(models.Model):    
    _name = "hc.care.plan.activity.detail.performer"    
    _description = "Care Plan Activity Detail Performer"        
    _inherit = ["hc.basic.association"]

    detail_id = fields.Many2one(
        comodel_name="hc.care.plan.activity.detail", 
        string="Detail", 
        help="In-line definition of activity.")                
    performer_type = fields.Selection(
        string="Performer Type", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Organization", "Organization"), 
            ("Related Person", "Related Person"), 
            ("Patient", "Patient")], 
        help="Type of entity assessed.")                
    performer_name = fields.Char(
        string="Performer", 
        compute="_compute_performer_name", 
        store="True", 
        help="Who will be responsible?")                
    performer_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Performer Practitioner", 
        help="Practitioner who will be responsible?")                
    performer_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Performer Organization", 
        help="Organization who will be responsible?")                
    performer_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Performer Related Person", 
        help="Related Person who will be responsible?")                
    performer_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Performer Patient", 
        help="Patient who will be responsible?")                           

class CarePlanActivityDetailReasonReference(models.Model):    
    _name = "hc.care.plan.activity.detail.reason.reference"    
    _description = "Care Plan Activity Detail Reason Reference"        
    _inherit = ["hc.basic.association"]

    detail_id = fields.Many2one(
        comodel_name="hc.care.plan.activity.detail", 
        string="Detail", 
        help="Detail associated with this Care Plan Activity Detail Reason Reference.")                
    reason_reference_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Reason Reference", 
        help="Reason Reference associated with this Care Plan Activity Detail Reason Reference.")                

class CarePlanActivityDetailScheduledTiming(models.Model):    
    _name = "hc.care.plan.activity.detail.scheduled.timing"    
    _description = "Care Plan Activity Detail Scheduled Timing"        
    _inherit = ["hc.basic.association", "hc.timing"]

class CarePlanActivityProgress(models.Model):    
    _name = "hc.care.plan.activity.progress"    
    _description = "Care Plan Activity Progress"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    activity_id = fields.Many2one(
        comodel_name="hc.care.plan.activity", 
        string="Detail", 
        help="Detail associated with this Care Plan Activity Progress.")                

class CarePlanAddresses(models.Model):    
    _name = "hc.care.plan.addresses"    
    _description = "Care Plan Addresses"        
    _inherit = ["hc.basic.association"]

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this Care Plan Addresses.")                
    addresses_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Addresses", 
        help="Condition associated with this Care Plan Addresses.")                

class CarePlanAuthor(models.Model):    
    _name = "hc.care.plan.author"    
    _description = "Care Plan Author"        
    _inherit = ["hc.basic.association"]

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this Care Plan Author.")                
    author_type = fields.Selection(
        string="Author Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Practitioner", "Practitioner"), 
            ("Related Person", "Related Person"), 
            ("Organization", "Organization")], 
        help="Type of entity assessed.")                
    author_name = fields.Char(
        string="Author", 
        compute="_compute_author_name", 
        store="True", 
        help="Who is responsible for plan.")                
    author_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Author Patient", 
        help="Patient who is responsible for plan.")                
    author_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author Practitioner", 
        help="Practitioner who is responsible for plan.")                
    author_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Author Related Person", 
        help="Related Person who is responsible for plan.")                
    author_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Author Organization", 
        help="Organization who is responsible for plan.")                          

class CarePlanCareTeam(models.Model):    
    _name = "hc.care.plan.care.team"    
    _description = "Care Plan Care Team"        
    _inherit = ["hc.basic.association"]

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this Care Plan Care Team.")                
    care_team_id = fields.Many2one(
        comodel_name="hc.res.care.team", 
        string="Care Team", 
        help="Care Team associated with this Care Plan Care Team.")                

class CarePlanGoal(models.Model):    
    _name = "hc.care.plan.goal"    
    _description = "Care Plan Goal"        
    _inherit = ["hc.basic.association"]

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this Care Plan Goal.")                
    goal_id = fields.Many2one(
        comodel_name="hc.res.goal", 
        string="Goal", 
        help="Goal associated with this Care Plan Goal.")                

class CarePlanIdentifier(models.Model):    
    _name = "hc.care.plan.identifier"    
    _description = "Care Plan Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this Care Plan Identifier.")                

class CarePlanNote(models.Model):    
    _name = "hc.care.plan.note"    
    _description = "Care Plan Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

class CarePlanSupport(models.Model):    
    _name = "hc.care.plan.support"    
    _description = "Care Plan Support"        
    _inherit = ["hc.basic.association"]

    care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Care Plan", 
        help="Care Plan associated with this Care Plan Support.")                
    support_type = fields.Selection(
        string="Support Type", 
        selection=[
            ("string", "String"), 
            ("Care Plan", "Care Plan")], 
        help="Type of Information considered as part of plan.")
    support_name = fields.Char(
        string="Support", 
        compute="_compute_support_name", 
        store="True", 
        help="Information considered as part of plan.")                
    support_string = fields.Char(
        string="Support String", 
        help="String information considered as part of plan.")                
    support_care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Support Care Plan", 
        help="Care Plan information considered as part of plan.")                

class CarePlanActivity(models.Model):    
    _name = "hc.vs.care.plan.activity"    
    _description = "Care Plan Activity"        
    _inherit = ["hc.value.set.contains"]

class CarePlanActivityCategory(models.Model):    
    _name = "hc.vs.care.plan.activity.category"    
    _description = "Care Plan Activity Category"        
    _inherit = ["hc.value.set.contains"]

class CarePlanCategory(models.Model):    
    _name = "hc.vs.care.plan.category"    
    _description = "Care Plan Category"        
    _inherit = ["hc.value.set.contains"]

class CarePlanOutcome(models.Model):    
    _name = "hc.vs.care.plan.outcome"    
    _description = "Care Plan Outcome"        
    _inherit = ["hc.value.set.contains"]

# External Reference

class ReferralRequestBasedOn(models.Model):    
    _inherit = "hc.referral.request.based.on"  

    based_on_type = fields.Selection(
        string="Based On Type", 
        selection=[
            ("Referral Request", "Referral Request"), 
            ("Care Plan", "Care Plan"), 
            ("Diagnostic Order", "Diagnostic Order"), 
            ("Procedure Request", "Procedure Request")], 
        help="Type of request fulfilled by this request.")
    based_on_care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Based On Care Plan", 
        help="Care Plan request fulfilled by this request.") 

class MedicationRequestBasedOn(models.Model):   
    _inherit= "hc.medication.request.based.on"

    based_on_type = fields.Selection(
        string="Based On Type", 
        selection=[
            ("Care Plan", "Care Plan"), 
            ("Diagnostic Request", "Diagnostic Request"), 
            ("Medication Request", "Medication Request"), 
            ("Procedure Request", "Procedure Request"), 
            ("Referral Request", "Referral Request")], 
        help="Type of what request fulfills.")                   
    based_on_care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Based On Care Plan", 
        help="Care Plan request fulfills.")