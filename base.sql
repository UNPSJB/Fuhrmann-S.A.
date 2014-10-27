select * from "appWeb_persona"
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Pedro','Santos','23766565','255662','pedro@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Juan','Wheeler','23757565','234662','juan@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Diego','Dominguez','12377666','1366768','diego@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Luis','Carabajal','17102446','1366769','luis@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Mariana','Anacleta','15377666','13668','mariana@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Carolina','Cerati','14377666','13768','carolina@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Roberto','Carlos','14377667','137689','roberto@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Diego','Van Haaster','14377668','137681','diego@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Gloria','Schanz','14377669','137685','gloria@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Sebastian','Lopez','14377676','137686','sebastian@gmail.com', false);
insert into "appWeb_persona"("Nombre", "Apellido", "DNI", "Telefono", "Email", "Baja")
values ('Esteban','Williams','14377688','137687','esteban@gmail.com', false);

select * from "appWeb_productor"
insert into "appWeb_productor"("persona_ptr_id", "CUIL")values ('23766565', '7676767');
insert into "appWeb_productor"("persona_ptr_id", "CUIL")values ('12377666', '12377666');
insert into "appWeb_productor"("persona_ptr_id", "CUIL")values ('17102446', '17102446');
insert into "appWeb_productor"("persona_ptr_id", "CUIL")values ('14377667', '14377667');
insert into "appWeb_productor"("persona_ptr_id", "CUIL")values ('14377688', '14377688');
insert into "appWeb_productor"("persona_ptr_id", "CUIL")values ('14377676', '14377676');
insert into "appWeb_productor"("persona_ptr_id", "CUIL")values ('14377668', '14377668');

select * from "appWeb_representante"
insert into "appWeb_representante"("persona_ptr_id", "NroLegajo","Zona")values ('23757565','1','Sur');
insert into "appWeb_representante"("persona_ptr_id", "NroLegajo","Zona")values ('15377666', '2','Norte' );
insert into "appWeb_representante"("persona_ptr_id", "NroLegajo","Zona")values ('14377666', '3', 'Sur');

select * from "appWeb_estancia"
insert into "appWeb_estancia"("Nombre","CUIT","Provincia","Zona","Baja","Representante_id","Productor_id")values ('La Eloisa','100','Chubut', 'Sur', false,'1','7676767');
insert into "appWeb_estancia"("Nombre","CUIT","Provincia","Zona","Baja","Representante_id","Productor_id")values ('Rio Frio','101','Santa Cruz', 'Sur', false,'2','12377666');
insert into "appWeb_estancia"("Nombre","CUIT","Provincia","Zona","Baja","Representante_id","Productor_id")values ('La Tranquera','102','Rio Negro', 'Norte', false,'3','17102446');

select * from "appWeb_compralote"
insert into "appWeb_compralote"("Representante_id","FechaLlegada")values ('1','10/04/2014');
insert into "appWeb_compralote"("Representante_id","FechaLlegada")values ('2','16/08/2014');
insert into "appWeb_compralote"("Representante_id","FechaLlegada")values ('3','7/10/2014');

select * from "appWeb_lote"
insert into "appWeb_lote"("NroLote","Peso","CantFardos","Baja")values ('1','3000','10', false);
insert into "appWeb_lote"("NroLote","Peso","CantFardos","Baja")values ('2','12000','40', false);
insert into "appWeb_lote"("NroLote","Peso","CantFardos","Baja")values ('3','9000','30', false);

select * from "appWeb_tipofardo"
insert into "appWeb_tipofardo"("Nombre","Descripcion")values ('Vellon','Calidad Alta');
insert into "appWeb_tipofardo"("Nombre","Descripcion")values ('Barriga','Calidad Media');
insert into "appWeb_tipofardo"("Nombre","Descripcion")values ('Garras','Calidad Baja');
insert into "appWeb_tipofardo"("Nombre","Descripcion")values ('Puntas Amarillas','Calidad Baja');
insert into "appWeb_tipofardo"("Nombre","Descripcion")values ('Desborde del vellon','Calidad Media');

select * from "appWeb_cuadricula"
insert into "appWeb_cuadricula"("NroCuadricula")values ('1');

select * from "appWeb_servicio"
insert into "appWeb_servicio" ("Nombre","Descripcion")values ('Lavado','Lava fardos');
insert into "appWeb_servicio" ("Nombre","Descripcion")values ('Peinado','Peina fardos');
insert into "appWeb_servicio" ("Nombre","Descripcion")values ('Cardado','Carda fardos');

select * from "appWeb_maquinaria"
insert into "appWeb_maquinaria" ("NroSerie", "TipoMaquinaria_id", "Descripcion")values ('1','Lavado','Lava');
insert into "appWeb_maquinaria" ("NroSerie", "TipoMaquinaria_id", "Descripcion")values ('2','Peinado','Peina');
insert into "appWeb_maquinaria" ("NroSerie", "TipoMaquinaria_id", "Descripcion")values ('3','Cardado','Carda');


select * from "appWeb_fardo"
insert into "appWeb_fardo"("NroFardo", "TipoFardo_id", "Peso", "Rinde", "Finura", "CV", "AlturaMedia", "Micronaje", "Romana", "Cuadricula_id", "DetalleOrden_id", "Compra_id")
values ()

select * from "appWeb_ordenproduccion"
insert into "appWeb_ordenproduccion"("NroOrden","FechaEmision","CantRequerida","CV","AlturaMedia", "Micronaje", "Romana", "FechaInicioProduccion","FechaFinProduccion", "MaquinaActual_id","EnProduccion","Finalizada")
values ('2','3/10/2014','1000','1','1','1','1','3/07/2014','7/10/2014','2',False,True);

select * from "appWeb_loteventa"
insert into "appWeb_loteventa"("NroPartida", "FechaCierreOrden", "Cantidad", "Cuadricula_id", "Baja", "OrdenProduccion_id")
values ('2','4/10/2014','1','1',False,'2');