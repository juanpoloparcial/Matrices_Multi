const prompt = require("prompt-sync")({ sigint: true });

console.log("\n- CARGA DE DATOS PERSONALES -\n");

// Lista donde se guardarán los datos de las personas
const personas = [];

while (true) {
  const nombre = prompt("Ingrese su Nombre: ");
  const apellido = prompt("Ingrese su Apellido: ");
  const dni = prompt("Ingrese su DNI: ");

  // Lista de teléfonos por persona
  const telefonos = [];
  while (true) {
    const tel = prompt("Ingrese su num de Teléfono (Para continuar presione ENTER): ");
    if (tel === "") break;
    telefonos.push(tel);
  }

  // Agregamos la persona a la lista
  personas.push([nombre, apellido, "DNI: ", dni, "Teléfonos: ", telefonos]);

  // Preguntamos si quiere agregar otra persona
  const agregarOtra = prompt("\n¿ Quiere Agregar otra persona ?  (SI/NO): ").toUpperCase();
  if (agregarOtra !== "SI") break;
}

// Mostramos la lista completa
console.log("\n- - Lista de Personas - -\n");
personas.forEach((persona) => {
  console.log(persona);
});
