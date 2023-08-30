persona = {
    'first_name': 'Edem',
    'last_name': 'Terraza',
    'age': 31,
    'country': 'Peru',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# a) Comprobar si la clave 'skills' existe en el diccionario y luego imprimir la habilidad del medio
if 'skills' in persona:
    skills_list = persona['skills']
    middle_skill_index = len(skills_list) // 2
    middle_skill = skills_list[middle_skill_index]
    print("Habilidad del medio:", middle_skill)

# b) Comprobar si la clave 'skills' existe y si la habilidad 'Python' está presente en las habilidades
if 'skills' in persona and 'Python' in persona['skills']:
    print("La persona tiene la habilidad 'Python'.")

# c) Comprobar las habilidades de la persona y determinar su título
skills = persona.get('skills', [])
if skills == ['JavaScript', 'React']:
    print("Él es un desarrollador frontend")
elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
    print("Él es un desarrollador backend")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
    print("Él es un desarrollador fullstack")
else:
    print("Título desconocido")