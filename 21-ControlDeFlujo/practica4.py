#aplicar la formula para calcular la masa corporal de una persona https://en.wikipedia.org/wiki/Body_mass_index https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal

masaCorporal= float(input('Coloque el peso en kg: \n\t'))
alturaCorporal=float(input('Coloque su altura en metros: \n\t'))

BMI=round((masaCorporal/(alturaCorporal**2)),1)
if BMI<16.0:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Bajo Peso con Delgadez Severa\nSe recomienda visitar un medico experto y optar por alimentos nutritivos y altos en calorias ")
elif BMI>=16 and BMI<16.9:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Bajo Peso con Delgadez moderada\nSe recomienda visitar un medico experto y optar por alimentos nutritivos y altos en calorias ")
elif BMI>=17 and BMI<18.4:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Bajo peso con Delgadez Leve\nSe recomienda visitar un medico experto y optar por alimentos nutritivos y altos en calorias")
elif BMI>=18.5 and BMI<24.9:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Rango normal de peso\n Enhorabuena! Te encuentras en buena forma, no olvides comer sano y hacer ejercicio")
elif BMI>=25.0 and BMI<29.9:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Sobrepeso Pre-Obeso\nSe recomienda visitar un medico experto y adoptar hábitos de vida saludables para perder peso de manera gradual y sostenible")
elif BMI>=30.0 and BMI<34.9:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Obeso de Clase I\nSe recomienda visitar un medico experto y adoptar hábitos de vida saludables para perder peso de manera gradual y sostenible")
elif BMI>=35.0 and BMI<39.9:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Obeso de Clase II\nSe recomienda visitar un medico experto y adoptar hábitos de vida saludables para perder peso de manera gradual y sostenible")
elif BMI>=40.0:
    print(f"Tu masa corporal actual es de: '{BMI}'\nTe encuentras en el rango de:\n\t Obeso de Clase II\nSe recomienda visitar un medico experto de manera inmediata, adoptar hábitos de vida saludables para perder peso de manera gradual y sostenible y realizarse chequeos con un especialista medico autorizado")
else:
    exec(masaCorporal)