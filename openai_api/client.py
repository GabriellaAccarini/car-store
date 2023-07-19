import openai

def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {}{}{} em apenas 250 caracteres. 
    Fale coisas especificas sobre esse modelo. 
    Descreva especificações técnicas sobre esse modelo
    '''
    openai.api_key = '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'
    prompt = prompt.format(brand, model, year)
    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = prompt,
        max_tokens=1000,
    )
    return response['choices'][0]['text']