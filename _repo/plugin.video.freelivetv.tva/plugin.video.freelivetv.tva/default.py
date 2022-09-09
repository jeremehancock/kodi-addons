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

from resources.lib.modules.channels import *

import xbmcplugin

mode = FreeLiveTV().plugin_queries['mode']

if mode == "main":
    patreon_notify()
    m7lib.Common.add_section("search-channels", search_icon, fanart, get_string(9007))
    Channels.channel_list()

elif mode == "search-channels":
    Channels.search_list()

else:
    Channels.get_channel(mode)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
