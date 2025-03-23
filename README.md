# Správa produktů (Python konzolová aplikace)

Tento Python skript umožňuje správu produktů ve skladu prostřednictvím jednoduchého textového rozhraní. Umožňuje přidávání, úpravu, vyhledávání a analýzu produktů na základě jejich ceny.

## Funkce aplikace

### 1. Výpis položek
Vypíše všechny produkty uložené v seznamu.

### 2. Přidání položky
Umožňuje uživateli přidat nový produkt do seznamu zadáním jeho jména a ceny.

### 3. Vyhledání položky
Umožňuje uživateli vyhledat produkt podle jeho názvu.

### 4. Celková cena produktů
Spočítá celkovou cenu všech produktů ve skladu.

### 5. Nejdražší položka na skladě
Vyhledá a zobrazí nejdražší produkt (nebo produkty, pokud mají stejnou cenu).

### 6. Nejlevnější položka na skladě
Vyhledá a zobrazí nejlevnější produkt (nebo produkty, pokud mají stejnou cenu).

### 7. Průměrná cena produktů
Spočítá a zobrazí průměrnou cenu všech produktů.

### 8. Editovat položku
Umožňuje uživateli upravit název nebo cenu vybraného produktu.

## Ovládání

Po spuštění programu se zobrazí hlavní menu s očíslovanými možnostmi. Stačí zadat číslo odpovídající požadované akci a potvrdit klávesou **Enter**.

## Možné problémy a jejich řešení

- **Zadání nečíselné hodnoty pro cenu** – Uživatel musí zadávat pouze číselné hodnoty pro cenu, jinak program vyvolá chybu.
- **Neplatný index při úpravě produktu** – Pokud uživatel zadá číslo mimo rozsah seznamu produktů, program může selhat. Ošetření vstupu by bylo vhodné vylepšit.

## Možná vylepšení

- Přidání možnosti mazání produktů.
- Ošetření chybného vstupu při zadávání čísel.

---
Autor: **Ondřej Brázdil**
