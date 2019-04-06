# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from os.path import dirname, join
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
from mycroft.skills.audioservice import AudioService

LOGGER = getLogger(__name__)

class WhiteNoiseSkill(MycroftSkill):
    def __init__(self):
        super(WhiteNoiseSkill, self).__init__(name="WhiteNoiseSkill")
        self.play_list = {
            0: join(dirname(__file__), "whitenoise.mp3"),
        }

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    @intent_handler(IntentBuilder("WhiteNoiseIntent")
                    .require("WhiteNoiseKeyword"))
    def handle_white_noise_intent(self, message):
        self.audio_service.play(self.play_list[0])

    def stop(self):
        pass

def create_skill():
    return WhiteNoiseSkill()
