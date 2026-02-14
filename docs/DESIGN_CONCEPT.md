# Design-Konzept: Sabines Kinderschminken - Moderne Website

## 🎨 Design-Philosophie

**Motto**: "Professionell, freundlich, bunt - aber nicht kindisch"

### Kernwerte
- **Vertrauenswürdig**: Eltern sollen sich sicher fühlen
- **Professionell**: Seriöser Service für Events
- **Kreativ**: Bunte, fröhliche Atmosphäre
- **Modern**: Zeitgemäßes, responsives Design

---

## 🎨 Farbschema

### Primärfarben
```css
--primary: #FF6B9D;        /* Freundliches Pink */
--primary-dark: #E54D7F;   /* Dunkleres Pink für Hover */
--primary-light: #FFB3D1;  /* Helles Pink für Akzente */

--secondary: #4ECDC4;      /* Türkis/Mint */
--secondary-dark: #45B7AF; /* Dunkleres Türkis */
--secondary-light: #A8E6E1;/* Helles Türkis */

--accent: #FFE66D;         /* Warmes Gelb */
--accent-dark: #F4D84A;    /* Goldgelb */
```

### Neutrale Farben
```css
--text-dark: #2C3E50;      /* Dunkelgrau für Text */
--text-medium: #546E7A;    /* Mittleres Grau */
--text-light: #95A5A6;     /* Helles Grau */

--background-white: #FFFFFF;
--background-light: #F8F9FA;
--background-cream: #FFF8F0; /* Warmer Hintergrund */
```

### Verwendung
- **Pink**: Hauptfarbe, CTAs, Links, wichtige Elemente
- **Türkis**: Sekundäre Buttons, Hervorhebungen, Service-Icons
- **Gelb**: Akzente, Hover-Effekte, Highlights
- **Grau**: Text, Schatten, Borders

---

## 📱 Layout & Struktur

### Header
```
┌─────────────────────────────────────────────┐
│  [LOGO]              Navigation              │
│                 Home | Services | Galerie   │
│                 Über | Kontakt              │
└─────────────────────────────────────────────┘
```

**Desktop**:
- Fixierter Header mit transparentem Hintergrund
- Wird beim Scrollen zu solidem Weiß mit leichtem Schatten
- Logo links, Navigation rechts
- CTA-Button "Jetzt anfragen" prominent (Pink)

**Mobile**:
- Hamburger-Menü rechts
- Logo zentriert oder links
- Slide-in Navigation von rechts

### Hero-Section (Startseite)
```
┌─────────────────────────────────────────────┐
│                                             │
│    [HERO-BILD: Kind mit Schmetterling]      │
│                                             │
│        Sabines Kinderschminken              │
│     Zauberhafte Momente für Ihr Event       │
│                                             │
│         [Jetzt anfragen] [Galerie]          │
│                                             │
└─────────────────────────────────────────────┘
```

- Vollbild-Hero mit Overlay
- Große, einladende Headline
- Subline mit USP
- Zwei CTAs (primär + sekundär)

### Service-Übersicht
```
┌─────────────────────────────────────────────┐
│           Unsere Leistungen                 │
│                                             │
│  [Icon]        [Icon]        [Icon]         │
│  Kinder-       Ballon-       Body-          │
│  schminken     Figuren       painting       │
│  + Text        + Text        + Text         │
│                                             │
│  [Icon]        [Icon]        [Icon]         │
│  Event-        Airbrush      Kinder-        │
│  Animation     Tattoos       geburtstag     │
│  + Text        + Text        + Text         │
└─────────────────────────────────────────────┘
```

- Grid-Layout (3 Spalten Desktop, 2 Tablet, 1 Mobile)
- Card-Design mit Hover-Effekt
- Icons in Primärfarbe
- Kurzbeschreibung
- "Mehr erfahren" Link

### Galerie
```
┌─────────────────────────────────────────────┐
│              Unsere Galerie                 │
│                                             │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐  │
│  │  Bild │ │  Bild │ │  Bild │ │  Bild │  │
│  └───────┘ └───────┘ └───────┘ └───────┘  │
│                                             │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐  │
│  │  Bild │ │  Bild │ │  Bild │ │  Bild │  │
│  └───────┘ └───────┘ └───────┘ └───────┘  │
└─────────────────────────────────────────────┘
```

- Masonry-Layout oder Grid
- Lightbox beim Klick
- Filterfunktion nach Kategorien (Kinderschminken, Ballons, Events)
- Lazy Loading

