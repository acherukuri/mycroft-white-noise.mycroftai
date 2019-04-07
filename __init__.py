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
from os.path import dirname, join
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.util.parse import match_one, extract_duration

LOGGER = getLogger(__name__)

class WhiteNoiseSkill(MycroftSkill):
    def __init__(self):
        super(WhiteNoiseSkill, self).__init__(name="WhiteNoiseSkill")
        self.play_list = {
            'waves': join(dirname(__file__), "waves.mp3"),
            'rain': join(dirname(__file__), "rain.mp3"),
            'wind': join(dirname(__file__), "wind.mp3"),
        }

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    def handle_white_noise_intent(self, message):
        utterance = message.data.get('utterance', "")
        try:
            track_duration = int(extract_duration(utterance)[0].total_seconds())
        except AttributeError:
            return None
        self.play_track(join(dirname(__file__), "whitenoise.mp3"),
                        track_duration, utterance)

    @intent_file_handler("white.noice.intent")
    def handle_file_white_noice_intent(self, message):
        self.handle_white_noise_intent(message)

    @intent_file_handler("waves.rain.wind.intent")
    def handle_file_rain_waves_wind_intent(self, message):
        self.handle_rain_waves_wind_intent(message)

    def handle_rain_waves_wind_intent(self, message):
        utterance = message.data.get('utterance', "")
        match, confidence = match_one(utterance, self.play_list)
        try:
            track_duration = int(extract_duration(utterance)[0].total_seconds())
        except AttributeError:
            return None
        self.play_track(match, track_duration, utterance)

    def play_track(self, track_name, track_duration, utterance):
        if(track_duration > 0):
            self.log.info('track_duration is: ' + str(track_duration))
            self.log.info('track url is: ' + track_name)
            self.audio_service.play(track_name, utterance, True)
            while track_duration > 0:
                time.sleep(1)
                track_duration -=1
            self.audio_service.stop()
        else:
            return None

    def stop(self):
        pass

def create_skill():
    return WhiteNoiseSkill()
