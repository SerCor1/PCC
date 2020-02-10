import re 

class Archivo:
  def __init__(self, name):
    self.name = name 
    self.file = open(name, "r+")
  
  def _counter_of(self, regex):
    counter = 0
    
    for line in self.file.readlines():
      c = len(re.findall(regex, line))
      counter += c if c else 0  

    self.file.seek(0)
    return counter 
  
  def cuenta_vocales(self):
    return self._counter_of(r"[AaEeIiOoUu]")

  def cuenta_consonates(self):
    return self._counter_of(r"[b-df-hj-np-tv-z]")

  def cuenta_signos_puntuacion(self):
    return self._counter_of(r"[;:.,]")

  def cuenta_espacios(self):
    return self._counter_of(r" ")

  def cuenta_palabras(self):
    return self._counter_of(r"")

  def cuenta_letras(self):
    return self._counter_of(r"[a-zA-Z]")

  def cuenta_lineas(self):
    return self._counter_of(r".$") 

  def cuenta_mayusculas(self):
    return self._counter_of(r"[A-Z]") 

  def cuenta_minusculas(self):
    return self._counter_of(r"[a-z]") 

  def copiar(self, archivo_destino):
    with open(archivo_destino, "w") as f:
      for line in self.file:
        f.write(line)
    self.file.seek(0)

  def convierte_mayusculas(self):
    process_line = ""
    last_offset = 0 

    for line in self.file.readlines():
      process_line = line.upper()  
      self.file.seek(last_offset) 
      self.file.write(process_line)
      last_offset = self.file.tell() 
    
    self.file.flush()
    self.file.seek(0)


  def convierte_minusculas(self):
    process_line = ""
    last_offset = 0 

    for line in self.file.readlines():
      process_line = line.lower()
      self.file.seek(last_offset) 
      self.file.write(process_line)
      last_offset = self.file.tell() 

      self.file.flush()
      self.file.seek(0)
    
  def muestra_hexadecimal(self):
    for line in self.file:
      print(f"{line.encode('utf-8').hex()}") 

  def close(self):
    self.file.close() 


def main():
  archivo = Archivo("test") 
  print("Numero de vocales: " + str(archivo.cuenta_vocales()))

  print("Numero de consonantes: " + str(archivo.cuenta_consonates()))

  print("Numero de signos de puntuación: " + str(archivo.cuenta_signos_puntuacion()))

  print("Numero de espacios: " + str(archivo.cuenta_espacios()))

  print("Numero de palabras: " + str(archivo.cuenta_palabras()))

  print("Numero de letras: " + str(archivo.cuenta_letras()))

  print("Numero de lineas: " + str(archivo.cuenta_lineas()))

  print("Numero de mayusculas: " + str(archivo.cuenta_mayusculas()))

  print("Numero de minusculas: " + str(archivo.cuenta_minusculas()))

  print("Copiando.." + str(archivo.copiar("nuevo")))

  print("Convirtiendo a mayusculas.." )

  print("Conviritiendo a minusculas.." )
    
  print("Mostrando hexadecimal..\n" + str(archivo.muestra_hexadecimal()))


if __name__ == "__main__":
    main()
