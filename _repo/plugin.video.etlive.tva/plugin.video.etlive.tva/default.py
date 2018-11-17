'''
    ET Live Add-on

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
'''

import sys,re,os,urllib,urllib2
from urllib2 import urlopen
import xbmc,xbmcgui,xbmcplugin,xbmcaddon

import m7lib

dlg = xbmcgui.Dialog()
addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_id = addon.getAddonInfo('id')
plugin_path = xbmcaddon.Addon(id=addon_id).getAddonInfo('path')
addon_logo = xbmc.translatePath(os.path.join(plugin_path,'tvaddons_logo.png'))
stream_failed = "Unable to get stream. Please try again later."

if __name__ == '__main__':
    xbmc.executebuiltin('Activatewindow(home)')

    # TVADDONS Branding
    dlg.notification(addon_name + ' is provided by:','www.tvaddons.co',addon_logo,10000,False)

    try:
        stream = m7lib.Stream().cbs_news()
        if stream is not None:
            li = xbmcgui.ListItem(addon_name)
            xbmc.Player().play(stream,li,False)
        else:
            dlg.ok(addon_name, stream_failed)
    except:
        dlg.ok(addon_name, stream_failed)
