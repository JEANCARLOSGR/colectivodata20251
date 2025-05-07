import pandas as pd

dataFrameAsistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

# ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
print(dataFrameAsistencia['estado'].unique())
print(dataFrameAsistencia['estrato'].unique())
print(dataFrameAsistencia['medio_transporte'].unique())

# FILTROS Y CONDICIONES PARA TRANSFORMAR DATOS
# 1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron = dataFrameAsistencia.query('estado=="asistio"')
# 2. Reportar todos los estudiantes que faltaron
estudiantesQueFaltaron = dataFrameAsistencia.query('estado=="inasistencia"')
# 3. Reportar todos los estudiantes que llegaron tarde (Justificado)
estudiantesQueLlegaronTarde = dataFrameAsistencia.query('estado=="tarde"')
# 4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno = dataFrameAsistencia.query('estrato==1')
# 5. Reportar todos los estudiantes de estratos altos (estrato >= 4)
estudiantesEstratosAltos = dataFrameAsistencia.query('estrato >= 4')
# 6. Reportar todos los estudiantes que llegan en metro
estudiantesQueUsanMetro = dataFrameAsistencia.query('medio_transporte=="metro"')
# 7. Reportar todos los estudiantes que llegan en bicicleta
estudiantesQueUsanBicicleta = dataFrameAsistencia.query('medio_transporte=="bicicleta"')
# 8. Reportar todos los estudiantes que no caminan para llegar a la universidad
estudiantesQueNoCaminan = dataFrameAsistencia.query('medio_transporte!="a pie"')
# 9. Reportar todos los registros de asistencia del mes de junio (suponiendo que tienes una columna de fecha)
estudiantesJunio = dataFrameAsistencia[dataFrameAsistencia['fecha'].str.contains("06", na=False)]
# 10. Reportar los estudiantes que faltaron y usan bus para llegar a la universidad
estudiantesQueFaltanUsanBus = dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
# 11. Reportar estudiantes que usan bus y son de estratos altos
estudiantesBusEstratosAltos = dataFrameAsistencia.query('medio_transporte=="bus" and estrato>=4')
# 12. Reportar estudiantes que usan bus y son de estratos bajos
estudiantesBusEstratosBajos = dataFrameAsistencia.query('medio_transporte=="bus" and estrato<=3')
# 13. Reportar estudiantes que llegan tarde y son de estrato 3, 4, 5 o 6
estudiantesTardeEstratosAltos = dataFrameAsistencia.query('estado=="tarde" and estrato in [3, 4, 5, 6]')
# 14. Reportar estudiantes que usan transportes ecológicos (bicicleta, metro)
estudiantesTransporteEcológico = dataFrameAsistencia.query('medio_transporte in ["bicicleta", "metro"]')
# 15. Reportar estudiantes que faltan y usan carro para transportarse
estudiantesFaltanUsanCarro = dataFrameAsistencia.query('medio_transporte=="carro" and estado=="inasistencia"')
# 16. Reportar estudiantes que asisten, son de estratos altos y caminan
estudiantesAsistenEstratosAltosCaminan = dataFrameAsistencia.query('estado=="asistio" and estrato>=4 and medio_transporte=="a pie"')
# 17. Reportar estudiantes que son estratos bajos y justifican su inasistencia
estudiantesEstratosBajosJustificanInasistencia = dataFrameAsistencia.query('estrato<=3 and estado=="tarde"')
# 18. Reportar estudiantes que son estratos altos y justifican su inasistencia
estudiantesEstratosAltosJustificanInasistencia = dataFrameAsistencia.query('estrato>=4 and estado=="tarde"')
# 19. Reportar estudiantes que usan carro y justifican su inasistencia
estudiantesUsanCarroJustificanInasistencia = dataFrameAsistencia.query('medio_transporte=="carro" and estado=="tarde"')
# 20. Reportar estudiantes que faltan, usan metro y son estratos medios
estudiantesFaltanMetroEstratosMedios = dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="metro" and estrato in [2, 3]')

# AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
# 1. Contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado = dataFrameAsistencia.groupby('estado').size()
# 2. Número de registros por estrato
conteoRegistrosPorEstrato = dataFrameAsistencia.groupby('estrato').size()
# 3. Cantidad de estudiantes por medio de transporte
conteoPorMedioTransporte = dataFrameAsistencia.groupby('medio_transporte').size()
# 4. Cantidad de registros por grupo (si tienes una columna de grupo)
conteoPorGrupo = dataFrameAsistencia.groupby('grupo').size()
# 5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte = dataFrameAsistencia.groupby(['estado', 'medio_transporte']).size()
# 6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado = dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoPorEstado)
# 7. Estrato promedio por medio de transporte
promedioEstratoPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()
print(promedioEstratoPorTransporte)
# 8. Máximo estrato por estado de asistencia
maxEstratoPorEstado = dataFrameAsistencia.groupby('estado')['estrato'].max()
print(maxEstratoPorEstado)
# 9. Mínimo estrato por estado de asistencia
minEstratoPorEstado = dataFrameAsistencia.groupby('estado')['estrato'].min()
print(minEstratoPorEstado)
# 10. Conteo de asistencias por grupo y por estado
conteoAsistenciasPorGrupoYEstado = dataFrameAsistencia.groupby(['grupo', 'estado']).size()
# 11. Transporte usado por cada grupo
transportePorGrupo = dataFrameAsistencia.groupby('grupo')['medio_transporte'].unique()
# 12. Cuántos grupos distintos registraron asistencia por fecha
gruposPorFecha = dataFrameAsistencia.groupby('fecha')['grupo'].nunique()
# 13. Promedio de estrato por fecha
promedioEstratoPorFecha = dataFrameAsistencia.groupby('fecha')['estrato'].mean()
# 14. Número de tipos de estado por transporte
conteoEstadoPorTransporte = dataFrameAsistencia.groupby('medio_transporte')['estado'].nunique()
# 15. Primer Registro de cada grupo (si tienes una columna de fecha)
primerRegistroPorGrupo = dataFrameAsistencia.sort_values('fecha').groupby('grupo').first()
