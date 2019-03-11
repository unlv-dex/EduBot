import time
import webbrowser
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

runTouchApp(Builder.load_string("""

<Button>
    spacing:80
    color:1,1,1,1
    background_color: .8, .2, .7, .8
    font_size:18
    size_hint:.1,.1


GridLayout:
    rows:4
    cols:4
    Button:
        text:'Math'
    Button:
        text:'Physics'
    Button:
        text:'Computer Science'
    Button:
        text:'Chemistry'
    Button:
        text:'English'
    Button:
        text:'Robotics'
    Button:
        text:'History'
    Button:
        text:'Politics'
    Button:
        text:'Philosophy'
    Button:
        text:'Biology'
    Button:
        text:'Business'
    Button:
        text:'A.I'



"""))
