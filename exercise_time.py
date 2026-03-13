def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    
    hora_restante = total_segundos // 3600
    segundos_restantes = total_segundos - 3600
    minutos_restantes = segundos_restantes // 60

    print(hora_restante)
    print(minutos_restantes)
    print(segundos_restantes - (minutos_restantes * 60))

time()
