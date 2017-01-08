# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Goal(models.Model):    
    _name = "hc.res.goal"    
    _description = "Goal"        

    identifier_ids = fields.One2many(
        comodel_name="hc.goal.identifier", 
        inverse_name="goal_id", 
        string="Identifiers", 
        help="External IDs for this goal.")                
    status = fields.Selection(
        string="Goal Status", 
        required="True", 
        selection=[
            ("proposed", "Proposed"), 
            ("planned", "Planned"), 
            ("accepted", "Accepted"), 
            ("rejected", "Rejected"), 
            ("in-progress", "In Progress"), 
            ("achieved", "Achieved"), 
            ("sustaining", "Sustaining"), 
            ("on-hold", "On Hold"), 
            ("cancelled", "Cancelled"), 
            ("on-target", "On Target"), 
            ("ahead-of-target", "Ahead Of Target"), 
            ("behind-target", "Behind-Target")],
        help="Indicates whether the goal has been reached and is still considered relevant.")
    category_ids = fields.Many2many(
        comodel_name="hc.vs.goal.category", 
        relation="goal_category_rel", 
        string="Categories", 
        help="E.g. Treatment, dietary, behavioral, etc.")               
    priority = fields.Selection(
        string="Goal Priority", 
        selection=[
            ("high", "High"), 
            ("medium", "Medium"), 
            ("low", "Low")], 
        help="Identifies the mutually agreed level of importance associated with reaching/sustaining the goal.")
    description_id = fields.Many2one(
        comodel_name="hc.vs.goal.description", 
        string="Description", 
        required="True", 
        help="Code or text describing goal.")
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("patient", "Patient"), 
            ("group", "Group"), 
            ("organization", "Organization")], 
        help="Type of who this goal is intended for.")                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Who this goal is intended for.")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient who this goal is intended for.")                
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group who this goal is intended for.")                
    subject_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Subject Organization", 
        help="Organization who this goal is intended for.")                
    start_type = fields.Selection(
        string="Start Type", 
        selection=[
            ("date", "Date"), 
            ("code", "Code")], 
        help="Type of when goal pursuit begins.")                
    start_name = fields.Char(
        string="Start", 
        compute="_compute_start_name", 
        store="True", 
        help="When goal pursuit begins.")                
    start_date = fields.Date(
        string="Start Date", 
        help="When goal pursuit begins.")                
    start_code_id = fields.Many2one(
        comodel_name="hc.vs.goal.start.event", 
        string="Start Code", 
        help="Code of when goal pursuit begins.")                
    target_type = fields.Selection(
        string="Target Type", 
        selection=[
            ("date", "Date"), 
            ("duration", "Duration")], 
        help="Type of reach goal on or before.")                
    target_name = fields.Char(
        string="Target", 
        compute="_compute_target_name", 
        store="True", 
        help="Reach goal on or before.")                
    target_date = fields.Date(
        string="Target Date", 
        help="Reach goal on or before.")                
    target_duration = fields.Float(
        string="Target Duration", 
        help="Duration reach goal on or before.")
    target_duration_uom_id = fields.Many2one(
        comodel_name="hc.vs.time.uom", 
        string="Target Duration UOM", 
        help="Target Duration unit of measure." )            
    # target_duration_uom = fields.Selection(
    #     string="Target Duration UOM", 
    #     selection=[
    #         ("s", "S"), 
    #         ("min", "Min"), 
    #         ("h", "H"), 
    #         ("d", "D"), 
    #         ("wk", "Wk"), 
    #         ("mo", "Mo"), 
    #         ("a", "A")], 
    #     help="Reach goal on or before unit of measure.")                                 
    status_date = fields.Date(
        string="Status Date", 
        help="When goal status took effect.")                
    status_reason_ids = fields.Many2many(
        comodel_name="hc.vs.goal.status.reason", 
        relation="goal_status_reason_rel", 
        string="Categories", 
        help="Reason for current status.")                
    expressed_by_type = fields.Selection(
        string="Expressed By Type", 
        selection=[
            ("patient", "Patient"), 
            ("practitioner", "Practitioner"), 
            ("related_person", "Related Person")], 
        help="Type of who is responsible for creating goal.")                
    expressed_by_name = fields.Char(
        string="Expressed By", 
        compute="_compute_expressed_by_name", 
        store="True", 
        help="Who's responsible for creating Goal?")                
    expressed_by_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Expressed By Patient", 
        help="Patient who's responsible for creating goal?")                
    expressed_by_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Expressed By Practitioner", 
        help="Practitioner who's responsible for creating goal?")                
    expressed_by_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Expressed By Related Person", 
        help="Related Person who's responsible for creating goal?")                                
    addresses_ids = fields.One2many(
        comodel_name="hc.goal.addresses", 
        inverse_name="goal_id", 
        string="Addressess", 
        help="Issues addressed by this goal.")                
    note_ids = fields.One2many(
        comodel_name="hc.goal.note", 
        inverse_name="goal_id", 
        string="Notes", 
        help="Comments about the goal.")                
    outcome_ids = fields.One2many(
        comodel_name="hc.goal.outcome", 
        inverse_name="goal_id", 
        string="Outcomes", 
        help="What was end result of goal?")                

