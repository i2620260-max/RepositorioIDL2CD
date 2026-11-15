# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
H = 0
M = 0
S = 0
N = 0
total_segundos = 0
nueva_H = 0
nuevo_M = 0
nuevo_S = 0
H = int(input('Ingrese la hora (0-23): '))
M = int(input('Ingrese los minutos (0-59): '))
S = int(input('Ingrese los segundos (0-59): '))
N = int(input('Ingrese los segundos a sumar (N): '))
# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
total_segundos = (H * 3600 + M * 60 + S + N) % 86400

nueva_H = total_segundos // 3600
nuevo_M = (total_segundos % 3600) // 60
nuevo_S = total_segundos % 60

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f'la hora {N} segundos despues sera: {nueva_H:02d}:{nuevo_M:02d}:{nuevo_S:02d}')
