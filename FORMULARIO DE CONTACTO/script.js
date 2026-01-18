const form = document.getElementById("contactForm");
const statusEl = document.getElementById("formStatus");

const fields = {
  fullName: document.getElementById("fullName"),
  email: document.getElementById("email"),
  phone: document.getElementById("phone"),
  subject: document.getElementById("subject"),
  message: document.getElementById("message"),
  terms: document.getElementById("terms"),
};

function setStatus(msg, type = "info") {
  statusEl.textContent = msg;

  // Estilos simples por tipo
  if (type === "ok") {
    statusEl.style.borderColor = "rgba(34,197,94,.7)";
  } else if (type === "error") {
    statusEl.style.borderColor = "rgba(239,68,68,.7)";
  } else {
    statusEl.style.borderColor = "rgba(209,250,229,1)";
  }
}

function setCustomMessages() {
  fields.fullName.setCustomValidity("");
  fields.email.setCustomValidity("");
  fields.phone.setCustomValidity("");
  fields.subject.setCustomValidity("");
  fields.message.setCustomValidity("");
  fields.terms.setCustomValidity("");

  if (fields.fullName.validity.valueMissing) {
    fields.fullName.setCustomValidity("Por favor, ingresa tu nombre completo.");
  } else if (fields.fullName.validity.tooShort) {
    fields.fullName.setCustomValidity("El nombre debe tener al menos 3 caracteres.");
  }

  if (fields.email.validity.valueMissing) {
    fields.email.setCustomValidity("Por favor, ingresa tu correo electrónico.");
  } else if (fields.email.validity.typeMismatch) {
    fields.email.setCustomValidity("Ingresa un correo con formato válido (ej. nombre@dominio.com).");
  }

  if (fields.phone.validity.valueMissing) {
    fields.phone.setCustomValidity("Por favor, ingresa tu teléfono.");
  } else if (fields.phone.validity.patternMismatch) {
    fields.phone.setCustomValidity("El teléfono debe tener al menos 8 caracteres y solo números/símbolos válidos.");
  }

  if (fields.subject.validity.valueMissing) {
    fields.subject.setCustomValidity("Selecciona un asunto/motivo.");
  }

  if (fields.message.validity.valueMissing) {
    fields.message.setCustomValidity("Escribe tu mensaje.");
  } else if (fields.message.validity.tooShort) {
    fields.message.setCustomValidity("El mensaje debe tener al menos 10 caracteres.");
  }

  if (fields.terms.validity.valueMissing) {
    fields.terms.setCustomValidity("Debes aceptar la política de privacidad y términos de uso.");
  }
}

Object.values(fields).forEach(el => {
  el.addEventListener("input", () => {
    setCustomMessages();
    // Quitar mensaje de estado mientras se corrige
    setStatus("Completa el formulario y presiona “Enviar Mensaje”.");
  });
});

form.addEventListener("submit", (e) => {
  e.preventDefault();
  setCustomMessages();

  if (!form.checkValidity()) {
    form.reportValidity();
    setStatus("Revisa los campos marcados en rojo e inténtalo de nuevo.", "error");
    return;
  }

  // Mostrar mensaje emergente de éxito
  showToast("¡Formulario enviado correctamente! 💌");

  // Aquí podrías enviar a un backend; por ahora solo limpiamos
  form.reset();
});

form.addEventListener("reset", () => {
  setStatus("Formulario limpiado. Puedes escribir un nuevo mensaje.");
});

// Función para mostrar el mensaje emergente
function showToast(message) {
  const toast = document.createElement("div");
  toast.classList.add("toast");
  toast.textContent = message;

  // Agregar al DOM
  document.body.appendChild(toast);

  // Mostrar por 3 segundos
  setTimeout(() => {
    toast.classList.add("show");
  }, 100);

  // Eliminar el mensaje después de 3 segundos
  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => toast.remove(), 500); // Eliminar del DOM con animación
  }, 4000);
}
