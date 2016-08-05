# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Organization(models.Model):   
    _name = "hc.res.organization"   
    _description = "Organization"       
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one(
        comodel_name="res.partner", 
        string="Partner", 
        required=True, 
        ondelete="restrict", 
        help="Partner associated with this organization.")
    identifier_ids = fields.One2many(
        comodel_name="hc.organization.identifier", 
        inverse_name="organization_id", 
        string="Identifiers", 
        help="Identifies this organization across multiple systems.")             
    is_active_organization = fields.Boolean(
        string="Active",
        default=True, 
        help="Whether the organization's record is still in active use.") 
    type_id = fields.Many2one(
        comodel_name="hc.vs.organization.type", 
        string="Type", 
        help="Kind of organization.") 
    name = fields.Char(
        string="Name", 
        help="Name used for the organization.")                      
    telecom_ids = fields.One2many(
        comodel_name="hc.organization.telecom", 
        inverse_name="organization_id", 
        string="Telecom", 
        help="A contact detail for the organization.")             
    address_ids = fields.One2many(
        comodel_name="hc.organization.address", 
        inverse_name="organization_id", 
        string="Addresses", 
        help="An address for the organization.")               
    part_of_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Part Of", 
        help="The organization of which this organization forms a part.")
    endpoint_ids = fields.One2many(
        comodel_name="hc.organization.endpoint", 
        inverse_name="organization_id", 
        string="Endpoints", 
        help="Technical endpoints providing access to services operated for the organization.")
    location_ids = fields.One2many(
        comodel_name="hc.organization.location", 
        inverse_name="organization_id", 
        string="Location", 
        help="A location for this organization.") 
    company_id = fields.Many2one(
        comodel_name="res.company", 
        string="Company", 
        help="The company associated with this organization.")                   
            
    _defaults = {
        "is_company": True,
        "customer": False,
        "company_type": "company",
        }

class OrganizationIdentifier(models.Model):   
    _name = "hc.organization.identifier"  
    _description = "Organization Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this identifier.")

class OrganizationType(models.Model):  
    _name = "hc.vs.organization.type"  
    _description = "Organization Type" 
    _inherit = ["hc.value.set.contains"]

class OrganizationTelecom(models.Model):  
    _name = "hc.organization.telecom" 
    _description = "Organization Telecom"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.telecom": "telecom_id"}
 
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this telecom contact point.")
    telecom_id = fields.Many2one(
        comodel_name="hc.telecom",
        string="Telecom",
        required=True,
        ondelete="restrict",
        help="Telecom contact point associated with this organization.")
    use = fields.Selection(string="Telecom Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old"),
            ("mobile", "Mobile")], 
        help="Purpose of this telecom contact point.")

class OrganizationAddress(models.Model):
    _name = "hc.organization.address" 
    _description = "Organization Address"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.address": "address_id"}

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this address.")
    address_id = fields.Many2one(
        comodel_name="hc.address", 
        string="Address", 
        required=True,
        ondelete="restrict", 
        help="Address associated with this organization.") 
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

class OrganizationEndpoint(models.Model):
    _name = "hc.organization.endpoint" 
    _description = "Organization Endpoint"
    _inherit = ["hc.basic.association"]
    # _inherits = {"hc.res.endpoint": "endpoint_id"}

    # endpoint_id = fields.Many2one(
    #     comodel_name="hc.res.endpoint", 
    #     string="Endpoint",
    #     equired=True,
    #     ondelete="restrict", 
    #     help="Endpoint associated with this organization.")
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this endpoint.")

class OrganizationLocation(models.Model):
    _name = "hc.organization.location" 
    _description = "Organization Location"
    _inherit = ["hc.basic.association"]

    # location_id = fields.Many2one(
    #     comodel_name="hc.res.location", 
    #     string="Location",
    #     help="Location associated with this organization.")
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this location.")
    
