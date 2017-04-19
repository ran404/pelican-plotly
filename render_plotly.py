# -*- coding: utf-8 -*-

import re
import uuid

from pelican import signals

main_regex = re.compile(r"(\[plotly\]([\s\S]*?)\[\/plotly\])")

js_block = '''
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
function getPlotlyJSON(div, url) {
    var request = new XMLHttpRequest();
    request.open('GET', url, true);
    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var figure = JSON.parse(request.responseText);
        Plotly.plot(div, figure.data, figure.layout);
      }
    };
    request.send();
}
%s
</script>
'''


def render_plotly(generator):
    for article in generator.articles + generator.drafts:
        plotly_figures = []
        for match in main_regex.findall(article._content):
            all_match_str, plotly_figure = match
            plotly_figure = plotly_figure.strip()

            plotly_id = uuid.uuid4()
            plotly_figures.append((plotly_id, plotly_figure))
            plotly_div = '<div id="{}"></div>'.format(plotly_id)
            article._content = article._content.replace(all_match_str, plotly_div)

        if plotly_figures:
            script = '\n'.join('getPlotlyJSON("{}", "{}");'.format(div, url) for div, url in plotly_figures)
            article._content = article._content + (js_block % script)


def register():
    signals.article_generator_finalized.connect(render_plotly)
