# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ResearchStudy(models.Model):    
    _name = "hc.res.research.study"    
    _description = "Research Study"
    _rec_name = "title"

    identifier_id = fields.Many2one(
        comodel_name="hc.research.study.identifier", 
        string="Identifier", 
        help="Business Identifer for study.")        
    title = fields.Char(
        string="Title", 
        help="Name for this study.")        
    protocol_ids = fields.One2many(
        comodel_name="hc.research.study.protocol", 
        inverse_name="research_study_id", 
        string="Protocols", 
        help="Steps followed in executing study.")        
    part_of_ids = fields.One2many(
        comodel_name="hc.research.study.part.of", 
        inverse_name="research_study_id", 
        string="Part Ofs", 
        help="Part of larger study.")        
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("in-progress", "In-Progress"), 
            ("suspended", "Suspended"), 
            ("stopped", "Stopped"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered In Error")], 
        help="The current state of the study.")        
    category_ids = fields.Many2many(
        comodel_name="hc.vs.research.study.category", 
        relation="research_study_category_rel", 
        string="Categories", 
        help="Codes categorizing the type of study such as investigational vs. observational, type of blinding, type of randomization, safety vs. efficacy, etc.")        
    focus_ids = fields.Many2many(
        comodel_name="hc.vs.research.study.focus", 
        relation="research_study_focus_rel", 
        string="Focuses", 
        help="Drugs, devices, conditions, etc. under study.")        
    contact_ids = fields.One2many(
        comodel_name="hc.research.study.contact", 
        inverse_name="research_study_id", 
        string="Contacts", 
        help="Contact details for the study.")        
    related_artifact_ids = fields.One2many(
        comodel_name="hc.research.study.related.artifact", 
        inverse_name="research_study_id", 
        string="Related Artifacts", 
        help="References and dependencies.")        
    keyword_ids = fields.Many2many(
        comodel_name="hc.vs.research.study.keyword", 
        relation="research_study_keyword_rel", 
        string="Keywords", 
        help="Used to search for the study.")        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="research_study_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Geographic region(s) for study.")        
    description = fields.Text(
        string="Description", 
        help="What this is study doing.")        
    enrollment_ids = fields.One2many(
        comodel_name="hc.research.study.enrollment", 
        inverse_name="research_study_id", 
        string="Enrollments", 
        help="Inclusion & exclusion criteria.")        
    period_start_date = fields.Datetime(
        string="Period Start Date", 
        help="When the study began.")        
    period_end_date = fields.Datetime(
        string="Period End Date", 
        help="When the study ended.")        
    sponsor_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Sponsor", 
        help="Organization responsible for the study.")        
    principle_investigator_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Principle Investigator", 
        help="Individual responsible for the study.")        
    site_ids = fields.One2many(
        comodel_name="hc.research.study.site", 
        inverse_name="research_study_id", 
        string="Sites", 
        help="Location involved in study execution.")        
    reason_stopped_id = fields.Many2one(
        comodel_name="hc.vs.research.study.reason.stopped", 
        string="Reason Stopped", 
        help="Reason for terminating study early.")        
    note_ids = fields.One2many(
        comodel_name="hc.research.study.note", 
        inverse_name="research_study_id", 
        string="Notes", 
        help="Comments made about the event.")        
    arm_ids = fields.One2many(
        comodel_name="hc.research.study.arm", 
        inverse_name="research_study_id", 
        string="Arm", 
        help="Defined path through the study for a subject.")        

class ResearchStudyArm(models.Model):    
    _name = "hc.research.study.arm"    
    _description = "Research Study Arm"        

    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Arm.")
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Label for study arm.")
    code_id = fields.Many2one(
        comodel_name="hc.vs.research.study.arm.category", 
        string="Code", 
        help="Categorization of arm. E.g. Experimental, active comparator, placebo comparator.")
    description = fields.Text(
        string="Description", 
        help="Short explanation of study path.")

class ResearchStudyIdentifier(models.Model):    
    _name = "hc.research.study.identifier"    
    _description = "Research Study Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class ResearchStudyProtocol(models.Model):    
    _name = "hc.research.study.protocol"    
    _description = "Research Study Protocol"        
    _inherit = ["hc.basic.association"]

    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Protocol.")
    protocol_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Protocol", 
        help="Steps followed in executing study.")

class ResearchStudyPartOf(models.Model):    
    _name = "hc.research.study.part.of"    
    _description = "Research Study Part Of"        
    _inherit = ["hc.basic.association"]

    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Part Of.")
    part_of_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Part Of", 
        help="Part of larger study.")

class ResearchStudyContact(models.Model):    
    _name = "hc.research.study.contact"    
    _description = "Research Study Contact"        
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Research Study Contact.")
    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Contact.")

class ResearchStudyRelatedArtifact(models.Model):    
    _name = "hc.research.study.related.artifact"    
    _description = "Research Study Related Artifact"        
    _inherit = ["hc.basic.association", "hc.related.artifact"]

    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Related Artifact.")

class ResearchStudyEnrollment(models.Model):    
    _name = "hc.research.study.enrollment"    
    _description = "Research Study Enrollment"        
    _inherit = ["hc.basic.association"]

    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Enrollment.")
    enrollment_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Enrollment", 
        help="Inclusion & exclusion criteria.")

class ResearchStudySite(models.Model):    
    _name = "hc.research.study.site"    
    _description = "Research Study Site"        
    _inherit = ["hc.basic.association"]

    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Site.")
    site_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Site", 
        help="Location involved in study execution.")

class ResearchStudyNote(models.Model):    
    _name = "hc.research.study.note"    
    _description = "Research Study Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    research_study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Research Study", 
        help="Research Study associated with this Research Study Note.")

class ResearchStudyCategory(models.Model):    
    _name = "hc.vs.research.study.category"    
    _description = "Research Study Category"        
    _inherit = ["hc.value.set.contains"]

class ResearchStudyFocus(models.Model):    
    _name = "hc.vs.research.study.focus"    
    _description = "Research Study Focus"        
    _inherit = ["hc.value.set.contains"]

class ResearchStudyKeyword(models.Model):    
    _name = "hc.vs.research.study.keyword"    
    _description = "Research Study Keyword"        
    _inherit = ["hc.value.set.contains"]

class ResearchStudyReasonStopped(models.Model):    
    _name = "hc.vs.research.study.reason.stopped"    
    _description = "Research Study Reason Stopped"        
    _inherit = ["hc.value.set.contains"]

class ResearchStudyArmCategory(models.Model):    
    _name = "hc.vs.research.study.arm.category"    
    _description = "Research Study Arm Category"        
    _inherit = ["hc.value.set.contains"]