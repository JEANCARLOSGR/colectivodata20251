import pandas as pd

# Suponiendo que el dataframe se llama 'dataFrameUsuarios'
dataFrameUsuarios = pd.read_csv("./data/usuarios.csv")

# FILTROS Y CONDICIONES PARA TRANSFORMAR DATOS
# 1. Solo estudiantes
soloEstudiantes = dataFrameUsuarios.query('tipo=="estudiante"')
# 2. Solo profesores
soloProfesores = dataFrameUsuarios.query('tipo=="profesor"')
# 3. Todos excepto estudiantes
todosExceptoEstudiantes = dataFrameUsuarios.query('tipo!="estudiante"')
# 4. Filtrar por especialidad
porEspecialidad = dataFrameUsuarios.query('especialidad=="[especialidad]"')  # Reemplaza [especialidad] por la especialidad deseada
# 5. Excluir una especialidad
excluirEspecialidad = dataFrameUsuarios.query('especialidad!="[especialidad]"')  # Reemplaza [especialidad] por la especialidad a excluir
# 6. Excluir administrativos
noAdministrativos = dataFrameUsuarios.query('tipo!="administrativo"')
# 7. Direcciones en Medellín
direccionesMedellin = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains("Medellín", na=False)]
# 8. Direcciones terminadas en sur
direccionesSur = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.endswith("sur", na=False)]
# 9. Direcciones que inician con calle
direccionesCalle = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.startswith("calle", na=False)]
# 10. Especialidades que contienen la palabra "datos"
especialidadesDatos = dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.contains("datos", na=False)]
# 11. Instructores en Itagüí
instructoresItagui = dataFrameUsuarios.query('tipo=="instructor" and direccion.str.contains("Itagüí", na=False)')
# 12. Nacidos después de 2000
nacidosDespuesDe2000 = dataFrameUsuarios[dataFrameUsuarios['fecha_nacimiento'].apply(lambda x: pd.to_datetime(x).year > 2000)]
# 13. Nacidos en los 90
nacidosEnLos90 = dataFrameUsuarios[dataFrameUsuarios['fecha_nacimiento'].apply(lambda x: 1990 <= pd.to_datetime(x).year <= 1999)]
# 14. Direcciones en Envigado
direccionesEnvigado = dataFrameUsuarios[dataFrameUsuarios['direccion'].str.contains("Envigado", na=False)]
# 15. Especialidades que empiezan por "I"
especialidadesI = dataFrameUsuarios[dataFrameUsuarios['especialidad'].str.startswith("I", na=False)]
# 16. Usuarios sin dirección
usuariosSinDireccion = dataFrameUsuarios[dataFrameUsuarios['direccion'].isnull()]
# 17. Usuarios sin especialidad
usuariosSinEspecialidad = dataFrameUsuarios[dataFrameUsuarios['especialidad'].isnull()]
# 18. Profesores que viven en Sabaneta
profesoresSabaneta = dataFrameUsuarios.query('tipo=="profesor" and direccion.str.contains("Sabaneta", na=False)')
# 19. Aprendices que viven en Bello
aprendicesBello = dataFrameUsuarios.query('tipo=="aprendiz" and direccion.str.contains("Bello", na=False)')
# 20. Nacidos en el nuevo milenio
nacidosNuevoMileno = dataFrameUsuarios[dataFrameUsuarios['fecha_nacimiento'].apply(lambda x: pd.to_datetime(x).year >= 2000)]

# AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
# 1. Total por tipo
totalPorTipo = dataFrameUsuarios.groupby('tipo').size()
# 2. Total por especialidad
totalPorEspecialidad = dataFrameUsuarios.groupby('especialidad').size()
# 3. Cantidad de especialidades distintas
cantidadEspecialidadesDistintas = dataFrameUsuarios['especialidad'].nunique()
# 4. Tipos de usuario por especialidad
tiposPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['tipo'].unique()
# 5. Usuario más antiguo por tipo
usuarioMasAntiguoPorTipo = dataFrameUsuarios.groupby('tipo')['fecha_nacimiento'].min()
# 6. Usuario más joven por tipo
usuarioMasJovenPorTipo = dataFrameUsuarios.groupby('tipo')['fecha_nacimiento'].max()
# 7. Primer registro por tipo
primerRegistroPorTipo = dataFrameUsuarios.sort_values('fecha_nacimiento').groupby('tipo').first()
# 8. Último registro por tipo
ultimoRegistroPorTipo = dataFrameUsuarios.sort_values('fecha_nacimiento').groupby('tipo').last()
# 9. Combinación tipo por especialidad
combinacionTipoPorEspecialidad = dataFrameUsuarios.groupby(['tipo', 'especialidad']).size()
# 10. El más viejo por especialidad
masViejoPorEspecialidad = dataFrameUsuarios.groupby('especialidad')['fecha_nacimiento'].min()
# 11. Cuántos de cada especialidad por tipo
cantidadPorEspecialidadYTipo = dataFrameUsuarios.groupby(['especialidad', 'tipo']).size()
# 12. Edad promedio por tipo
edadPromedioPorTipo = dataFrameUsuarios.groupby('tipo').apply(lambda x: (pd.to_datetime('today') - pd.to_datetime(x['fecha_nacimiento'])).dt.days.mean() // 365)
# 13. Años de nacimiento más frecuente por especialidad
anioNacimientoMasFrecuentePorEspecialidad = dataFrameUsuarios.groupby('especialidad')['fecha_nacimiento'].apply(lambda x: pd.to_datetime(x).dt.year.mode()[0])
# 14. Mes de nacimiento más frecuente por tipo
mesNacimientoMasFrecuentePorTipo = dataFrameUsuarios.groupby('tipo')['fecha_nacimiento'].apply(lambda x: pd.to_datetime(x).dt.month.mode()[0])
# 15. UNA CONSULTA O FILTRO QUE UD PROPONGA
# Aquí puedes agregar cualquier filtro o agrupación que desees, por ejemplo:
# Filtrar por tipo de usuario y dirección específica
usuariosEnUnaDireccion = dataFrameUsuarios.query('tipo=="estudiante" and direccion.str.contains("Calle 100", na=False)')
