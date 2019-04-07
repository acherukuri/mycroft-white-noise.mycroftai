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
from mycroft.util.log import getLogger
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
from mycroft.util.parse import match_one, extract_duration

LOGGER = getLogger(__name__)

track_list = {
    'white noise for': join(dirname(__file__), "whitenoise.mp3"),
    'white noise waves for': join(dirname(__file__), "waves.mp3"),
    'white noise rain for': join(dirname(__file__), "rain.mp3"),
    'white noise wind for': join(dirname(__file__), "wind.mp3"),
}

class WhiteNoiseSkill(CommonPlaySkill):
    def CPS_match_query_phrase(self, phrase):
        match, confidence = match_one(phrase, track_list)
        if confidence > 0.5:
            return (match, CPSMatchLevel.TITLE, {"track": match})
        else:
            return None

    def CPS_start(self, phrase, data):
        url = data['track']
        try:
            track_duration = int(extract_duration(phrase)[0].total_seconds())
        except AttributeError:
            return None
        self.log.info('track_duration is: ' + str(track_duration))
        self.log.info('track name is: ' + url)
        self.audioservice.play(url, phrase, True)
        while track_duration > 0:
            time.sleep(1)
            track_duration -=1
        self.audioservice.stop()


def create_skill():
    return WhiteNoiseSkill()
