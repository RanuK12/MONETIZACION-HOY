# KIT 2: Customer Feedback Analyzer

## Descripción
Convierte feedback de clientes en insights de producto y validación de mercado automáticamente.

## Instrucciones (Copy-Paste Ready)

### Paso 1: Recolecta feedback
Usa cualquiera de estos (gratuitos):
- Typeform (5 respuestas gratis)
- Google Forms
- Twitter polls
- Comentarios de clientes existentes
- Emails de usuarios

### Paso 2: Copia este prompt exacto

```
Analiza este feedback de clientes y dame:
1. Problemas principales (top 3)
2. Tono del cliente (frustración, interés, neutral)
3. Oportunidades de venta (qué necesitan)
4. Quotes para testimonios (las mejores frases)
5. Mejoras de producto sugeridas
6. Próximos pasos recomendados

FEEDBACK:
[INSERTA EL FEEDBACK AQUÍ]

Formato de salida:
🔴 PROBLEMAS: [lista]
📊 TONO: [análisis]
💰 OPORTUNIDADES: [lista]
💬 QUOTES: [frases textuales]
🔧 MEJORAS: [ideas]
→ ACCIÓN: [qué hacer ahora]
```

### Paso 3: Ejecuta análisis
Pega en Claude/ChatGPT y obtén insights en segundos.

### Paso 4: Actúa sobre los resultados
- Usa quotes en tu marketing
- Implementa mejoras rápidas
- Segmenta clientes por problema
- Crea soluciones específicas

## Prompts Listos (Copy-Paste)

### Análisis Rápido:
```
Tengo 5 emails de clientes. Dime en 3 puntos: qué problema tienen, qué solución esperan, y si pagarían por mejorar.

CLIENTES:
[email 1]
[email 2]
[email 3]
[email 4]
[email 5]
```

### Análisis Profundo:
```
Eres analista de productos. Estos son comentarios de usuarios de mi [TU PRODUCTO].
Identifica:
- Necesidades explícitas (dicen "necesito X")
- Necesidades implícitas (lo que no dicen pero necesitan)
- Tamaño del problema (cuántos lo mencionan)
- Disposición a pagar (qué tan urgente es)
- Competencia implícita (qué usan ahora)

FEEDBACK:
[INSERTA TODOS LOS COMENTARIOS]
```

### Análisis de Sentimiento:
```
Clasifica estos comentarios por:
1. Satisfacción (0-10)
2. Posible churn (sí/no)
3. Potencial de referral (sí/no)
4. Mejor momento para upsell (cuándo)
5. Riesgo de que se vaya a competencia (alto/medio/bajo)

COMENTARIOS:
[INSERTA AQUÍ]
```

## Integración (Sin Código)

### Opción 1: Google Forms + Sheets + ChatGPT
1. Google Forms → recolecta feedback
2. Copia respuestas a Sheets
3. Pega en ChatGPT con el prompt
4. Guarda análisis en mismo Sheets

### Opción 2: Zapier Automático (Gratis hasta 100 tareas)
1. Google Forms → Zapier
2. Zapier → ChatGPT API (con Zapier)
3. Resultado → Google Sheets
4. Recibe análisis cada vez que alguien contesta

## Formato CSV para Recolectar

Guarda esto como `feedback-raw.csv`:

```
fecha,fuente,cliente,feedback,problema,disposicion_pago,urgencia
2026-04-15,email,Carlos,"Necesito herramienta que...",integracion,si,alta
2026-04-15,twitter,Sofia,"No funciona bien cuando...",performance,no,media
2026-04-14,form,Juan,"Perfecto, pero falta...",feature,si,baja
```

## Resultados Esperados
- Semana 1: identifica 2-3 problemas principales
- Semana 2: 5+ quotes para marketing
- Mes 1: roadmap de mejoras validado por clientes
- Mes 2: argumentos de venta específicos por segmento

## Monetización
- Productos: crea basado en feedback de customers
- Pricing: valida con "disposicion_pago"
- Copy: usa quotes directamente en Gumroad
- Testimonios: convierte feedback → social proof
