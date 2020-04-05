# -*- coding: utf-8 -*-

from flectra import models, fields, api

class CarRequest(models.Model):
    _name = "car.request" #table in DB => car_request
    _description = "Car Request"

    name = fields.Char(string="Request", required=True)

    #car request start date
    date_from  = fields.Datetime(
        string='Starting Date',
        default=fields.Datetime.now(),
    )

    #retrieve the requested car model
    car_id = fields.Many2one(
        string="Car",
        comodel_name="fleet.vehicle", 
        required=True,
    )
    
    #car request end date
    date_to = fields.Datetime(
        string = 'End Date',
        required = False,
    )

    #retrieve the employee that wants to request a car
    employee_id = fields.Many2one(
        string = 'Employee',
        comodel_name = 'hr.employee', # this can be found out through the employee list http url as well
        required=True,
    )
    

    
    
    