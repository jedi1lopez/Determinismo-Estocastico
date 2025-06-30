# Determinismo-Estocastico
Repositorio del Determinismo Estocastico I

Este trabajo fusiona la perspectiva filosófica del determinismo con la modelación estadística estocástica, demostrando que la aleatoriedad no excluye el orden, sino que puede ser interpretada como un estado transitorio de comprensión incompleta. La implementación en Python ejemplifica cómo un modelo sencillo puede capturar tanto la parte determinística como la aleatoria de un fenómeno real. En este sentido, el modelo representa una reconciliación metodológica entre la predictibilidad y la adaptabilidad, entre el control y la emergencia, entre el ser y el devenir, donde la incertidumbre no es un obstáculo, sino una herramienta epistemológica fundamental para construir los sistemas más robustos, interpretables y alineados con los principios éticos y racionales de la ciencia moderna

Modelo autorregresivo de primer orden, conocido como AR-1 ya que es un modelo muy común en series las temporales y en los contextos de las investigaciones, relacionado con la detección del fraude financiero mediante los modelos híbridos.

¿Qué es el Modelo AR-1?

El modelo autorregresivo de primer orden (AR-1) es una herramienta estadística utilizada para modelar series temporales. Su nombre proviene de la idea de que el valor actual de una variable depende linealmente de su valor inmediatamente anterior, más un término de error aleatorio.

La fórmula general del modelo es:

y_t=φy_(t-1)+ε_t

De donde:

y_t: Valor de la serie en el tiempo (t.)
y_(t-1): Valor de la serie en el periodo anterior.
φ : Coeficiente autorregresivo que indica la influencia del valor anterior.
ε_t: Término de error aleatorio, normalmente distribuido con media cero.

Este modelo pertenece a la familia de los modelos ARIMA (Box & Jenkins, 1976,) ampliamente usados en economía, finanzas, ingeniería y ciencias sociales para predecir los comportamientos futuros basados en datos históricos.


¿Qué hace el Modelo AR-1?

El modelo AR-1 tiene varias funciones clave:

Predicción de valores futuros:

El modelo permite predecir el siguiente valor de una serie temporal utilizando solo el valor inmediatamente anterior. Es especialmente útil cuando hay una dependencia serial o correlación entre las observaciones consecutivas.

Si estás analizando el volumen de las transacciones diarias sospechosas, el modelo puede ayudarte a prever cuántas podría haber mañana basándose en el hoy.

“Los modelos autorregresivos son fundamentales para comprender y predecir fenómenos que evolucionan en el tiempo” (Hyndman & Athanasopoulos, 2021.)

Modelado de tendencias simples:

Si el coeficiente (φ) está entre (-1 ∧ 1,) el modelo es estacionario, lo que significa que oscila alrededor de un promedio constante. Esto es útil para modelar las series financieras que no tienen tendencias explosivas ni patrones estacionales complejos.

Detección de cambios en el comportamiento: 

En el contexto de detección de fraude, el modelo AR-1 puede usarse como un modelo base para identificar desviaciones significativas del comportamiento esperado. Si una transacción se aparta demasiado de lo predicho, podría ser señal de actividad fraudulenta.

Ventajas del Modelo AR-1:

Sencillez: Es fácil de entender, estimar e implementar.
Interpretabilidad: El coeficiente (φ) tiene un significado claro sobre cómo el pasado influye en el presente.
Base para modelos más complejos: Muchos modelos avanzados (como ARIMA, GARCH o redes neuronales recurrentes) parten de los conceptos básicos como los del AR-1.

Limitaciones del Modelo AR-1:

Solo captura relaciones lineales: No detecta patrones no lineales o complejos.
No maneja estacionalidad: Para series con ciclos regulares, se necesitan modelos adicionales.
Requiere estacionariedad: Si la serie tiene tendencias crecientes o decrecientes, debe transformarse antes de aplicar el modelo.

Aunque no sustituye a los modelos más avanzados como los basados en aprendizaje por refuerzo (RL) o las redes neuronales, puede servir como pilares iniciales en la construcción de los sistemas de detección inteligentes y robustos.

