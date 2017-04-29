# -*- coding: utf-8 -*-

from openerp import models, fields, api

class TestScript(models.Model):    
    _name = "hc.res.test.script"    
    _description = "Test Script"                

    url = fields.Char(
    	string="URI", 
    	required="True", 
    	help="Logical uri to reference this test script (globally unique).")                        
    identifier_id = fields.Many2one(
    	comodel_name="hc.test.script.identifier", 
    	string="Identifier", 
    	help="Additional identifier for the test script.")                        
    version = fields.Char(
    	string="Version", 
    	help="Business version of the test script.")                        
    name = fields.Char(
    	string="Name", 
    	required="True", 
    	help="Name for this test script (Computer friendly).")                        
    title = fields.Text(
    	string="Title", 
    	help="Name for this test script (Human friendly).")                        
    status = fields.Selection(
    	string="Test Script Status", 
    	required="True", 
    	selection=[
    		("draft", "Draft"), 
    		("active", "Active"), 
    		("retired", "Retired")], 
    	help="The status of this test script. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(
    	string="Experimental", 
    	help="If for testing purposes, not real usage.")                        
    publisher = fields.Char(
    	string="Publisher", 
    	help="Name of the publisher (Organization or individual).")                        
    contact_ids = fields.One2many(
    	comodel_name="hc.test.script.contact", 
    	inverse_name="test_script_id", 
    	string="Contacts", 
    	help="Contact details for the publisher.")                        
    date = fields.Datetime(
    	string="Date", 
    	help="Date this was last changed.")                        
    description = fields.Text(
    	string="Description", 
    	help="Natural language description of the test script.")                        
    use_context_ids = fields.One2many(
    	comodel_name="hc.test.script.use.context", 
    	inverse_name="test_script_id", 
    	string="Use Contexts", 
    	help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
    	comodel_name="hc.vs.jurisdiction", 
    	relation="test_script_jurisdiction_rel", 
    	string="Jurisdictions", 
    	help="Intended jurisdiction for test script (if applicable).")                        
    purpose = fields.Text(
    	string="Purpose", 
    	help="Why this test script is defined.")                        
    copyright = fields.Text(
    	string="Copyright", 
    	help="Use and/or publishing restrictions.")                        
    profile_ids = fields.One2many(
    	comodel_name="hc.test.script.profile", 
    	inverse_name="test_script_id", 
    	string="Profiles", 
    	help="Reference of the validation profile.")                        
    origin_ids = fields.One2many(
    	comodel_name="hc.test.script.origin", 
    	inverse_name="test_script_id", 
    	string="Origins", 
    	help="An abstract server representing a client or sender in a message exchange.")                        
    destination_ids = fields.One2many(
    	comodel_name="hc.test.script.destination", 
    	inverse_name="test_script_id", 
    	string="Destinations", 
    	help="An abstract server representing a destination or receiver in a message exchange.")                        
    metadata_ids = fields.One2many(
    	comodel_name="hc.test.script.metadata", 
    	inverse_name="test_script_id", 
    	string="Metadata", 
    	help="Required capability that is assumed to function correctly on the FHIR server being tested.")                        
    fixture_ids = fields.One2many(
    	comodel_name="hc.test.script.fixture", 
    	inverse_name="test_script_id", 
    	string="Fixtures", 
    	help="Fixture in the test script - either by reference (uri) or embedded (Resource).")                        
    variable_ids = fields.One2many(
    	comodel_name="hc.test.script.variable", 
    	inverse_name="test_script_id", 
    	string="Variables", 
    	help="Placeholder for evaluated elements.")                        
    rule_ids = fields.One2many(
    	comodel_name="hc.test.script.rule", 
    	inverse_name="test_script_id", 
    	string="Rules", 
    	required="True", 
    	help="The referenced rule within the ruleset.")                        
    ruleset_ids = fields.One2many(
    	comodel_name="hc.test.script.ruleset", 
    	inverse_name="test_script_id", 
    	string="Rulesets", 
    	help="Assert ruleset used within the test script.")                        
    setup_ids = fields.One2many(
    	comodel_name="hc.test.script.setup", 
    	inverse_name="test_script_id", 
    	string="Setups", 
    	help="A series of required setup operations before tests are executed.")                        
    test_ids = fields.One2many(
    	comodel_name="hc.test.script.test", 
    	inverse_name="test_script_id", 
    	string="Tests", 
    	help="A test in this script.")                        
    teardown_ids = fields.One2many(
    	comodel_name="hc.test.script.teardown", 
    	inverse_name="test_script_id", 
    	string="Teardowns", 
    	help="A series of required clean up steps.")                        

