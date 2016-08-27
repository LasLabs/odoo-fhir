# -*- coding: utf-8 -*-

from openerp import models, fields, api

class EpisodeOfCare(models.Model):    
    _name = "hc.res.episode.of.care"    
    _description = "Episode Of Care"        

    identifier_ids = fields.One2many(comodel_name="hc.episode.of.care.identifier", inverse_name="episode_of_care_id", string="Identifiers", help="Identifier(s) by which this Episode Of are is known.")                
    status = fields.Selection(string="Episode Of Care Status", required="True", selection=[("planned", "Planned"), ("waitlist", "Waitlist"), ("active", "Active"), ("onhold", "Onhold"), ("finished", "Finished"), ("cancelled", "Cancelled")], help="The status of the episode of care.")                
    type_ids = fields.One2many(comodel_name="hc.episode.of.care.type", inverse_name="episode_of_care_id", string="Types", help="Specific type of Episode Of Care.")                
    patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", required="True", help="The patient that this Episode Of Care applies to.")                
    managing_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Managing Organization", help="The organization that has assumed the specific responsibilities for the specified duration.")                
    start_date = fields.Datetime(string="Start Date", help="Start of the the interval during which the managing organization assumes the defined responsibility.")                
    end_date = fields.Datetime(string="End Date", help="End of the the interval during which the managing organization assumes the defined responsibility.")                
    condition_ids = fields.One2many(comodel_name="hc.episode.of.care.condition", inverse_name="episode_of_care_id", string="Conditions", help="A list of conditions/problems/diagnoses that this episode of care is intended to be providing care for.")                
    referral_request_ids = fields.One2many(comodel_name="hc.episode.of.care.referral.request", inverse_name="episode_of_care_id", string="Referral Requests", help="Referral Request(s) that this Episode Of are manages activities within.")                
    care_manager_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Care Manager", help="The practitioner that is the care manager/care co-ordinator for this patient.")                
    status_history_ids = fields.One2many(comodel_name="hc.episode.of.care.status.history", inverse_name="episode_of_care_id", string="Status History", help="status history for the Episode Of Care.")                
    care_team_ids = fields.One2many(comodel_name="hc.episode.of.care.care.team", inverse_name="episode_of_care_id", string="Care Teams", help="list of practitioners that may be facilitating this episode of care for specific purposes.")                

class EpisodeOfCareStatusHistory(models.Model):    
    _name = "hc.episode.of.care.status.history"    
    _description = "Episode Of Care Status History"        

    episode_of_care_id = fields.Many2one(comodel_name="hc.res.episode.of.care", string="Episode Of Care", required="True", help="Episode of care associated with this status history.")                
    status = fields.Selection(string="Status History Status", required="True", selection=[("planned", "Planned"), ("waitlist", "Waitlist"), ("active", "Active"), ("onhold", "Onhold"), ("finished", "Finished"), ("cancelled", "Cancelled")], help="The status of the episode of care.")                
    start_date = fields.Datetime(string="Start Date", required="True", help="Start of the the period during this Episode Of Care that the specific status applied.")                
    end_date = fields.Datetime(string="End Date", required="True", help="End of the the period during this Episode Of Care that the specific status applied.")                

class EpisodeOfCareCareTeam(models.Model):    
    _name = "hc.episode.of.care.care.team"    
    _description = "Episode Of Care Care Team"        

    episode_of_care_id = fields.Many2one(comodel_name="hc.res.episode.of.care", string="Episode Of Care", required="True", help="Episode of care associated with this care team.")                
    member_type = fields.Selection(string="Member Type", required="True", selection=[("practitioner", "Practitioner"), ("organization", "Organization")], help="Type of practitioner (or Organization) within the team.")                
    member_name = fields.Char(string="Member", compute="compute_member_name", help="The practitioner (or Organization) within the tea.")                
    member_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Member Practitioner", help="Practitioner the practitioner (or organization) within the team.")                
    member_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Member Organization", help="Organization the practitioner (or organization) within the team.")                
    role_ids = fields.One2many(comodel_name="hc.episode.of.care.care.team.role", inverse_name="participant_role_id", string="Roles", help="The role that this team member is taking within this episode of care.")                
    start_date = fields.Datetime(string="Start Date", help="Start of the the period of time that this practitioner is performing some role within the episode of care.")                
    end_date = fields.Datetime(string="End Date", help="End of the the period of time that this practitioner is performing some role within the episode of care.")                

class EpisodeOfCareIdentifier(models.Model):    
    _name = "hc.episode.of.care.identifier"    
    _description = "Episode Of Care Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    episode_of_care_id = fields.Many2one(comodel_name="hc.res.episode.of.care", string="Episode Of Care", required="True", help="Episode of care associated with this episode of care identifier.")                

class EpisodeOfCareCondition(models.Model):    
    _name = "hc.episode.of.care.condition"    
    _description = "Episode Of Care Condition"        
    _inherit = ["hc.basic.association"]

    episode_of_care_id = fields.Many2one(comodel_name="hc.res.episode.of.care", string="Episode Of Care", required="True", help="Episode of care associated with this episode of care condition.")                
    # condition_id = fields.Many2one(
    #     comodel_name="hc.res.condition", 
    #     string="Condition", 
    #     help="Condition associated with this episode of care condition.")                

class EpisodeOfCareReferralRequest(models.Model):    
    _name = "hc.episode.of.care.referral.request"    
    _description = "Episode Of Care Referral Request"        
    _inherit = ["hc.basic.association"]

    episode_of_care_id = fields.Many2one(comodel_name="hc.res.episode.of.care", string="Episode Of Care", required="True", help="Episode of care associated with this episode of care referral request.")                
    # referral_request_id = fields.Many2one(
    #     comodel_name="hc.res.referral.request", 
    #     string="Referral Request", 
    #     required="True", 
    #     help="Referral request associated with this episode of care referral request.")                

class EpisodeOfCareType(models.Model):    
    _name = "hc.episode.of.care.type"    
    _description = "Episode Of Care Type"        
    _inherit = ["hc.basic.association"]

    episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Episode Of Care", 
        required="True", 
        help="Episode of care associated with this episode of care type.")                
    episode_of_care_type_id = fields.Many2one(
        comodel_name="hc.vs.episode.of.care.type", 
        string="Episode Of Care Type", 
        required="True", 
        help="Episode Of care type associated with this episode of care.")                

class EpisodeOfCareCareTeamRole(models.Model):    
    _name = "hc.episode.of.care.care.team.role"    
    _description = "Episode Of Care Care Team Role"        
    _inherit = ["hc.basic.association"]

    episode_of_care_care_team_id = fields.Many2one(
        comodel_name="hc.episode.of.care.care.team", 
        string="Episode Of Care", 
        required="True", 
        help="Care Team member associated with this care team role.")                
    participant_role_id = fields.Many2one(
        comodel_name="hc.vs.participant.role", 
        string="Participant Role", 
        required="True", 
        help="Participant role associated with this care team member.")                

class EpisodeOfCareType(models.Model):    
    _name = "hc.vs.episode.of.care.type"    
    _description = "Episode Of Care Type"        
    _inherit = ["hc.value.set.contains"]

# External Reference

# class Condition(models.Model):
#     _inherit = ["res.condition"]

#     context_episode_of_care_id = fields.Many2one(
#         comodel_name="hc.res.episode.of.care", 
#         string="Context Episode Of Care", 
#         help="Episode Of Care when condition first asserted.")