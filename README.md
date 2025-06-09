# Juegos Didácticos - Don Bosco Pampahasi

![Licencia](https://img.shields.io/badge/licencia-MIT-blue.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

Un portal web interactivo con 16 juegos educativos diseñados para niños de primaria, desarrollados para la unidad educativa "Don Bosco Pampahasi". El proyecto abarca diversas áreas del conocimiento como lenguaje, matemáticas y ciencias naturales, utilizando mecánicas de juego sencillas e intuitivas.

---

<details>
<summary>🇬🇧 **View in English**</summary>

# Didactic Games - Don Bosco Pampahasi

An interactive web portal with 16 educational games designed for elementary school children, developed for the "Don Bosco Pampahasi" educational unit. The project covers various areas of knowledge such as language, mathematics, and natural sciences, using simple and intuitive game mechanics.

</details>

---

## 🎮 Los Juegos

A continuación, se presenta una tabla con todos los juegos disponibles en el portal.

| # | Juego | Descripción | Habilidades |
| :--- | :--- | :--- | :--- |
| 1 | **Adivina el Animal** | Identifica al animal por su imagen y escribe su nombre correctamente. | Ortografía, Vocabulario |
| 2 | **Adivina el Alimento** | Reconoce alimentos a partir de imágenes y escribe su nombre letra por letra. | Ortografía, Vocabulario |
| 3 | **Partes del Cuerpo** | Aprende a escribir las partes del cuerpo humano viendo una imagen de cada una. | Vocabulario, Anatomía |
| 4 | **Inglés y Español** | Traduce palabras del inglés al español (y viceversa) con ayuda de imágenes. | Bilingüismo, Vocabulario |
| 5 | **Mecanografía y Ortografía** | Mejora la velocidad de escritura y la ortografía escribiendo palabras que corresponden a imágenes aleatorias. | Mecanografía, Ortografía |
| 6 | **Juego de Sílabas** | Forma la palabra correcta haciendo clic en sus sílabas desordenadas. | Conciencia fonológica |
| 7 | **Ordena el Alfabeto** | Haz clic en las letras en el orden alfabético correcto para completar el abecedario. | Abecedario, Secuenciación |
| 8 | **Reglas de Acentuación** | Clasifica palabras como Agudas, Graves, Esdrújulas o Sobresdrújulas. | Ortografía, Gramática |
| 9 | **Tablas de Multiplicar** | Completa una tabla de multiplicar tradicional. | Cálculo, Multiplicación |
| 10 | **Multiplicación Aleatoria**| Resuelve multiplicaciones en una tabla con números generados al azar. | Cálculo, Multiplicación |
| 11 | **Juego de Sumas** | Resuelve una tabla de sumas con números aleatorios de hasta dos cifras. | Cálculo, Suma |
| 12 | **Juego de Restas** | Resuelve una tabla de restas asegurando que el resultado nunca sea negativo. | Cálculo, Resta |
| 13 | **Juego de Divisiones** | Completa una tabla con divisiones que siempre tienen un resultado entero. | Cálculo, División |
| 14 | **Juego de Múltiplos** | Identifica y haz clic en todos los múltiplos de un número dado en una cuadrícula. | Teoría de números |
| 15 | **Pares e Impares** | Encuentra todos los números pares o impares en una cuadrícula. | Teoría de números |
| 16 | **Contar hasta 100** | Aprende los números del 1 al 100 de forma interactiva escribiendo cada número. | Conteo, Reconocimiento numérico |

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera para facilitar su mantenimiento y expansión:
/
├── index.html                  # Página principal que sirve como portal
├── logo.png                    # Logo de la institución
├── src/                        # Carpeta para recursos compartidos (imágenes, etc.)
│   ├── animales.png
│   ├── mult.png
│   └── ... (imágenes para las tarjetas y los juegos)
├── animales/
│   └── animales.html           # HTML del juego de adivinar animales
├── multiplicacion/
│   └── multiplicacion.html     # HTML del juego de tablas de multiplicar
└── ... (una carpeta por cada uno de los 16 juegos)

## 🚀 Cómo Empezar

Este proyecto no requiere un proceso de instalación complejo. Está construido con HTML, CSS y JavaScript puros, utilizando Tailwind CSS a través de un CDN.

**Requisitos:**
* Un navegador web moderno (Chrome, Firefox, Edge, etc.).
* Un servidor web local (opcional, pero recomendado para evitar problemas de CORS).

**Pasos:**
1.  **Clona o descarga el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/juegos-didacticos.git](https://github.com/tu-usuario/juegos-didacticos.git)
    ```
    O descarga el archivo ZIP y extráelo.

2.  **Navega a la carpeta del proyecto:**
    ```bash
    cd juegos-didacticos
    ```

3.  **Abre el archivo `index.html`:**
    * Puedes abrir `index.html` directamente en tu navegador.
    * **Recomendado:** Para asegurar que todo funcione correctamente (especialmente la carga de imágenes y otros recursos locales), utiliza un servidor local. Si tienes Python instalado, puedes ejecutar:
        ```bash
        # Python 3.x
        python -m http.server
        ```
        Luego, abre tu navegador y ve a `http://localhost:8000`.

## ⚙️ Uso y API

La mayoría de los juegos funcionan de manera local sin necesidad de conexión a internet, excepto dos de ellos:

* **Mecanografía y Ortografía**
* **Inglés y Español**

Estos juegos utilizan la **API de Unsplash** para cargar imágenes de forma dinámica. Para que funcionen, necesitas obtener una clave de API gratuita:
1.  Ve a [Unsplash Developers](https://unsplash.com/developers).
2.  Crea una cuenta y registra una nueva aplicación.
3.  Copia tu **"Access Key"**.
4.  Abre los archivos `mecanografia/mecanografia.html` e `ingles/ingles.html` y pega tu clave donde se indica:
    ```javascript
    const YOUR_UNSPLASH_ACCESS_KEY = "AQUÍ_VA_TU_CLAVE_DE_API";
    ```

## 🛠️ Tecnologías Utilizadas

* **HTML5:** Estructura de las páginas.
* **CSS3:** Estilos generales.
* **Tailwind CSS:** Framework de CSS para un diseño rápido y responsivo, cargado a través de CDN.
* **JavaScript (ES6+):** Lógica e interactividad de todos los juegos.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

Desarrollado con ❤️ por **Ing. Paulo Daniel Batuani Hurtado**.
