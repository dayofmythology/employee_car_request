# -*- coding: utf-8 -*-

from flectra import models, fields, api

class CarRequest(models.Model):
    _name = "car.request" #table in DB => car_request
    _description = "Car Request"

<<<<<<< HEAD
    name = fields.Char(string="Request", required=True)
=======
    name = fields.Char(string="Request", required=True ,)
>>>>>>> 1ccb438addfb89c3829aafda12f79dd0190bb154

    #car request start date
    date_from  = fields.Datetime(
        string='Starting Date',
<<<<<<< HEAD
        default=fields.Datetime.now(),
    )

    #retrieve the requested car model
    car_id = fields.Many2one(
        string="Car",
        comodel_name="fleet.vehicle", 
        required=True,
=======
        default=fields.Datetime.now,
>>>>>>> 1ccb438addfb89c3829aafda12f79dd0190bb154
    )
    
    #car request end date
    date_to = fields.Datetime(
<<<<<<< HEAD
        string = 'End Date',
        required = False,
=======
        string='End Date',
        required=False
>>>>>>> 1ccb438addfb89c3829aafda12f79dd0190bb154
    )

    #retrieve the employee that wants to request a car
    employee_id = fields.Many2one(
<<<<<<< HEAD
        string = 'Employee',
        comodel_name = 'hr.employee', # this can be found out through the employee list http url as well
        required=True,
    )
    

=======
        string='Employee',
        comodel_name='hr.employee', # this can be found out through the employee list http url as well
        required=True,
    )
    
    #retrieve the requested car model
    field_name_id = fields.Many2one(
        string='car',
        comodel_name='fleet.vehicle', 
        required=True,
    )
>>>>>>> 1ccb438addfb89c3829aafda12f79dd0190bb154
    
    
    