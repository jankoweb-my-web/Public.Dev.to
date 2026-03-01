# Vkládání ukázek kódu do článků

Cíl: v článku mít odkaz na soubor se zdrojovým kódem, ne kód přímo. Při změně kódu stačí změnit soubor – článek se aktualizuje automaticky při publikaci.

## Aktuální řešení: lokální soubory + `:(cesta)`

Kód uložte jako samostatný soubor vedle článku a odkažte ho v Markdownu:

```
:(example.js)
```

Při publikaci na DEV.to workflow automaticky nahradí syntaxi obsahem souboru jako kódový blok.

Ve VS Code vidíte náhled díky pluginu **Markdown Preview Include Files (Markus Stamminger)** – nainstalujte z Marketplace.

**Výhody:**
- Kód je soubor v repozitáři – lze commitovat, verzovat, editovat samostatně.
- VS Code zobrazuje náhled se skutečným kódem.
- Jedno místo pro změny – soubor kódu, ne článek.

**Zpracování** zajišťuje `scripts/include_processor.py`. Spusťte lokálně:
```bash
python scripts/include_processor.py posts/muj-clanek/clanek.md
# nebo přes env var:
export FILES="posts/muj-clanek/clanek.md"
python scripts/include_processor.py
```

---

## Alternativa: GitHub Gist

GitHub Gist umožňuje hostovat úryvky kódu veřejně s vlastní URL.

**Postup:**
1. Vytvořte Gist na [gist.github.com](https://gist.github.com)
2. Zkopírujte Raw URL (tlačítko „Raw" na stránce Gistu)
3. V článku buď vložte odkaz, nebo použijte embed

**Embed v DEV.to** (liquid tag):
```
{% gist <gist_id> %}
```

**Nevýhody oproti lokálnímu řešení:**
- Kód žije mimo repozitář – změny Gistu se neprojeví automaticky v zobrazení článku (embed aktualizuje, ale raw odkaz v kódovém bloku ne).
- VS Code nenabídne náhled obsahu Gistu přímo v Markdownu.
- Nutná ruční správa Gistů mimo VS Code workflow.

---

## Alternativa: Raw odkaz na GitHub soubor

Kód uložte v repozitáři a odkažte přímý raw odkaz v článku jako embed nebo odkaz:

```
https://raw.githubusercontent.com/<user>/<repo>/<branch>/posts/my-article/example.js
```

DEV.to neumí automaticky includovat raw URL jako kódový blok, takže tato varianta vyžaduje ruční zkopírování obsahu nebo jiný mechanismus.

---

## Doporučení

Používejte **lokální soubory + `:(cesta)` syntaxi** (aktuální řešení). Je nejjednodušší, funguje v VS Code náhledu i v GitHub Actions workflow.
