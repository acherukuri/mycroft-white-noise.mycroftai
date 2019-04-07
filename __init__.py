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
from mycroft import intent_file_handler
from mycroft.skills.audioservice import AudioService
from mycroft.util.parse import match_one, extract_duration

LOGGER = getLogger(__name__)

class WhiteNoiseSkill(MycroftSkill):
    def __init__(self):
        super(WhiteNoiseSkill, self).__init__(name="WhiteNoiseSkill")
        self.play_list = {
            0: join(dirname(__file__), "whitenoise.mp3"),
            'white noise waves for': join(dirname(__file__), "waves.mp3"),
            'white noise rain for': join(dirname(__file__), "rain.mp3"),
            'white noise wind for': join(dirname(__file__), "wind.mp3"),
        }

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    def handle_white_noise_intent(self, message):
        utterance = message.data.get('utterance', "")
        try:
            track_duration = int(extract_duration(utterance)[0].total_seconds())
        except AttributeError:
            return None
        if(track_duration > 0):
            self.log.info('track_duration is: ' + str(track_duration))
            self.audio_service.play(join(dirname(__file__), "whitenoise.mp3"),
                                    utterance, True)
            while track_duration > 0:
                time.sleep(1)
                track_duration -=1
            self.audio_service.stop()
        else:
            return None

    @intent_file_handler("play.white.noice.intent")
    def handle_query_time_alt(self, message):
        self.handle_white_noise_intent(message)

    def stop(self):
        pass

def create_skill():
    return WhiteNoiseSkill()