class TestScriptOrigin(models.Model):    
    _name = "hc.test.script.origin"    
    _description = "Test Script Origin"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Origin.")                        
    index = fields.Integer(
    	string="Index", 
    	required="True", 
    	help="The index of the abstract origin server starting at 1.")                        
    profile_id = fields.Many2one(
    	comodel_name="hc.vs.test.script.profile.origin.type", 
    	string="Profile", 
    	required="True", 
    	help="The type of origin profile the test system supports.")                        

class TestScriptDestination(models.Model):    
    _name = "hc.test.script.destination"    
    _description = "Test Script Destination"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Destination.")                        
    index = fields.Integer(
    	string="Index", 
    	required="True", 
    	help="The index of the abstract destination server starting at 1.")                        
    profile_id = fields.Many2one(
    	comodel_name="hc.vs.test.script.profile.destination.type", 
    	string="Profile", 
    	required="True", 
    	help="The type of destination profile the test system supports.")                        

class TestScriptMetadata(models.Model):    
    _name = "hc.test.script.metadata"    
    _description = "Test Script Metadata"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Metadata.")                        
    link_ids = fields.One2many(
    	comodel_name="hc.test.script.metadata.link", 
    	inverse_name="metadata_id", 
    	string="Links", 
    	help="Link this test to the specification.")                        
    capability_ids = fields.One2many(
    	comodel_name="hc.test.script.metadata.capability", 
    	inverse_name="metadata_id", 
    	string="Capabilities", 
    	required="True", 
    	help="Capabilities that are assumed to function correctly on the FHIR server being tested.")                        

class TestScriptMetadataLink(models.Model):    
    _name = "hc.test.script.metadata.link"    
    _description = "Test Script Metadata Link"                

    metadata_id = fields.Many2one(
    	comodel_name="hc.test.script.metadata", 
    	string="Metadata", 
    	help="Metadata associated with this Test Script Metadata Link.")                        
    url = fields.Char(
    	string="URI", 
    	required="True", 
    	help="URL to the specification.")                        
    description = fields.Text(
    	string="Description", 
    	help="Short description.")                        

class TestScriptMetadataCapability(models.Model):    
    _name = "hc.test.script.metadata.capability"    
    _description = "Test Script Metadata Capability"                

    metadata_id = fields.Many2one(
    	comodel_name="hc.test.script.metadata", 
    	string="Metadata", 
    	help="Metadata associated with this Test Script Metadata Capability.")                        
    is_required = fields.Boolean(
    	string="Required", 
    	help="Are the capabilities required?")                        
    is_validated = fields.Boolean(
    	string="Validated", 
    	help="Are the capabilities validated?")                        
    description = fields.Text(
    	string="Description", 
    	help="The expected capabilities of the server.")                        
    origin_ids = fields.One2many(
    	comodel_name="hc.test.script.metadata.capability.origin", 
    	inverse_name="capability_id", 
    	string="Origins", 
    	help="An indicator of the intended usage for the supplemental data element.")                        
    destination = fields.Integer(
    	string="Destination", 
    	help="Which server these requirements apply to.")                        
    link_ids = fields.One2many(
        comodel_name="hc.test.script.metadata.capability.link", 
        inverse_name="capability_id", 
        string="Link URIs", 
        help="An indicator of the intended usage for the supplemental data element.")                      
    capabilities_id = fields.Many2one(
    	comodel_name="hc.res.capability.statement", 
    	string="Capabilities", 
    	required="True", 
    	help="Required Capability Statement.")                        

