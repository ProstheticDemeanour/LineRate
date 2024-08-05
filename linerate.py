import cigre601
import conductor

ambient_temperature = 48.0
wind_speed = 1
angle_of_attack = 90
solar_irradiation = 1000
conductor_temperature = 80
horizontal_angle = 0
elevation = 0.0


cigre = cigre601.thermal_rating(
    ambient_temperature,
    wind_speed,
    angle_of_attack,
    solar_irradiation,
    conductor.pawpaw_constants,
    conductor_temperature,
    horizontal_angle,
    elevation=elevation,
)

print(cigre)

