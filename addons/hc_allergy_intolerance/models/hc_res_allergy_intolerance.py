# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AllergyIntolerance(models.Model): 
    _name = "hc.res.allergy.intolerance"    
    _description = "Allergy Intolerance"
    _inherit = ["hc.basic.association"]
 
    name = fields.Char(
        string="Allergy/Intolerance", 
        # compute='compute_allergy', 
        # store=True, 
        help="Patient's allergy/intolerance.")
    identifier_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.identifier", 
        inverse_name="allergy_intolerance_id", 
        string="Identifiers", 
        help="External IDs for the allergy.")                   
    status = fields.Selection(
        string="Status", 
        selection=[
            ("active", "Active"), 
            ("unconfirmed", "Unconfirmed"), 
            ("confirmed", "Confirmed"), 
            ("inactive", "Inactive"), 
            ("resolved", "Resolved"), 
            ("refuted", "Refuted"), 
            ("entered-in-error", "Entered in Error")], 
        default="active",
        help="Assertion about certainty associated with a propensity, or potential risk, of a reaction to the identified Substance.")                    
    type = fields.Selection(
        string="Type", 
        selection=[
            ("allergy", "Allergy"), 
            ("intolerance", "Intolerance")],
        default="allergy", 
        help="Identification of the underlying physiological mechanism for a Reaction Risk.")                    
    category = fields.Selection(
        string="Category", 
        selection=[
            ("food", "Food"), 
            ("medication", "Medication"), 
            ("environment", "Environment"), 
            ("other", "Other")], 
        help="Category of an identified Substance.")
    category_other = fields.Char(
        string="Other Category",
        help="Describe other category.")                 
    criticality = fields.Selection(
        string="Criticality", 
        selection=[
            ("low", "Low"), 
            ("high", "High"), 
            ("unable-to-assess", "Unable to Assess Risk")], 
        help="Estimate of the potential clinical harm, or seriousness, of a reaction to an identified Substance.")                    
    substance_id = fields.Many2one(
        comodel_name="hc.vs.allergy.intolerance.substance.code", 
        string="Substance", 
        required="True", 
        help="Type of the substance and Negation codes for reporting no known allergies.")                    
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        required="True", 
        help="Patient who the sensitivity is for.")                    
    recorded_date = fields.Datetime(
        string="Recorded Date", 
        help="When recorded.")                  
    recorder_type = fields.Selection(
        string="Recorder Type", 
        selection=[
            ("Practitioner", "Practitioner"),
            ("Patient", "Patient")],
        help="Type of individual who recorded the sensitivity.")
    recorder_name = fields.Char(
        string="Recorder",
        compute="compute_recorder_name",
        help="Individual who recorded the sensitivity.")
    recorder_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Recorder Practitioner", 
        help="Practitioner who recorded the sensitivity.")                   
    recorder_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Recorder Patient", 
        help="Patient who recorded the sensitivity.")                   
    
    reporter_type = fields.Selection(
        string="Reporter Type", 
        selection=[
            ("Practitioner", "Practitioner"),
            ("Patient", "Patient"),
            ("Related Person", "Related Person")],
        help="Type of source of the information about the allergy.")
    reporter_name = fields.Char(
        string="Reporter",
        compute="compute_reporter_name",
        help="Individuals ource of the information about the allergy.")
    reporter_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Reporter Patient", 
        help="Patient source of the information about the allergy.")                    
    reporter_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Reporter Related Person", 
        help="Related Person source of the information about the allergy.")                    
    reporter_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Reporter Practitioner", 
        help="Practitioner source of the information about the allergy.")                    
    
    onset = fields.Datetime(
        string="Onset Date", 
        help="Date(/time) when manifestations showed.")                    
    last_occurence = fields.Datetime(
        string="Last Occurence Date", 
        help="Date(/time) of last known occurence of a reaction.")                   
    note_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.annotation", 
        inverse_name="allergy_intolerance_id", 
        string="Notes", 
        help="Additional text (i.e., comment, explanation) not captured in other fields.")
    reaction_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.reaction", 
        inverse_name="allergy_intolerance_id", 
        string="Reactions", 
  
        help="Adverse Reaction Events linked to exposure to substance.")

    @api.multi
    def compute_recorder_name(self):
        for hc_annotation in self:

            if hc_annotation.recorder_type == 'Practitioner':
                hc_annotation.recorder_name = hc_annotation.recorder_practitioner_id.name
            elif hc_annotation.recorder_type == 'Patient':
                hc_annotation.recorder_name = hc_annotation.recorder_patient_id.name
            
    @api.multi
    def compute_reporter_name(self):
        for hc_annotation in self:
            if hc_annotation.reporter_type == 'Practitioner':
                hc_annotation.reporter_name = hc_annotation.reporter_practitioner_id.name
            elif hc_annotation.reporter_type == 'Patient':
                hc_annotation.reporter_name = hc_annotation.reporter_patient_id.name
            elif hc_annotation.reporter_type == 'Related Person':
                hc_annotation.reporter_name = hc_annotation.reporter_related_person_id.name

    # @api.depends('patient','substance','patient_id','substance_id')
    # def compute_allergy(self):
    #     allergy = ''
    #     patient = self.patient_id and ', '+self.patient_id.name or ''   
    #     substance = self.substance_id and ', '+self.substance_id.name or ''
    #     allergy = patient+substance+allergy
    #     self.name = allergy

