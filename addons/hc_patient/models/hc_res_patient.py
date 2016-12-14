# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Patient(models.Model):    
    _name = "hc.res.patient"    
    _description = "Patient"
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Person", 
        ondelete="restrict", 
        required="True", 
        help="Person associated with this Patient.")
    identifier_ids = fields.One2many(
        comodel_name="hc.patient.identifier", 
        inverse_name="patient_id", 
        string="Identifiers", 
        help="A human identifier for this patient.")
    is_active = fields.Boolean(
        string="Active", 
        help="Whether this patient's record is in active use.")
    name_ids = fields.One2many(
        comodel_name="hc.patient.name", 
        inverse_name="patient_id", 
        string="Names", 
        help="A name associated with the patient.")
    telecom_ids = fields.One2many(
        comodel_name="hc.patient.telecom", 
        inverse_name="patient_id", 
        string="Telecoms", 
        help="A contact detail for the patient.")
    gender = fields.Selection(
        string="Patient Gender", 
        selection=[
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other"), 
            ("unknown", "Unknown")], 
        help="The gender that the patient is considered to have for administration and record keeping purposes.")
    birth_date = fields.Date(
        string="Birth Date", 
        help="The date of birth for the patient.")
    birth_time = fields.Char(
        string="Birth Time", 
        help="The time when the patient was born.")
    is_deceased = fields.Boolean(
        string="Deceased", 
        required="False", 
        help="Indicates if the patient is deceased or not.")
    deceased_date = fields.Date(
        string="Deceased Date", 
        help="The date when the patient died.")
    deceased_time = fields.Char(
        string="Deceased Time", 
        help="The time when the patient died.")
    address_ids = fields.One2many(
        comodel_name="hc.patient.address", 
        inverse_name="patient_id", 
        string="Addresses", 
        help="One or more addresses for this patient.")
    language_ids = fields.One2many(
        comodel_name="hc.patient.language",
        inverse_name="patient_id",
        string="Languages",
        help="Language of a person")
    marital_status_id = fields.Many2one(
        comodel_name="hc.vs.marital.status", 
        string="Marital Status", 
        help="Marital (civil) status of a patient.")
    marital_history_ids = fields.One2many(
        comodel_name="hc.patient.marital.history", 
        inverse_name="patient_id", 
        string="Marital Histories", 
        help="Marital (civil) history of a patient.")
    race_ids = fields.Many2many(
        comodel_name="hc.vs.race", 
        relation="race_patient_rel", 
        string="Races", 
        help="General race category reported by the patient - subject may have more than one.")
    ethnicity_ids = fields.Many2many(
        comodel_name="hc.vs.ethnicity", 
        relation="ethnicity_patient_rel", 
        string="Ethnicities", 
        help="General ethnicity category reported by the patient - subject may have more than one.")
    photo_ids = fields.One2many(
        comodel_name="hc.patient.photo", 
        inverse_name="patient_id", 
        string="Photos", 
        help="Image of the patient.")
    contact_ids = fields.One2many(
        comodel_name="hc.patient.contact", 
        inverse_name="patient_id", 
        string="Contacts", 
        help="Contact parties (e.g. guardian, partner, friend) for the patient.")
    is_multiple_birth = fields.Boolean(
        string="Multiple Birth", 
        help="Whether patient is part of a multiple birth.")
    multiple_birth_count = fields.Integer(
        string="Multiple Birth Count", 
        size=1, 
        help="Number of births in a multiple birth.")
    multiple_birth_order = fields.Integer(
        string="Multiple Birth Order", 
        size=1, 
        help="The actual birth order in a multiple birth.")
    care_provider_practitioner_ids = fields.One2many(
        comodel_name="hc.patient.care.provider.practitioner", 
        inverse_name="patient_id", 
        string="Care Provider Practitioners", 
        help="Practitioner who is patient's nominated care provider.")
    care_provider_organization_ids = fields.One2many(
        comodel_name="hc.patient.care.provider.organization", 
        inverse_name="patient_id", 
        string="Care Provider Organizations", 
        help="Organization who is patient's nominated care provider.")
    managing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Managing Organization", 
        help="Organization that is the custodian of the patient record.")
    animal_ids = fields.One2many(
        comodel_name="hc.patient.animal", 
        inverse_name="patient_id", 
        string="Animal", 
        help="If this patient is an animal (non-human).")
    link_ids = fields.One2many(
        comodel_name="hc.patient.link", 
        inverse_name="patient_id", 
        string="Links", 
        help="Link to another patient resource that concerns the same actual person.")
    contact_ids = fields.One2many(
        comodel_name="hc.patient.contact", 
        inverse_name="patient_id", 
        string="Contacts", 
        help="A contact party (e.g. guardian, partner, friend) for the patient.")
    communication_ids = fields.One2many(
        comodel_name="hc.patient.language", 
        inverse_name="patient_id", 
        string="Languages", 
        help="A list of Languages which may be used to communicate with the patient about his or her health.")

    _defaults = {
        "is_patient": True,
        }

    @api.model
    def create(self, vals):
        vals['is_patient'] = self.env.context.get('is_patient', False)
        return super(Patient, self).create(vals)