class GoalOutcome(models.Model):    
    _name = "hc.goal.outcome"    
    _description = "Goal Outcome"        

    goal_id = fields.Many2one(
        comodel_name="hc.res.goal", 
        string="Goal", 
        help="Goal associated with this Goal Outcome.")                
    result_type = fields.Selection(
        string="Result Type", 
        selection=[
            ("code", "Code"), 
            ("observation", "Observation")], 
        help="Type of reach goal on or before.")                
    result_name = fields.Char(
        string="Result", 
        compute="_compute_result_name", 
        store="True", 
        help="Code or observation that resulted from goal.")                
    result_code_id = fields.Many2one(
        comodel_name="hc.vs.goal.outcome.result", 
        string="Result Code", 
        help="Code that resulted from goal.")                
    result_observation_id = fields.Many2one(
        comodel_name="hc.res.observation", 
        string="Result Observation", 
        help="Observation that resulted from goal.")                

class GoalAddresses(models.Model):    
    _name = "hc.goal.addresses"    
    _description = "Goal Addresses"        
    _inherit = ["hc.basic.association"]

    goal_id = fields.Many2one(
        comodel_name="hc.res.goal", 
        string="Goal", 
        help="Goal associated with this Goal Addresses.")                
    addresses_type = fields.Selection(
        string="Addresses Type", 
        selection=[
            ("Condition", "Condition"), 
            ("Observation", "Observation"),
            ("Medication Statement", "Medication Statement"), 
            ("Nutrition Request", "Nutrition Request"),
            ("Procedure Request", "Procedure Request"), 
            ("Risk Assessment", "Risk Assessment")],
        help="Type of issues addressed by this goal.")                
    addresses_name = fields.Char(
        string="Addresses", 
        compute="_compute_addresses_name", 
        store="True", 
        help="Issues addressed by this goal.")                
    addresses_condition_ids = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Addresses Conditions", 
        help="Condition issues addressed by this goal.")                
    addresses_observation_ids = fields.Many2one(
        comodel_name="hc.res.observation", 
        string="Addresses Observations", 
        help="Observation issues addressed by this goal.")                
    addresses_medication_statement_ids = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Addresses Medication Statements", 
        help="Medication Statement issues addressed by this goal.")                
    addresses_nutrition_request_ids = fields.Many2one(
        comodel_name="hc.res.nutrition.request", 
        string="Addresses Nutrition Requests", 
        help="Nutrition Request issues addressed by this goal.")                
    addresses_procedure_request_ids = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Addresses Procedure Requests", 
        help="Procedure Request issues addressed by this goal.")                
    addresses_risk_assessment_ids = fields.Many2one(
        comodel_name="hc.res.risk.assessment", 
        string="Addresses Risk Assessments", 
        help="Risk Assessment issues addressed by this goal.")                            

class GoalIdentifier(models.Model):    
    _name = "hc.goal.identifier"    
    _description = "Goal Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    goal_id = fields.Many2one(
        comodel_name="hc.res.goal", 
        string="Goal", 
        help="Goal associated with this Goal Identifier.")                

class GoalNote(models.Model):    
    _name = "hc.goal.note"    
    _description = "Goal Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    goal_id = fields.Many2one(
        comodel_name="hc.res.goal", 
        string="Goal", 
        help="Goal associated with this Goal Note.")                               

class GoalDescription(models.Model):    
    _name = "hc.vs.goal.description"    
    _description = "Goal Description"        
    _inherit = ["hc.value.set.contains"]

class GoalOutcomeResult(models.Model):    
    _name = "hc.vs.goal.outcome.result"    
    _description = "Goal Outcome Result"        
    _inherit = ["hc.value.set.contains"]

class GoalStartEvent(models.Model):    
    _name = "hc.vs.goal.start.event"    
    _description = "Goal Start Event"        
    _inherit = ["hc.value.set.contains"]

class GoalCategory(models.Model):    
    _name = "hc.vs.goal.category"    
    _description = "Goal Category"        
    _inherit = ["hc.value.set.contains"]

class GoalStatusReason(models.Model):    
    _name = "hc.vs.goal.status.reason"    
    _description = "Goal Status Reason"        
    _inherit = ["hc.value.set.contains"]
