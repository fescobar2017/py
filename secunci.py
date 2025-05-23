import hashlib

# Función de transformación personalizada
def custom_transform(number):
    # Definir el mapeo personalizado
    custom_mapping = {
        '0': 'A', '1': 'D', '2': 'E', '3': 'K', '4': 'M',
        '5': 'N', '6': 'P', '7': 'Q', '8': 'R', '9': 'S'
    }
    
    # Convertir el número a una cadena
    number_str = str(number)
    
    # Transformar el número usando el mapeo personalizado
    transformed_str = ''.join(custom_mapping[digit] for digit in number_str)
    
    return transformed_str

def custom_transform_to_md5_hex(number):
    # Transformar el número usando la transformación personalizada
    transformed_str = custom_transform(number)
    
    # Crear un objeto de hash MD5
    md5_hash = hashlib.md5()
    
    # Actualizar el objeto de hash con los bytes de la cadena transformada
    md5_hash.update(transformed_str.encode('utf-8'))
    
    # Obtener la representación hexadecimal del hash MD5
    md5_hex = md5_hash.hexdigest()
    
    return md5_hex

# Ejemplo de uso
number = 200
md5_hex = custom_transform_to_md5_hex(number)
print(f"La representación hexadecimal MD5 del número {number} transformado es: {md5_hex}")
