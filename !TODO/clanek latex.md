
# Instalace LaTeXu a nastavení VS Code (Windows)

[Instalace na Windows](https://tug.org/texlive/windows.html#install) - pozor, trvá asi 2h (samotná instalace má 5000 malých balíčků)


Po úpravě PATH restartujte VS Code (důležité, aby načetl nové proměnné prostředí).

---

**4) Nainstalujte rozšíření do VS Code**

1. Otevřete VS Code a nainstalujte rozšíření `LaTeX Workshop` (Tuinwoon/James-Yu community fork — vyhledejte "LaTeX Workshop").
2. Restartujte VS Code po instalaci a po změně PATH.

**5) Doporučené nastavení VS Code (User settings)**

LaTeX Workshop většinou autodetekuje `latexmk`. Pokud je potřeba explicitně nastavit, přidejte do uživatelského `settings.json` následující (Otevřete `Preferences: Open Settings (JSON)`):

```json
{
	"latex-workshop.latex.recipes": [
		{ "name": "latexmk (pdf)", "tools": ["latexmk"] }
	],
	"latex-workshop.latex.tools": [
		{
			"name": "latexmk",
			"command": "latexmk",
			"args": ["-pdf","-interaction=nonstopmode","-synctex=1","-outdir=%OUTDIR%","%DOC%"]
		}
	],
	"latex-workshop.latex.autoBuild.run": "onSave"
}
```

Po této konfiguraci by výchozí build recipe `latexmk (pdf)` měl fungovat.

**6) Test a ověření**

1. V příkazové řádce ověřte:

```powershell
perl -v
latexmk -version
pdflatex --version
```

2. Otevřete `.tex` soubor ve VS Code a spusťte build (`LaTeX Workshop: Build with recipe` nebo uložení souboru pokud máte `autoBuild.run = onSave`).

Pokud se objeví chyba podobná té původní (Perl nenalezen), znamená to, že buď `perl` není v PATH, nebo VS Code nebylo restartováno po změně PATH.

**Rychlá řešení problémů**
- Pokud `latexmk` není nainstalován: zkontrolujte instalaci LaTeX Live nebo doinstalujte balíček přes MiKTeX Console (pokud používáte MiKTeX).
- Pokud VS Code stále hlásí chybu: zavřete a znovu otevřete celý VS Code (ne jen okno).
- Spusťte `where.exe latexmk` a `where.exe perl` v PowerShellu, abyste zjistili, odkud se spouští příkazy.

**Zdroje & odkazy**


Pokud chcete, upravím nastavení `settings.json` přímo za vás nebo přidám konkrétní příklad PATH pro vaši instalaci (řekněte mi, kam jste nainstaloval/a TeX Live a Perl). 
## VS Code highlight settings

Přidejte následující do nastavení VS Code (např. `.vscode/settings.json` nebo uživatelského `settings.json`) pro zvýraznění referencí a citací v LaTeXu:

```json
"highlight.regexes": {
	"(\\ref\\{)(fig:[^\\}]+)(\\})": [
		{},
		{ "color": "#00E5FF", "fontWeight": "bold" },
		{}
	],
	"(\\ref\\{)(tab:[^\\}]+)(\\})": [
		{},
		{ "color": "#FF8C00", "fontWeight": "bold" },
		{}
	],
	"(\\ref\\{)(eq:[^\\}]+)(\\})": [
		{},
		{ "color": "#3be020", "fontWeight": "bold" },
		{}
	],
	"(\\cite\\{)([^\\}]+)(\\})": [
		{},
		{ "color": "#FFCC00", "fontWeight": "bold" },
		{}
	]
},
"highlight.decorations": {
	"rangeBehavior": 1
}
```

