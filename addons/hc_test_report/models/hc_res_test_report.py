# -*- coding: utf-8 -*-

from openerp import models, fields, api

class TestReport(models.Model):    
    _name = "hc.res.test.report"    
    _description = "Test Report"                

    identifier_id = fields.Many2one(comodel_name="hc.test.report.identifier", string="Identifier", help="External identifier.")                        
    name = fields.Char(string="Name", help="Informal name of the executed TestScript.")                        
    status = fields.Selection(string="Test Report Status", required="True", selection=[("complete", "Complete"), ("pending", "Pending"), ("error", "Error")], help="The status of the Test Report.")                        
    score = fields.Float(string="Score", help="The final score (percentage of tests passed) resulting from the execution of the TestScript.")                        
    tester = fields.Char(string="Tester", help="Name of the tester producing this report (Organization or individual).")                        
    test_script_id = fields.Many2one(comodel_name="hc.res.test.script", string="Test Script", required="True", help="Reference to the version-specific TestScript that was executed to produce this TestReport.")                        
    issued = fields.Datetime(string="Issued", help="When the TestScript was executed and this TestReport was generated.")                        
    participant_ids = fields.One2many(comodel_name="hc.test.report.participant", inverse_name="test_report_id", string="Participants", help="A participant in the test execution, either the execution engine, a client, or a server.")                        
    setup_ids = fields.One2many(comodel_name="hc.test.report.setup", inverse_name="test_report_id", string="Setups", help="The results of the series of required setup operations before the tests were executed.")                        
    teardown_ids = fields.One2many(comodel_name="hc.test.report.teardown", inverse_name="test_report_id", string="Teardowns", help="The results of running the series of required clean up steps.")                        
    test_ids = fields.One2many(comodel_name="hc.test.report.test", inverse_name="test_report_id", string="Tests", help="A test executed from the test script.")                        

class TestReportParticipant(models.Model):    
    _name = "hc.test.report.participant"    
    _description = "Test Report Participant"                

    test_report_id = fields.Many2one(comodel_name="hc.res.test.report", string="Test Report", help="Test Report associated with this Test Report Participant.")                        
    type = fields.Selection(string="Participant Type", required="True", selection=[("test-engine", "Test-Engine"), ("client", "Client"), ("server", "Server")], help="The type of participant.")                        
    uri = fields.Char(string="URI", required="True", help="The uri of the participant. An absolute URL is preferred.")                        
    display = fields.Char(string="Display", help="The display name of the participant.")                        

class TestReportSetup(models.Model):    
    _name = "hc.test.report.setup"    
    _description = "Test Report Setup"                

    test_report_id = fields.Many2one(comodel_name="hc.res.test.report", string="Test Report", help="Test Report associated with this Test Report Setup.")                        
    action_ids = fields.One2many(comodel_name="hc.test.report.setup.action", inverse_name="setup_id", string="Actions", required="True", help="A setup operation or assert that was executed.")                        

class TestReportSetupAction(models.Model):    
    _name = "hc.test.report.setup.action"    
    _description = "Test Report Setup Action"                

    setup_id = fields.Many2one(comodel_name="hc.test.report.setup", string="Setup", help="The results of the series of required setup operations before the tests were executed.")                        
    assert_ids = fields.One2many(comodel_name="hc.test.report.setup.action.assert", inverse_name="setup_action_id", string="Asserts", help="The assertion to perform.")                        
    operation_ids = fields.One2many(comodel_name="hc.test.report.setup.action.operation", inverse_name="setup_action_id", string="Operations", help="The operation to perform.")                        

class TestReportSetupActionOperation(models.Model):    
    _name = "hc.test.report.setup.action.operation"    
    _description = "Test Report Setup Action Operation"                

    setup_action_id = fields.Many2one(comodel_name="hc.test.report.setup.action", string="Setup Action", help="A setup operation or assert that was executed.")                        
    test_action_id = fields.Many2one(comodel_name="hc.test.report.test.action", string="Test Action", help="One or more teardown operations performed.")                        
    teardown_action_id = fields.Many2one(comodel_name="hc.test.report.teardown.action", string="Teardown Action", help="A test operation or assert that was performed.")                        
    result = fields.Selection(string="Operation Result", required="True", selection=[("pass", "Pass"), ("skip", "Skip"), ("fail", "Fail"), ("warning", "Warning"), ("error", "Error")], help="The result of this operation.")                        
    message = fields.Text(string="Message", help="A message associated with the result.")                        
    detail = fields.Char(string="Detail URI", help="A link to further details on the result.")                        

class TestReportSetupActionAssert(models.Model):    
    _name = "hc.test.report.setup.action.assert"    
    _description = "Test Report Setup Action Assert"                

    setup_action_id = fields.Many2one(comodel_name="hc.test.report.setup.action", string="Setup Action", help="A setup operation or assert that was executed.")                        
    test_action_id = fields.Many2one(comodel_name="hc.test.report.test.action", string="Test Action", help="A test operation or assert that was performed.")                        
    result = fields.Selection(string="Assert Result", required="True", selection=[("pass", "Pass"), ("skip", "Skip"), ("fail", "Fail"), ("warning", "Warning"), ("error", "Error")], help="The result of this assertion.")                        
    message = fields.Text(string="Message", help="A message associated with the result.")                        
    detail = fields.Char(string="Detail", help="A link to further details on the result.")                        

class TestReportTest(models.Model):    
    _name = "hc.test.report.test"    
    _description = "Test Report Test"                

test_report_id = fields.Many2one(comodel_name="hc.res.test.report", string="Test Report", help="Test Report associated with this Test Report Test.")                        
name = fields.Char(string="Name", help="Tracking/logging name of this test.")                        
description = fields.Text(string="Description", help="Tracking/reporting short description of the test.")                        
action_ids = fields.One2many(comodel_name="hc.test.report.test.action", inverse_name="test_id", string="Actions", required="True", help="A test operation or assert that was performed.")                        

class TestReportTestAction(models.Model):    
    _name = "hc.test.report.test.action"    
    _description = "Test Report Test Action"                

test_id = fields.Many2one(comodel_name="hc.test.report.test", string="Test", help="A test executed from the test script.")                        
operation_ids = fields.One2many(comodel_name="hc.test.report.test.action.operation", inverse_name="test_action_id", string="Operations", help="The operation performed.")                        
assert_ids = fields.One2many(comodel_name="hc.test.report.test.action.assert", inverse_name="test_action_id", string="Asserts", help="The assertion performed.")                        

class TestReportTeardown(models.Model):    
    _name = "hc.test.report.teardown"    
    _description = "Test Report Teardown"                

    test_report_id = fields.Many2one(comodel_name="hc.res.test.report", string="Test Report", help="Test Report associated with this Test Report Teardown.")                        
    action_ids = fields.One2many(comodel_name="hc.test.report.teardown.action", inverse_name="teardown_id", string="Actions", required="True", help="One or more teardown operations performed.")                        

class TestReportTeardownAction(models.Model):    
    _name = "hc.test.report.teardown.action"    
    _description = "Test Report Teardown Action"                

    teardown_id = fields.Many2one(comodel_name="hc.test.report.teardown", string="Teardown", help="The results of running the series of required clean up steps.")                        
    operation_ids = fields.One2many(comodel_name="hc.test.report.teardown.action.operation", inverse_name="teardown_action_id", string="Operations", required="True", help="The teardown operation performed.")                        

class TestReportIdentifier(models.Model):    
    _name = "hc.test.report.identifier"    
    _description = "Test Report Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]    
