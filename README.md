# Pelican plugin for rendering raw plotly figures

This plugin allows you to embed raw plotly figures (json data) using the \[plotly\] tag.

## Usage

In your article file, add:

```
[plotly] /plots/figure-01.json [/plotly]

```

This will render /plots/figure-01.json as an interactive plotly graph in the browser.

## Installation

Add the plugin path to your PLUGINS setting in the pelicanconf.py file.

```
PLUGINS = [... , 'pelican-plotly' , ... ]
```

To add this plugin as a sub module:

```
git submodule add git://github.com/ran404/pelican-plotly.git plugins/pelican-plotly
```
