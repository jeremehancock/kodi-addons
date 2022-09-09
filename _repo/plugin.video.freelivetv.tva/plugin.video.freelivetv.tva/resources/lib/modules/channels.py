"""
    Free Live TV Add-on
    Developed by mhancoc7
    https://patreon.m7kodi.dev

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    # Python 3
    from resources.lib.modules.common import *
except ImportError:
    # Python 2
    from common import *

import m7lib

class Channels:

    @staticmethod
    def channel_list():
        try:
            # Generate Channel List
            for channel in m7lib.Common.get_channels():
                m7lib.Common.add_channel(channel["slug"], channel["poster"], fanart, channel["name"].encode(encoding='UTF-8', errors='strict').decode('UTF-8'), True)
        except SyntaxError:
            dlg_oops(addon_name)

    @staticmethod
    def search_list():
        try:
            # Generate Channel List from search query
            retval = dlg.input(get_string(9007), type=xbmcgui.INPUT_ALPHANUM)
            if retval and len(retval) > 0:
                search_list = m7lib.Common.search_channels(retval)
                if len(search_list) > 0:
                    for channel in sorted(search_list, key=lambda x: x['slug']):
                        m7lib.Common.add_channel(channel["slug"], channel["poster"], fanart, channel["name"].encode(encoding='UTF-8', errors='strict').decode('UTF-8'), True)
                else:
                    dlg.ok(addon_name, get_string(9008))
                    exit()
            else:
                dlg.ok(addon_name, get_string(9009))
                exit()
        except SyntaxError:
            dlg_oops(addon_name)

    @staticmethod
    def get_channel(mode):
        try:
            m7lib.Common.get_stream_and_play(mode)
        except SyntaxError:
            dlg_oops(addon_name)

