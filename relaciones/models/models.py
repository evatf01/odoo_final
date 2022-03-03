# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class relaciones(models.Model):
#     _name = 'relaciones.relaciones'
#     _description = 'relaciones.relaciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date 

class Paquetes(models.Model):
    _name = 'relaciones.paquetes'
    _description = 'relaciones.paquetes'
    cod = fields.Char('COD', required=True)
    peso = fields.Integer('Peso', required=True)
    precio = fields.Integer('Precio', requiered=True)
    total = fields.Integer("Total", compute="_get_total")

    @api.depends('precio')
    def _get_total(self):
        for pers in self:
            pers.total =  pers.precio * pers.peso


class Articulos(models.Model):
    _name = 'relaciones.articulos'
    _description = 'relaciones.articulos'
    cod = fields.Char('COD', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    proveedor = fields.Many2one('relaciones.proveedores', 'Proveedores')
    precio = fields.Float('Precio', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    total = fields.Integer("Total", compute="_get_total")
    
    @api.depends('precio')
    def _get_total(self):
        for pers in self:
            pers.total =  pers.precio * pers.cantidad


class Proveedores(models.Model):
    _name = 'relaciones.proveedores'
    _description = 'relaciones.proveedores'
    cif = fields.Char('CIF', required=True)
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Dirección', required=False)
    poblacion = fields.Char('Población', required=False)
    provincia = fields.Char('Provincia', required=False)
    codPostal = fields.Integer('Cod Postal', required=False)
    telefono = fields.Integer('Telefono', required=True)
    email = fields.Char('Email', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))

        return res


class Clientes(models.Model):
    _name = 'relaciones.clientes'
    _description = 'relaciones.clientes'
    dni = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    provincia = fields.Char('Provincia', required=False)
    codPostal = fields.Integer('Cod Postal', required=False)
    telefono = fields.Integer('Telefono', required=True)
    email = fields.Char('Email', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
    annos = fields.Integer("Años", compute="_get_annos")

    @api.depends('fecha_nacimiento')
    def _get_annos(self):
        for pers in self:
            hoy=date.today()
            pers.annos = relativedelta(hoy, pers.fecha_nacimiento).years



class Destinos(models.Model):
    _name = 'relaciones.destinos'
    _description = 'relaciones.destinos'
    cod = fields.Char('COD', required=True)
    poblacion = fields.Char('Población', required=True)
    provincia = fields.Char('Provincia', required=True)
    codPostal = fields.Integer('CodPostal', required=True)


class Ventas(models.Model):
    _name = 'relaciones.ventas'
    _description = 'relaciones.ventas'
    cod = fields.Char('COD', required=True)
    fecha_venta = fields.Date('Fecha Venta', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    cliente = fields.Many2one('relaciones.clientes', 'Clientes', required=True)
    articulo = fields.Many2one('relaciones.articulos', 'Articulos', required=True)
    destino = fields.Many2one('relaciones.destinos','Destinos', requiered=True)
    precio = fields.Integer()
    cantidad = fields.Integer('Cantidad', required=True)
    paquete = fields.Many2many('relaciones.paquetes', requiered = True)


class Factura(models.Model):
    _name = 'relaciones.factura'
    _description = 'relaciones.factura'
    cod = fields.Char('COD', required=True)
    numLinea = fields.Integer('Numero Linea', requiered=True)
    cliente = fields.Many2one('relaciones.clientes', 'Clientes', required=True)
    venta =  fields.Many2one('relaciones.ventas','Ventas', requiered=True)


    















  




    