class PatientIdentifier(models.Model):  
    _name = "hc.patient.identifier" 
    _description = "Patient Identifier"         
    _inherits = {"hc.person.identifier": "identifier_id"}

    identifier_id = fields.Many2one(
        comodel_name="hc.person.identifier", 
        string="Person Identifier",
        required="True",
        ondelete="restrict", 
        help="Person Identifier associated with this Patient Identifier.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Identifier.")                    

class PatientName(models.Model): 
    _name = "hc.patient.name"    
    _description = "Patient Name"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.human.name": "human_name_id"}

    human_name_id = fields.Many2one(
        comodel_name="hc.human.name",
        string="Human Name",
        required="True",
        ondelete="restrict", 
        help="Human Name associated with this Patient Name.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Name.")                  

class PatientAddress(models.Model): 
    _name = "hc.patient.address"    
    _description = "Patient Address"        
    _inherits = {"hc.person.address": "address_id"}

    address_id = fields.Many2one(
        comodel_name="hc.person.address", 
        string="Person Address", 
        required="True", 
        ondelete="restrict", 
        help="Address associated with this Patient Address.")                 
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Address.")                                  

class PatientTelecom(models.Model): 
    _name = "hc.patient.telecom"    
    _description = "Patient Telecom"        
    _inherit = ["hc.contact.point.use"] 
    _inherits = {"hc.contact.point": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.contact.point", 
        string="Telecom", 
        ondelete="restrict", 
        required="True", 
        help="Telecom associated with this Patient Telecom.")                 
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Telecom.")                                               

class PatientMaritalHistory(models.Model):    
    _name = "hc.patient.marital.history" 
    _description = "Patient Marital History"     
    _inherit = ["hc.basic.association"]
    
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Marital History.")              
    marital_status_id = fields.Many2one(
        comodel_name="hc.vs.marital.status", 
        string="Marital Status", 
        help="Marital (civil) status of a patient.")
    partner_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Spouse", 
        help="Person married to this Patient.")
               
class PatientPhoto(models.Model):   
    _name = "hc.patient.photo"  
    _description = "Patient Photo"
    _inherits = {"hc.person.photo": "photo_id"}

    photo_id = fields.Many2one(
        comodel_name="hc.person.photo", 
        string="Photo",
        required="True",
        ondelete="restrict",  
        help="Photo associated with this Patient Photo.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Photo.")      

class PatientCareProviderPractitioner(models.Model):
    _name = "hc.patient.care.provider.practitioner"    
    _description = "Patient Care Provider Practitioner"
    _inherit = ["hc.basic.association"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Care Provider Practitioner.")
    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Care Provider Practitioner", 
        help="Practitioner who is this Patient Care Provider Practitioner.")

class PatientCareProviderOrganization(models.Model):
    _name = "hc.patient.care.provider.organization"    
    _description = "Patient Care Provider Organization"
    _inherit = ["hc.basic.association"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Care Provider Organization.")
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Care Provider Organization", 
        help="Organization that is this Patient Care Provider Organization.")

class PatientAnimal(models.Model):  
    _name = "hc.patient.animal" 
    _description = "Patient Animal" 

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Identifies patient associated with animal.")
    species_id = fields.Many2one(
        comodel_name="hc.vs.animal.species", 
        string="Species", 
        help="Identifies the high level taxonomic categorization of the kind of animal (e.g., dog, cow).")
    breed_id = fields.Many2one(
        comodel_name="hc.vs.animal.breed", 
        string="Breed", 
        help="Identifies the detailed categorization of the kind of animal (e.g., poodle, angus).")
    gender_status_id = fields.Many2one(
        comodel_name="hc.vs.animal.gender.status", 
        string="Gender Status", 
        help="Indicates the current state of the animal's reproductive organs (e.g., neutered, intact).")

class PatientLanguage(models.Model):
    _name = "hc.patient.language"
    _description = "Patient Language"
    _inherit = ["hc.basic.association"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Language.")
    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language",
        help="Language associated with this Patient Language.")
    proficiency_ids = fields.One2many(
        comodel_name="hc.patient.language.proficiency", 
        inverse_name="patient_language_id", 
        string="Proficiencies", 
        help="Patient's proficiency and skill with this Patient Language.")

class PatientLanguageProficiency(models.Model):
    _name = "hc.patient.language.proficiency"
    _description = "Patient Language Proficiency"
    _inherit = ["hc.basic.association"]

    patient_language_id = fields.Many2one(
        comodel_name="hc.patient.language", 
        string="Patient Language",
        help="Patient Language associated with this Patient Language Proficiency.")
    language_proficiency_id = fields.Many2one(
        comodel_name="hc.vs.language.proficiency", 
        string="Language Proficiency", 
        help="Language Proficiency associated with this Patient Language Proficiency.")
    language_skill_id = fields.Many2one(
        comodel_name="hc.vs.language.skill", 
        string="Language Skill", 
        help="Language Skill associated with this Patient Language Proficiency.")

