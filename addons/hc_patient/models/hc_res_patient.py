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
    marital_status_id = fields.Many2one(
        comodel_name="hc.vs.marital.status", 
        string="Marital Status", 
        help="Marital (civil) status of a patient.")
    # Additional field
    marital_history_ids = fields.One2many(
        comodel_name="hc.patient.marital.history", 
        inverse_name="patient_id", 
        string="Marital Histories", 
        help="Marital (civil) history of a patient.")
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
    photo_ids = fields.One2many(
        comodel_name="hc.patient.photo", 
        inverse_name="patient_id", 
        string="Photos", 
        help="Image of the patient.")   
    general_practitioner_ids = fields.One2many(
        comodel_name="hc.patient.general.practitioner", 
        inverse_name="patient_id", 
        string="General Practitioners", 
        help="Patient's nominated primary care provider.")
    managing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Managing Organization", 
        help="Organization that is the custodian of the patient record.")
    # Additional field
    race_ids = fields.Many2many(
        comodel_name="hc.vs.race", 
        relation="patient_race_rel", 
        string="Races", 
        help="General race category reported by the patient - subject may have more than one.")
    # Additional field
    ethnicity_ids = fields.Many2many(
        comodel_name="hc.vs.ethnicity", 
        relation="patient_ethnicity_rel", 
        string="Ethnicities", 
        help="General ethnicity category reported by the patient - subject may have more than one.")
    contact_ids = fields.One2many(
        comodel_name="hc.patient.contact", 
        inverse_name="patient_id", 
        string="Contacts", 
        help="Contact parties (e.g. guardian, partner, friend) for the patient.")    
    animal_id = fields.Many2one(
        comodel_name="hc.patient.animal", 
        string="Animal", 
        help="If this patient is an animal (non-human).")
    link_ids = fields.One2many(
        comodel_name="hc.patient.link", 
        inverse_name="patient_id", 
        string="Links", 
        help="Link to another patient resource that concerns the same actual person.")
    communication_ids = fields.One2many(
        comodel_name="hc.patient.communication", 
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

class PatientAnimal(models.Model):  
    _name = "hc.patient.animal" 
    _description = "Patient Animal" 

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
            ("seealso", "See Also")], 
        help="The type of link between this patient resource and another patient resource.")

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

class PatientCommunication(models.Model):   
    _name = "hc.patient.communication"  
    _description = "Patient Communication"

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Communication.")
    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language", 
        required="True", 
        help="The language which can be used to communicate with the patient about his or her health.")
    is_preferred = fields.Boolean(
        string="Preferred", 
        help="Language preference indicator.")
    # Additional field
    proficiency_ids = fields.One2many(
        comodel_name="hc.patient.language.proficiency", 
        inverse_name="communication_id", 
        string="Proficiencies", 
        help="Patient's proficiency and skill with this language.")

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
    _inherit = ["hc.human.name.use"]
    _inherits = {"hc.human.name": "name_id"}

    name_id = fields.Many2one(
        comodel_name="hc.human.name",
        string="Human Name",
        required="True",
        ondelete="restrict", 
        help="Human Name associated with this Patient Name.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Name.")                   

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

class PatientAddress(models.Model): 
    _name = "hc.patient.address"    
    _description = "Patient Address" 
    _inherit = ["hc.address.use"]
    _inherits = {"hc.address": "address_id"}

    address_id = fields.Many2one(
        comodel_name="hc.address", 
        string="Address", 
        ondelete="restrict", 
        required="True", 
        help="Address associated with this Patient Address.")         
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Address.")                                                                           

# Additional class
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
        help="Marital Status associated with this Patient Marital History.")
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
        ondelete="restrict", 
        required="True", 
        help="Person Photo associated with this Patient Photo.")                      
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient Photo.")                           

class PatientGeneralPractitioner(models.Model): 
    _name = "hc.patient.general.practitioner"   
    _description = "Patient General Practitioner"           
    _inherit = ["hc.basic.association"]
    
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this Patient General Practitioner.")
    general_practititoner_type = fields.Selection(
        string="General Practititoner Type", 
        selection=[
            ("Organization", "Organization"), 
            ("Practititioner", "Practititioner")], 
        help="Type of patient's nominated primary care provider.")              
    general_practititoner_name = fields.Char(
        string="General Practititoner", 
        compute="_compute_general_practititoner_name", 
        store="True", 
        help="Patient's nominated primary care provider.")                    
    general_practititoner_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="General Practititoner Organization", 
        help="Organization that is patient's nominated primary care provider.")                    
    general_practititoner_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="General Practititoner Person", 
        help="Practitioner who is patient's nominated primary care provider.")                 
                    
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

# Additional class
class PatientLanguageProficiency(models.Model):
    _name = "hc.patient.language.proficiency"
    _description = "Patient Language Proficiency"
    _inherit = ["hc.basic.association"]

    communication_id = fields.Many2one(
        comodel_name="hc.patient.communication", 
        string="Communication", 
        help="Communication associated with this Patient Language Proficiency.")
    language_proficiency_id = fields.Many2one(
        comodel_name="hc.vs.language.proficiency", 
        string="Language Proficiency", 
        help="Language Proficiency associated with this Patient Language Proficiency.")
    language_skill_id = fields.Many2one(
        comodel_name="hc.vs.language.skill", 
        string="Language Skill", 
        help="Language Skill associated with this Patient Language Proficiency.")

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