# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RelatedPerson(models.Model):  
    _name = "hc.res.related.person" 
    _description = "Related Person"
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person",
        string="Person",
        required=True,
        ondelete="restrict",
        help="Person who is this related person.")
    # identifier_ids = fields.One2many(
    #     comodel_name="hc.related.person.identifier", 
    #     inverse_name="related_person_id", 
    #     string="Identifiers", 
    #     help="A human identifier for this related person.")     
    # name_ids = fields.One2many(
    #     comodel_name="hc.related.person.name", 
    #     inverse_name="related_person_id", 
    #     string="Names", 
    #     help="A name associated with this related person.")
    # telecom_ids = fields.One2many(
    #     comodel_name="hc.person.telecom", 
    #     inverse_name="person_id", 
    #     string="Telecom Contact Points", 
    #     help="A contact detail for this related person.")
    # gender = fields.Selection(
    #     string="Gender", 
    #     selection=[
    #         ("male", "Male"), 
    #         ("female", "Female"), 
    #         ("other", "Other"), 
    #         ("unknown", "Unknown")],          
    #     help="The gender of a related person used for administrative purposes.")
    # address_ids = fields.One2many(
    #     comodel_name="hc.related.person.address", 
    #     inverse_name="related_person_id", 
    #     string="Addresses", 
    #     help="One or more addresses for the person.")
    # attachment_ids = fields.One2many(
    #     comodel_name="hc.related.person.attachment", 
    #     inverse_name="related_person_id", 
    #     string="Attachments", 
    #     help="Image of the related person.")
    patient_ids = fields.One2many(
        comodel_name="hc.related.person.patient",
        inverse_name="related_person_id", 
        string="Patients", 
        required=True, 
        help="Patient(s) related to this person.")

    @api.model
    def create(self, vals):
        vals['is_related_person'] = self.env.context.get('is_related_person', False)
        return super(RelatedPerson, self).create(vals)

class RelatedPersonIdentifier(models.Model):  
    _name = "hc.related.person.identifier" 
    _description = "Related Person Identifier"         
    _inherits = {"hc.person.identifier": "person_identifier_id"}

    person_identifier_id = fields.Many2one(
        comodel_name="hc.person.identifier", 
        string="Person Identifier",
        required=True,
        ondelete="restrict", 
        help="Person identifier associated with this related person.")
    related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Related Person", 
        help="Related person associated with this person identifier.")

class RelatedPersonName(models.Model): 
    _name = "hc.related.person.name"    
    _description = "Related Person Name"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.human.name": "human_name_id"}

    human_name_id = fields.Many2one(
        comodel_name="hc.human.name",
        string="Human Name",
        required=True,
        ondelete="restrict", 
        help="Human name associated with this related person name.")
    related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Related Person", 
        help="Related Person associated with this human name.")

class RelatedPersonTelecom(models.Model):  
    _name = "hc.related.person.telecom" 
    _description = "Related Person Telecom"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.telecom": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.telecom",
        string="Telecom",
        required=True,
        ondelete="restrict",
        help="Telecom contact point associated with this related person.")
    related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Related Person", 
        help="Related person associated with this telecom contact point.")
    use = fields.Selection(string="Telecom Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old"),
            ("mobile", "Mobile")], 
        help="Purpose of this telecom contact point.")

class RelatedPersonAddress(models.Model):
    _name = "hc.related.person.address" 
    _description = "Related Person Address"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.address": "address_id"}

    address_id = fields.Many2one(
        comodel_name="hc.address", 
        string="Address", 
        required=True,
        ondelete="restrict", 
        help="Address associated with this entity.") 
    related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Related Person", 
        help="Related person associated with this address.")

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

class RelatedPersonAttachment(models.Model):   
    _name = "hc.related.person.attachment"  
    _description = "Related Person Attachment"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.attachment": "attachment_id"}

    attachment_id = fields.Many2one(
        comodel_name="hc.attachment", 
        string="Attachment",
        required=True,
        ondelete="restrict",  
        help="Attachment associated with this related person.")
    related_person_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Related Person", 
        help="Related person associated with this attachment.")      

class RelatedPersonRelationshipType(models.Model):  
    _name = "hc.vs.related.person.relationship.type"    
    _description = "Related Person Relationship Type"
    _inherit = ["hc.value.set.contains"]

class RelatedPersonPatient(models.Model): 
    _name = "hc.related.person.patient"    
    _description = "Related Person Patient"
    _inherit = ["hc.basic.association"]

    related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Related Person", 
        help="Related Person associated with this patient.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient",
        string="Patient",
        help="Patient associated with this related person.")
    relationship_id = fields.Many2one(
        comodel_name="hc.vs.related.person.relationship.type", 
        string="Relationship", 
        help="The nature of the relationship.")
    # start_date = fields.Date(
    #     string="Start Date", 
    #     help="Start of the period of time that this relationship is considered valid.")       
    # end_date = fields.Date(
    #     string="End Date", 
    #     help="End of the period of time that this relationship is considered valid.")
    
# External Reference

class Partner(models.Model):
    _inherit = ["res.partner"]

    is_related_person = fields.Boolean(
        string="Is a related person", 
        help="This partner is a related person.")

class PersonLink(models.Model):
    _inherit = ["hc.person.link"]

target_related_person_id = fields.Many2one(
    comodel_name="hc.res.related.person", 
    string="Target Related Person", 
    help="Related Person who is the resource to which this actual person is associated.")

class Patient(models.Model):
    _inherit = ["hc.res.patient"]

    related_person_ids = fields.One2many(
        comodel_name="hc.related.person.patient",
        inverse_name="patient_id",
        string="Related Persons", 
        help="Person(s) related to this patient.")

class Annotation(models.Model):
    _inherit = ["hc.annotation"]

    author_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Author Related Person", 
        help="Related person responsible for the annotation.")

    @api.multi
    def compute_author_name(self):
        for hc_annotation in self:
            if hc_annotation.author_type == 'string':
                hc_annotation.author_name = hc_annotation.author_string
            elif hc_annotation.author_type == 'patient':
                hc_annotation.author_name = hc_annotation.author_patient_id.name
            elif hc_annotation.author_type == 'practitioner':
                hc_annotation.author_name = hc_annotation.author_practitioner_id.name
            elif hc_annotation.author_type == 'related person':
                hc_annotation.author_name = hc_annotation.author_related_person_id.name