class PatientContact(models.Model): 
    _name = "hc.patient.contact"    
    _description = "Patient Contact"           
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Person", 
        ondelete="restrict", 
        required="True", 
        help="Person associated with this Patient Contact.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Contact.")
    relationship_ids = fields.Many2many(
        comodel_name="hc.vs.patient.contact.relationship", 
        relation="patient_contact_relationship_rel", 
        string="Relationships", 
        help="The kind of relationship.")
    name_id = fields.Many2one(
        comodel_name="hc.human.name", 
        string="Name", 
        help="A name associated with the contact person.")
    telecom_ids = fields.One2many(
        comodel_name="hc.patient.contact.telecom", 
        inverse_name="contact_id", 
        string="Telecoms", 
        help="A contact detail for the contact person.")
    address_id = fields.Many2one(
        comodel_name="hc.address", 
        string="Address", 
        help="Address for the contact person.")
    gender = fields.Selection(
        string="Gender", 
        selection=[
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other"), 
            ("unknown", "Unknown")], 
        help="The gender that the patient contact is considered to have for administration and record keeping purposes.")
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization that is associated with the contact.")
    start_date = fields.Datetime(
        string="Valid from", 
        help="Start of the the period during which this contact person or organization is valid to be contacted relating to this patient.")
    end_date = fields.Datetime(
        string="Valid to", 
        help="End of the the period during which this contact person or organization is valid to be contacted relating to this patient.")  

class PatientLink(models.Model):    
    _name = "hc.patient.link"   
    _description = "Patient Link"

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient",
        help="Patient associated with this Link.")
    other_type = fields.Selection(
        string="Other Type", 
        required="True", 
        selection=[
            ("Patient", "Patient"), 
            ("Related Person", "Related Person")], 
        help="Type of resource that the link refers to.")
    other_name = fields.Char(
        string="Other", 
        compute="_compute_other_name", 
        store="True", 
        help="The other patient or related person resource that the link refers to.")
    other_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Other Patient", 
        help="Patient resource that the link refers to.")
    other_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Other Related Person", 
        help="Related Person resource that the link refers to.")
    type = fields.Selection(
        string="Link Type", 
        selection=[
            ("replace", "Replace"), 
            ("refer", "Refer"), 
            ("seealso", "See also")], 
        help="The type of link between this patient resource and another patient resource.")

class PatientContactTelecom(models.Model):  
    _name = "hc.patient.contact.telecom"    
    _description = "Patient Contact Telecom"            
    _inherit = ["hc.contact.point.use"] 
    _inherits = {"hc.contact.point": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.contact.point", 
        string="Telecom", 
        ondelete="restrict", 
        required="True", 
        help="Telecom associated with this Patient Contact Telecom.")                     
    contact_id = fields.Many2one(
        comodel_name="hc.patient.contact", 
        string="Contact", 
        help="Contact associated with this Patient Contact Telecom.")                     

class ContactRelationship(models.Model):    
    _name = "hc.vs.patient.contact.relationship"    
    _description = "Patient Contact Relationship"   
    _inherit = ["hc.value.set.contains"]    

# External Reference

class PersonLink(models.Model):
    _inherit = ["hc.person.link"]

    target_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Target Patient", 
        help="Patient who is the resource to which this actual person is associated.")

    @api.multi          
    def _compute_target_name(self):         
        for hc_res_person in self:      
            if hc_res_person.target_type == 'Person': 
                hc_res_person.target_name = hc_res_person.target_person_id.name
            elif hc_res_person.target_type == 'Practitioner':   
                hc_res_person.target_name = hc_res_person.target_practitioner_id.name
            elif hc_res_person.target_type == 'Related Person': 
                hc_res_person.target_name = hc_res_person.target_related_person_id.name
            elif hc_res_person.target_type == 'Patient':  
                hc_res_person.target_name = hc_res_person.target_patient_id.name

class RelatedPersonPatient(models.Model): 
    _inherit = ["hc.related.person.patient"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient",
        string="Patient",
        help="Patient associated with this Related Person Patient.")

class Annotation(models.Model):
    _inherit = ["hc.annotation"]
 

    author_name = fields.Char(
        string="Author", 
        compute="_compute_author_name", 
        store="True",
        help="Individual responsible for the annotation.")
    author_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Author Patient", 
        help="Patient responsible for the annotation.")

    @api.multi
    @api.depends('author_string', 'author_practitioner_id', 'author_related_person_id', 'author_patient_id')
    def _compute_author_name(self):
        for hc_annotation in self:
            if hc_annotation.author_type == 'string':
                hc_annotation.author_name = hc_annotation.author_string
            elif hc_annotation.author_type == 'practitioner':
                hc_annotation.author_name = hc_annotation.author_practitioner_id.name
            elif hc_annotation.author_type == 'related_person':
                hc_annotation.author_name = hc_annotation.author_related_person_id.name
            elif hc_annotation.author_type == 'patient':
                hc_annotation.author_name = hc_annotation.author_patient_id.name

class Signature(models.AbstractModel):    
    _inherit = "hc.signature"
   
    who_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Who Patient", 
        help="Patient who signed.")

    on_behalf_of_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="On Behalf Of Patient", 
        help="Patient the party represented.")