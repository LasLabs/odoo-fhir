# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MeasureReport(models.Model):    
    _name = "hc.res.measure.report"    
    _description = "Measure Report"            

    measure_id = fields.Many2one(
        comodel_name="hc.res.measure", 
        string="Measure", 
        required="True", 
        help="Measure that was evaluated.")                    
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("individual", "Individual"), 
            ("patient-list", "Patient List"), 
            ("summary", "Summary")], 
        help="The type of measure report.")                    
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Optional Patient.")                    
    period_start_date = fields.Datetime(
        string="Period Start Date", 
        required="True", 
        help="Start of the reporting period.")                    
    period_end_date = fields.Datetime(
        string="Period End Date", 
        required="True", 
        help="End of the reporting period.")                    
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("complete", "Complete"), 
            ("pending", "Pending"), 
            ("error", "Error")], 
        help="The report status.")                    
    date = fields.Datetime(
        string="Date", 
        help="Date the report was generated.")                    
    reporting_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Reporting Organization", 
        help="Reporting Organization.")                    
    evaluated_resource_id = fields.Many2one(
        comodel_name="hc.res.bundle", 
        string="Evaluated Resource", 
        help="Evaluated Resources.")                    
    group_ids = fields.One2many(
        comodel_name="hc.measure.report.group", 
        inverse_name="measure_report_id", 
        string="Group", 
        help="Measure results for each group.")                    

class MeasureReportGroup(models.Model):    
    _name = "hc.measure.report.group"    
    _description = "Measure Report Group"            

    measure_report_id = fields.Many2one(
        comodel_name="hc.res.measure.report", 
        string="Measure Report", 
        help="Measure Report associated with this group.")                    
    identifier_id = fields.Many2one(
        comodel_name="hc.measure.report.group.identifier", 
        string="Identifier", 
        required="True", 
        help="Identifier of the population group being reported.")                    
    measure_score = fields.Float(
        string="Measure Score", 
        help="The measure score.")                    
    population_ids = fields.One2many(
        comodel_name="hc.measure.report.group.population", 
        inverse_name="group_id", 
        string="Population", 
        help="The populations in the group.")                    
    stratifier_ids = fields.One2many(
        comodel_name="hc.measure.report.group.stratifier", 
        inverse_name="group_id", 
        string="Stratifier", 
        help="Stratification results.")                    
    supplemental_data_ids = fields.One2many(
        comodel_name="hc.measure.report.group.supplemental.data", 
        inverse_name="group_id", 
        string="Supplemental Data", 
        help="Supplemental data elements for the measure.")                    

class MeasureReportGroupPopulation(models.Model):    
    _name = "hc.measure.report.group.population"    
    _description = "Measure Report Group Population"            

    group_id = fields.Many2one(
        comodel_name="hc.measure.report.group", 
        string="Group", 
        help="Measure results for each group.")                    
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("initial-population", "Initial Population"), 
            ("numerator", "Numerator"), 
            ("numerator-exclusion", "Numerator Exclusion"), 
            ("denominator", "Denominator"), 
            ("denominator-exclusion", "Denominator Exclusion"), 
            ("denominator-exception", "Denominator Exception"), 
            ("measure-population", "Measure Population"), 
            ("measure-population-exclusion", "Measure Population Exclusion"), 
            ("measure-score", "Measure Score")], 
        help="The type of the population.")                    
    count = fields.Integer(
        string="Count", 
        help="Size of the population.")                    
    patient_list_id = fields.Many2one(
        comodel_name="hc.res.list", 
        string="Patient List", 
        help="For patient-list reports, the patients in this population.")                    

class MeasureReportGroupStratifier(models.Model):    
    _name = "hc.measure.report.group.stratifier"    
    _description = "Measure Report Group Stratifier"            

    group_id = fields.Many2one(
        comodel_name="hc.measure.report.group", 
        string="Group", 
        help="Measure results for each group.")                    
    identifier_id = fields.Many2one(
        comodel_name="hc.measure.report.group.stratifier.identifier", 
        string="Identifier", 
        required="True", 
        help="Identifier of the stratifier.")                    
    group_ids = fields.One2many(
        comodel_name="hc.measure.report.group.stratifier.group", 
        inverse_name="stratifier_id", 
        string="Group", 
        help="Stratum results, one for each unique value in the stratifier.")                    