class OrganizationContact(models.Model):    
    _name = "hc.organization.contact"   
    _description = "Organization Contact"       
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Person",
        required=True,
        ondelete="restrict", 
        help="Person associated with this organization contact.") 
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this identifier.")
    purpose_id = fields.Many2one(
        comodel_name="hc.vs.contact.entity.type", 
        string="Purpose", 
        help="The type of contact.")              
    name_id = fields.Many2one(
        comodel_name="hc.human.name", 
        string="Name", 
        help="A name associated with the organization contact.")              
    # telecom_ids = fields.One2many(
    #     comodel_name="hc.organization.contact.telecom", 
    #     inverse_name="organization_contact_id", 
    #     string="Telecom Contacts", 
    #     help="Contact details (telephone, email, etc.) for a contact.")             
    # address_ids = fields.One2many(
    #     comodel_name="hc.organization.contact.address",
    #     inverse_name="organization_contact_id",  
    #     string="Addresses", 
    #     help="Visiting or postal addresses for the organization contact.")             

class OrganizationContactPurpose(models.Model): 
    _name = "hc.vs.contact.entity.type"    
    _description = "Organization Contact Purpose"       
    _inherit = ["hc.value.set.contains"]

class OrganizationContactAddress(models.Model):
    _name = "hc.organization.contact.address" 
    _description = "Organization Contact Address"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.address": "address_id"}

    organization_contact_id = fields.Many2one(
        comodel_name="hc.organization.contact", 
        string="Organization Contact", 
        help="Organization contact associated with this address.")
    address_id = fields.Many2one(
        comodel_name="hc.address", 
        string="Address", 
        required=True,
        ondelete="restrict", 
        help="Address associated with this organization contact.") 
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

class OrganizationContactName(models.Model): 
    _name = "hc.organization.contact.name"    
    _description = "Organization Contact Name"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.human.name": "human_name_id"}

    human_name_id = fields.Many2one(
        comodel_name="hc.human.name",
        string="Human Name",
        required=True,
        ondelete="restrict", 
        help="Human name associated with this organization contact.")
    organization_contact_id = fields.Many2one(
        comodel_name="hc.organization.contact", 
        string="Organization Contact", 
        help="Organization contact associated with this human name.")

class OrganizationContactTelecom(models.Model):  
    _name = "hc.organization.contact.telecom" 
    _description = "Organization Contact Telecom"
    _inherit = ["hc.basic.association"]
    _inherits = {"hc.telecom": "telecom_id"}
 
    telecom_id = fields.Many2one(
        comodel_name="hc.telecom",
        string="Telecom",
        required=True,
        ondelete="restrict",
        help="Telecom contact point associated with this organization contact.")
    organization_contact_id = fields.Many2one(
        comodel_name="hc.organization.contact", 
        string="Organization Contact", 
        help="Organization contact associated with this telecom contact point.")
    use = fields.Selection(
        string="Telecom Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old"),
            ("mobile", "Mobile")], 
        help="Purpose of this telecom contact point.")

# External Reference

class Partner(models.Model):
 
    _inherit = ["res.partner"]

    is_organization = fields.Boolean(
        string="Is an Organization", 
        help="This partner is a health care-related organization record.")     
    is_organization_contact = fields.Boolean(
        string="Is an Organization Contact", 
        help="This partner is an organization contact.")

class Identifier(models.Model):
    _inherit = ["hc.identifier"]

    identifier_assigner_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Identifier Assigner Organization", 
        help="Organization that issued id (may be just text).")

class Person(models.Model):
    _inherit = ["hc.res.person"]

    person_managing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Person Managing Organization", 
        help="Organization that is the custodian of the person record.")

class Patient(models.Model):
    _inherit = ["hc.res.patient"]

    patient_managing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Patient Managing Organization", 
        help="Organization that is the custodian of the patient record.")

class PatientCareProviderOrganization(models.Model):
    _inherit = ["hc.patient.care.provider.organization"]

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this care provider.")

class PatientContact(models.Model):
    _inherit = ["hc.patient.contact"]

    patient_contact_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Patient Contact Organization", 
        help="Organization that is associated with the contact.")

class PractitionerQualification(models.Model):
    _inherit = ["hc.practitioner.qualification"]
    
    qualification_issuer_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Qualification Issuer Organization", 
        help="Organization that regulates and issues the qualification.")        

class PractitionerRole(models.Model):
    _inherit = ["hc.res.practitioner.role"]
    
    practitioner_role_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Practitioner Role Organization", 
        help="Organization where the roles are performed.")