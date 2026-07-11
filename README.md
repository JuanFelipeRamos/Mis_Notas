# Mis notas

Una aplicación web que permite organizar tareas mediante listas y grupos para gestionarlas fácilmente.

![Python](https://img.shields.io/badge/Python-3.14.6+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Screenshots
<img width="1919" height="797" alt="image" src="https://github.com/user-attachments/assets/2bf49d64-a354-460d-988d-76d11b5f9b83" />
<img width="1919" height="915" alt="image" src="https://github.com/user-attachments/assets/c418f46d-d473-470b-8f33-6312b082f67b" />
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/3a658e41-dd35-4a35-8fd6-3978403f08c5" />



## Características
- Manejo de grupos (tableros) para dividir tareas por temas/proyectos (Crear, Editar y Eliminar grupos).
- Manejo de listas dentro de los grupos para organizar mejor las tareas (Crear, Editar y Eliminar listas).
- Manejo de tareas con acciones como Crear, Marcar como REALIZADA o PENDIENTE y Eliminar.
- Interfaz fácil de manejar.

## Instalación
- **Clonar repositorio al local:** git clone https://github.com/JuanFelipeRamos/Mis_Notas.git
- **Instalar dependencias del backend:** cd Backend, python -m venv env, env\Scripts\activate, pip install -r requirements.txt.
- **Instalar dependencias del frontend:** cd vue-project, npm install.

## Uso
1. **Backend:** cd Backend, env\Scripts\activate, python manage.py runserver.
2. **Frontend**: cd vue-project, npm run dev.
3. Abre `http://localhost:5173` en tu navegador.
4. Crea un usuario y luego inicia sesión con tus credenciales.
5. Desde el dashboard puedes:
  - Crear, editar y eliminar grupos.
  - Crear, editar y eliminar listas.
  - Gestionar tareas.

## Tecnologías usadas
- Python 3.14.6
- Django 5.2.1
- Django rest framework 3.16.0
- vue 3.5.13
- MySQL

## Contribuir
Las contribuciones son bienvenidas:

1. Haz un fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcion`)
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva función'`)
4. Sube la rama (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
