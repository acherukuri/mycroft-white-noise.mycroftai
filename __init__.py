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
import time
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
            1: join(dirname(__file__), "waves.mp3"),
            2: join(dirname(__file__), "rain.mp3"),
            3: join(dirname(__file__), "wind.mp3"),
        }

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    @intent_handler(IntentBuilder("WhiteNoiseIntent")
                    .require("PlayWhiteNoiseKeyword"))
    def handle_white_noise_intent(self, message):
        self.audio_service.play(self.play_list[0],
                                message.data['utterance'],
                                True)
        boom = 5
        while boom > 0:
            time.sleep(1)
            boom -=1
        self.stop_audio_service()

    @intent_handler(IntentBuilder("WhiteNoiseStopIntent")
                    .require("StopWhiteNoiseKeyword"))
    def stop_white_noise_intent(self, message):
        self.stop_audio_service()

    @intent_handler(IntentBuilder("WhiteNoiseWavesIntent")
                    .require("PlayWhiteNoiseWavesKeyword"))
    def handle_white_noise_waves_intent(self, message):
        self.audio_service.play(self.play_list[1],
                                message.data['utterance'],
                                True)
        boom = 5
        while boom > 0:
            time.sleep(1)
            boom -=1
        self.stop_audio_service()

    @intent_handler(IntentBuilder("WhiteNoiseWavesStopIntent")
                    .require("StopWhiteNoiseWavesKeyword"))
    def stop_white_noise_waves_intent(self, message):
        self.stop_audio_service()

    @intent_handler(IntentBuilder("WhiteNoiseRainIntent")
                    .require("PlayWhiteNoiseRainKeyword"))
    def handle_white_noise_rain_intent(self, message):
        self.audio_service.play(self.play_list[2],
                                message.data['utterance'],
                                True)
        boom = 5
        while boom > 0:
            time.sleep(1)
            boom -=1
        self.stop_audio_service()

    @intent_handler(IntentBuilder("WhiteNoiseRainStopIntent")
                    .require("StopWhiteNoiseRainKeyword"))
    def stop_white_noise_rain_intent(self, message):
        self.stop_audio_service()

    @intent_handler(IntentBuilder("WhiteNoiseWindIntent")
                    .require("PlayWhiteNoiseWindKeyword"))
    def handle_white_noise_wind_intent(self, message):
        self.audio_service.play(self.play_list[3],
                                message.data['utterance'],
                                True)
        boom = 5
        while boom > 0:
            time.sleep(1)
            boom -=1
        self.stop_audio_service()

    @intent_handler(IntentBuilder("WhiteNoiseWindStopIntent")
                    .require("StopWhiteNoiseWindKeyword"))
    def stop_white_noise_wind_intent(self, message):
        self.stop_audio_service()

    def stop_audio_service(self):
        self.audio_service.stop()

    def stop(self):
        pass

def create_skill():
    return WhiteNoiseSkill()
