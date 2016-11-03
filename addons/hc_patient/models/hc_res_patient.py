# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Patient(models.Model):    
    _name = "hc.res.patient"    
    _description = "Patient"
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person",
        string="Person",
        required="True",
        ondelete="restrict",
        help="Person who is this patient.")
    identifier_ids = fields.One2many(
        comodel_name="hc.patient.identifier", 
        inverse_name="patient_id", 
        string="Identifiers", 
        help="A human identifier for this patient.")
    name_ids = fields.One2many(
        comodel_name="hc.patient.name", 
        inverse_name="patient_id", 
        string="Names", 
        help="A name associated with this patient.")
    address_ids = fields.One2many(
        comodel_name="hc.patient.address", 
        inverse_name="patient_id", 
        string="Addresses", 
        help="One or more addresses for this patient.")
    telecom_ids = fields.One2many(
        comodel_name="hc.patient.telecom", 
        inverse_name="patient_id", 
        string="Telecoms", 
        help="A contact detail for the patient.")
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
    language_ids = fields.One2many(
        comodel_name="hc.patient.language",
        inverse_name="patient_id",
        string="Languages",
        help="Language of a person")
    marital_status_ids = fields.One2many(
        comodel_name="hc.patient.marital.status",
        inverse_name="patient_id", 
        string="Marital Statuses", 
        help="Marital (civil) status of a person.")
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
    is_active_patient = fields.Boolean(
        string="Active Patient", 
        default=True, 
        help="Whether this patient's record is in active use.")

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
    _inherit = ["hc.basic.association"] 
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
    use = fields.Selection(
        string="Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old")],
        default="home", 
        help="The purpose of this address.")                    
    type = fields.Selection(
        string="Type", 
        selection=[
            ("postal", "Postal"), 
            ("physical", "Physical"), 
            ("both", "Both")],
        default="both", 
        help="Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.")                  

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

class PatientMaritalStatus(models.Model):   
    _name = "hc.patient.marital.status"  
    _description = "Patient Marital Status"
    _inherit = ["hc.basic.association"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Marital Status.")
    marital_status_id = fields.Many2one(
        comodel_name="hc.vs.marital.status", 
        string="Marital Status", 
        help="Marital Status associated with this Patient Marital Status.")

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
        help="Patient associated with this language.")
    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language",
        help="Language associated with this patient.")
    proficiency_ids = fields.One2many(
        comodel_name="hc.patient.language.proficiency", 
        inverse_name="patient_language_id", 
        string="Proficiency", 
        help="Patient's proficiency and skill for this language.")

class PatientLanguageProficiency(models.Model):
    _name = "hc.patient.language.proficiency"
    _description = "Patient Language Proficiency"
    _inherit = ["hc.basic.association"]

    patient_language_id = fields.Many2one(
        comodel_name="hc.patient.language", 
        string="Patient Language",
        help="Patient's language with proficiency for this skill.")
    language_proficiency_id = fields.Many2one(
        comodel_name="hc.vs.language.proficiency", 
        string="Language Proficiency", 
        help="Patient's proficiency with this language.")
    language_skill_id = fields.Many2one(
        comodel_name="hc.vs.language.skill", 
        string="Language Skill", 
        help="Skill associated with this patient's language proficiency.")

class PatientContact(models.Model): 
    _name = "hc.patient.contact"    
    _description = "Patient Contact"    
    _inherit = ["hc.res.person"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        tring="Patient", 
        help="Identifies patient associated with contact.")
    relationship_ids = fields.One2many(
        comodel_name="hc.patient.contact.relationship", 
        inverse_name="patient_contact_id", 
        string="Relationships", 
        help="The kind of relationship.")
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
 
class ContactRelationship(models.Model):    
    _name = "hc.vs.patient.contact.relationship"    
    _description = "Patient Contact Relationship"   
    _inherit = ["hc.value.set.contains"]

class PatientContactRelationship(models.Model): 
    _name = "hc.patient.contact.relationship"   
    _description = "Patient Contact Relationship"       
    _inherit = ["hc.basic.association"]

    patient_contact_id = fields.Many2one(
        comodel_name="hc.patient.contact", 
        string="Contact", 
        help="Identifies patient contact associated with this contact relationship.")             
    contact_relationship_id = fields.Many2one(
        comodel_name="hc.vs.patient.contact.relationship", 
        string="Patient Contact Relationship", 
        help="Identifies contact relationship associated with this patient contact.")              

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

# External Reference

class PersonLink(models.Model):
    _inherit = ["hc.person.link"]

    target_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Target Patient", 
        required="True", 
        help="Patient who is the resource to which this actual person is associated.")

class RelatedPersonPatient(models.Model): 
    _inherit = ["hc.related.person.patient"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient",
        string="Patient",
        help="Patient associated with this Related Person Patient.")

class Annotation(models.Model):
    _inherit = ["hc.annotation"]

    author_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Author Patient", 
        help="Patient responsible for the annotation.")

    @api.multi
    def _compute_author_name(self):
        for hc_annotation in self:
            if hc_annotation.author_type == 'string':
                hc_annotation.author_name = hc_annotation.author_string
            elif hc_annotation.author_type == 'practitioner':
                hc_annotation.author_name = hc_annotation.author_practitioner_id.name
            elif hc_annotation.author_type == 'related person':
                hc_annotation.author_name = hc_annotation.author_related_person_id.name
            elif hc_annotation.author_type == 'patient':
                hc_annotation.author_name = hc_annotation.author_patient_id.name