class TestScriptFixture(models.Model):    
    _name = "hc.test.script.fixture"    
    _description = "Test Script Fixture"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Fixture.")                        
    is_autocreate = fields.Boolean(
    	string="Autocreate", 
    	help="Whether or not to implicitly create the fixture during setup.")                        
    is_autodelete = fields.Boolean(
    	string="Autodelete", 
    	help="Whether or not to implicitly delete the fixture during teardown.")                        
    resource_type = fields.Selection(
    	string="Resource Type", 
    	selection=[
    		("string", "String"), 
    		("Resource Type", "Resource Type")], 
    	help="Type of reference of the resource.")                        
    resource_name = fields.Char(
    	string="Resource", 
    	compute="_compute_resource_name", 
    	store="True", help="Reference of the resource.")                        
    resource_string = fields.Char(
    	string="Resource String", 
    	help="String of reference of the resource.")                        
    resource_code_id = fields.Many2one(
    	comodel_name="hc.vs.resource.type", 
    	string="Resource Code", 
    	help="Code reference of the resource.")                        

class TestScriptVariable(models.Model):    
    _name = "hc.test.script.variable"    
    _description = "Test Script Variable"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Variable.")                        
    name = fields.Char(
    	string="Name", 
    	required="True", 
    	help="Descriptive name for this variable.")                        
    default_value = fields.Char(
    	string="Default Value", 
    	help="Default, hard-coded, or user-defined value for this variable.")                        
    description = fields.Text(
    	string="Description", 
    	help="Natural language description of the variable.")                        
    expression = fields.Char(
    	string="Expression", 
    	help="The fluentpath expression against the fixture body.")                        
    header_field = fields.Char(
    	string="Header Field", 
    	help="HTTP header field name for source.")                        
    hint = fields.Char(
    	string="Hint", 
    	help="Hint help text for default value to enter.")                        
    path = fields.Char(
    	string="Path", 
    	help="XPath or JSONPath against the fixture body.")                        
    source_id = fields.Char(
    	string="Source Id", 
    	help="Fixture Id of source expression or headerField within this variable.")                        

class TestScriptRule(models.Model):    
    _name = "hc.test.script.rule"    
    _description = "Test Script Rule"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Rule.")                        
    resource_type = fields.Selection(
    	string="Resource Type", 
    	required="True", 
    	selection=[
    		("string", "String"), 
    		("Resource Type", "Resource Type")], 
    	help="Type of assert rule resource reference.")                        
    resource_name = fields.Char(
    	string="Resource", 
    	compute="_compute_resource_name", 
    	store="True", help="Assert rule resource reference.")                        
    resource_string = fields.Char(
    	string="Resource String", 
    	help="String of assert rule resource reference.")                        
    resource_code_id = fields.Many2one(
    	comodel_name="hc.vs.resource.type", 
    	string="Resource Code", 
    	help="Code assert rule resource reference.")                        
    param_ids = fields.One2many(
    	comodel_name="hc.test.script.rule.param", 
    	inverse_name="rule_id", 
    	string="Params", 
    	help="Rule parameter template.")                        

class TestScriptRuleParam(models.Model):    
    _name = "hc.test.script.rule.param"    
    _description = "Test Script Rule Param"                

    rule_id = fields.Many2one(
    	comodel_name="hc.test.script.rule", 
    	string="Rule", 
    	help="Rule associated with this Test Script Rule Param.")                        
    name = fields.Char(
    	string="Name", 
    	required="True", 
    	help="Parameter name matching external assert rule parameter.")                        
    value = fields.Char(
    	string="Value", 
    	help="Parameter value defined either explicitly or dynamically.")                        

