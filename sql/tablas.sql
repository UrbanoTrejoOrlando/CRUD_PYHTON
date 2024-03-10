CREATE TABLE persona (
	clv_persona VARCHAR(5),
	nombre VARCHAR(50) NOT NULL,
	apellido_p VARCHAR(50) NOT NULL,
	apellido_m VARCHAR(50) NOT NULL,
	usuario_nombre VARCHAR(20) NOT NULL,
	contrasenia VARCHAR(10) NOT NULL,
   edad INT NOT NULL,  
   PRIMARY KEY(clv_persona)
);
