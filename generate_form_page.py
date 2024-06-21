from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('form.html')

data = {
    'title': 'User Form',
    'heading': 'Fill in your details',
    'name': '',
    'email': '',
    'age': ''
}

rendered = template.render(data)

with open('output/form_page.html', 'w') as f:
    f.Write(rendered)

print("HTML form generated successfully")