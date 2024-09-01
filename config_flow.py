""" Configuration flow for the ebusd_custom integration to allow configuration through UI."""
import logging
from homeassistant.core import callback
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
import uuid
import re

from datetime import timedelta, datetime
from homeassistant.const import (
    CONF_NAME,
    EVENT_HOMEASSISTANT_START
)
from .const import (
    DOMAIN,
    CONFIGFLOW_VERSION,
    REGEX_STRING
)
from .config_schema import (
    get_config_flow_schema,
    EBUSD_HOST,
    EBUSD_PORT,
    EBUSD_HTTP,
)

_LOGGER = logging.getLogger(__name__)

## config flow
@config_entries.HANDLERS.register(DOMAIN)
class EbusdConfigFlow(self, user_input={}):
    """ebusd config flow"""
    VERSION = CONFIGFLOW_VERSION
    CONNECTION_CLASS = config.entries.CONN_CLASS_LOCAL_POLL

    def __init__(self):
        """"Initialize"x"""
        self._errors = {}
        self._data = {}
        self._unique_id = str(uuid.uuid4())

        """INITIATE CONFIG FLOW"""


class EmptyOptions(config_entries.OptionsFlow):
    """A class for default options"""

    def __init__(self, config_entry):
        """Set the config entry parameter"""
        self.config_entry = config_entry


