# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DeviceUseStatement(models.Model):	
    _name = "hc.res.device.use.statement"	
    _description = "Device Use Statement"		

    body_site_type = fields.Selection(string="Body Site Type", selection=[("code", "Code"), ("Body Site", "Body Site")], help="Type of definition or protocol.")				
    body_site_name = fields.Char(string="Body Site", compute="_compute_body_site_name", store="True", help="Target body site.")				
    body_site_code_id = fields.Many2one(comodel_name="hc.vs.body.site.code", string="Body Site Code", help="Code of the target body site.")				
    body_site_id = fields.Many2one(comodel_name="hc.res.body.site", string="Body Site", help="Body Site target body site.")				
    when_used_start_date = fields.Datetime(string="When Used Start Date", help="Start of the period when used.")				
    when_used_end_date = fields.Datetime(string="When Used End Date", help="End of the period when used.")				
    device_id = fields.Many2one(comodel_name="hc.res.device", string="Device", required="True", help="Period when used.")				
    identifier_ids = fields.One2many(comodel_name="hc.device.use.statement.identifier", inverse_name="device_use_statement_id", string="Identifiers", help="Period when used.")				
    indication_ids = fields.Many2many(comodel_name="hc.vs.act.reason", string="Indications", help="Reason or justification for the use of the device.")			
    note_ids = fields.One2many(comodel_name="hc.device.use.statement.note", inverse_name="device_use_statement_id", string="Notes", help="Details about the device statement that were not represented at all or sufficiently in one of the attributes provided in a class. These may include for example a comment, an instruction, or a note associated with the statement.")				
    recorded_on = fields.Datetime(string="Recorded On", help="The time at which the statement was made/recorded.")				
    subject_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject", required="True", help="The patient who used the device.")				
    timing_type = fields.Selection(string="Timing Type", selection=[("Timing", "Timing"), ("Period", "Period"), ("dateTime", "Datetime")], help="Type of how often the device was used.")				
    timing_name = fields.Char(string="Timing", compute="_compute_timing_name", store="True", help="How often the device was used.")				
    timing_ids = fields.Many2one(comodel_name="hc.device.use.statement.timing", string="Timing", help="Timing the patient used the device.")				
    timing_start_date = fields.Datetime(string="Scheduled Start Date", help="Start of the period when the patient used the device.")				
    timing_end_date = fields.Datetime(string="Scheduled End Date", help="End of the period when the patient used the device.")				
    timing = fields.Datetime(string="Timing Date", help="Datetime the patient used the device.")				

class DeviceUseStatementIdentifier(models.Model):	
    _name = "hc.device.use.statement.identifier"	
    _description = "Device Use Statement Identifier"		
    _inherit = ["hc.basic.association", "hc.identifier"]

    device_use_statement_id = fields.Many2one(
        comodel_name="hc.res.device.use.statement", 
        string="Device Use Statement", 
        help="Device Use Statement associated with this Device Use Statement Identifier.")				

class DeviceUseStatementNote(models.Model):	
    _name = "hc.device.use.statement.note"	
    _description = "Device Use Statement Note"		
    _inherit = ["hc.basic.association", "hc.annotation"]

    device_use_statement_id = fields.Many2one(
        comodel_name="hc.res.device.use.statement", 
        string="Device Use Statement", 
        help="Device Use Statement associated with this Device Use Statement Note.")				

class DeviceUseStatementTiming(models.Model):	
    _name = "hc.device.use.statement.timing"	
    _description = "Device Use Statement Timing"		
    _inherit = ["hc.basic.association", "hc.timing"]			
