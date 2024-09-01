"""Constants for ebus component."""

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPressure,
    UnitOfTemperature,
    UnitOfTime,
)

DOMAIN = "ebusd-custom"

EBUSD_HOST = "localhost"
EBUSD_PORT = "8887"
EBUSD_HTTP = False

#  SensorTypes from ebusdpy module :
#  0='decimal', 1='time-schedule', 2='switch', 3='string', 4='value;status'

# circuitName: {
#       "ebus-name": [ ha-name, unittype, icon, SensorType from ebusdpy, SensorDeviceClass.Unit, ]
#}

DEFAULT_CIRCUITS = ["bai", "ehp", "700"]

DEFAULT_SENSOR_TYPES = {
    "bai": {

        "Status01": [
            "Status01",
            None, # UnitOfTemperature.CELSIUS,
            None,
            3,
            None, # SensorDeviceClass.TEMPERATURE,
        ],
        "Status02": [
            "Status02",
            None, # UnitOfTemperature.CELSIUS,
            None,
            3,
            None, # SensorDeviceClass.TEMPERATURE,
        ],
        "StatusCirPump": [
            "StatusCirPump",
            None, # UnitOfTemperature.CELSIUS,
            None,
            4,
            None,
        ],
    },
}
