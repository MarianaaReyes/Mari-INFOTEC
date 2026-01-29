// Validación estilo Bootstrap + alertas (demo)
(() => {
  const form = document.getElementById("contact-form");
  const alertOk = document.getElementById("formAlertSuccess");
  const alertErr = document.getElementById("formAlertError");
  const btnReset = document.getElementById("btnReset");

  if (!form) return;

  const hideAlerts = () => {
    alertOk?.classList.add("d-none");
    alertErr?.classList.add("d-none");
  };

  hideAlerts();

  form.addEventListener("submit", (event) => {
    hideAlerts();

    if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
      alertErr?.classList.remove("d-none");
    } else {
      // Demo: no enviamos a servidor
      event.preventDefault();
      alertOk?.classList.remove("d-none");
      form.reset();
      form.classList.remove("was-validated");
      return;
    }

    form.classList.add("was-validated");
  });

  btnReset?.addEventListener("click", () => {
    hideAlerts();
    form.classList.remove("was-validated");
  });
})();
