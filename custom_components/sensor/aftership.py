"""
A component which allows you to get information about pending parcels.

For more details about this component, please refer to the documentation at
https://github.com/HalfDecent/HA-Custom_components/ruter
"""
import logging
import voluptuous as vol
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (DOMAIN, PLATFORM_SCHEMA)

__version__ = '0.3.0'

REQUIREMENTS = ['pyaftership==0.0.2']

CONF_API_KEY = 'api_key'
CONF_NAME = 'name'

TITLE = 'title'
SLUG = 'slug'
TRACKING_NUMBER = 'tracking_number'

DATA = 'aftership_data'

SERVICE_NEW_TRACKING = 'aftership_new_tracking'

NEW_TRACKING_SERVICE_SCHEMA = vol.Schema({
    vol.Required(TITLE): cv.string,
    vol.Required(SLUG): cv.string,
    vol.Required(TRACKING_NUMBER): cv.string,
})

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_NAME, default='AfterShip'): cv.string,
})

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the sensor platform"""
    api_key = config.get(CONF_API_KEY)
    name = config.get(CONF_NAME)
    add_devices([AftershipSensor(hass, api_key, name)])

    def handle_new_tracking(call):
        """Call when a user creates a new Afterhip tracking from HASS."""
        from pyaftership import AfterShip
        title = call.data[TITLE]
        slug = call.data[SLUG]
        tracking_number = call.data[TRACKING_NUMBER]

        _aftership = AfterShip()
        _aftership.add_tracking(api_key, slug, title, tracking_number)

        if not result['success']:
            _LOGGER.debug("Created Aftership tracking")
        else:
            _LOGGER.error("Failed to create new tracking")

    hass.services.register(DOMAIN, SERVICE_NEW_TRACKING, handle_new_tracking,
                           schema=NEW_TRACKING_SERVICE_SCHEMA)

class AftershipSensor(Entity):
    """The sensor class"""
    def __init__(self, hass, api_key, name):
        from pyaftership import AfterShip
        self._aftership = AfterShip()
        self.hass = hass
        self._name = name
        self._api_key = api_key
        self._state = 0
        self.hass.data[DATA] = {}
        self.update()


    def update(self):
        """Update the sensor"""
        base_link = 'https://track.aftership.com/'
        result = self._aftership.get_trackings(self._api_key)
        if not result['success']:
            return False
        else:
            self.hass.data[DATA] = {}
            data = result['data']
            self._state = data['count']
            for parcel in data['trackings']:
                parcel_data = {}
                if not parcel['title']:
                    title = parcel['tracking_number']
                else:
                    title = parcel['title']
                parcel_data['title'] = title
                if parcel['tag'] == 'InTransit':
                    parcel_data['status'] = 'In transit'
                else:
                    parcel_data['status'] = parcel['tag']
                parcel_data['slug'] = parcel['slug']
                parcel_data['last_update'] = parcel['updated_at']
                parcel_data['tracking_number'] = parcel['tracking_number']
                parcel_data['link'] = base_link + parcel['slug'] + '/' + parcel['tracking_number']
                self.hass.data[DATA][parcel['tracking_number']] = parcel_data

    @property
    def name(self):
        """Return the name of the sensor"""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor"""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor"""
        return 'mdi:package'

    @property
    def device_state_attributes(self):
        """Return the attributes of the sensor"""
        return self.hass.data[DATA]