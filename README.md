
# Simulador de Ocupación Hospitalaria

Este proyecto simula la ocupación de un hospital en diferentes plantas a lo largo de un rango de fechas y horas. Se genera un archivo CSV que contiene la ocupación en cada planta, teniendo en cuenta variaciones diarias y semanales. El simulador se ejecuta para un rango de fechas específico y genera los datos para cada hora en las plantas del hospital.

## Descripción

El simulador crea datos de ocupación hospitalaria para tres plantas del hospital:

- **Planta Baja**
- **Primera Planta**
- **Segunda Planta**

Cada planta tiene una ocupación base que varía dependiendo de la hora del día, el día de la semana y la variabilidad aleatoria. El archivo generado es un CSV con las siguientes columnas:

- **Fecha**: La fecha en formato `YYYY-MM-DD`.
- **Hora**: La hora en formato `0-23`.
- **Planta**: La planta del hospital (Planta Baja, Primera Planta, Segunda Planta).
- **Ocupación**: Número de pacientes ocupando la planta en esa hora.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes paquetes en tu entorno de Python:

- `pandas`
- `numpy`

Puedes instalar estos paquetes utilizando `pip`:

```
pip install pandas numpy
```

## Uso

1. Clona el repositorio en tu máquina local:

```
git clone https://github.com/tu_usuario/simulador-ocupacion-hospital.git
```

2. Navega a la carpeta del proyecto:

```
cd simulador-ocupacion-hospital
```

3. Ejecuta el script de Python para generar el archivo CSV:

```
python generar_ocupacion.py
```

4. El archivo `ocupacion_hospital.csv` se generará en el mismo directorio.

## Ejemplo de datos generados

El archivo `ocupacion_hospital.csv` tendrá un formato como el siguiente:

```
Fecha,Hora,Planta,Ocupación
2025-01-01,0,Planta Baja,12
2025-01-01,1,Planta Baja,11
2025-01-01,2,Planta Baja,10
...
```

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b nueva-rama`).
3. Haz los cambios que desees y realiza un commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu repositorio (`git push origin nueva-rama`).
5. Abre un Pull Request en GitHub para que se revisen tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
