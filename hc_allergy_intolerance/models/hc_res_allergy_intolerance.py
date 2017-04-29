# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AllergyIntolerance(models.Model): 
    _name = "hc.res.allergy.intolerance"    
    _description = "Allergy Intolerance"
    _inherit = ["hc.basic.association"]

    name = fields.Char(
        string="Event Name", 
        required="True", 
        help="Text representation of the allergy intolerance event. Patient + Allergy + Onset Name.")
    identifier_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.identifier", 
        inverse_name="allergy_intolerance_id", 
        string="Identifiers", 
        help="External IDs for the allergy.")                   
    clinical_status = fields.Selection(
        string="Clinical Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("resolved", "Resolved")],
        default="draft", 
        help="The clinical status of the allergy or intolerance.")
    verification_status = fields.Selection(
        string="Verification Status", 
        required="True", 
        selection=[
            ("unconfirmed", "Unconfirmed"), 
            ("confirmed", "Confirmed"), 
            ("refuted", "Refuted"), 
            ("entered-in-error", "Entered-In-Error")],
        default="unconfirmed", 
        help="Assertion about certainty associated with the propensity, or potential risk, of a reaction to the identified substance (including pharmaceutical product).")                    
    type = fields.Selection(
        string="Type", 
        selection=[
            ("allergy", "Allergy"), 
            ("intolerance", "Intolerance")],
        default="allergy", 
        help="Identification of the underlying physiological mechanism for a Reaction Risk.")                    
    category_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.category", 
        inverse_name="allergy_intolerance_id", 
        string="Categories", 
        help="Category of the identified substance.")                 
    criticality = fields.Selection(
        string="Criticality", 
        selection=[
            ("low", "Low"), 
            ("high", "High"), 
            ("unable-to-assess", "Unable to Assess")],
        default="low", 
        help="Estimate of the potential clinical harm, or seriousness, of a reaction to an identified Substance.")                    
    code_id = fields.Many2one(
        comodel_name="hc.vs.allergy.intolerance.code", 
        string="Allergy/Intolerance", 
        help="Allergy or intolerance.")                   
    code = fields.Char(
        string="Code", 
        related="code_id.code", 
        help="Allergy or intolerance code.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        required="True", 
        help="Patient who the sensitivity is for.")                    
    onset_type = fields.Selection(
        string="Onset Type", 
        selection=[
            ("date_time", "Date Time"), 
            ("age", "Age"), 
            ("period", "Period"), 
            ("range", "Range"), 
            ("string", "String")], 
        help="Type of when allergy or intolerance was identified.")
    onset_name = fields.Char(
        string="Onset", 
        compute="_compute_onset_name", 
        store="True", 
        help="When allergy or intolerance was identified.")
    onset_date_time = fields.Datetime(
        string="Onset Datetime", 
        help="Date Time when allergy or intolerance was identified.")
    onset_age = fields.Integer(
        string="Onset Age", 
        size=3, 
        help="Age when allergy or intolerance was identified.")
    onset_age_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Onset Age UOM",
        # domain=[("category_id", '=', "uom_categ_utime")],
        default="a", 
        help="Onset age unit of measure.")
    onset_start_date = fields.Datetime(
        string="Onset Start Date", 
        help="Start of when allergy or intolerance was identified.")
    onset_end_date = fields.Datetime(
        string="Onset End Date", 
        help="End of when allergy or intolerance was identified.")
    onset_range_low = fields.Float(
        string="Onset Range Low", 
        help="Low limit of range when allergy or intolerance was identified.")
    onset_range_high = fields.Float(
        string="Onset Range High", 
        help="High limit of range when allergy or intolerance was identified.")
    onset_string = fields.Char(
        string="Onset String", 
        help="String of when allergy or intolerance was identified.")
    asserted_date = fields.Datetime(
        string="Asserted Date", 
        help="Date record was believed accurate.")               
    recorder_type = fields.Selection(
        string="Recorder Type", 
        selection=[
            ("practitioner", "Practitioner"),
            ("patient", "Patient")],
        help="Type of individual who recorded the sensitivity.")
    recorder_name = fields.Char(
        string="Recorder",
        compute="_compute_recorder_name",
        # store="True",
        help="Individual who recorded the sensitivity.")
    recorder_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Recorder Practitioner", 
        help="Practitioner who recorded the sensitivity.")                   
    recorder_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Recorder Patient", 
        help="Patient who recorded the sensitivity.")
    asserter_type = fields.Selection(
        string="Asserter Type", 
        selection=[
            ("patient", "Patient"), 
            ("related_person", "Related Person"), 
            ("practitioner", "Practitioner")], 
        help="Type of source of the information about the allergy.")
    asserter_name = fields.Char(
        string="Asserter", 
        compute="_compute_asserter_name", 
        # store="True", 
        help="Source of the information about the allergy.")
    asserter_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Asserter Patient", 
        help="Patient source of the information about the allergy.")
    asserter_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Asserter Related Person", 
        help="Related Person source of the information about the allergy.")
    asserter_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Asserter Practitioner", 
        help="Practitioner source of the information about the allergy.")                                        
    last_occurence = fields.Datetime(
        string="Last Occurence Date", 
        help="Date(/time) of last known occurence of a reaction.")                   
    note_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.note", 
        inverse_name="allergy_intolerance_id", 
        string="Notes", 
        help="Additional text (i.e., comment, explanation) not captured in other fields.")
    reaction_ids = fields.One2many(
        comodel_name="hc.allergy.intolerance.reaction", 
        inverse_name="allergy_intolerance_id", 
        string="Reactions", 
        help="Adverse Reaction Events linked to exposure to substance.")

    @api.depends('onset_type')              
    def _compute_onset_name(self):              
        for hc_res_allergy_intolerance in self: 
            if hc_res_allergy_intolerance.onset_type == 'date_time':        
                    hc_res_allergy_intolerance.onset_name = str(hc_res_allergy_intolerance.onset_date_time)
            elif hc_res_allergy_intolerance.onset_type == 'age':    
                    hc_res_allergy_intolerance.onset_name = str(hc_res_allergy_intolerance.onset_age) + ' ' + str(hc_res_allergy_intolerance.onset_age_uom_id.name)
            elif hc_res_allergy_intolerance.onset_type == 'period':     
                    hc_res_allergy_intolerance.onset_name = 'Between ' + str(hc_res_allergy_intolerance.onset_start_date) + ' and ' + str(hc_res_allergy_intolerance.onset_end_date)
            elif hc_res_allergy_intolerance.onset_type == 'range':      
                    hc_res_allergy_intolerance.onset_name = 'Between ' + str(hc_res_allergy_intolerance.onset_range_low) + ' and ' + str(hc_res_allergy_intolerance.onset_range_high)
            elif hc_res_allergy_intolerance.onset_type == 'string':     
                    hc_res_allergy_intolerance.onset_name = hc_res_allergy_intolerance.onset_string

    @api.depends('recorder_type')
    def _compute_recorder_name(self):
        for hc_res_allergy_intolerance in self:
            if hc_res_allergy_intolerance.recorder_type == 'practitioner':
                hc_res_allergy_intolerance.recorder_name = hc_res_allergy_intolerance.recorder_practitioner_id.name
            elif hc_res_allergy_intolerance.recorder_type == 'patient':
                hc_res_allergy_intolerance.recorder_name = hc_res_allergy_intolerance.recorder_patient_id.name
            
    @api.depends('asserter_type')
    def _compute_asserter_name(self):
        for hc_res_allergy_intolerance in self:
            if hc_res_allergy_intolerance.asserter_type == 'patient':
                hc_res_allergy_intolerance.asserter_name = hc_res_allergy_intolerance.asserter_patient_id.name
            elif hc_res_allergy_intolerance.asserter_type == 'related_person':
                hc_res_allergy_intolerance.asserter_name = hc_res_allergy_intolerance.asserter_related_person_id.name
            elif hc_res_allergy_intolerance.asserter_type == 'practitioner':
                hc_res_allergy_intolerance.asserter_name = hc_res_allergy_intolerance.asserter_practitioner_id.name
    
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
            ("confirmed", "Confirmed"),
            ("unknown", "Unknown")], 
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
        comodel_name="product.uom", 
        string="Duration UOM",
        # domain=[('category_id', '=', 'uom_categ_utime')], 
        help="Duration unit of measure.")            
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
        comodel_name="hc.allergy.intolerance.reaction.note", 
        inverse_name="reaction_id", 
        string="Notes", 
        help="Text about event not captured in other fields.")                    

