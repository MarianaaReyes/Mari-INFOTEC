// ========================
// Datos base de eventos
// ========================
const EVENTOS = [
  {
    id: "edu",
    nombre: "Tecnología Educativa",
    fecha: "2026-02-12 10:00",
    lugar: "Auditorio A",
    categoria: "Educación",
    descripcion: "Tendencias, herramientas y estrategias para mejorar el aprendizaje."
  },
  {
    id: "web",
    nombre: "Desarrollo Web",
    fecha: "2026-02-18 16:00",
    lugar: "Sala 2",
    categoria: "Tecnología",
    descripcion: "Front-end, back-end y buenas prácticas para proyectos modernos."
  },
  {
    id: "mkt",
    nombre: "Marketing Digital",
    fecha: "2026-03-02 09:00",
    lugar: "Centro de cómputo",
    categoria: "Marketing",
    descripcion: "Estrategias, redes sociales, anuncios y crecimiento."
  },
  {
    id: "biz",
    nombre: "Innovación Empresarial",
    fecha: "2026-03-10 12:30",
    lugar: "Sala de juntas",
    categoria: "Negocios",
    descripcion: "Modelos de negocio, liderazgo e innovación."
  }
];

const MAP_EVENTOS = Object.fromEntries(EVENTOS.map(e => [e.id, e]));

// ========================
// LocalStorage helpers
// ========================
function getParticipantes() {
  return JSON.parse(localStorage.getItem("participantes")) || [];
}
function setParticipantes(arr) {
  localStorage.setItem("participantes", JSON.stringify(arr));
}
function fmtFecha(d) {
  const pad = n => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}
function qparam(name) {
  return new URLSearchParams(location.search).get(name);
}

// ========================
// INDEX: render tarjetas
// ========================
function initIndex() {
  const grid = document.getElementById("eventGrid");
  if (!grid) return;

  const q = document.getElementById("q");
  const cat = document.getElementById("cat");
  const sort = document.getElementById("sort");

  function countsPorEvento() {
    const datos = getParticipantes();
    const out = {};
    for (const ev of EVENTOS) out[ev.id] = { total: 0, ponentes: 0 };

    for (const p of datos) {
      if (!out[p.evento]) continue;
      out[p.evento].total++;
      if (p.tipo === "Ponente") out[p.evento].ponentes++;
    }
    return out;
  }

  function render() {
    const counts = countsPorEvento();
    let list = [...EVENTOS];

    // filtros
    const qv = (q.value || "").trim().toLowerCase();
    const cv = cat.value;

    if (qv) list = list.filter(e => e.nombre.toLowerCase().includes(qv));
    if (cv) list = list.filter(e => e.categoria === cv);

    // sort
    const mode = sort.value;
    list.sort((a, b) => {
      if (mode === "name_az") return a.nombre.localeCompare(b.nombre);
      if (mode === "participants_desc") {
        return (counts[b.id]?.total || 0) - (counts[a.id]?.total || 0);
      }
      // date_desc por defecto
      return b.fecha.localeCompare(a.fecha);
    });

    grid.innerHTML = "";
    list.forEach(e => {
      const c = counts[e.id] || { total: 0, ponentes: 0 };

      const card = document.createElement("section");
      card.className = "evento";
      card.innerHTML = `
        <h3>${e.nombre}</h3>
        <p><strong>Fecha:</strong> ${e.fecha}</p>
        <p><strong>Lugar:</strong> ${e.lugar}</p>
        <p><strong>Categoría:</strong> ${e.categoria}</p>
        <p>${e.descripcion}</p>

        <div class="statsMini">
          <span class="pill">Participantes: ${c.total}</span>
          <span class="pill pill--pon">Ponentes: ${c.ponentes}</span>
        </div>

        <div class="actions">
          <a href="registro.html?event=${e.id}&type=Asistente">Registrarme (Asistente)</a>
          <a href="registro.html?event=${e.id}&type=Ponente">Registrarme (Ponente)</a>
          <a href="participantes.html?event=${e.id}">Ver participantes</a>
          <a href="#" data-detail="${e.id}">Ver detalles</a>
        </div>
      `;
      grid.appendChild(card);
    });

    grid.querySelectorAll("[data-detail]").forEach(a => {
      a.addEventListener("click", (ev) => {
        ev.preventDefault();
        const id = a.getAttribute("data-detail");
        const e = MAP_EVENTOS[id];
        alert(
          `${e.nombre}\n\nFecha: ${e.fecha}\nLugar: ${e.lugar}\nCategoría: ${e.categoria}\n\n${e.descripcion}`
        );
      });
    });
  }

  [q, cat, sort].forEach(el => el.addEventListener("input", render));
  render();
}