class TestScriptRuleset(models.Model):    
    _name = "hc.test.script.ruleset"    
    _description = "Test Script Ruleset"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Ruleset.")                        
    resource_type = fields.Selection(
    	string="Resource Type", 
    	required="True", 
    	selection=[
    		("string", "String"), 
    		("Resource Type", "Resource Type")], 
    	help="Type of assert ruleset resource reference.")                        
    resource_name = fields.Char(
    	string="Resource", 
    	compute="_compute_resource_name", 
    	store="True", 
    	help="Assert ruleset resource reference.")                        
    resource_string = fields.Char(
    	string="Resource String", 
    	help="String of assert ruleset resource reference.")                        
    resource_code_id = fields.Many2one(
    	comodel_name="hc.vs.resource.type", 
    	string="Resource Code", 
    	help="Code assert ruleset resource reference.")                        
    rule_ids = fields.One2many(
    	comodel_name="hc.test.script.ruleset.rule", 
    	inverse_name="ruleset_id", 
    	string="Rules", 
    	required="True", 
    	help="The referenced rule within the ruleset.")                        

class TestScriptRulesetRule(models.Model):    
    _name = "hc.test.script.ruleset.rule"    
    _description = "Test Script Ruleset Rule"                

    ruleset_id = fields.Many2one(
    	comodel_name="hc.test.script.ruleset", 
    	string="Ruleset", 
    	help="Ruleset associated with this Test Script Ruleset Rule.")                        
    rule_id = fields.Char(
    	string="Rule Id", 
    	required="True", 
    	help="Id of referenced rule within the ruleset.")                        
    param_ids = fields.One2many(
    	comodel_name="hc.test.script.ruleset.rule.param", 
    	inverse_name="rule_id", 
    	string="Params", 
    	help="Ruleset rule parameter template.")                        

class TestScriptRulesetRuleParam(models.Model):    
    _name = "hc.test.script.ruleset.rule.param"    
    _description = "Test Script Ruleset Rule Param"                

    rule_id = fields.Many2one(
    	comodel_name="hc.test.script.ruleset.rule", 
    	string="Rule", 
    	help="Rule associated with this Test Script Ruleset Rule Param.")                        
    name = fields.Char(
    	string="Name", 
    	required="True", 
    	help="Parameter name matching external assert ruleset rule parameter.")                        
    value = fields.Char(
    	string="Value", 
    	help="Parameter value defined either explicitly or dynamically.")                        

class TestScriptSetup(models.Model):    
    _name = "hc.test.script.setup"    
    _description = "Test Script Setup"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Setup.")                        
    action_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action", 
    	inverse_name="setup_id", 
    	string="Actions", 
    	required="True", 
    	help="A setup operation or assert to perform.")                        

class TestScriptSetupAction(models.Model):    
    _name = "hc.test.script.setup.action"    
    _description = "Test Script Setup Action"                

    setup_id = fields.Many2one(
    	comodel_name="hc.test.script.setup", 
    	string="Setup", 
    	help="Setup associated with this Test Script Setup Action.")                        
    operation_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.operation", 
    	inverse_name="setup_action_id", 
    	string="Operations", 
    	help="The setup operation to perform.")                        
    assert_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.assert", 
    	inverse_name="setup_action_id", 
    	string="Asserts", 
    	help="The assertion to perform.")                        

