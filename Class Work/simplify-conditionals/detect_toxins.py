# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def is_dangerous(ingredients):
    return 'sodium nitrate' in ingredients \
        or 'sodium benzoate' in ingredients \
        or 'sodium oxide' in ingredients


def make_alert_sound():
    print('!!!')
    print('there is a toxin in the food!')
    print('!!!')


def make_accept_sound():
    print('***')
    print('Toxin Free')
    print('***')


ingredients = ['sodium benzoate']
if is_dangerous(ingredients):
    make_alert_sound()
else:
    make_accept_sound()