class AllergyIntoleranceReaction(models.Model): 
    _name = "hc.allergy.intolerance.reaction"   
    _description = "Allergy Intolerance Reaction"

    allergy_intolerance_id = fields.Many2one(
        comodel_name="hc.res.allergy.intolerance", 
        string="Allergy Intolerance", 
        required="True", 
        help="Allergy intolerance.")                   
    substance_id = fields.Many2one(
        comodel_name="hc.vs.substance.code", 
        string="Substance", 
        help="Type of the substance.")                  
    certainty = fields.Selection(
        string="Reaction Certainty", 
        selection=[
            ("unlikely", "Unlikely"), 
            ("likely", "Likely"), 
            ("confirmed", "Confirmed")], 
        help="Statement about the degree of clinical certainty that a Specific Substance was the cause of the Manifestation in a reaction event.")                   
    manifestation_ids = fields.Many2many(
        comodel_name="hc.vs.manifestation.code",
        string="Manifestations", 
        required="True", 
        help="Clinical symptoms and/or signs that are observed or associated with an Adverse Reaction Event.")
    description = fields.Text(
        string="Description", 
        help="Description of the event as a whole.")                    
    onset = fields.Datetime(
        string="Onset Date", 
        help="Date(/time) when manifestations showed.")                    
    duration = fields.Float(
        string="Duration", 
        help="How long Manifestations persisted.")
    duration_uom_id = fields.Many2one(
        comodel_name="hc.vs.uom", 
        string="Duration UOM", 
        help="How long Manifestations persisted unit of measure.")            
    severity = fields.Selection(
        string="Reaction Severity", 
        selection=[
            ("mild", "Mild"), 
            ("moderate", "Moderate"), 
            ("severe", "Severe")], 
        help="Clinical assessment of the severity of a reaction event as a whole, potentially considering multiple different manifestations.")                    
    exposure_route_id = fields.Many2one(
        comodel_name="hc.vs.route.code", 
        string="Exposure Route", 
        help="The route or physiological path of administration of a therapeutic agent into or onto the body of a subject.")                 
    note_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.reaction.annotation", 
        inverse_name="allergy_intolerance_reaction_id", 
        string="Notes", 
        help="Text about event not captured in other fields.")                    

class AllergyIntoleranceIdentifier(models.Model):   
    _name = "hc.allergy.intolerance.identifier" 
    _description = "Allergy Intolerance Identifier"     
    _inherit = ["hc.basic.association", "hc.identifier"]    
    
    allergy_intolerance_id = fields.Many2one(
        comodel_name="hc.res.allergy.intolerance", 
        string="Allergy Intolerance", 
        help="Allergy Intolerance with this identifier.")                 

class AllergyIntoleranceAnnotation(models.Model):   
    _name = "hc.allergy.intolerance.annotation" 
    _description = "Allergy Intolerance Annotation"     
    _inherit = ["hc.basic.association", "hc.annotation"]

    allergy_intolerance_id = fields.Many2one(
        comodel_name="hc.res.allergy.intolerance", 
        string="Allergy Intolerance", 
        help="Allergy Intolerance with this annotation.")

    @api.multi
    def compute_author_name(self):
        for hc_allergy_intolerance_annotation in self:
            if hc_allergy_intolerance_annotation.author_type == 'string':
                hc_allergy_intolerance_annotation.author_name = hc_allergy_intolerance_annotation.author_string
            elif hc_allergy_intolerance_annotation.author_type == 'Practitioner':
                hc_allergy_intolerance_annotation.author_name = hc_allergy_intolerance_annotation.author_practitioner_id.name
            elif hc_allergy_intolerance_annotation.author_type == 'Patient':
                hc_allergy_intolerance_annotation.author_name = hc_allergy_intolerance_annotation.author_patient_id.name
            elif hc_allergy_intolerance_annotation.author_type == 'Related Person':
                hc_allergy_intolerance_annotation.author_name = hc_allergy_intolerance_annotation.author_related_person_id.name                    

class AllergyIntoleranceReactionAnnotation(models.Model):   
    _name = "hc.allergy.intolerance.reaction.annotation"    
    _description = "Allergy Intolerance Reaction Annotation"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    allergy_intolerance_reaction_id = fields.Many2one(
        comodel_name="hc.allergy.intolerance.reaction", 
        string="Allergy Intolerance Reaction", 
        help="Allergy Intolerance Reaction with this annotation.")

    @api.multi
    def compute_author_name(self):
        for hc_allergy_intolerance_reaction_annotation in self:
            if hc_allergy_intolerance_reaction_annotation.author_type == 'string':
                hc_allergy_intolerance_reaction_annotation.author_name = hc_allergy_intolerance_reaction_annotation.author_string
            elif hc_allergy_intolerance_reaction_annotation.author_type == 'Practitioner':
                hc_allergy_intolerance_reaction_annotation.author_name = hc_allergy_intolerance_reaction_annotation.author_practitioner_id.name
            elif hc_allergy_intolerance_reaction_annotation.author_type == 'Patient':
                hc_allergy_intolerance_reaction_annotation.author_name = hc_allergy_intolerance_reaction_annotation.author_patient_id.name
            elif hc_allergy_intolerance_reaction_annotation.author_type == 'Related Person':
                hc_allergy_intolerance_reaction_annotation.author_name = hc_allergy_intolerance_reaction_annotation.author_related_person_id.name                  
              
class AllergyIntoleranceSubstanceCode(models.Model):    
    _name = "hc.vs.allergy.intolerance.substance.code"  
    _description = "Allergy Intolerance Substance Code"     
    _inherit = ["hc.value.set.contains"]     

# External Reference

class Patient(models.Model):
    _inherit = ["hc.res.patient"]

    allergy_intolerance_ids = fields.One2many(
        comodel_name="hc.res.allergy.intolerance",
        inverse_name="patient_id", 
        string="Allergies/Intolerances", 
        help="Allergies and intolerances of this patient.")