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
        help="Person who is this patient.")
    # name_id = fields.Many2one(
    #     comodel_name="hc.human.name",
    #     string="Full Name",
    #     help="Related person's First Name and Last Name")
    # identifier_ids = fields.One2many(
    #     comodel_name="hc.related.person.identifier", 
    #     inverse_name="related_person_id", 
    #     string="Identifiers", 
    #     help="A human identifier for this related person.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        required=True, 
        help="The patient this person is related to.")     
    relationship_id = fields.Many2one(
        comodel_name="hc.vs.related.person.relationship.type", 
        string="Relationship", 
        help="The nature of the relationship.")
    # name_ids = fields.One2many(
    #     comodel_name="hc.related.person.name", 
    #     inverse_name="related_person_id", 
    #     string="Names", 
    #     help="A name associated with this related person.")
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
    start_date = fields.Date(
        string="Start Date", 
        help="Start of the period of time that this relationship is considered valid.")       
    end_date = fields.Date(
        string="End Date", 
        help="End of the period of time that this relationship is considered valid.")

class PersonLink(models.Model):
    _inherit = ["hc.person.link"]

target_related_person_id = fields.Many2one(
    comodel_name="hc.res.related.person", 
    string="Target Related Person", 
    help="Related Person who is the resource to which this actual person is associated.")

class RelatedPersonRelationshipType(models.Model):  
    _name = "hc.vs.related.person.relationship.type"    
    _description = "Related Person Relationship Type"
    _inherit = ["hc.value.set.contains"]

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

# External Reference

# class Partner(models.Model):
#     _inherit = ["res.partner"]

#     is_related_person = fields.Boolean(
#         string="Is a related person", 
#         help="This partner is a related person.")

class Annotation(models.Model):
    _inherit = ["hc.annotation"]

    author_related_person_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Author Related Person", 
        help="Related person responsible for the annotation.")