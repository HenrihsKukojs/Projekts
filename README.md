# Projekts
# IMDb Filmu Datu Vācējs

Šis ir vienkāršs Python kods, kas palīdz savākt (ielādēt) informāciju par labākajām 250 filmām no IMDb mājaslapas. Programma mēģina iegūt filmas nosaukumu, tās iznākšanas gadu un to, kāds reitings filmai ir dots. Iegūtos datus saglabājam īpašā failā, ko sauc par JSON failu.

**Svarīgi zināt:** IMDb mājaslapa ir diezgan "gudra" – liela daļa informācijas tajā parādās tikai pēc tam, kad pārlūkprogramma izpilda slēptu programmas kodu (JavaScript). Mūsu kods strādā ar to lapas daļu, kas parādās uzreiz. Tāpēc var gadīties, ka kods nevarēs savākt pilnīgi visus 250 filmu datus vai tos vispār neatradīs, jo tie parādās vēlāk. Ja gribam savākt visus datus no tādām lapām, mums būtu jāizmanto sarežģītāki rīki, kas spēj "uzgaidīt", līdz visa lapa ir ielādējusies. Bet šis projekts parāda pašus pamatus!

## Ko dara šis projekts (Projekta Uzdevums)

Šī koda galvenais mērķis ir parādīt, kā mēs varam likt datoram "lasīt" un savākt datus no interneta lapām. Precīzāk, šis kods:

1.  **Apmeklē lapu:** Automātiski dodas uz IMDb Top 250 filmu saraksta lapu internetā.
2.  **Meklē datus:** Pārbauda lapas iekšējo uzbūvi (HTML kodu) un meklē tur filmu nosaukumus, gadus un reitingus.
3.  **Sakārto datus:** Atrasto informāciju (par katru filmu) sakārto tā, lai datoram būtu viegli to saprast un izmantot.
4.  **Saglabā datus:** Iegūtos datus ieliek īpašā failā (JSON failā), lai mēs tos vēlāk varētu apskatīt vai izmantot citām programmām.
5.  **Parāda rezultātu:** Kad kods pabeidz darbu, tas parāda savākto informāciju gan datora logā (terminālī), gan saglabā failā.

## Kādas programmu daļas (bibliotēkas) un kāpēc tās tiek izmantotas

Mūsu kods izmanto dažas gatavas Python programmu daļas (mēs tās saucam par bibliotēkām), kas palīdz izdarīt konkrētus darbus:

1.  **`requests` (pieprasījumi)**:
    * **Ko dara:** Šī daļa palīdz mums "pieprasīt" interneta lapas. Tas ir kā jūsu pārlūkprogramma, kas lūdz lapu no interneta servera.
    * **Kāpēc:** Bez tās mēs nevarētu saņemt IMDb lapas saturu, lai to vēlāk lasītu. Tāpat tā ļauj mums "pateikt" lapai, ka mēs esam "normāla" pārlūkprogramma, lai mūs nebloķētu.

2.  **`BeautifulSoup4` (skaistā zupa)**:
    * **Ko dara:** Kad esam saņēmuši lapas saturu (kas ir daudz teksta), `BeautifulSoup` palīdz to "sakārtot" un saprast. Iedomājieties, ka tā visu lapas tekstu pārvērš par viegli lasāmu un meklējamu sarakstu.
    * **Kāpēc:** Ar tās palīdzību mēs varam viegli atrast konkrētas vietas lapā, piemēram, kur atrodas filmu nosaukumi vai reitingi.

3.  **`json` (datiem)**:
    * **Ko dara:** Šī daļa palīdz mums strādāt ar JSON formātu. Tas ir veids, kā sakārtoti saglabāt datus, lai tos varētu saprast gan cilvēki, gan datori.
    * **Kāpēc:** Kad esam savākuši visas filmu detaļas, mēs tās ar šo bibliotēku ieliekam JSON failā, lai tās būtu glīti sakārtotas un varētu tās vēlāk viegli izmantot.

4.  **`os` (operētājsistēmai)**:
    * **Ko dara:** Šī daļa ļauj mūsu programmai "runāt" ar datora operētājsistēmu (piemēram, Windows, macOS, Linux).
    * **Kāpēc:** Mēs to izmantojam, lai izveidotu īpašu mapi (`dati`), kurā tiks saglabāts mūsu JSON fails. Tā arī palīdz pareizi atrast ceļu līdz šim failam neatkarīgi no tā, kādu operētājsistēmu jūs izmantojat.

## Kā dati tiek sakārtoti (Pašu definētās datu struktūras)

Kad mēs savācam datus, mēs tos sakārtojam tā, lai datoram būtu viegli tos saprast un apstrādāt. Mēs izmantojam divus galvenos veidus, kā datus uzglabāt:

1.  **Saraksts (`list`)**:
    * Iedomājieties to kā lielu iepirkumu sarakstu. Katrs ieraksts šajā sarakstā ir viena filma.
    * Mūsu kodā tas ir mainīgais `filmas`. Mēs sākam ar tukšu sarakstu un pakāpeniski pievienojam jaunas filmas.

2.  **Vārdnīca (`dictionary`)**:
    * Iedomājieties to kā vizītkarti par katru filmu. Katrai vizītkartei ir sava "vietas" (piemēram, "Nosaukums", "Gads", "Reitings") un tām atbilstošās vērtības (piemēram, "Šūšankas glābšana", "1994", "9.3").
    * Mūsu kodā katra atsevišķa filma tiek saglabāta kā vārdnīca, kurā mēs paši esam izdomājuši atslēgas (piemēram, "Nosaukums", "Gads", "Reitings"), lai skaidri pateiktu, kas ir kas.

Tātad, mēs galu galā iegūstam "sarakstu ar vārdnīcām" – katra vārdnīca ir viena filma ar tās detaļām, un visas šīs filmas ir saliktas lielā sarakstā.

## Kā lietot programmu (Programmatūras izmantošanas metodes)

Lai palaistu un izmantotu šo programmu, veiciet šīs vienkāršās darbības:

### 1. Sagatavošanās

Pirms sākat, pārliecinieties, ka jūsu datorā ir Python (versija 3 vai jaunāka). Pēc tam jums būs jāinstalē dažas papildu programmu daļas. Atveriet datora komandrindu (sauktu arī par Terminal vai Command Prompt) un ierakstiet:

```bash
pip install requests beautifulsoup4