### Footer
```
┌─────────────────────────────────────────────┐
│  [LOGO]          Links         Social       │
│                                             │
│  Slogan       • Home          [FB] [IG]    │
│               • Services                    │
│               • Galerie                     │
│               • Kontakt                     │
│                                             │
│  ─────────────────────────────────────────  │
│                                             │
│  © 2026 Sabines Kinderschminken             │
│  Impressum | Datenschutz                    │
└─────────────────────────────────────────────┘
```

---

## 🔤 Typografie

### Schriftarten

**Option 1: Modern & Freundlich**
```css
--font-heading: 'Poppins', sans-serif;     /* Überschriften */
--font-body: 'Inter', sans-serif;          /* Fließtext */
--font-accent: 'Pacifico', cursive;        /* Akzente/Logo */
```

**Option 2: Klassisch & Elegant**
```css
--font-heading: 'Montserrat', sans-serif;
--font-body: 'Open Sans', sans-serif;
--font-accent: 'Dancing Script', cursive;
```

### Größen
```css
--h1: 3.5rem;     /* 56px - Hero Headlines */
--h2: 2.5rem;     /* 40px - Section Headings */
--h3: 2rem;       /* 32px - Subsections */
--h4: 1.5rem;     /* 24px - Card Titles */
--body: 1rem;     /* 16px - Basis */
--small: 0.875rem;/* 14px - Captions */
```

**Mobile-Anpassungen**: -20% bis -30%

---

## 🎯 Komponenten

### Buttons

**Primär-Button** (CTA)
```css
background: linear-gradient(135deg, #FF6B9D, #E54D7F);
padding: 14px 32px;
border-radius: 30px;
font-weight: 600;
box-shadow: 0 4px 15px rgba(255, 107, 157, 0.3);
transition: all 0.3s ease;

hover: transform: translateY(-2px);
       box-shadow: 0 6px 20px rgba(255, 107, 157, 0.4);
```

**Sekundär-Button**
```css
background: transparent;
border: 2px solid #4ECDC4;
color: #4ECDC4;
padding: 12px 30px;
border-radius: 30px;

hover: background: #4ECDC4;
       color: white;
```

### Cards (Service-Karten)
```css
background: white;
border-radius: 20px;
padding: 30px;
box-shadow: 0 10px 40px rgba(0,0,0,0.08);
transition: all 0.3s ease;

hover: transform: translateY(-5px);
       box-shadow: 0 15px 50px rgba(0,0,0,0.12);
```

### Icons
- Farbige Icons (Primär- oder Sekundärfarbe)
- Größe: 48px - 64px
- Linien-Icons (nicht zu verspielt)
- Konsistent im Stil

---

## 📐 Spacing & Grid

### Container
```css
max-width: 1200px;
padding: 0 20px;
margin: 0 auto;
```

### Spacing-System (8px-Basis)
```css
--space-xs: 8px;
--space-sm: 16px;
--space-md: 24px;
--space-lg: 48px;
--space-xl: 80px;
--space-xxl: 120px;
```

### Grid
- 12-Column Grid (Desktop)
- 8-Column Grid (Tablet)
- 4-Column Grid (Mobile)

---

## 🎭 Animationen & Interaktionen

### Micro-Interactions
```css
/* Smooth Transitions */
transition: all 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);

/* Hover-Effekte */
- Cards: Lift + Shadow
- Buttons: Lift + Brightness
- Images: Scale (1.05)
- Links: Color Change + Underline
```

### Scroll-Animationen
- Fade-in beim Scrollen (Intersection Observer)
- Slide-in von unten für Sections
- Stagger-Animation für Grid-Items

### Loading States
- Skeleton Screens für Bilder
- Smooth Fade-in nach Laden

---

## 📱 Responsive Breakpoints

```css
/* Mobile First Approach */
--mobile: 320px - 767px;
--tablet: 768px - 1023px;
--desktop: 1024px - 1439px;
--wide: 1440px+;
```

### Anpassungen
- **Mobile**: 1-Column, Hamburger-Menü, gestackte Inhalte
- **Tablet**: 2-Column, reduzierte Abstände
- **Desktop**: 3-Column, volle Features
- **Wide**: Maximale Container-Breite, mehr Whitespace

---

## 🖼️ Bildstil & Behandlung

### Foto-Stil
- Hochauflösende Fotos
- Natürliche, freundliche Ausstrahlung
- Fröhliche Kinder mit professionellem Schminken
- Gut beleuchtete Event-Fotos

### Bildbehandlung
```css
/* Subtle Overlay für Text-Lesbarkeit */
.hero-image::after {
  background: linear-gradient(
    180deg,
    rgba(0,0,0,0) 0%,
    rgba(0,0,0,0.3) 100%
  );
}

/* Border-Radius für moderne Optik */
img {
  border-radius: 15px;
}

/* Lazy Loading */
loading="lazy"
```

