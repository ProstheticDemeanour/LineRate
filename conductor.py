from collections import namedtuple
from email.message import EmailMessage
import re
import nusselt

# Notes from Prysmian Brochure:
# Technical Information - Electrical
# 1. Emissivity:
# The standard value for bright new conductor is taken as 0.3.
# After weathering, the emissivity increases up to a maximum
# value of 0.5 for a rural weathering and 0.8 in an industrial/
# polluted environment. Small changes in Emissivity have
# little effect on current rating

# 3. Absorbance:
# The standard value for a bright conductor is 0.6. Weathering
# will reduce this value to 0.5 for a rural environment with a
# corresponding increase in current rating.

ConductorConstants = namedtuple(
    "ConductorConstants",
    [
        "stranded",
        "high_rs",
        "diameter",
        "cross_section",
        "absortivity",
        "emmisivity",
        "materials_heat",
        "resistance",
    ],
)

HeatMaterial = namedtuple(
    "HeatMaterial", ["name", "mass_per_unit_length", "specific_heat_20deg", "beta"]
)


def drake_resistance(conductor_temperature):
    at_25 = 7.283e-5
    at_75 = 8.688e-5

    per_1 = (at_75 - at_25) / (75 - 25)

    resistance = at_25 + (conductor_temperature - 25) * per_1
    return resistance


# From CIGRE601 examples
# AAC 1350 conductors: drake, venus
drake_constants = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=28.1e-3,
    cross_section=None,
    absortivity=0.5, # was 0.8
    emmisivity=0.5,  # was 0.8
    materials_heat=[
        HeatMaterial("steel", 0.5119, 481, 1.00e-4),
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=drake_resistance,
)

drake_constants_ieee738 = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=28.14e-3,
    cross_section=None,
    absortivity=0.5, # was 0.8
    emmisivity=0.5,  # was 0.8
    materials_heat=[
        HeatMaterial("steel", 0.5119, 481, 1.00e-4),
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=drake_resistance,
)

drake_constants_example_b = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=28.1e-3,
    cross_section=None,
    absortivity=0.5, 
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("steel", 0.5119, 481, 1.00e-4),
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=drake_resistance,
)

def venus_resistance(conductor_temperature):
    at_20 = 0.0429e-3
    at_75 = 0.054e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

venus_constants = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=33.8e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=venus_resistance,
)

# AAAC Conductors: phosphorus & sulphur
def phosphorus_resistance(conductor_temperature):
    at_20 = 0.0731e-3
    at_75 = 0.09e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

phosphorous_constants = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=26.3e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=phosphorus_resistance,
)

def sulphur_resistance(conductor_temperature):
    at_20 = 0.0444e-3
    at_75 = 0.056e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

sulphur_constants = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=33.8e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=sulphur_resistance,
)

# ACSR/GZ Conductors: Grape, Lemon, Lychee, Lime, Mango, Orange, Olive, Paw Paw, Peach
def grape_resistance(conductor_temperature):
    at_20 = 0.196e-3
    at_75 = 0.24e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

grape_constants = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=17.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=grape_resistance,
)

def lemon_resistance(conductor_temperature):
    at_20 = 0.136e-3
    at_75 = 0.167e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

lemon_constants = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=21e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=lemon_resistance
)

def lychee_resistance(conductor_temperature):
    at_20 = 0.116e-3
    at_75 = 0.142e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

lychee_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=22.8e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=lychee_resistance
)

def lime_resistance(conductor_temperature):
    at_20 = 0.1e-3
    at_75 = 0.123e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

lime_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=24.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=lime_resistance
)

def mango_resistance(conductor_temperature):
    at_20 = 0.0758e-3
    at_75 = 0.0967e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

mango_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=27e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=mango_resistance
)

def orange_resistance(conductor_temperature):
    at_20 = 0.0646e-3
    at_75 = 0.0827e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

orange_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=29.3e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=orange_resistance
)

def olive_resistance(conductor_temperature):
    at_20 = 0.0557e-3
    at_75 = 0.0716e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

olive_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=31.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=olive_resistance
)

def pawpaw_resistance(conductor_temperature):
    at_20 = 0.0485e-3
    at_75 = 0.0628e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

pawpaw_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=33.8e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=pawpaw_resistance
)

def peach_resistance(conductor_temperature):
    at_20 = 0.0303e-3
    at_75 = 0.0408e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

peach_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=42.8e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=peach_resistance
)

# ACSR/AC Conductors: skating, soccer, swimming, tennis, angling, archery, baseball, bowls, cricket, darts, dice, diving, golf, gymastics, hurdles

def skating_resistance(conductor_temperature):
    at_20 = 2.75e-3
    at_75 = 3.35e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

skating_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=5.3e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=skating_resistance
)

def soccer_resistance(conductor_temperature):
    at_20 = 1.34e-3
    at_75 = 1.63e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

soccer_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=7.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=soccer_resistance
)

def swimming_resistance(conductor_temperature):
    at_20 = 0.807e-3
    at_75 = 1.05e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

swimming_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=9e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=swimming_resistance
)

def tennis_resistance(conductor_temperature):
    at_20 = 0.517e-3
    at_75 = 0.689e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

tennis_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=11.3e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=tennis_resistance
)

def angling_resistance(conductor_temperature):
    at_20 = 0.923e-3
    at_75 = 1.12e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

angling_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=7.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=angling_resistance
)

def archery_resistance(conductor_temperature):
    at_20 = 0.641e-3
    at_75 = 0.844e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

archery_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=9e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=archery_resistance
)

def baseball_resistance(conductor_temperature):
    at_20 = 0.41e-3
    at_75 = 0.555e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

baseball_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=11.3e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=baseball_resistance
)

def bowls_resistance(conductor_temperature):
    at_20 = 0.259e-3
    at_75 = 0.356e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

bowls_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=14.3e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=bowls_resistance
)

def cricket_resistance(conductor_temperature):
    at_20 = 0.182e-3
    at_75 = 0.223e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

cricket_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=17.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=cricket_resistance
)

def darts_resistance(conductor_temperature):
    at_20 = 0.126e-3
    at_75 = 0.155e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

darts_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=21e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=darts_resistance
)

def dice_resistance(conductor_temperature):
    at_20 = 0.108e-3
    at_75 = 0.133e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

dice_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=22.8e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=dice_resistance
)

def diving_resistance(conductor_temperature):
    at_20 = 0.0928e-3
    at_75 = 0.114e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

diving_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=24.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=diving_resistance
)

def golf_resistance(conductor_temperature):
    at_20 = 0.0726e-3
    at_75 = 0.0908e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

golf_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=27e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=golf_resistance
)

def gymnastics_resistance(conductor_temperature):
    at_20 = 0.0619e-3
    at_75 = 0.078e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

gymnastics_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=29.3e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=gymnastics_resistance
)

def hurdles_resistance(conductor_temperature):
    at_20 = 0.0533e-3
    at_75 = 0.0678e-3

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance

hurdles_constants = ConductorConstants(
    stranded=True,
    high_rs=True, 
    diameter=31.5e-3,
    cross_section=None,
    absortivity=0.5,
    emmisivity=0.5,
    materials_heat=[
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
        HeatMaterial("steel", 0.5119, 481, 1.00e-4)
    ],
    resistance=hurdles_resistance
)