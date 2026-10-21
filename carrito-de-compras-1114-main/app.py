import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_folder=".", template_folder=".")

# Almacenamiento en memoria de las listas guardadas
saved_carts = []


@app.route("/")
def index():
  """Ruta principal para servir la aplicación AZcart."""
  return render_template("index.html")


@app.route("/api/submit-cart", methods=["POST"])
def submit_cart():
  """Ruta API para recibir y guardar la lista de compras."""
  # Obtener datos si vienen por Formulario HTML o por JSON (fetch)
  if request.is_json:
    data = request.get_json()
    user_email = data.get("user_email")
    cart_summary = data.get("cart_summary")
  else:
    user_email = request.form.get("user_email")
    cart_summary = request.form.get("cart_summary")

  # Validación de datos obligatorios
  if not user_email or not cart_summary:
    return (
        jsonify({
            "status": "error",
            "message": (
                "Datos incompletos. Debe proporcionar correo y productos."
            ),
        }),
        400,
    )

  # Intentar parsear el JSON de productos si viene como string
  try:
    if isinstance(cart_summary, str):
      parsed_items = json.loads(cart_summary)
    else:
      parsed_items = cart_summary
  except Exception:
    parsed_items = cart_summary

  # Validar que la lista de compras no esté vacía
  if not parsed_items or parsed_items == []:
    return (
        jsonify({
            "status": "error",
            "message": "La lista de compras está vacía.",
        }),
        400,
    )

  # Guardar en la base de datos temporal
  record = {"email": user_email, "items": parsed_items}
  saved_carts.append(record)

  print(
      f"[AZcart Python Backend] Lista recibida para {user_email}:"
      f" {parsed_items}"
  )

  # Responder según el tipo de petición
  if request.is_json:
    return jsonify({
        "status": "success",
        "message": "Lista de compras guardada con éxito.",
        "data": record,
    })

  # Respuesta HTML profesional si se envía directamente desde un <form>
  return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>AZcart - Confirmación</title>
        <style>
            body {{
                background-color: #0A192F;
                color: #F8FAFC;
                font-family: 'Times New Roman', serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background-color: #112240;
                border: 2px solid #D4AF37;
                border-radius: 8px;
                padding: 3rem;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                max-width: 500px;
            }}
            h2 {{ color: #D4AF37; margin-bottom: 1rem; font-size: 2rem; }}
            p {{ font-size: 1.1rem; line-height: 1.6; color: #8892B0; }}
            .btn {{
                display: inline-block;
                margin-top: 1.5rem;
                padding: 0.8rem 1.8rem;
                background-color: #D4AF37;
                color: #0A192F;
                text-decoration: none;
                font-weight: bold;
                border-radius: 4px;
                transition: background 0.3s;
            }}
            .btn:hover {{ background-color: #F3E5AB; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>⚜️ ¡Lista Guardada Exitosamente!</h2>
            <p>Se ha procesado y enviado la confirmación de su mercado al correo:<br><strong style="color:#F8FAFC;">{user_email}</strong></p>
            <a href="/" class="btn">Regresar a AZcart</a>
        </div>
    </body>
    </html>
    """


@app.route("/api/get-carts", methods=["GET"])
def get_carts():
  """Ruta opcional para consultar los carritos guardados."""
  return jsonify({"status": "success", "total": len(saved_carts), "carts": saved_carts})


if __name__ == "__main__":
  app.run(debug=True, port=5000)