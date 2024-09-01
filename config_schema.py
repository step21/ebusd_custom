import voluptuous as vol
import logging
import homeassistant.helpers.config_validation as cv

from homeassistant.const import CONF_NAME, CONF_ENTITIES

from .const import (
    DOMAIN,
    DEFAULT_CIRCUITS,
    DEFAULT_SENSOR_TYPES,
    )

_LOGGER = logging.getLogger(__name__)

EBUSD_HOST = ""
EBUSD_PORT = ""
EBUSD_HTTP = False

EBUSD_SCHEMA = {
        vol.Required(EBUSD_HOST): cv.string,
        vol.Required(EBUSD_PORT): cv.int,
        vol.Required(EBUSD_HTTP): cv.bool,
        }

def get_config_flow_schema(config: dict = {}, config_flow_step: int = 0) -> dict:
    config = {
        CONF_NAME: DEFAULT_NAME,
        EBUSD_HOST: "",
        EBUSD_PORT: "",
        EBUSD_HTTP: False,
            }
    return config