---

## 🎨 Besondere Design-Elemente

### Geometrische Formen als Dekoration
- Soft Blobs im Hintergrund (SVG)
- Bunte Kreise als visuelle Akzente
- Wellenförmige Divider zwischen Sections

### Illustrationen
- Optional: Süße Icon-Illustrationen für Services
- Hand-drawn Stil (nicht zu kindisch)
- In Primärfarben

### Schatten
```css
--shadow-sm: 0 2px 8px rgba(0,0,0,0.08);
--shadow-md: 0 8px 24px rgba(0,0,0,0.12);
--shadow-lg: 0 16px 48px rgba(0,0,0,0.16);
```

---

## 🛠️ Technologie-Stack

### Frontend
**Empfehlung: Next.js + Tailwind CSS**

**Begründung**:
- ✅ SEO-optimiert (SSR/SSG)
- ✅ Schnelle Ladezeiten
- ✅ Moderne React-Komponenten
- ✅ Tailwind für schnelles Styling
- ✅ Deployment auf Vercel (kostenlos)

**Alternative: Plain HTML + CSS**
- Für Einfachheit
- Wenn kein Framework gewünscht

### Performance
- Next.js Image Optimization
- Lazy Loading
- Code Splitting
- Minimierte CSS/JS

### SEO
- Semantic HTML5
- Meta-Tags optimiert
- Strukturierte Daten (Schema.org)
- Sitemap.xml
- robots.txt

---

## 📄 Seiten-Struktur

### 1. **Home** (`/`)
- Hero-Section
- Service-Übersicht (Top 6)
- Galerie-Teaser (6 Bilder)
- Über-mich-Teaser
- Service-Gebiete
- Testimonials
- CTA "Jetzt anfragen"

### 2. **Services** (`/services`)
- Übersicht aller Services
- Detailseiten für jeden Service
- Preisinfos (auf Anfrage)
- Buchungsprozess

### 3. **Galerie** (`/galerie`)
- Alle Fotos
- Filter nach Kategorien
- Lightbox-Ansicht

### 4. **Über mich** (`/ueber-mich`)
- Vorstellung Sabine
- Team (falls vorhanden)
- Qualifikationen
- Erfahrung
- Referenzen

### 5. **Kontakt** (`/kontakt`)
- Kontaktformular
- Telefon, E-Mail
- Servicegebiet-Karte
- Social Media Links
- Anfahrtsbeschreibung

### 6. **Buchung** (optional) (`/buchung`)
- Terminanfrage-Formular
- Verfügbarkeitskalender
- Service-Auswahl
- Preiskalkulator

### 7. **Rechtliches**
- Impressum (`/impressum`)
- Datenschutz (`/datenschutz`)

---

## ✨ Besondere Features

### Hero-Animation
- Text fade-in + slide-up
- CTA-Buttons mit Delay
- Hintergrundbild mit Parallax (subtil)

### Service-Icons mit Animation
- Icon bounce on scroll-in
- Hover: Rotation oder Scale

### Galerie-Filter
- Smooth transition zwischen Kategorien
- Animierte Grid-Umordnung

### Contact Form
- Inline-Validierung
- Success-Animation
- Loading-State während Submit

### Mobile Menu
- Slide-in Animation
- Backdrop-Blur
- Smooth Close

---

## 🎯 Performance-Ziele

- **Lighthouse Score**: > 95
- **Ladezeit (LCP)**: < 2.5s
- **Time to Interactive**: < 3.5s
- **Mobile Score**: > 90

---

## 🚀 Launch-Checklist

### Design
- [x] Farbschema definiert
- [x] Typografie festgelegt
- [x] Komponenten entworfen
- [ ] Wireframes erstellt
- [ ] High-Fidelity Mockups

### Content
- [x] Bilder heruntergeladen
- [ ] Texte finalisiert
- [ ] SEO-Keywords definiert
- [ ] Meta-Descriptions geschrieben

### Entwicklung
- [ ] Projekt-Setup (Next.js)
- [ ] Komponenten entwickelt
- [ ] Responsive getestet
- [ ] Cross-Browser getestet

### SEO & Legal
- [ ] Meta-Tags implementiert
- [ ] Strukturierte Daten
- [ ] Impressum & Datenschutz
- [ ] Cookie-Banner (falls nötig)

### Deployment
- [ ] Domain eingerichtet
- [ ] Hosting (Vercel)
- [ ] SSL-Zertifikat
- [ ] Analytics (DSGVO-konform)

---

**Design-Konzept Version**: 1.0
**Erstellt**: 2026-02-13
**Status**: ✅ Bereit für Review & Implementierung
