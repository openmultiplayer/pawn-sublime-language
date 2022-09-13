import sublime
import sublime_plugin
import webbrowser


class OpenWikiOnString(sublime_plugin.TextCommand):
    def run(self, edit):
        query = self.view.substr(self.view.sel()[0])
        
        if 'On' in query:
            webbrowser.open_new("https://open.mp/docs/scripting/callbacks" + query)
        else:
            webbrowser.open_new("https://open.mp/docs/scripting/functions" + query)
