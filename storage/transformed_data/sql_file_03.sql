INSERT INTO cursos ( ID, Nombre, Profesor ) VALUES (1, 'Matem�ticas', 'Dr. Garc�a');
INSERT INTO cursos ( ID, Nombre, Profesor ) VALUES (2, 'Historia', 'Prof. Mart�nez');
INSERT INTO cursos ( ID, Nombre, Profesor ) VALUES (3, 'Ciencias', 'Dr. S�nchez');
INSERT INTO cursos ( ID, Nombre, Profesor ) VALUES (4, 'Ingl�s', 'Prof. Gonz�lez');
INSERT INTO cursos ( ID, Nombre, Profesor ) VALUES (5, 'Geograf�a', 'Dr. Ram�rez');
INSERT INTO estudiantes ( ID, Nombre, Apellido, Edad ) VALUES (1, 'Juan', 'P�rez', 20);
INSERT INTO estudiantes ( ID, Nombre, Apellido, Edad ) VALUES (2, 'Mar�a', 'G�mez', 22);
INSERT INTO estudiantes ( ID, Nombre, Apellido, Edad ) VALUES (3, 'Pedro', 'Rodr�guez', 21);
INSERT INTO estudiantes ( ID, Nombre, Apellido, Edad ) VALUES (4, 'Ana', 'L�pez', 23);
INSERT INTO estudiantes ( ID, Nombre, Apellido, Edad ) VALUES (5, 'Carlos', 'Mart�nez', 25);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (1, 1, 1);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (2, 1, 3);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (3, 2, 2);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (4, 3, 1);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (5, 4, 3);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (6, 5, 2);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (7, 2, 4);
INSERT INTO inscripcion ( ID, ID_Estudiante, ID_Curso ) VALUES (8, 4, 5);