class MeasureReportGroupStratifierGroup(models.Model):    
    _name = "hc.measure.report.group.stratifier.group"    
    _description = "Measure Report Group Stratifier Group"            

    stratifier_id = fields.Many2one(
        comodel_name="hc.measure.report.group.stratifier", 
        string="Stratifier", 
        help="Stratification results.")                    
    value = fields.Char(
        string="Value", 
        required="True", 
        help="The stratum value, e.g. male.")                    
    measure_score = fields.Float(
        string="Measure Score", 
        help="The measure score.")                    
    population_ids = fields.One2many(
        comodel_name="hc.measure.report.group.stratifier.group.population", 
        inverse_name="group_id", 
        string="Population", 
        help="Population results in this stratum.")                    

class MeasureReportGroupStratifierGroupPopulation(models.Model):    
    _name = "hc.measure.report.group.stratifier.group.population"    
    _description = "Measure Report Group Stratifier Group Population"            

    group_id = fields.Many2one(
        comodel_name="hc.measure.report.group.stratifier.group", 
        string="Group", 
        help="Stratum results, one for each unique value in the stratifier.")                    
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("initial-population", "Initial Population"), 
            ("numerator", "Numerator"), 
            ("numerator-exclusion", "Numerator Exclusion"), 
            ("denominator", "Denominator"), 
            ("denominator-exclusion", "Denominator Exclusion"), 
            ("denominator-exception", "Denominator Exception"), 
            ("measure-population", "Measure Population"), 
            ("measure-population-exclusion", "Measure Population Exclusion"), 
            ("measure-score", "Measure Score")], 
        help="The type of the population.")                    
    count = fields.Integer(
        string="Count", 
        help="Size of the population.")                    
    patient_list_id = fields.Many2one(
        comodel_name="hc.res.list", 
        string="Patient List", 
        help="For patient-list reports, the patients in this population.")                    

class MeasureReportGroupSupplementalData(models.Model):    
    _name = "hc.measure.report.group.supplemental.data"    
    _description = "Measure Report Group Supplemental Data"            

    group_id = fields.Many2one(
        comodel_name="hc.measure.report.group", 
        string="Group", 
        help="Measure results for each group.")                    
    identifier_id = fields.Many2one(
        comodel_name="hc.measure.report.group.supplemental.data.identifier", 
        string="Identifier", 
        required="True", 
        help="Identifier of the supplemental data element.")                    
    group_ids = fields.One2many(
        comodel_name="hc.measure.report.group.supplemental.data.group", 
        inverse_name="supplemental_data_id", 
        string="Group", 
        help="Supplemental data results, one for each unique supplemental data value.")                    

class MeasureReportGroupSupplementalDataGroup(models.Model):    
    _name = "hc.measure.report.group.supplemental.data.group"    
    _description = "Measure Report Group Supplemental Data Group"            

    supplemental_data_id = fields.Many2one(
        comodel_name="hc.measure.report.group.supplemental.data", 
        string="Supplemental Data", 
        help="Supplemental data elements for the measure.")                    
    value = fields.Char(
        string="Value", 
        required="True", 
        help="The data value, e.g. male.")                    
    count = fields.Integer(
        string="Count", 
        help="Number of members in the group.")                    
    patient_list_id = fields.Many2one(
        comodel_name="hc.res.list", 
        string="Patient List", 
        help="For patient-list reports, the patients in this population.")                    

class MeasureReportGroupIdentifier(models.Model):    
    _name = "hc.measure.report.group.identifier"    
    _description = "Measure Report Group Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

class MeasureReportGroupStratifierIdentifier(models.Model):    
    _name = "hc.measure.report.group.stratifier.identifier"    
    _description = "Measure Report Group Stratifier Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

class MeasureReportGroupSupplementalDataIdentifier(models.Model):    
    _name = "hc.measure.report.group.supplemental.data.identifier"    
    _description = "Measure Report Group Supplemental Data Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    
