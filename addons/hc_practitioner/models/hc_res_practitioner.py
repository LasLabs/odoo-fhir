# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Practitioner(models.Model):   
    _name = "hc.res.practitioner"   
    _description = "Practitioner"   
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person",
        string="Person",
        required=True,
        ondelete="restrict",
        help="Person who is this practitioner.")
    identifier_ids = fields.One2many(
        comodel_name="hc.practitioner.identifier", 
        inverse_name="practitioner_id", 
        string="Identifiers", 
        help="A human identifier for this person.")
    name_ids = fields.One2many(
        comodel_name="hc.practitioner.name", 
        inverse_name="practitioner_id", 
        string="Names", 
        help="A name associated with this practitioner.")
    telecom_ids = fields.One2many(
        comodel_name="hc.practitioner.telecom", 
        inverse_name="practitioner_id", 
        string="Telecom Contacts", 
        help="A contact detail for this practitioner.")
    address_ids = fields.One2many(
        comodel_name="hc.practitioner.address", 
        inverse_name="practitioner_id", 
        string="Addresses", 
        help="One or more addresses for this practitioner.")
    language_ids = fields.One2many(
        comodel_name="hc.practitioner.language", 
        inverse_name="practitioner_id", 
        string="Languages", 
        help="A language the practitioner is able to use in patient communication.")
    gender = fields.Selection(
        string="Gender", 
        selection=[
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other"), 
            ("unknown", "Unknown")],          
        help="The gender of a practitioner used for administrative purposes.")
    birthdate = fields.Date(
        string="Birth Date", 
        help="The birth date for the practitioner.")
    photo_ids = fields.One2many(
        comodel_name="hc.practitioner.photo", 
        inverse_name="practitioner_id", 
        string="Photos", 
        help="Image of the Practitioner.")
    is_active_practitioner = fields.Boolean(
        string="Active Practitioner", 
        default=True, 
        help="Whether this practitioner's record is in active use.")
    specialty_id = fields.Many2one(
        comodel_name="hc.vs.practitioner.specialty", 
        string="Primary Specialty", 
        help="Primary specialty of the practitioner.")
    qualification_ids = fields.One2many(
        comodel_name="hc.practitioner.qualification", 
        inverse_name="practitioner_id", 
        string="Qualification", 
        help="Qualification obtained by training and certification")
    # role_ids = fields.One2many(
    #     comodel_name="hc.res.practitioner.role", 
    #     inverse_name="practitioner_id", 
    #     string="Role", 
    #     help="Roles/organizations that the practitioner is associated with.")

    # @api.model
    # def create(self, vals):
    #     name = self.env['hc.human.name'].browse(vals['name_id'])
    #     vals['name'] = name.first_id.name+' '+name.surname_id.name
    #     return super(Practitioner, self).create(vals)

    # _defaults = {
    #     "is_company": False,
    #     "customer": False,
    #     "company_type": "person",
    #     "is_person": True,
    #     }

    @api.model
    def create(self, vals):
        vals['is_practitioner'] = self.env.context.get('is_practitioner', False)
        return super(Practitioner, self).create(vals)

class PractitionerIdentifier(models.Model):   
    _name = "hc.practitioner.identifier"  
    _description = "Practitioner Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner who associated with this qualification.")

class PractitionerName(models.Model): 
    _name = "hc.practitioner.name"    
    _description = "Practitioner Name"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.human.name": "human_name_id"}

    human_name_id = fields.Many2one(
        comodel_name="hc.human.name",
        string="Human Name",
        required=True,
        ondelete="restrict", 
        help="Human name associated with this practitioner name.")
    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner associated with this human name.")

class PractitionerTelecom(models.Model):  
    _name = "hc.practitioner.telecom" 
    _description = "Practitioner Telecom"
    _inherit = ["hc.telecom.contact.point"]
    _inherits = {"hc.telecom": "telecom_id"}
 
    telecom_id = fields.Many2one(
        comodel_name="hc.telecom",
        string="Telecom",
        required=True,
        ondelete="restrict",
        help="Telecom contact point associated with this practitioner.")
    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner associated with this telecom contact point.")
        