class AllergyIntoleranceIdentifier(models.Model):   
    _name = "hc.allergy.intolerance.identifier" 
    _description = "Allergy Intolerance Identifier"         
    _inherit = ["hc.basic.association", "hc.identifier"]    

    allergy_intolerance_id = fields.Many2one(
        comodel_name="hc.res.allergy.intolerance", 
        string="Allergy Intolerance", 
        help="Allergy Intolerance associated with this Allergy Intolerance Identifier.")                      

class AllergyIntoleranceNote(models.Model):   
    _name = "hc.allergy.intolerance.note"   
    _description = "Allergy Intolerance Note"           
    _inherit = ["hc.basic.association", "hc.annotation"]    

    allergy_intolerance_id = fields.Many2one(
        comodel_name="hc.res.allergy.intolerance", 
        string="Allergy Intolerance", 
        help="Allergy Intolerance associated with this Allergy Intolerance Note.")                        

class AllergyIntoleranceCategory(models.Model): 
    _name = "hc.allergy.intolerance.category"   
    _description = "Allergy Intolerance Category"           
    _inherit = ["hc.basic.association"] 

    allergy_intolerance_id = fields.Many2one(
        comodel_name="hc.res.allergy.intolerance", 
        string="Allergy Intolerance", 
        help="Allergy Intolerance associated with this Allergy Intolerance Category.")                        
    category = fields.Selection(
        string="Category", 
        selection=[
            ("food", "Food"), 
            ("medication", "Medication"), 
            ("biologic", "Biologic"), 
            ("environment", "Environment")], 
        help="Category of the identified substance.")                      

