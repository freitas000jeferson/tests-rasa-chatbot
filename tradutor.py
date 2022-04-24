from translate import Translator

t =  Translator(from_lang= "portuguese", to_lang="english")
result = t.translate("Olá meu nome é Jeferson")
print(result)