class TestScriptSetupActionOperation(models.Model):    
    _name = "hc.test.script.setup.action.operation"    
    _description = "Test Script Setup Action Operation"                

    setup_action_id = fields.Many2one(
    	comodel_name="hc.test.script.setup.action", 
    	string="Setup Action", 
    	help="Setup Action associated with this Test Script Setup Action Operation.")                        
    test_action_id = fields.Many2one(
    	comodel_name="hc.test.script.test.action", 
    	string="Test Action", 
    	help="Test Action associated with this Test Script Setup Action Operation.")                        
    teardown_action_id = fields.Many2one(
    	comodel_name="hc.test.script.teardown.action", 
    	string="Teardown Action", 
    	help="Teardown Action associated with this Test Script Setup Action Operation.")                        
    type_id = fields.Many2one(
    	comodel_name="hc.vs.test.script.operation.code", 
    	string="Type", 
    	help="The operation code type that will be executed.")                        
    resource_id = fields.Many2one(
    	comodel_name="hc.vs.defined.type", 
    	string="Resource", 
    	help="Resource type.")                        
    label = fields.Char(
    	string="Label", 
    	help="Tracking/logging operation label.")                        
    description = fields.Text(
    	string="Description", 
    	help="Tracking/reporting operation description.")                        
    accept = fields.Selection(
    	string="Operation Accept", 
    	selection=[
    		("xml", "XML"), 
    		("json", "JSON"), 
    		("ttl", "TTL"), 
    		("none", "None")], 
    	help="The content-type or mime-type to use for RESTful operation in the 'Accept' header.")                        
    content_type = fields.Selection(
    	string="Operation Content Type", 
    	selection=[
    		("xml", "XML"), 
    		("json", "JSON"), 
    		("ttl", "TTL"), 
    		("none", "None")], 
    	help="The content-type or mime-type to use for RESTful operation in the 'Content-Type' header.")                        
    destination = fields.Integer(
    	string="Destination", 
    	help="Server responding to the request.")                        
    is_encode_request_url = fields.Boolean(
    	string="Encode Request URL", 
    	help="Whether or not to send the request url in encoded format.")                        
    origin = fields.Integer(
    	string="Origin", 
    	help="Server initiating the request.")                        
    params = fields.Char(
    	string="Params", 
    	help="Explicitly defined path parameters.")                        
    request_id = fields.Char(
    	string="Request Id", 
    	help="Fixture Id of mapped request.")                        
    response_id = fields.Char(
    	string="Response Id", 
    	help="Fixture Id of mapped response.")                        
    source_id = fields.Char(
    	string="Source Id", 
    	help="Fixture Id of body for PUT and POST requests.")                        
    target_id = fields.Char(
    	string="Target Id", 
    	help="Id of fixture used for extracting the [id], [type], and [vid] for GET requests.")                        
    url = fields.Char(
    	string="URL", 
    	help="Request URL.")                        
    request_header_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.operation.request.header", 
    	inverse_name="operation_id", 
    	string="Request Headers", 
    	help="Each operation can have one ore more header elements.")                        

class TestScriptSetupActionOperationRequestHeader(models.Model):    
    _name = "hc.test.script.setup.action.operation.request.header"    
    _description = "Test Script Setup Action Operation Request Header"                

    operation_id = fields.Many2one(
    	comodel_name="hc.test.script.setup.action.operation", 
    	string="Operation", 
    	help="Operation associated with this Test Script Setup Action Operation Request Header.")                        
    field = fields.Char(
    	string="Field", 
    	required="True", 
    	help="HTTP header field name.")                        
    value = fields.Char(
    	string="Value", 
    	required="True", 
    	help="HTTP header field value.")                        

