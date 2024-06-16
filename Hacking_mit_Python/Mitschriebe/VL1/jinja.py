import jinja2 as jinja

def print_mails():
    env = jinja.Environment()
    temp = env.from_string("Hello, {{name}}. "
                           "How are you doing? "
                           "Greetings, Bobi")

    for word in ["Luke", "Anakin", "Padme"]:
        print(temp.render(name=word))


def print_text():
    env = jinja.Environment()
    temp = env.from_string("{% for text in texts %} {{text}} {% endfor %}\n")

    texts = ["Luke is a jedi", "Vader is a sith", "Han is a snitch"]

    print(temp.render(texts=texts))


print_mails()
print_text()