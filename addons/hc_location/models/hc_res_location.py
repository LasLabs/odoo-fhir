# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Location(models.Model):
    _name = "hc.res.location"
    _description = "Location"

    identifier_ids = fields.One2many(
        comodel_name="hc.location.identifier", 
        inverse_name="location_id", 
        string="Identifiers", 
        help="Unique code or number identifying the location to its users.")
    status = fields.Selection(
        string="Status", 
        selection=[
            ("active", "Active"), 
            ("suspended", "Suspended"), 
            ("inactive", "Inactive")], 
        help="Indicates whether the location is still in use.")
    name = fields.Char(
        string="Name", 
        help="Name of the location as used by humans.")
    alias_ids = fields.One2many(
        comodel_name="hc.location.alias", 
        inverse_name="location_id", 
        string="Aliases", 
        help="A list of alternate names that the location is known as, or was known as in the past.")
    description = fields.Text(
        string="Description", 
        help="Description of the Location, which helps in finding or referencing the place.")
    mode = fields.Selection(
        string="Mode", 
        selection=[
            ("instance", "Instance"), 
            ("kind", "Kind")], 
        help="Indicates whether a resource instance represents a specific location or a class of locations.")
    type_id = fields.Many2one(
        comodel_name="hc.vs.location.type", 
        string="Type", 
        help="Indicates the type of function performed at the location.")
    telecom_ids = fields.One2many(
        comodel_name="hc.location.telecom", 
        inverse_name="location_id", 
        string="Telecom", 
        help="Contact details of the location.")
    address_id = fields.Many2one(
        comodel_name="hc.address", 
        string="Address", 
        help="Physical location.")
    physical_type_id = fields.Many2one(
        comodel_name="hc.vs.location.physical.type", 
        string="Physical Type", 
        help="Physical form of the location.")
    longitude = fields.Float(
        string="Longitude", 
        help="Longitude with WGS84 datum.")
    latitude = fields.Float(
        string="Latitude", 
        help="Latitude with WGS84 datum.")
    altitude = fields.Float(
        string="Altitude", 
        help="Altitude with WGS84 datum.")
    managing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Managing Organization", 
        help="The organization that is responsible for the provisioning and upkeep of the location.")
    part_of_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Part Of", 
        help="Another Location which this Location is physically part of.")
    endpoint_ids = fields.One2many(
        comodel_name="hc.location.endpoint", 
        inverse_name="location_id", 
        string="Endpoints", 
        help="Technical endpoints providing access to services operated for the location.")

class LocationIdentifier(models.Model):   
    _name = "hc.location.identifier"  
    _description = "Location Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location", 
        help="Location associated with this Location Identifier.")
    
class LocationTelecom(models.Model):    
    _name = "hc.location.telecom"   
    _description = "Location Telecom"       
    _inherit = ["hc.contact.point.use"] 
    _inherits = {"hc.contact.point": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.contact.point", 
        string="Telecom", 
        ondelete="restrict", 
        required="True", 
        help="Telecom associated with this Location Telecom.")                    
    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location", 
        help="Location associated with this Location Telecom.")                    

class LocationAlias(models.Model):  
    _name = "hc.location.alias" 
    _description = "Location Alias"     
    _inherit = ["hc.basic.association"]

    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location", 
        help="Location associated with this Location Alias.")
    alias = fields.Char(
        string="Alias", 
        help="Alias associated with this Location Alias.")

class LocationEndpoint(models.Model):   
    _name = "hc.location.endpoint"  
    _description = "Location Endpoint"      
    _inherit = ["hc.basic.association"]

    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location", 
        help="Location associated with this Location Endpoint.")
    endpoint_id = fields.Many2one(
        comodel_name="hc.res.endpoint", 
        string="Endpoint", 
        help="Endpoint associated with this Location Endpoint.")

class LocationType(models.Model):  
    _name = "hc.vs.location.type"  
    _description = "Location Type" 
    _inherit = ["hc.value.set.contains"]

class LocationPhysicalType(models.Model):  
    _name = "hc.vs.location.physical.type"  
    _description = "Location Physical Type" 
    _inherit = ["hc.value.set.contains"]

# External Reference

# class PractitionerRoleLocation(models.Model):   
#     _inherit = ["hc.practitioner.role.location"]
                 
#     location_id = fields.Many2one(
#         comodel_name="hc.res.location", 
#         string="Location", 
#         help="Location associated with this practitioner role.")

# class OrganizationLocation(models.Model):
#     _inherit = ["hc.organization.location"] 

#     location_id = fields.Many2one(
#         comodel_name="hc.res.location", 
#         string="Location",
#         help="Location associated with this organization.")