# DjangoIssueTracker
Navrhnout a implementovat v Djangu jednoduchý issue tracker:‎

- issue má zadavatele, řešitele, textový popis, stav, kategorii (např. bug, vylepšení, dokumentace)

- issues lze ve webovém rozhraní přidávat, editovat a budou mít stránku se seznamem (lze použít Django Admin nebo jakoukoliv jinou knihovnu)

- seznam issues zobrazuje v hlavičce jednoduché statistiky (průměrný, nejdelší a nejkratší čas řešení issue)

- kategorie stačí mít pouze v DB, bez administrace, ale v budoucnu by její přidání mělo být co nejjednodušší

- 2 uživatelské role: superuser a staff, staff nesmí nic měnit ani přidávat, superuser může vše

- REST/JSON API pro seznam a detail issues (lze použít knihovnu nebo čisté Django)

- testy podle uvážení

- smysluplné verzování Gitem

- jako DB stačí sqlite‎

- musí být jasné, jak projekt nainstalovat a spustit