// ========================
// REGISTRO
// ========================
function initRegistro() {
  const form = document.getElementById("formRegistro");
  if (!form) return;

  const selEvento = document.getElementById("evento");
  const asist = document.getElementById("asistenteCampos");
  const pon = document.getElementById("ponenteCampos");

  // llenar select
  selEvento.innerHTML = EVENTOS.map(e => `<option value="${e.id}">${e.nombre}</option>`).join("");

  // preselección por query params
  const ev = qparam("event");
  const tp = qparam("type");
  if (ev && MAP_EVENTOS[ev]) selEvento.value = ev;

  if (tp === "Ponente" || tp === "Asistente") {
    const radio = document.querySelector(`input[name="tipo"][value="${tp}"]`);
    if (radio) radio.checked = true;
  }

  function toggle() {
    const tipo = document.querySelector("input[name='tipo']:checked").value;
    asist.style.display = (tipo === "Asistente") ? "block" : "none";
    pon.style.display = (tipo === "Ponente") ? "block" : "none";
  }

  document.querySelectorAll("input[name='tipo']").forEach(r => r.addEventListener("change", toggle));
  toggle();

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const tipo = document.querySelector("input[name='tipo']:checked").value;

    const participante = {
      id: crypto?.randomUUID ? crypto.randomUUID() : String(Date.now()),
      evento: selEvento.value,
      tipo,
      // comunes
      nombre: document.getElementById("nombre").value.trim(),
      email: document.getElementById("email").value.trim(),
      telefono: document.getElementById("telefono").value.trim(),
      empresa: document.getElementById("empresa").value.trim(),
      pais: document.getElementById("pais").value.trim(),
      fechaRegistro: fmtFecha(new Date()),
      // asistente
      nivel: document.getElementById("nivel").value,
      intereses: document.getElementById("intereses").value.trim(),
      certificado: document.getElementById("certificado").checked,
      // ponente
      titulo: document.getElementById("titulo").value.trim(),
      duracion: document.getElementById("duracion").value,
      requisitos: document.getElementById("requisitos").value.trim(),
      bio: document.getElementById("bio").value.trim(),
      redes: document.getElementById("redes").value.trim()
    };

    // validación mínima
    if (!participante.nombre || !participante.email || !participante.telefono) {
      alert("Completa los campos obligatorios: Nombre, Email y Teléfono.");
      return;
    }

    const datos = getParticipantes();
    datos.push(participante);
    setParticipantes(datos);

    alert("Registrado correctamente ✅");
    form.reset();
    // mantener evento seleccionado si venía desde una tarjeta
    if (ev && MAP_EVENTOS[ev]) selEvento.value = ev;
    // default a asistente
    document.querySelector(`input[name="tipo"][value="Asistente"]`).checked = true;
    toggle();
  });
}

// ========================
// PARTICIPANTES (TABLA)
// ========================
function initParticipantes() {
  const tbody = document.getElementById("tbody");
  if (!tbody) return;

  const fEvento = document.getElementById("fEvento");
  const fSearch = document.getElementById("fSearch");
  const btnLimpiar = document.getElementById("btnLimpiar");

  const statTotal = document.getElementById("statTotal");
  const statAsist = document.getElementById("statAsist");
  const statPon = document.getElementById("statPon");

  // llenar select de evento
  fEvento.innerHTML = `
    <option value="">Todos los eventos</option>
    ${EVENTOS.map(e => `<option value="${e.id}">${e.nombre}</option>`).join("")}
  `;

  const qpEv = qparam("event");
  if (qpEv && MAP_EVENTOS[qpEv]) fEvento.value = qpEv;

  function render() {
    const datos = getParticipantes();
    const ev = fEvento.value;
    const s = (fSearch.value || "").trim().toLowerCase();

    let list = [...datos];
    if (ev) list = list.filter(p => p.evento === ev);
    if (s) list = list.filter(p =>
      (p.nombre || "").toLowerCase().includes(s) ||
      (p.email || "").toLowerCase().includes(s)
    );

    const asistentes = list.filter(p => p.tipo === "Asistente").length;
    const ponentes = list.filter(p => p.tipo === "Ponente").length;

    statTotal.textContent = `Total: ${list.length}`;
    statAsist.textContent = `Asistentes: ${asistentes}`;
    statPon.textContent = `Ponentes: ${ponentes}`;

    tbody.innerHTML = "";
    list.forEach(p => {
      const evName = MAP_EVENTOS[p.evento]?.nombre || p.evento;

      const detalle = (p.tipo === "Asistente")
        ? `Nivel: ${p.nivel || "-"} | Intereses: ${p.intereses || "-"} | Cert: ${p.certificado ? "Sí" : "No"}`
        : `Ponencia: ${p.titulo || "-"} | Dur: ${p.duracion || "-"} | Redes: ${p.redes || "-"}`;

      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${evName}</td>
        <td><span class="badge ${p.tipo === "Ponente" ? "badge--pon" : "badge--asist"}">${p.tipo}</span></td>
        <td>${p.nombre || ""}</td>
        <td>${p.email || ""}</td>
        <td>${p.telefono || ""}</td>
        <td>${p.empresa || ""}</td>
        <td>${p.pais || ""}</td>
        <td>${p.fechaRegistro || ""}</td>
        <td class="small">${detalle}</td>
        <td><button class="btn-delete" data-del="${p.id}">Eliminar</button></td>
      `;
      tbody.appendChild(tr);
    });

    tbody.querySelectorAll("[data-del]").forEach(btn => {
      btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-del");
        if (!confirm("¿Eliminar este registro?")) return;
        const datos = getParticipantes().filter(x => x.id !== id);
        setParticipantes(datos);
        render();
      });
    });
  }

  btnLimpiar.addEventListener("click", () => {
    fEvento.value = "";
    fSearch.value = "";
    render();
  });

  fEvento.addEventListener("change", render);
  fSearch.addEventListener("input", render);

  render();
}

// ========================
// Init general
// ========================
initIndex();
initRegistro();
initParticipantes();
