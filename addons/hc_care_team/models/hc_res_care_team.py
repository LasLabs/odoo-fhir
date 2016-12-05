# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CareTeam(models.Model):    
    _name = "hc.res.care.team"    
    _description = "Care Team"        

    identifier_ids = fields.One2many(
        comodel_name="hc.care.team.identifier", 
        inverse_name="care_team_id", 
        string="Identifiers", 
        help="External Ids for this team.")                
    status = fields.Selection(
        string="Status", 
        selection=[
            ("active", "Active"), 
            ("suspended", "Suspended"), 
            ("inactive", "Inactive"), 
            ("entered in error", "Entered In Error")], 
        help="Indicates whether the care team is currently active, suspended, inactive, or entered in error.")                
    type_ids = fields.Many2many(
        comodel_name="hc.vs.participant.type", 
        relation="care_team_content_type_rel", 
        string="Categories", 
        help="Identifies what kind of team.")                
    name = fields.Char(
        string="Name", 
        help="Name of the team, such as crisis assessment team.")                
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group")], 
        help="Type of who care team is for.")                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Who care team is for.")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient who care team is for.")
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group who care team is for.")                
    managing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Managing Organization", 
        help="Organization responsible for the care team.")                
    participant_ids = fields.One2many(
        comodel_name="hc.care.team.participant", 
        inverse_name="care_team_id", 
        string="Participants", 
        help="Members of the team.")                

class CareTeamParticipant(models.Model):    
    _name = "hc.care.team.participant"    
    _description = "Care Team Participant"        

    care_team_id = fields.Many2one(
        comodel_name="hc.res.care.team", 
        string="Care Team", 
        help="Care Team associated with this participant.")                
    role_id = fields.Many2one(
        comodel_name="hc.vs.participant.role", 
        string="Role", 
        help='Indicates specific responsibility of an individual within the care team, such as "Primary physician", "Team coordinator", "Caregiver", etc.')                
    member_type = fields.Selection(
        string="Member Type", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Related Person", "Related Person"), 
            ("Patient", "Patient"), 
            ("Organization", "Organization")], 
        help="Type of who is involved.")                
    member_name = fields.Char(
        string="Member", 
        compute="_compute_member_name", 
        store="True", 
        help="Who is involved.")                
    member_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Member Practitioner", 
        help="Practitioner who is involved.")                
    member_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Member Related Person", 
        help="Related Person who is involved.")                
    member_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Member Patient", 
        help="Patient who is involved.")                
    member_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Member Organization", 
        help="Organization who is involved.")                
    period_start_date = fields.Datetime(
        string="Period Start Date", 
        help="Start of the time period of participant.")                
    period_end_date = fields.Datetime(
        string="Period End Date", 
        help="End of the time period of participant.")                

class CareTeamIdentifier(models.Model):    
    _name = "hc.care.team.identifier"    
    _description = "Care Team Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    care_team_id = fields.Many2one(
        comodel_name="hc.res.care.team", 
        string="Care Team", 
        help="Care Team associated with this Care Team Identifier.")                           

class ParticipantRole(models.Model):    
    _name = "hc.vs.participant.role"    
    _description = "Participant Role"        
    _inherit = ["hc.value.set.contains"]

class ParticipantType(models.Model):    
    _name = "hc.vs.participant.type"    
    _description = "Participant Type"        
    _inherit = ["hc.value.set.contains"]