class TestScriptSetupActionAssert(models.Model):    
    _name = "hc.test.script.setup.action.assert"    
    _description = "Test Script Setup Action Assert"                

    setup_action_id = fields.Many2one(
    	comodel_name="hc.test.script.setup.action", 
    	string="Setup Action", 
    	help="Setup Action associated with this Test Script Setup Action Assert.")                        
    test_action_id = fields.Many2one(
    	comodel_name="hc.test.script.test.action", 
    	string="Test Action", 
    	help="Test Action associated with this Test Script Setup Action Assert.")                        
    label = fields.Char(
    	string="Label", 
    	help="Tracking/logging assertion label.")                        
    description = fields.Text(
    	string="Description", 
    	help="Tracking/reporting assertion description.")                        
    direction = fields.Selection(
    	string="Assert Direction", 
    	selection=[
    		("response", "Response"), 
    		("request", "Request")], 
    	help="The direction to use for the assertion.")                        
    compare_to_source_id = fields.Char(
    	string="Compare To Source Id", 
    	help="Id of the source fixture to be evaluated.")                        
    compare_to_source_expression = fields.Char(
    	string="Compare To Source Expression", 
    	help="The fluentpath expression to evaluate against the source fixture.")                        
    compare_to_source_path = fields.Char(
    	string="Compare To Source Path", 
    	help="XPath or JSONPath expression to evaluate against the source fixture.")                        
    content_type = fields.Selection(
    	string="Assert Content Type", 
    	selection=[
    		("xml", "XML"), 
    		("json", "JSON"), 
    		("ttl", "TTL"), 
    		("none", "None")], 
    	help="The content-type or mime-type to use for RESTful operation in the 'Content-Type' header.")                        
    expression = fields.Char(
    	string="Expression", 
    	help="The fluentpath expression to be evaluated.")                        
    header_field = fields.Char(
    	string="Header Field", 
    	help="HTTP header field name.")                        
    minimum_id = fields.Char(
    	string="Minimum Id", 
    	help="Fixture Id of minimum content resource.")                        
    is_navigation_links = fields.Boolean(
    	string="Navigation Links", 
    	help="Perform validation on navigation links?")                        
    operator = fields.Selection(
        string="Assert Operator", 
        selection=[
            ("equals", "Equals"), 
            ("notequals", "Not Equals"), 
            ("in", "In"), 
            ("notin", "Not In"), 
            ("greaterthan", "Greater Than"), 
            ("lessthan", "Less Than"), 
            ("empty", "Empty"), 
            ("notempty", "Not Empty"), 
            ("contains", "Contains"), 
            ("notcontains", "Not Contains"), 
            ("eval", "Eval")], 
        default="equals",
        help="The operator type defines the conditional behavior of the assert. If not defined, the default is equals.")                        
    path = fields.Char(
    	string="Path", 
    	help="XPath or JSONPath expression.")                        
    request_url = fields.Char(
    	string="Request URL", 
    	help="Request URL comparison value.")                        
    resource_id = fields.Many2one(
    	comodel_name="hc.vs.defined.type", 
    	string="Resource", 
    	help="Resource type.")                        
    response = fields.Selection(
    	string="Assert Response", 
        selection=[
            ("okay", "Okay"), 
            ("created", "Created"), 
            ("nocontent", "No Content"), 
            ("notmodified", "Not Modified"), 
            ("bad", "Bad"), 
            ("forbidden", "Forbidden"), 
            ("notfound", "Not Found"), 
            ("methodnotallowed", "Method Not Allowed"), 
            ("conflict", "Conflict"), 
            ("gone", "Gone"), 
            ("preconditionfailed", "Precondition Failed"), 
            ("unprocessable", "Unprocessable")], 
        help="The type of response code to use for assertion.")                        
    response_code = fields.Char(
    	string="Response Code", 
    	help="HTTP response code to test.")                        
    source_id = fields.Char(
    	string="Source Id", 
    	help="Fixture Id of source expression or headerField.")                        
    validate_profile_id = fields.Char(
    	string="Validate Profile Id", 
    	help="Profile Id of validation profile reference.")                        
    value = fields.Char(
    	string="Value", 
    	help="The value to compare to.")                        
    is_warning_only = fields.Boolean(
    	string="Warning Only", 
    	help="Will this assert produce a warning only on error?.")                        
    rule_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.assert.rule", 
    	inverse_name="assert_id", 
    	string="Rules", 
    	help="The reference to a TestScript.rule.")                        
    ruleset_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.assert.ruleset", 
    	inverse_name="assert_id", 
    	string="Rulesets", 
    	help="The reference to a TestScript.ruleset.")                        

class TestScriptSetupActionAssertRule(models.Model):    
    _name = "hc.test.script.setup.action.assert.rule"    
    _description = "Test Script Setup Action Assert Rule"                

    assert_id = fields.Many2one(
    	comodel_name="hc.test.script.setup.action.assert", 
    	string="Assert", 
    	help="Assert associated with this Test Script Setup Action Assert Rule.")                        
    rule_id = fields.Char(
    	string="Rule Id", 
    	required="True", 
    	help="Id of the TestScript.rule.")                        
    param_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.assert.rule.param", 
    	inverse_name="rule_id", 
    	string="Params", 
    	help="Rule parameter template.")                        

