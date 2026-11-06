"""Prompt Architect: a dependency-free local prompt quality inspector."""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass

COMPONENTS = {
    "rol": ["actúa como", "actua como", "eres un", "asume el rol", "especialista", "experto", "consultor"],
    "objetivo": ["crea", "diseña", "disena", "escribe", "analiza", "genera", "resume", "explica", "compara", "planifica"],
    "contexto": ["para", "contexto", "audiencia", "empresa", "marca", "sector", "datos:", "basado en"],
    "restricciones": ["máximo", "maximo", "no ", "solo ", "evita", "incluye", "tono", "límite", "limite"],
    "formato": ["bullets", "lista", "tabla", "markdown", "json", "pasos", "apartados", "párrafos", "parrafos"],
}

SUGGESTIONS = {
    "rol": "Define quién debe responder (ej.: «Actúa como analista de datos»).",
    "objetivo": "Empieza con un verbo concreto: crea, analiza, compara o diseña.",
    "contexto": "Añade para quién es, el sector, los datos disponibles o el caso de uso.",
    "restricciones": "Marca límites: extensión, tono, cosas a evitar y criterios de éxito.",
    "formato": "Pide cómo quieres recibir la respuesta: tabla, bullets, JSON o pasos.",
}

@dataclass
class Analysis:
    score: int
    detected: list[str]
    missing: list[str]
    proposed_prompt: str

def analyze(prompt: str) -> Analysis:
    normalized = prompt.lower()
    detected = [
        component for component, signals in COMPONENTS.items()
        if any(signal in normalized for signal in signals)
    ]
    missing = [component for component in COMPONENTS if component not in detected]
    score = min(100, len(detected) * 18 + min(len(prompt) // 15, 10))

    additions = []
    if "rol" in missing:
        additions.append("Actúa como especialista en el tema.")
    if "objetivo" in missing:
        additions.append("Realiza la tarea solicitada de forma práctica.")
    if "contexto" in missing:
        additions.append("Ten en cuenta la audiencia, el sector y el objetivo final.")
    if "restricciones" in missing:
        additions.append("Sé claro, específico y evita información no verificada.")
    if "formato" in missing:
        additions.append("Entrega la respuesta con títulos y bullets accionables.")

    proposed = prompt.strip()
    if additions:
        proposed = " ".join(additions) + "\n\nSolicitud original: " + proposed
    return Analysis(score, detected, missing, proposed)

def display(analysis: Analysis) -> None:
    print(f"\nPuntuación: {analysis.score}/100")
    print("Detectado:", ", ".join(analysis.detected) or "ningún componente")
    if analysis.missing:
        print("\nMejoras recomendadas:")
        for component in analysis.missing:
            print(f"- {component.title()}: {SUGGESTIONS[component]}")
    print("\nPrompt propuesto:\n")
    print(analysis.proposed_prompt)

def main() -> None:
    parser = argparse.ArgumentParser(description="Analiza y mejora prompts localmente.")
    parser.add_argument("prompt", nargs="*", help="Prompt que quieres revisar")
    parser.add_argument("--interactive", action="store_true", help="Escribir el prompt en modo interactivo")
    args = parser.parse_args()

    prompt = " ".join(args.prompt).strip()
    if args.interactive or not prompt:
        prompt = input("Pega tu prompt: ").strip()
    if not prompt:
        raise SystemExit("Necesito un prompt para analizar.")
    display(analyze(prompt))

if __name__ == "__main__":
    main()
