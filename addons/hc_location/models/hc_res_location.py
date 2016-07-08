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
    name = fields.Char(
        string="Name", 
        help="Name of the location as used by humans.")
    description = fields.Char(
        string="Description", 
        help="Description of the Location, which helps in finding or referencing the place.")
    mode = fields.Selection(
        string="Location Mode", 
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
    status = fields.Selection(
        string="Location Status", 
        selection=[
            ("active", "Active"), 
            ("suspended", "Suspended"), 
            ("inactive", "Inactive")], 
        help="Indicates whether the location is still in use.")
    # endpoint_id = fields.Many2one(
    #     comodel_name="hc.res.endpoint", 
    #     string="Endpoint", 
    #     help="Technical endpoints providing access to services operated for the location.")

    class LocationType(models.Model):  
        _name = "hc.vs.location.type"  
        _description = "Location Type" 
        _inherit = ["hc.value.set.contains"]

    class LocationPhysicalType(models.Model):  
        _name = "hc.vs.location.physical.type"  
        _description = "Location Physical Type" 
        _inherit = ["hc.value.set.contains"]

    class locationIdentifier(models.Model):   
        _name = "hc.location.identifier"  
        _description = "location Identifier"
        _inherit = ["hc.basic.association"]
        _inherits = {"hc.identifier": "identifier_id"}

        identifier_id = fields.Many2one(
            comodel_name="hc.identifier",
            string="Identifier",
            required=True,
            ondelete="restrict", 
            help="Identifier associated with this location identifier.")
        location_id = fields.Many2one(
            comodel_name="hc.res.location", 
            string="Location", 
            help="Location associated with this identifier.")
    
    class locationTelecom(models.Model):  
        _name = "hc.location.telecom" 
        _description = "location Telecom"
        _inherit = ["hc.basic.association"]
        _inherits = {"hc.telecom": "telecom_id"}
     
        telecom_id = fields.Many2one(
            comodel_name="hc.telecom",
            string="Telecom",
            required=True,
            ondelete="restrict",
            help="Telecom contact point associated with this location.")
        location_id = fields.Many2one(
            comodel_name="hc.res.location", 
            string="Location", 
            help="location associated with this telecom contact point.")
        use = fields.Selection(
            string="Telecom Use", 
            selection=[
                ("home", "Home"), 
                ("work", "Work"), 
                ("temp", "Temp"),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                ("old", "Old"),
                ("mobile", "Mobile")], 
            help="Purpose of this telecom contact point.")