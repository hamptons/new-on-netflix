from jinja2 import Environment


class HtmlBuilder:
    CONST_TEMPLATE = """\
<html>
  <head></head>
  <body>
    <h3>Films</h3>
    <ul>
    {% for film in films %}
        <li>{{ film }}</li>
    {% endfor %}
    </ul>
    <h3>TV Shows</h3>
    <ul>
    {% for show in tv_shows %}
        <li>{{ show }}</li>
    {% endfor %}
    </ul>
  </body>
</html>
"""

    def build_html(self, films, tv_shows):
        return Environment().from_string(self.CONST_TEMPLATE).render(
            films=films,
            tv_shows=tv_shows
        ), "html"