class PractitionerAddress(models.Model):
    _name = "hc.practitioner.address" 
    _description = "Practitioner Address"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.address": "address_id"}

    address_id = fields.Many2one(
        comodel_name="hc.address", 
        string="Address", 
        required=True,
        ondelete="restrict", 
        help="Address associated with this practitioner.") 
    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner associated with this address.")
    use = fields.Selection(string="Use",
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old")],
        default="home",  
        help="The purpose of this address.")
    type = fields.Selection(string="Type", 
        selection=[
            ("postal", "Postal"), 
            ("physical", "Physical"), 
            ("both", "Both")], 
        default="both", 
        help="Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.")

class PractitionerPhoto(models.Model):   
    _name = "hc.practitioner.photo"  
    _description = "Practitioner Photo"
    _inherits = {"hc.person.photo": "photo_id"}

    photo_id = fields.Many2one(
        comodel_name="hc.person.photo", 
        string="Photo",
        required=True,
        ondelete="restrict",  
        help="Photo associated with this practitioner.")
    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner associated with this photo.")    

class PractitionerLanguage(models.Model):   
    _name = "hc.practitioner.language"  
    _description = "Practitioner Language"
    _inherit = ["hc.basic.association"]

    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner associated with this language.") 
    language_id = fields.Many2one(
        comodel_name="hc.vs.language", 
        string="Language", 
        help="A language the practitioner is able to use in patient communication.")
    proficiency_ids = fields.One2many(
        comodel_name="hc.practitioner.language.proficiency", 
        inverse_name="practitioner_language_id", 
        string="Proficiencies", 
        help="Proficiency of the practitioner with this language.")

class PractitionerLanguageProficiency(models.Model):    
    _name = "hc.practitioner.language.proficiency"  
    _description = "Practitioner Language Proficiency"      
    _inherit = ["hc.basic.association"]

    practitioner_language_id = fields.Many2one(
        comodel_name="hc.practitioner.language", 
        string="Practitioner Language", 
        help="Practitioner language with this proficiency and skill.")              
    language_proficiency_id = fields.Many2one(
        comodel_name="hc.vs.language.proficiency", 
        string="Language Proficiency", 
        help="Language proficiency with this language.")                
    language_skill_id = fields.Many2one(
        comodel_name="hc.vs.language.skill", 
        string="Language Skill", 
        help="Language skill with this language.")                


class PractitionerQualification(models.Model):  
    _name = "hc.practitioner.qualification" 
    _description = "Practitioner Qualification"
    _inherit = ["hc.basic.association"]

    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner associated with this qualification.")
    code_id = fields.Many2one(
        comodel_name="hc.vs.occupation.code", 
        string="Qualification Code", 
        help="Coded representation of the qualification.") 
    identifier_ids = fields.One2many(
        comodel_name="hc.practitioner.qualification.identifier", 
        inverse_name="practitioner_qualification_id", 
        string="Identifiers", 
        help="An identifier for this qualification for the practitioner.")                 
    issuer_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Issuer Organization", 
        help="Organization that regulates and issues the qualification.")        

class PractitionerSpecialty(models.Model):  
    _name = "hc.vs.practitioner.specialty"  
    _description = "Practitioner Specialty"     
    _inherit = ["hc.value.set.contains"]

class PractitionerQualificationIdentifier(models.Model):  
    _name = "hc.practitioner.qualification.identifier"  
    _description = "Practitioner Qualification Identifier" 
    _inherit = ["hc.basic.association", "hc.identifier"]
 
    practitioner_qualification_id = fields.Many2one(
        comodel_name="hc.practitioner.qualification", 
        string="Practitioner Qualification", 
        help="Practitioner Qualification which is associated with this identifier.")

# External Reference

# class Partner(models.Model):
#     _inherit = ["res.partner"]

#     is_practitioner = fields.Boolean(
#         string="Is a practitioner", 
#         help="This partner is a health care practitioner.")

class PersonLink(models.Model):
    _inherit = ["hc.person.link"]

    target_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Target Practitioner", 
        help="Practitioner who is the resource to which this actual person is associated.")

class Annotation(models.Model):
    _inherit = ["hc.annotation"]

    author_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author Practitioner", 
        help="Practitioner responsible for the annotation.")

    @api.multi
    def _compute_author_name(self):
        for hc_annotation in self:
            if hc_annotation.author_type == 'string':
                hc_annotation.author_name = hc_annotation.author_string
            elif hc_annotation.author_type == 'practitioner':
                hc_annotation.author_name = hc_annotation.author_practitioner_id.name