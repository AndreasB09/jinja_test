from jinja2 import Template

template = Template("Hey, {{ name }}")

rendered = template.render(name="Universe")

print(rendered)