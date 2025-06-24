# En este archivo estará la lógica para enviar correos electrónicos a los usuarios
import requests
from django.conf import settings

# Función para enviar emails
def send_email(email_user, subject, html_content):
    url = "https://api.resend.com/emails"

    headers = {
        "Authorization": f"Bearer {settings.RESEND_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
      "from": "Mis Tareas <onboarding@resend.dev>", # Solo funciona en desarrollo
      "to": [email_user],
      "subject": subject,
      "html": html_content
    }

    print("Enviando con estos datos:")
    print("Headers:", headers)
    print("Data:", data)

    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)

        print("Respuesta:", response.text)

        if response.status_code == 200:
            return "Correo enviado exitosamente."
        else:
            return f"Error al enviar el correo. Código: {response.status_code}, respuesta: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error en la petición a la API: {str(e)}"