class TestScriptSetupActionAssertRuleParam(models.Model):    
    _name = "hc.test.script.setup.action.assert.rule.param"    
    _description = "Test Script Setup Action Assert Rule Param"                

    rule_id = fields.Many2one(
        comodel_name="hc.test.script.setup.action.assert.rule", 
        string="Rule", 
        help="Rule associated with this Test Script Setup Action Assert Rule Param.")                        
    name = fields.Char(
    	string="Name", 
    	required="True", 
    	help="Parameter name matching external assert rule parameter.")                        
    value = fields.Char(
    	string="Value", 
    	required="True", 
    	help="Parameter value defined either explicitly or dynamically.")                        

class TestScriptSetupActionAssertRuleset(models.Model):    
    _name = "hc.test.script.setup.action.assert.ruleset"    
    _description = "Test Script Setup Action Assert Ruleset"                

    assert_id = fields.Many2one(
    	comodel_name="hc.test.script.setup.action.assert", 
    	string="Assert", 
    	help="Assert associated with this Test Script Setup Action Assert Ruleset.")                        
    ruleset_id = fields.Char(
    	string="Ruleset Id", 
    	required="True", 
    	help="Id of the TestScript.ruleset.")                        
    rule_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.assert.ruleset.rule", 
    	inverse_name="ruleset_id", 
    	string="Rules", 
    	help="The referenced rule within the ruleset.")                        

class TestScriptSetupActionAssertRulesetRule(models.Model):    
    _name = "hc.test.script.setup.action.assert.ruleset.rule"    
    _description = "Test Script Setup Action Assert Ruleset Rule"                

    ruleset_id = fields.Many2one(
    	comodel_name="hc.test.script.setup.action.assert.ruleset", 
    	string="Ruleset", 
    	help="Ruleset associated with this Test Script Setup Action Assert Ruleset Rule.")                        
    rule_id = fields.Char(
    	string="Rule Id", 
    	required="True", 
    	help="Id of referenced rule within the ruleset.")                        
    param_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.assert.ruleset.rule.param", 
    	inverse_name="rule_id", 
    	string="Params", 
    	help="Rule parameter template.")                        

class TestScriptSetupActionAssertRulesetRuleParam(models.Model):    
    _name = "hc.test.script.setup.action.assert.ruleset.rule.param"    
    _description = "Test Script Setup Action Assert Ruleset Rule Param"                

    rule_id = fields.Many2one(
    	comodel_name="hc.test.script.setup.action.assert.ruleset", 
    	string="Rule", 
    	help="Rule associated with this Test Script Setup Action Assert Ruleset Rule Param.")                        
    name = fields.Char(
    	string="Name", 
    	required="True", 
    	help="Parameter name matching external assert ruleset rule parameter.")                        
    value = fields.Char(
    	string="Value", 
    	required="True", 
    	help="Parameter value defined either explicitly or dynamically.")                        

class TestScriptTest(models.Model):    
    _name = "hc.test.script.test"    
    _description = "Test Script Test"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Test.")                        
    name = fields.Char(
    	string="Name", 
    	help="The name of this test.")                        
    description = fields.Text(
    	string="Description", 
    	help="Short description of the test.")                        
    action_ids = fields.One2many(
    	comodel_name="hc.test.script.test.action", 
    	inverse_name="test_id", 
    	string="Actions", 
    	required="True", 
    	help="A test operation or assert to perform.")                        

class TestScriptTestAction(models.Model):    
    _name = "hc.test.script.test.action"    
    _description = "Test Script Test Action"                

    test_id = fields.Many2one(
    	comodel_name="hc.test.script.test", 
    	string="Test", 
    	help="Test associated with this Test Script Test Action.")                        
    operation_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.operation", 
    	inverse_name="test_action_id", 
    	string="Operations", 
    	help="The setup operation to perform.")                        
    assert_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.assert", 
    	inverse_name="test_action_id", 
    	string="Asserts", 
    	help="The setup assertion to perform.")                        

class TestScriptTeardown(models.Model):    
    _name = "hc.test.script.teardown"    
    _description = "Test Script Teardown"                

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Teardown.")                        
    action_ids = fields.One2many(
    	comodel_name="hc.test.script.teardown.action", 
    	inverse_name="teardown_id", 
    	string="Actions", 
    	required="True", 
    	help="One or more teardown operations to perform.")                        

