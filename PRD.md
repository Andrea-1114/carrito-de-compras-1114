# *Product Requirement Document (PRD) — AZcart*

## 1. DESCRIPCIÓN DEL PRODUCTO

**AZcart** es una aplicación web interactiva y de diseño *luxury* (paleta negro profundo con acentos dorados imperiales) diseñada para optimizar y simplificar la experiencia de compra en supermercados y boutique de mascotas.

El sistema permite a los usuarios estructurar, categorizar y gestionar una lista de compras inteligente en tiempo real. Cuenta con un **presupuesto límite de $400.000 COP**, el cual se descuenta dinámicamente con cada producto agregado, ofreciendo validación de duplicados, cálculo automático de saldos, un asistente guía impulsado por IA, catálogo navegable por categorías, componentes visuales interactivos (escena 3D Spline, banner curvo SVG animado y tarjetas nutricionales multi-imagen) y un **formulario de contacto asíncrono con Web3Forms / Fetch API** para la recepción directa de sugerencias o la finalización de solicitudes.

---

## 2. OBJETIVOS

- **Control de Presupuesto en Tiempo Real:** Garantizar que el gasto no exceda los $400.000 COP mediante un indicador dinámico de saldo restante y total gastado.
- **Organización y Clasificación Eficiente:** Agrupar productos por categorías clave (Verduras, Frutas, Lácteos, Carnes, Belleza/Higiene, Perros, Gatos, Mascotas Exóticas, Boutique, etc.).
- **Integridad de los Datos:** Prevenir productos duplicados en el carrito y validar la consistencia de precios.
- **Experiencia de Usuario Inmersiva:** Proveer una interfaz rápida, accesible (con toggle de modo claro/oscuro que mantiene la textura de fondo) y enriquecida con animaciones canvas de partículas doradas, visor 3D e itinerarios dinámicos.
- **Comunicación Directa Cliente-Administrador:** Facilitar el envío de mensajes o solicitudes desde la interfaz cliente usando Web3Forms sin necesidad de recargar la página.

---

## 3. FUNCIONALIDADES PRINCIPALES

### 3.1. Gestión de Lista y Carrito de Compras

- **Añadir Productos:**
  - Registro manual a través de formulario (Nombre, Precio en COP y Categoría).
  - Selección directa desde el **Catálogo interactivo** mediante el botón `+ Añadir`.
- **Edición y Eliminación:** Botón de eliminación directa (`✕`) por ítem que reajusta y reintegra automáticamente el valor al presupuesto disponible.
- **Acceso Rápido en Menú Header:** Botón interactivo `🛒 Carrito` con badge contador de productos en tiempo real (`cartMenuBadge`) que realiza *scroll* suave directo a la lista activa.

### 3.2. Formulario de Contacto e Integración Servidor (Web3Forms)

- **Envío de Mensajes y Solicitudes:** Formulario integrado que recopila Nombre, Correo y Mensaje del usuario.
- **Procesamiento Asíncrono (Fetch API):** Envío en segundo plano hacia la API de Web3Forms sin recargar la página web.
- **Feedback Dinámico:** Deshabilitación temporal del botón de envío (`submitBtn.disabled = true`), cambio de texto en pantalla y alertas de confirmación (`Success`/`Error`).

### 3.3. Control de Presupuesto

- **Límite Inicial:** Configurado en **$400.000 COP**.
- **Cálculo Automático:** Resta continua del saldo disponible y actualización instantánea del gasto acumulado.
- **Alertas de Límite:** Notificación del sistema si un producto excede el saldo restante del presupuesto.

### 3.4. Catálogo, Búsqueda y Organización de Datos

- **Filtrado por Categorías:** Barra de filtros interactiva (`btn-filter`) para segmentar productos (Verduras, Frutas, Lácteos, Carnes, Higiene, Perros, Gatos, Snacks, Boutique, etc.).
- **Búsqueda en Tiempo Real:** Input de búsqueda instantánea que filtra de manera simultánea el catálogo general y la lista de compras activa.
- **Orden y Agrupación:** Los productos se presentan estructurados visualmente con metadatos de categoría.

### 3.5. Componentes Interactivos y Visuales Avanzados

- **Efecto Canvas de Burbujas Doradas:** Partículas dinámicas flotantes sobre fondo oscuro.
- **Hero Slider Multimedia:** Carrusel panorámico borderless con imágenes promocionales e indicadores.
- **Banner Curvo SVG (Marquee):** Texto marquesina con movimiento continuo (*"Descuentos únicos en frutas y verduras aplica términos y condiciones..."*).
- **Visor 3D Spline:** Integración de la escena `<spline-viewer>` para interacción tridimensional.
- **Tarjetas Categorías Interactivas:** Tarjetas con doble capa de imagen que abren modales emergentes con tablas nutricionales detalladas.

### 3.6. Servicio del Sistema e IA Guía

- **Asistente Virtual AZcart IA:** Caja de consultas con sugerencias rápidas (*chips*) para orientar la optimización del presupuesto de $400.000 COP según los intereses del cliente.

---

## 4. CRITERIOS DE ÉXITO

1. **Gestión Sin Errores:** El usuario puede armar, modificar y gestionar su lista de mercado sin duplicar ítems ni generar inconsistencias de precios.
2. **Precisión Financiera:** El presupuesto inicial de $400.000 COP se descuenta e incrementa con un margen de error del 0%.
3. **Flujo de Usuario Intuitivo:** El conteo del badge del carrito en el header se actualiza en tiempo real y permite la navegación directa a la sección de compras.
4. **Envío de Formularios Fluido:** El formulario de contacto de Web3Forms procesa el mensaje de manera asíncrona mediante Fetch API, proporcionando respuesta visual sin recargar la página.
