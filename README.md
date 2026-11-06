# Prompt Architect

> Analiza un prompt antes de enviarlo a una IA y conviértelo en una instrucción más clara, completa y accionable.

**Prompt Architect** es una mini herramienta local para detectar puntos débiles habituales: falta de contexto, objetivo poco concreto, ausencia de restricciones, formato de respuesta indefinido o rol no especificado.

## Qué hace

- Puntúa la calidad del prompt sobre 100.
- Detecta cinco componentes: rol, objetivo, contexto, restricciones y formato.
- Explica qué falta con recomendaciones concretas.
- Genera una versión mejorada como punto de partida.
- Funciona localmente, sin API key ni datos enviados a terceros.

## Demo rápida

```bash
python app.py "Hazme una estrategia de marketing"
```

## Instalación

```bash
git clone https://github.com/alvaroalcalaa/prompt-architect.git
cd prompt-architect
python app.py "Escribe un post para LinkedIn sobre IA"
```

Requiere Python 3.10 o superior. No tiene dependencias externas.

## Ejemplos

```bash
python app.py "Actúa como recruiter tech. Con este CV: [texto], crea 5 mejoras. Máximo 200 palabras y usa bullets."
python app.py --interactive
```

## Estructura

```text
prompt-architect/
├── app.py          # CLI y motor de análisis
├── tests.py        # Pruebas rápidas
├── README.md
└── LICENSE
```

## English

Prompt Architect is a privacy-first local CLI that reviews a prompt, scores its completeness and proposes a stronger version. It needs no API key and sends no data anywhere.

## Licencia

MIT © 2026 Álvaro Alcalá