class TestScriptTeardownAction(models.Model):    
    _name = "hc.test.script.teardown.action"    
    _description = "Test Script Teardown Action"                

    teardown_id = fields.Many2one(
    	comodel_name="hc.test.script.teardown", 
    	string="Teardown", 
    	help="Teardown associated with this Test Script Teardown Action.")                        
    operation_ids = fields.One2many(
    	comodel_name="hc.test.script.setup.action.operation", 
    	inverse_name="teardown_action_id", 
    	string="Operations", 
    	required="True", 
    	help="The teardown operation to perform.")                        

class TestScriptIdentifier(models.Model):    
    _name = "hc.test.script.identifier"    
    _description = "Test Script Identifier"             
    _inherit = ["hc.basic.association", "hc.identifier"]    

class TestScriptContact(models.Model):    
    _name = "hc.test.script.contact"    
    _description = "Test Script Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
    	comodel_name="hc.contact.detail", 
    	string="Contact", 
    	ondelete="restrict", 
    	required="True", 
    	help="Contact Detail associated with this Test Script Contact.")                        
    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Contact.")                        

class TestScriptUseContext(models.Model):    
    _name = "hc.test.script.use.context"    
    _description = "Test Script Use Context"          
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Use Context.")                        

class TestScriptProfile(models.Model):    
    _name = "hc.test.script.profile"    
    _description = "Test Script Profile"            
    _inherit = ["hc.basic.association"]    

    test_script_id = fields.Many2one(
    	comodel_name="hc.res.test.script", 
    	string="Test Script", 
    	help="Test Script associated with this Test Script Profile.")                        
    profile_type = fields.Selection(
    	string="Profile Type", 
    	selection=[
    		("string", "String"), 
    		("Resource Type", "Resource Type")], 
    	help="Type of reference of the validation profile.")                        
    profile_name = fields.Char(
    	string="Profile", 
    	compute="_compute_profile_name", 
    	store="True", 
    	help="Reference of the validation profile.")                        
    profile_string = fields.Char(
    	string="Profile String", 
    	help="String of reference of the validation profile.")                        
    profile_code_id = fields.Many2one(
    	comodel_name="hc.vs.resource.type", 
    	string="Profile Code", 
    	help="Code reference of the validation profile.")                        

class TestScriptMetadataCapabilityOrigin(models.Model):    
    _name = "hc.test.script.metadata.capability.origin"    
    _description = "Test Script Metadata Capability Origin"            
    _inherit = ["hc.basic.association"]    

    capability_id = fields.Many2one(
    	comodel_name="hc.test.script.metadata.capability", 
    	string="Capability", 
    	help="Capability associated with this Test Script Metadata Capability Origin.")                        
    origin = fields.Integer(
    	string="Origin", 
    	help="Origin associated with this Test Script Metadata Capability Origin.")                        

class TestScriptMetadataCapabilityLink(models.Model):    
    _name = "hc.test.script.metadata.capability.link"    
    _description = "Test Script Metadata Capability Link"            
    _inherit = ["hc.basic.association"]    

    capability_id = fields.Many2one(
    	comodel_name="hc.test.script.metadata.capability", 
    	string="Capability", 
    	help="Capability associated with this Test Script Metadata Capability Link.")                        
    link = fields.Char(
    	string="Import URL", 
    	help="URL of links to the FHIR specification.")                        

class TestScriptProfileOriginType(models.Model):    
    _name = "hc.vs.test.script.profile.origin.type"    
    _description = "Test Script Profile Origin Type"            
    _inherit = ["hc.value.set.contains"]    

class TestScriptProfileDestinationType(models.Model):    
    _name = "hc.vs.test.script.profile.destination.type"    
    _description = "Test Script Profile Destination Type"            
    _inherit = ["hc.value.set.contains"]    

class TestScriptOperationCode(models.Model):    
    _name = "hc.vs.test.script.operation.code"    
    _description = "Test Script Operation Code"            
    _inherit = ["hc.value.set.contains"]    