class AllergyIntoleranceReactionNote(models.Model):
    _name = "hc.allergy.intolerance.reaction.note"  
    _description = "Allergy Intolerance Reaction Note"          
    _inherit = ["hc.basic.association", "hc.annotation"]    

    reaction_id = fields.Many2one(
        comodel_name="hc.allergy.intolerance.reaction", 
        string="Reaction", 
        help="Reaction associated with this Allergy Intolerance Reaction Note.")           

class AllergyIntoleranceCode(models.Model): 
    _name = "hc.vs.allergy.intolerance.code"   
    _description = "Allergy Intolerance Code"        
    _inherit = ["hc.value.set.contains"]     

    name = fields.Char(
        string="Name", 
        help="Name of this allergy intolerance.")
    code = fields.Char(
        string="Code", 
        help="Code of this allergy intolerance.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.allergy.intolerance.code", 
        string="Parent",
        help="Parent concept.")

class ManifestationCode(models.Model): 
    _name = "hc.vs.manifestation.code" 
    _description = "Manifestation Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this manifestation.")
    code = fields.Char(
        string="Code", 
        help="Code of this manifestation.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.manifestation.code", 
        string="Parent",
        help="Parent concept.")    

# External Reference

class Patient(models.Model):
    _inherit = ["hc.res.patient"]

    allergy_intolerance_ids = fields.One2many(
        comodel_name="hc.res.allergy.intolerance",
        inverse_name="patient_id", 
        string="Allergies/Intolerances", 
        help="Allergies and intolerances of this patient.")
