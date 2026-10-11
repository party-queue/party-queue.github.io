#!/usr/bin/env python3
"""Builds en/index.html and pl/index.html (and the root redirect) from the text below. Run: python3 tools/build.py"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "https://github.com/party-queue/party-queue"
APK = REPO + "/releases/latest/download/party-queue.apk"
SHA = REPO + "/releases/latest/download/party-queue.apk.sha256"
SITE = "https://party-queue.github.io"
BUILD = __import__("time").strftime("%Y%m%d%H%M")

# Inline SVG flags: emoji flags show up as the letters "GB" / "PL" on Windows.
FLAG = {
    "en": '<svg class="flag" width="30" height="20" viewBox="0 0 60 30" aria-hidden="true" focusable="false"><clipPath id="fs"><path d="M0,0 v30 h60 v-30 z"/></clipPath><clipPath id="ft"><path d="M30,15 h30 v15 z v15 h-30 z h-30 v-15 z v-15 h30 z"/></clipPath><g clip-path="url(#fs)"><path d="M0,0 v30 h60 v-30 z" fill="#012169"/><path d="M0,0 L60,30 M60,0 L0,30" stroke="#fff" stroke-width="6"/><path d="M0,0 L60,30 M60,0 L0,30" clip-path="url(#ft)" stroke="#C8102E" stroke-width="4"/><path d="M30,0 v30 M0,15 h60" stroke="#fff" stroke-width="10"/><path d="M30,0 v30 M0,15 h60" stroke="#C8102E" stroke-width="6"/></g></svg>',
    "pl": '<svg class="flag" width="30" height="20" viewBox="0 0 8 5" aria-hidden="true" focusable="false"><rect width="8" height="5" fill="#fff"/><rect y="2.5" width="8" height="2.5" fill="#dc143c"/></svg>',
}

# -------------------------------------------------------------------------------------------------------------- text
T = {}

T["en"] = dict(
    lang="en", other="pl", other_name="Polski", locale="en_GB",
    title="Party Queue – a party jukebox for Android: YouTube without ads, guests add the songs",
    desc="Party Queue turns an Android phone into a party jukebox: ad-free YouTube, a queue everyone can add songs to from their own phone or laptop through a web page, no accounts. Free and open source.",
    nav=[("features", "Features"), ("screens", "Screenshots"), ("install", "Install"), ("update", "Update"), ("faq", "FAQ")],
    theme=("Auto", "Light", "Dark"),
    h1="One phone.<br><span>One queue.</span><br>Everyone's songs.",
    lead="Party Queue turns an Android phone into a party jukebox. It plays YouTube <b>without ads</b>, your guests add songs from <b>their own phones or laptops</b> through a web page, and you decide what plays next. No accounts, no API keys, nothing to install for guests.",
    dl_btn="Download for Android", all_rel="All releases", src="Source code",
    latest="Latest version: {v} · {date} · {mb} MB",
    latest_fallback="Latest version: see the releases page · about 225 MB",
    req="Android 10 or newer · 64-bit (arm64) phone or tablet · about 225 MB",
    dl_h="Get the app", dl_sub="Scan the code with the phone you want to use as the jukebox, or open the link on it.",
    qr_main="Scan to download the APK", 
    dl_steps_h="Direct links",
    dl_links=[("Latest APK (always the newest version)", APK), ("Checksum (SHA-256)", SHA), ("Release notes and older versions", REPO + "/releases"), ("New releases as a feed (RSS/Atom)", REPO + "/releases.atom")],
    how_h="How it works",
    how_sub="Three minutes from install to the first song.",
    how=[("Install and open it on the host phone", "The phone that plays the music. Keep it plugged in near the speakers. Join Wi-Fi (or switch on the phone's hotspot)."),
         ("Pick the music", "Open a YouTube playlist (<i>YouTube</i> tab) or search for songs. The queue is yours; nothing is written back to YouTube."),
         ("Show the QR code", "In the <i>Zaproś</i> (Invite) tab. Guests scan it, type a name and propose songs; you approve them as <i>next</i> or <i>at the end</i>. Make a friend a co-host and they can run the party from a laptop.")],
    feat_h="Everything it does",
    feat_sub="The complete list: what the host's app and the guests' web page can do.",
    groups=[
        ("▶ Plays YouTube – without ads", [
            "<b>Ad-free playback</b> in an embedded Firefox engine (GeckoView) with uBlock Origin built in. No Google account, no API key.",
            "<b>Keeps playing with the screen off</b> (foreground service and notification). CPU and Wi-Fi locks are held only while they are needed.",
            "<b>Instant song changes:</b> the next song is already loaded in a hidden second player. YouTube makes people who block ads wait 5–13 s for a video to start; this hides that wait.",
            "<b>Smooth hand-over:</b> when you skip, go back or play a song now, the old song fades out (2 s) while the new one fades in. A song that ends on its own switches instantly.",
            "<b>Good sound:</b> the best audio stream YouTube offers (Opus, about 160 kb/s). The picture is tiny (144p) and hidden by default to save power; one button cycles hidden → small → full screen.",
            "<b>A pause stays a pause.</b> After 10 minutes the players are released to save the battery; <i>play</i> continues at the same position.",
            "<b>Volume slider</b> for the phone's media volume (it follows the volume keys); tap the speaker to mute.",
            "<b>Tells you what is wrong:</b> if a song has not started after 20 s the app says why – no internet, a network without access, Data Saver, Android's sleep mode, battery saver, or just a slow start. Songs that cannot be played are skipped after 45 s.",
            "Cookie banners are rejected automatically; the queue survives restarts (it comes back paused).",
        ]),
        ("☰ A queue you control", [
            "<b>Playlists:</b> open any public or unlisted YouTube playlist and press <i>Ustaw jako aktualną playlistę</i> (Set as current playlist). Songs keep YouTube's order (shuffle is a switch); the first ~100 songs are loaded. YouTube Mixes can be imported from a video page. Private playlists work after signing in (experimental – setting the list to <i>Unlisted</i> is the easy way).",
            "<b>Search in the app:</b> <i>Szukaj piosenki do dodania</i> opens a full-screen search (title, artist or a pasted link). Every result has two icon buttons – an arrow to the top of a list (<b>play next</b>) and an arrow to the bottom (<b>end of the queue</b>). The search stays open so you can add several songs in a row.",
            "<b>YouTube tab:</b> the real mobile YouTube with an <b>address bar</b> (type a search or paste a video or playlist link). The page fills the screen – the app's bars scroll away with it. The round <b>+</b> button is grey while the page has nothing to add; on a playlist or video it slides up a panel (playlist: shuffle and <i>set as current</i>; video: <i>next</i> / <i>end of the queue</i>) that goes away again.",
            "<b>Gestures on the queue:</b> tap a song to move it to the top, swipe right to play it now, swipe left to remove it, hold and drag to reorder (the list scrolls at the edges). A gentle hint wiggles the first row now and then. <i>Wyczyść</i> clears the queue (after asking); <i>Powtarzaj</i> (repeat) refills it from the playlist.",
            "<b>Proposals</b> from guests wait in the <i>Propozycje</i> tab. Approve each as <b>next</b> or <b>at the end</b>, or reject it.",
            "Thumbnails everywhere; long titles scroll slowly so you can read them (they stand still if you turned animations off in Android).",
        ]),
        ("👥 Guests join with a link, not an app", [
            "The phone serves a <b>web page on the local network</b> (<code>http://192.168.x.x:8080/</code>). The <i>Zaproś</i> tab shows its <b>QR code</b>, the address, <i>Udostępnij link</i> (share) and <i>Kopiuj</i> (copy), and lets you choose the network if the phone has several.",
            "A guest types a <b>name</b> and is in – no code, no account, nothing to install. Works on phones, tablets and computers.",
            "Guests see the <b>live queue</b> and what is playing, <b>search YouTube</b>, <b>propose songs</b> (up to 5 waiting, no duplicates), follow their proposals and can <b>ask for host rights</b>.",
            "You can close the door (<i>Przyjmuj nowych gości</i>), see who is online, remove anyone, and <b>make any guest a co-host</b> with one tap – no request needed. Their page reloads into host mode; take it back whenever you like.",
            "If your router isolates Wi-Fi clients, use the phone's hotspot.",
        ]),
        ("⌨ Run it from a laptop or another phone", [
            "A <b>co-host has the same powers as the host</b>: play/pause, seek (click the progress bar), previous/next, repeat, volume; move, play now, remove and clear queue items; approve proposals and other co-hosts; load a playlist from a link; search and add songs as next or at the end.",
            "The page is <b>responsive</b>: a phone layout and a two-column desktop layout, light/dark/auto theme, a banner when the connection drops and automatic reconnecting.",
            "<b>Keyboard:</b> <kbd>Space</kbd> play/pause · <kbd>N</kbd> / <kbd>P</kbd> next / previous · <kbd>R</kbd> repeat · <kbd>+</kbd> <kbd>−</kbd> volume · <kbd>M</kbd> mute · <kbd>↑</kbd> <kbd>↓</kbd> or <kbd>J</kbd> <kbd>K</kbd> select a song · <kbd>Enter</kbd> play it · <kbd>T</kbd> move to top · <kbd>Alt</kbd>+<kbd>↑</kbd>/<kbd>↓</kbd> move · <kbd>Delete</kbd> remove · <kbd>/</kbd> search · <kbd>1</kbd>–<kbd>5</kbd> tabs · <kbd>D</kbd> theme · <kbd>?</kbd> help.",
            "<b>Mouse:</b> drag and drop to reorder, double-click to play, icon buttons with tooltips that show their shortcut.",
        ]),
        ("🎨 Looks like a party, sips power", [
            "Light, dark or automatic theme; gradients, an animated equalizer and a slowly flowing now-playing card; portrait and landscape layouts; an adaptive launcher icon (with a themed variant).",
            "The title bar hides after a few seconds; pull down or tap its handle to bring it back. In the YouTube tab the bars scroll away so the page gets the whole screen.",
            "<b>Battery:</b> the screen is not kept on unless you switch <i>Nie wygaszaj ekranu</i> on; locks are held only while needed; the network updates to guests are calm; animations run only while music plays.",
        ]),
        ("🔒 Private by design", [
            "<b>No account, no tracking, no analytics, no ads.</b> The queue lives on the phone. The only traffic is YouTube's own and the local web page.",
            "The page is plain HTTP on your local network (no TLS): use a network you trust. Guests get random tokens; the host approves every proposal.",
            "<b>Open source</b> (AGPL-3.0). Components used: GeckoView, uBlock Origin, Ktor, Jetpack Compose and others, listed in the repository.",
        ]),
    ],
    shots_h="Screenshots", shots_sub="The host's app on the phone and the web page that guests and co-hosts see.",
    shots_app="The app on the host's phone", shots_web="The web page for guests and co-hosts",
    cap=dict(
        queue=("The queue", "Now playing with volume, the queue, and the search button."),
        search=("Search", "Two arrow buttons: play next or add to the end."),
        proposals=("Proposals", "Approve a guest's song as next or at the end."),
        invite=("Invite", "The QR code opens the guest page; promote guests to co-hosts."),
        youtube=("YouTube tab", "The real YouTube, an address bar, and the grey + button with its hint."),
        panel=("The + panel", "Slides up on a playlist or video page – and goes away again."),
        landscape=("Landscape", "The player on the left, the tabs on the right."),
        light=("Light theme", "Light, dark or automatic."),
        web_queue_dark=("Host page on a computer – dark", "Two columns, the keyboard and mouse work as you expect."),
        web_queue_light=("Host page – light", "Same page in the light theme."),
        web_search=("Search on the host page", "Next / end of the queue as icon buttons."),
        web_proposals=("Proposals on the host page", "Approve as next or at the end, or reject."),
        web_guests=("Guests", "Who is online; promote, demote or remove."),
        web_guest_queue=("A guest's view", "The live queue and what is playing."),
        web_guest_search=("A guest proposes a song", "The host decides."),
        web_mobile=("On phones", "The same page, in a phone layout."),
    ),
    inst_h="Install",
    inst_sub="Party Queue is not on Google Play, so you install the APK file yourself. It takes a minute.",
    inst_steps=[
        ("Download the APK on the phone", f"Scan the QR code above with the phone's camera, or open <a href=\"{APK}\">this link</a> on it. Your browser may warn that this type of file can harm your device – choose <i>Download anyway</i> / <i>Keep</i>. The file is about 225 MB."),
        ("Allow the installation", "Open the downloaded <code>party-queue.apk</code>. If Android asks, allow your browser (or file manager) to <i>Install unknown apps</i>: <i>Settings → Apps → Special access → Install unknown apps</i>. Google Play Protect may say the app was not scanned or comes from an unknown developer – choose <i>More details → Install anyway</i>."),
        ("Open it and say yes twice", "Allow notifications (Android 13+; they keep the music alive with the screen off), and press <i>Pozwól</i> (Allow) on the banner that asks to let the app run in the background."),
        ("Connect and start the party", "Join the phone to Wi-Fi (or switch on its hotspot). Open the <i>YouTube</i> tab, pick a playlist, then show the QR code from the <i>Zaproś</i> tab. Guests must be on the same network."),
    ],
    verify_h="Check the download (optional)",
    verify_p="Every release carries a checksum file. Put both files in one folder and run:",
    verify_cmds="# macOS / Linux\nshasum -a 256 -c party-queue.apk.sha256\n\n# Windows (PowerShell)\n(Get-FileHash party-queue.apk -Algorithm SHA256).Hash.ToLower()   # compare with the .sha256 file\n\n# or install from a computer\nadb install -r party-queue.apk",
    upd_h="Update",
    upd_sub="There is no store, so updates are manual – and just as simple.",
    upd_steps=[
        ("Check which version you have", "<i>Settings → Apps → Party Queue</i> shows the version at the bottom. The newest version is at the top of this page and on the <a href=\"" + REPO + "/releases\">releases page</a>."),
        ("Download the new APK and open it", "Use the same QR code or link. Android installs it <b>over the old version</b>; your queue, guests and settings stay."),
        ("Get told about new versions", "On GitHub press <i>Watch → Custom → Releases</i> on the <a href=\"" + REPO + "\">repository</a>, or subscribe to the <a href=\"" + REPO + "/releases.atom\">releases feed</a> in any feed reader."),
    ],
    upd_note="<b>If Android says the app was not installed because it conflicts with an existing package</b>, the old copy was signed with a different key (this can happen once, when switching between a build made by someone else and a release from this site). Uninstall Party Queue once and install again – the queue and guest list are lost, nothing else is: the app keeps no data anywhere but on the phone. Releases from this site are signed with one project key, so later updates install over each other.",
    faq_h="Questions",
    faq=[
        ("Guests cannot open the page.", "Check that they are on the same Wi-Fi as the host phone, and use the address shown in the <i>Zaproś</i> tab – the phone's address can change after it reconnects. Some routers and guest networks isolate devices from each other; switch on the host phone's hotspot and join it instead."),
        ("The music stops when the screen turns off.", "Allow notifications and press <i>Pozwól</i> on the banner (battery optimisation off for the app). On some phones also set the app to <i>Unrestricted</i> battery use in the system settings."),
        ("A song does not start.", "Wait 20 seconds: the app then shows why under the player (no internet, Data Saver, sleep mode…). YouTube itself sometimes delays the start of a video; songs that cannot be played are skipped after 45 seconds."),
        ("Can I use my private playlists?", "Public and unlisted playlists work without signing in. For a private one, sign in on the <i>YouTube</i> tab (experimental) – or set the playlist to <i>Unlisted</i> on YouTube, which is the easiest way."),
        ("Do I need a Google account or an API key?", "No. The app reads the same public pages a browser does."),
        ("Are there ads?", "No, uBlock Origin is built in. If one ever slips through, please report it on GitHub."),
        ("Can I use an iPhone as the host?", "No – the host must be an Android phone (Android 10+, 64-bit). Guests can use any phone, tablet or computer with a browser."),
        ("Is it legal?", "It is not affiliated with YouTube, Google or Mozilla. Using it may conflict with YouTube's Terms of Service; use it at your own risk and for private events."),
    ],
    foot_l="Party Queue is free software (AGPL-3.0). Not affiliated with YouTube, Google or Mozilla.",
    foot_r=[("Source", REPO), ("Report a problem", REPO + "/issues"), ("Changelog", REPO + "/blob/main/CHANGELOG.md"), ("Organisation", "https://github.com/party-queue")],
    top="Back to top",
)

T["pl"] = dict(
    lang="pl", other="en", other_name="English", locale="pl_PL",
    title="Party Queue – imprezowy jukebox na Androida: YouTube bez reklam, goście dodają piosenki",
    desc="Party Queue zamienia telefon z Androidem w imprezowy jukebox: YouTube bez reklam i kolejka, do której każdy dodaje piosenki z własnego telefonu lub laptopa przez stronę WWW. Bez kont. Darmowa i otwarta.",
    nav=[("features", "Funkcje"), ("screens", "Zrzuty ekranu"), ("install", "Instalacja"), ("update", "Aktualizacja"), ("faq", "Pytania")],
    theme=("Auto", "Jasny", "Ciemny"),
    h1="Jeden telefon.<br><span>Jedna kolejka.</span><br>Piosenki wszystkich.",
    lead="Party Queue zamienia telefon z Androidem w imprezowy jukebox. Gra YouTube <b>bez reklam</b>, goście dodają piosenki <b>z własnych telefonów i laptopów</b> przez stronę WWW, a Ty decydujesz, co zagra dalej. Bez kont, bez kluczy API i bez instalowania czegokolwiek przez gości.",
    dl_btn="Pobierz na Androida", all_rel="Wszystkie wydania", src="Kod źródłowy",
    latest="Najnowsza wersja: {v} · {date} · {mb} MB",
    latest_fallback="Najnowsza wersja: zobacz stronę wydań · ok. 225 MB",
    req="Android 10 lub nowszy · telefon lub tablet 64-bitowy (arm64) · ok. 225 MB",
    dl_h="Pobierz aplikację", dl_sub="Zeskanuj kod telefonem, który ma być jukeboxem, albo otwórz na nim link.",
    qr_main="Zeskanuj, aby pobrać APK", 
    dl_steps_h="Bezpośrednie linki",
    dl_links=[("Najnowszy APK (zawsze najnowsza wersja)", APK), ("Suma kontrolna (SHA-256)", SHA), ("Opis zmian i starsze wersje", REPO + "/releases"), ("Nowe wydania jako kanał (RSS/Atom)", REPO + "/releases.atom")],
    how_h="Jak to działa",
    how_sub="Trzy minuty od instalacji do pierwszej piosenki.",
    how=[("Zainstaluj i uruchom na telefonie gospodarza", "Na tym, który gra muzykę. Niech leży przy głośnikach, najlepiej na ładowarce. Połącz go z Wi-Fi (albo włącz na nim hotspot)."),
         ("Wybierz muzykę", "Otwórz playlistę z YouTube (karta <i>YouTube</i>) albo wyszukaj piosenki. Kolejka jest Twoja; nic nie wraca na YouTube."),
         ("Pokaż kod QR", "W karcie <i>Zaproś</i>. Goście skanują go, wpisują imię i proponują piosenki; Ty zatwierdzasz je jako <i>następną</i> albo <i>na koniec kolejki</i>. Zrób ze znajomego współhosta, a poprowadzi imprezę z laptopa.")],
    feat_h="Wszystko, co potrafi",
    feat_sub="Pełna lista: co umie aplikacja gospodarza i strona dla gości.",
    groups=[
        ("▶ Gra YouTube – bez reklam", [
            "<b>Odtwarzanie bez reklam</b> w osadzonym silniku Firefoksa (GeckoView) z wbudowanym uBlock Origin. Bez konta Google i bez klucza API.",
            "<b>Gra przy wyłączonym ekranie</b> (usługa na pierwszym planie i powiadomienie). Blokady procesora i Wi-Fi są trzymane tylko wtedy, gdy są potrzebne.",
            "<b>Natychmiastowa zmiana piosenki:</b> następna jest już wczytana w ukrytym, drugim odtwarzaczu. YouTube każe osobom z blokadą reklam czekać 5–13 s na start filmu; w ten sposób to czekanie znika.",
            "<b>Płynne przejścia:</b> gdy przeskakujesz, wracasz albo włączasz piosenkę od razu, stara cichnie (2 s), a nowa narasta. Piosenka, która skończy się sama, przełącza się natychmiast.",
            "<b>Dobry dźwięk:</b> najlepszy strumień audio, jaki daje YouTube (Opus, ok. 160 kb/s). Obraz jest maleńki (144p) i domyślnie ukryty, żeby oszczędzać energię; jeden przycisk przełącza: ukryty → mały → pełny ekran.",
            "<b>Pauza zostaje pauzą.</b> Po 10 minutach odtwarzacze są zwalniane, żeby oszczędzać baterię; <i>play</i> wznawia od tego samego miejsca.",
            "<b>Suwak głośności</b> głośności multimediów telefonu (idzie za przyciskami głośności); stuknięcie głośnika wycisza.",
            "<b>Mówi, co jest nie tak:</b> jeśli piosenka nie ruszyła po 20 s, aplikacja podaje powód – brak internetu, sieć bez dostępu, Oszczędzanie danych, uśpienie Androida, tryb oszczędzania baterii albo po prostu wolny start. Piosenki, których nie da się odtworzyć, są pomijane po 45 s.",
            "Okienka cookies są odrzucane automatycznie; kolejka przetrwa restart (wraca zatrzymana).",
        ]),
        ("☰ Kolejka pod Twoją kontrolą", [
            "<b>Playlisty:</b> otwórz dowolną publiczną lub niepubliczną playlistę YouTube i wybierz <i>Ustaw jako aktualną playlistę</i>. Utwory zachowują kolejność z YouTube (losowa kolejność to przełącznik); wczytuje się ok. 100 pierwszych. Miksy YouTube można importować ze strony filmu. Playlisty prywatne działają po zalogowaniu (eksperymentalnie – najłatwiej ustawić je jako <i>Niepubliczne</i>).",
            "<b>Wyszukiwanie w aplikacji:</b> <i>Szukaj piosenki do dodania</i> otwiera pełnoekranowe wyszukiwanie (tytuł, wykonawca albo wklejony link). Każdy wynik ma dwa przyciski z ikonką – strzałka na początek listy (<b>zagraj jako następną</b>) i strzałka na koniec (<b>na koniec kolejki</b>). Wyszukiwanie zostaje otwarte, więc dodasz kilka piosenek pod rząd.",
            "<b>Karta YouTube:</b> prawdziwy mobilny YouTube z <b>paskiem adresu</b> (wpisz wyszukiwanie albo wklej link do filmu lub playlisty). Strona zajmuje cały ekran – paski aplikacji przewijają się razem z nią. Okrągły przycisk <b>+</b> jest szary, gdy na stronie nie ma czego dodać; na playliście lub filmie wysuwa się panel (playlista: losowa kolejność i <i>ustaw jako aktualną</i>; film: <i>następna</i> / <i>na koniec kolejki</i>), który potem znika.",
            "<b>Gesty na kolejce:</b> stuknij piosenkę, by przenieść ją na górę, przesuń w prawo, by zagrać od razu, w lewo, by usunąć; przytrzymaj i przeciągnij, by zmienić kolejność (lista przewija się przy brzegach). Od czasu do czasu pierwszy wiersz delikatnie pokazuje, jak to działa. <i>Wyczyść</i> czyści kolejkę (po zapytaniu); <i>Powtarzaj</i> uzupełnia ją z playlisty.",
            "<b>Propozycje</b> gości czekają w karcie <i>Propozycje</i>. Zatwierdzasz każdą jako <b>następną</b> albo <b>na koniec</b>, albo odrzucasz.",
            "Miniaturki wszędzie; długie tytuły przewijają się powoli, żebyś mógł je przeczytać (stoją w miejscu, jeśli wyłączysz animacje w Androidzie).",
        ]),
        ("👥 Goście wchodzą przez link, nie przez aplikację", [
            "Telefon udostępnia <b>stronę WWW w sieci lokalnej</b> (<code>http://192.168.x.x:8080/</code>). Karta <i>Zaproś</i> pokazuje jej <b>kod QR</b>, adres, <i>Udostępnij link</i> i <i>Kopiuj</i> oraz pozwala wybrać sieć, jeśli telefon ma ich kilka.",
            "Gość wpisuje <b>imię</b> i jest w środku – bez kodu, bez konta, bez instalowania. Działa na telefonach, tabletach i komputerach.",
            "Goście widzą <b>kolejkę na żywo</b> i co gra, <b>szukają na YouTube</b>, <b>proponują piosenki</b> (do 5 oczekujących, bez duplikatów), śledzą swoje propozycje i mogą <b>poprosić o uprawnienia hosta</b>.",
            "Możesz zamknąć drzwi (<i>Przyjmuj nowych gości</i>), zobaczyć, kto jest online, usunąć każdego i <b>zrobić z dowolnego gościa współhosta</b> jednym dotknięciem – bez prośby. Jego strona przeładuje się w tryb hosta; możesz mu to odebrać w każdej chwili.",
            "Jeśli router izoluje urządzenia w Wi-Fi, użyj hotspotu na telefonie.",
        ]),
        ("⌨ Prowadź z laptopa albo innego telefonu", [
            "<b>Współhost ma takie same uprawnienia jak host</b>: play/pauza, przewijanie (kliknięcie paska postępu), poprzedni/następny, powtarzanie, głośność; przesuwanie, granie od razu, usuwanie i czyszczenie kolejki; zatwierdzanie propozycji i innych współhostów; wczytanie playlisty z linku; szukanie i dodawanie piosenek jako następnych lub na koniec.",
            "Strona jest <b>responsywna</b>: układ na telefon i dwukolumnowy na komputer, motyw jasny/ciemny/auto, pasek przy utracie połączenia i automatyczne łączenie ponownie.",
            "<b>Klawiatura:</b> <kbd>Spacja</kbd> play/pauza · <kbd>N</kbd> / <kbd>P</kbd> następny / poprzedni · <kbd>R</kbd> powtarzanie · <kbd>+</kbd> <kbd>−</kbd> głośność · <kbd>M</kbd> wyciszenie · <kbd>↑</kbd> <kbd>↓</kbd> albo <kbd>J</kbd> <kbd>K</kbd> wybór piosenki · <kbd>Enter</kbd> zagraj ją · <kbd>T</kbd> na górę · <kbd>Alt</kbd>+<kbd>↑</kbd>/<kbd>↓</kbd> przesuń · <kbd>Delete</kbd> usuń · <kbd>/</kbd> szukaj · <kbd>1</kbd>–<kbd>5</kbd> karty · <kbd>D</kbd> motyw · <kbd>?</kbd> pomoc.",
            "<b>Mysz:</b> przeciąganie do zmiany kolejności, dwuklik odtwarza, przyciski z ikonkami i podpowiedziami ze skrótem.",
        ]),
        ("🎨 Wygląda jak impreza, oszczędza energię", [
            "Motyw jasny, ciemny albo automatyczny; gradienty, animowany equalizer i powoli płynąca karta „teraz gra”; układ pionowy i poziomy; adaptacyjna ikona aplikacji (także w wersji monochromatycznej).",
            "Pasek tytułowy chowa się po kilku sekundach; przeciągnij w dół lub stuknij jego uchwyt, żeby wrócił. W karcie YouTube paski przewijają się z stroną, więc dostaje ona cały ekran.",
            "<b>Bateria:</b> ekran nie jest trzymany włączony, dopóki nie włączysz <i>Nie wygaszaj ekranu</i>; blokady tylko wtedy, gdy trzeba; spokojne aktualizacje dla gości; animacje tylko podczas grania.",
        ]),
        ("🔒 Prywatność od początku", [
            "<b>Bez konta, bez śledzenia, bez analityki, bez reklam.</b> Kolejka mieszka w telefonie. Jedyny ruch to YouTube i lokalna strona WWW.",
            "Strona działa przez zwykłe HTTP w sieci lokalnej (bez TLS): używaj zaufanej sieci. Goście dostają losowe tokeny; host zatwierdza każdą propozycję.",
            "<b>Otwarte oprogramowanie</b> (AGPL-3.0). Użyte składniki: GeckoView, uBlock Origin, Ktor, Jetpack Compose i inne – lista w repozytorium.",
        ]),
    ],
    shots_h="Zrzuty ekranu", shots_sub="Aplikacja gospodarza na telefonie i strona WWW, którą widzą goście i współhostowie.",
    shots_app="Aplikacja na telefonie gospodarza", shots_web="Strona WWW dla gości i współhostów",
    cap=dict(
        queue=("Kolejka", "Teraz gra, głośność, kolejka i przycisk wyszukiwania."),
        search=("Wyszukiwanie", "Dwa przyciski ze strzałkami: jako następna albo na koniec."),
        proposals=("Propozycje", "Zatwierdź piosenkę gościa jako następną albo na koniec."),
        invite=("Zaproś", "Kod QR otwiera stronę gości; awansuj gości na współhostów."),
        youtube=("Karta YouTube", "Prawdziwy YouTube, pasek adresu i szary przycisk + z dymkiem."),
        panel=("Panel +", "Wysuwa się na playliście lub filmie – i znika."),
        landscape=("Widok poziomy", "Odtwarzacz po lewej, karty po prawej."),
        light=("Motyw jasny", "Jasny, ciemny albo automatyczny."),
        web_queue_dark=("Strona hosta na komputerze – ciemna", "Dwie kolumny; klawiatura i mysz działają tak, jak trzeba."),
        web_queue_light=("Strona hosta – jasna", "Ta sama strona w jasnym motywie."),
        web_search=("Wyszukiwanie na stronie hosta", "Następna / na koniec kolejki jako przyciski z ikonami."),
        web_proposals=("Propozycje na stronie hosta", "Zatwierdź jako następną lub na koniec albo odrzuć."),
        web_guests=("Goście", "Kto jest online; awansuj, odbierz uprawnienia lub usuń."),
        web_guest_queue=("Widok gościa", "Kolejka na żywo i co aktualnie gra."),
        web_guest_search=("Gość proponuje piosenkę", "Decyduje host."),
        web_mobile=("Na telefonach", "Ta sama strona w układzie na telefon."),
    ),
    inst_h="Instalacja",
    inst_sub="Party Queue nie ma w Google Play, więc plik APK instalujesz sam. Zajmuje to minutę.",
    inst_steps=[
        ("Pobierz APK na telefon", f"Zeskanuj kod QR powyżej aparatem telefonu albo otwórz na nim <a href=\"{APK}\">ten link</a>. Przeglądarka może ostrzec, że ten typ pliku może zaszkodzić urządzeniu – wybierz <i>Pobierz mimo to</i> / <i>Zachowaj</i>. Plik ma ok. 225 MB."),
        ("Zezwól na instalację", "Otwórz pobrany <code>party-queue.apk</code>. Jeśli Android zapyta, pozwól przeglądarce (albo menedżerowi plików) <i>Instalować nieznane aplikacje</i>: <i>Ustawienia → Aplikacje → Dostęp specjalny → Instalowanie nieznanych aplikacji</i>. Google Play Protect może napisać, że aplikacja nie była skanowana albo pochodzi od nieznanego dewelopera – wybierz <i>Więcej szczegółów → Zainstaluj mimo to</i>."),
        ("Otwórz i dwa razy się zgódź", "Zezwól na powiadomienia (Android 13+; dzięki nim muzyka gra przy wyłączonym ekranie) i naciśnij <i>Pozwól</i> na pasku, który prosi o pozwolenie na pracę w tle."),
        ("Połącz i zacznij imprezę", "Połącz telefon z Wi-Fi (albo włącz hotspot). Otwórz kartę <i>YouTube</i>, wybierz playlistę i pokaż kod QR z karty <i>Zaproś</i>. Goście muszą być w tej samej sieci."),
    ],
    verify_h="Sprawdź pobrany plik (opcjonalnie)",
    verify_p="Każde wydanie ma plik z sumą kontrolną. Połóż oba pliki w jednym folderze i uruchom:",
    verify_cmds="# macOS / Linux\nshasum -a 256 -c party-queue.apk.sha256\n\n# Windows (PowerShell)\n(Get-FileHash party-queue.apk -Algorithm SHA256).Hash.ToLower()   # porównaj z plikiem .sha256\n\n# albo instalacja z komputera\nadb install -r party-queue.apk",
    upd_h="Aktualizacja",
    upd_sub="Nie ma sklepu, więc aktualizacje są ręczne – i równie proste.",
    upd_steps=[
        ("Sprawdź, jaką masz wersję", "<i>Ustawienia → Aplikacje → Party Queue</i> pokazuje wersję na dole. Najnowsza jest na górze tej strony i na <a href=\"" + REPO + "/releases\">stronie wydań</a>."),
        ("Pobierz nowy APK i otwórz go", "Użyj tego samego kodu QR lub linku. Android zainstaluje go <b>na starej wersji</b>; kolejka, goście i ustawienia zostają."),
        ("Dowiaduj się o nowych wersjach", "Na GitHubie wybierz <i>Watch → Custom → Releases</i> w <a href=\"" + REPO + "\">repozytorium</a> albo zasubskrybuj <a href=\"" + REPO + "/releases.atom\">kanał wydań</a> w dowolnym czytniku."),
    ],
    upd_note="<b>Jeśli Android napisze, że aplikacja nie została zainstalowana z powodu konfliktu z istniejącym pakietem</b>, stara kopia była podpisana innym kluczem (może się to zdarzyć raz, przy przejściu między wersją zbudowaną przez kogoś innego a wydaniem z tej strony). Odinstaluj Party Queue i zainstaluj ponownie – tracisz kolejkę i listę gości, nic więcej: aplikacja nie trzyma danych nigdzie poza telefonem. Wydania z tej strony są podpisane jednym kluczem projektu, więc kolejne aktualizacje instalują się jedna na drugiej.",
    faq_h="Pytania",
    faq=[
        ("Goście nie mogą otworzyć strony.", "Sprawdź, czy są w tym samym Wi-Fi co telefon gospodarza, i użyj adresu z karty <i>Zaproś</i> – adres telefonu może się zmienić po ponownym połączeniu. Niektóre routery i sieci dla gości izolują urządzenia od siebie; włącz hotspot na telefonie gospodarza i połącz się z nim."),
        ("Muzyka przestaje grać po wygaszeniu ekranu.", "Zezwól na powiadomienia i naciśnij <i>Pozwól</i> na pasku (wyłączona optymalizacja baterii dla aplikacji). Na niektórych telefonach ustaw też w ustawieniach systemu zużycie baterii aplikacji na <i>Bez ograniczeń</i>."),
        ("Piosenka nie startuje.", "Poczekaj 20 sekund: aplikacja pokaże wtedy pod odtwarzaczem powód (brak internetu, Oszczędzanie danych, tryb uśpienia…). YouTube sam czasem opóźnia start filmu; piosenki, których nie da się odtworzyć, są pomijane po 45 sekundach."),
        ("Czy mogę używać prywatnych playlist?", "Playlisty publiczne i niepubliczne działają bez logowania. Dla prywatnej zaloguj się w karcie <i>YouTube</i> (eksperymentalnie) – albo ustaw playlistę na YouTube jako <i>Niepubliczną</i>, co jest najłatwiejsze."),
        ("Czy potrzebuję konta Google albo klucza API?", "Nie. Aplikacja czyta te same publiczne strony co przeglądarka."),
        ("Czy są reklamy?", "Nie, uBlock Origin jest wbudowany. Jeśli któraś się przedrze, zgłoś to na GitHubie."),
        ("Czy iPhone może być gospodarzem?", "Nie – gospodarzem musi być telefon z Androidem (10+, 64-bitowy). Goście mogą używać dowolnego telefonu, tabletu lub komputera z przeglądarką."),
        ("Czy to legalne?", "Projekt nie jest powiązany z YouTube, Google ani Mozillą. Korzystanie z niego może naruszać regulamin YouTube; używasz go na własną odpowiedzialność i do prywatnych wydarzeń."),
    ],
    foot_l="Party Queue to wolne oprogramowanie (AGPL-3.0). Niepowiązane z YouTube, Google ani Mozillą.",
    foot_r=[("Kod źródłowy", REPO), ("Zgłoś problem", REPO + "/issues"), ("Lista zmian", REPO + "/blob/main/CHANGELOG.md"), ("Organizacja", "https://github.com/party-queue")],
    top="Do góry",
)

APP_ORDER = ["queue", "search", "proposals", "invite", "youtube", "panel", "landscape", "light"]
WEB_ORDER = ["web_queue_dark", "web_queue_light", "web_search", "web_proposals", "web_guests", "web_guest_queue", "web_guest_search", "web_mobile"]
WIDE = {"web_queue_dark", "web_queue_light", "web_mobile", "landscape"}


def screen_path(key):
    return f"assets/img/screens/{'app-' + key if not key.startswith('web_') else key.replace('_', '-')}.jpg"


def gallery(t):
    out = []
    app = [k for k in APP_ORDER if os.path.exists(os.path.join(ROOT, screen_path(k)))]
    if app:
        figs = "".join(
            f'<figure><a href="../{screen_path(k)}"><img loading="lazy" src="../{screen_path(k)}" alt="{html.escape(t["cap"][k][0])}"></a>'
            f'<figcaption><b>{html.escape(t["cap"][k][0])}</b>{html.escape(t["cap"][k][1])}</figcaption></figure>'
            for k in app if k != "landscape")
        land = ""
        if "landscape" in app:
            k = "landscape"
            land = (f'<div class="gallery" style="margin-top:18px"><figure class="wide"><a href="../{screen_path(k)}"><img loading="lazy" src="../{screen_path(k)}" alt="{html.escape(t["cap"][k][0])}"></a>'
                    f'<figcaption><b>{html.escape(t["cap"][k][0])}</b>{html.escape(t["cap"][k][1])}</figcaption></figure></div>')
        out.append(f'<h3 style="margin:28px 0 14px">{t["shots_app"]}</h3><div class="phones">{figs}</div>{land}')
    web = [k for k in WEB_ORDER if os.path.exists(os.path.join(ROOT, screen_path(k)))]
    figs = "".join(
        f'<figure class="{"wide" if k in WIDE else ""}"><a href="../{screen_path(k)}"><img loading="lazy" src="../{screen_path(k)}" alt="{html.escape(t["cap"][k][0])}"></a>'
        f'<figcaption><b>{html.escape(t["cap"][k][0])}</b>{html.escape(t["cap"][k][1])}</figcaption></figure>'
        for k in web)
    out.append(f'<h3 style="margin:34px 0 14px">{t["shots_web"]}</h3><div class="gallery">{figs}</div>')
    return "".join(out)


def page(t):
    L, O = t["lang"], t["other"]
    nav = "".join(f'<a href="#{a}">{n}</a>' for a, n in t["nav"])
    feats = "".join(
        f'<div class="card"><h3>{g}</h3><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"
        for g, items in t["groups"])
    how = "".join(f"<li><b>{h}</b>{d}</li>" for h, d in t["how"])
    inst = "".join(f"<li><b>{h}</b>{d}</li>" for h, d in t["inst_steps"])
    upd = "".join(f"<li><b>{h}</b>{d}</li>" for h, d in t["upd_steps"])
    links = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in t["dl_links"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    foot = " · ".join(f'<a href="{u}">{n}</a>' for n, u in t["foot_r"])
    hero_shot = "../assets/img/screens/web-queue-dark.jpg"
    return f'''<!doctype html>
<html lang="{L}" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t["title"])}</title>
<meta name="description" content="{html.escape(t["desc"])}">
<meta name="theme-color" content="#7c3aed">
<link rel="icon" type="image/svg+xml" href="../assets/img/icon.svg">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="pl" href="{SITE}/pl/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="canonical" href="{SITE}/{L}/">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(t["title"])}">
<meta property="og:description" content="{html.escape(t["desc"])}">
<meta property="og:url" content="{SITE}/{L}/">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:image" content="{SITE}/assets/img/screens/web-queue-dark.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="../assets/style.css?v={BUILD}">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="#top"><img src="../assets/img/icon.svg" alt="" width="34" height="34">Party Queue</a>
  <nav class="main" aria-label="Menu">{nav}</nav>
  <span class="sp"></span>
  <button class="pillbtn" id="themeBtn" type="button" data-auto="{t["theme"][0]}" data-light="{t["theme"][1]}" data-dark="{t["theme"][2]}"><span aria-hidden="true">◐</span><span class="lb"> {t["theme"][0]}</span></button>
  <a class="pillbtn flagbtn" href="../{O}/" hreflang="{O}" lang="{O}" data-lang="{O}" title="{t["other_name"]}" aria-label="{t["other_name"]}">{FLAG[O]}</a>
</div></header>

<main id="top">
<section class="hero"><div class="wrap grid">
  <div>
    <h1>{t["h1"]}</h1>
    <p class="lead">{t["lead"]}</p>
    <div class="cta">
      <a class="btn primary" href="{APK}">⬇ {t["dl_btn"]}</a>
      <a class="btn small" href="{REPO}/releases">{t["all_rel"]}</a>
      <a class="btn small" href="{REPO}">{t["src"]}</a>
    </div>
    <p class="meta" data-latest="{t["latest"]}">{t["latest_fallback"]}</p>
    <p class="meta">{t["req"]}</p>
  </div>
  <div><img class="shot-hero" src="{hero_shot}" alt="Party Queue" width="1440" height="813"></div>
</div></section>

<section id="download"><div class="wrap">
  <h2>{t["dl_h"]}</h2><p class="sub">{t["dl_sub"]}</p>
  <div class="dl">
    <div class="qr-main"><figure><img class="qr" src="../assets/img/qr-download.svg" alt="QR code: {APK}" width="230" height="230"><figcaption>{t["qr_main"]}</figcaption></figure></div>
    <div>
      <h3 style="margin-top:0">{t["dl_steps_h"]}</h3>
      <ul>{links}</ul>
    </div>
  </div>
</div></section>

<section id="how"><div class="wrap"><h2>{t["how_h"]}</h2><p class="sub">{t["how_sub"]}</p><ol class="steps">{how}</ol></div></section>

<section id="features"><div class="wrap"><h2>{t["feat_h"]}</h2><p class="sub">{t["feat_sub"]}</p><div class="cards">{feats}</div></div></section>

<section id="screens"><div class="wrap"><h2>{t["shots_h"]}</h2><p class="sub">{t["shots_sub"]}</p>{gallery(t)}</div></section>

<section id="install"><div class="wrap"><h2>{t["inst_h"]}</h2><p class="sub">{t["inst_sub"]}</p><ol class="steps">{inst}</ol>
  <h3 style="margin:30px 0 8px">{t["verify_h"]}</h3><p>{t["verify_p"]}</p><pre><code>{html.escape(t["verify_cmds"])}</code></pre>
</div></section>

<section id="update"><div class="wrap"><h2>{t["upd_h"]}</h2><p class="sub">{t["upd_sub"]}</p><ol class="steps">{upd}</ol><div class="note">{t["upd_note"]}</div></div></section>

<section id="faq"><div class="wrap"><h2>{t["faq_h"]}</h2>{faq}</div></section>
</main>

<footer><div class="wrap"><div>{t["foot_l"]}</div><div>{foot} · <a href="#top">{t["top"]}</a></div></div></footer>
<script src="../assets/site.js?v={BUILD}"></script>
</body>
</html>
'''


for L in ("en", "pl"):
    os.makedirs(os.path.join(ROOT, L), exist_ok=True)
    with open(os.path.join(ROOT, L, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(T[L]))

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Party Queue</title>
<meta name="description" content="Party Queue – a party jukebox for Android. / Imprezowy jukebox na Androida.">
<link rel="icon" type="image/svg+xml" href="assets/img/icon.svg">
<link rel="alternate" hreflang="en" href="{SITE}/en/">
<link rel="alternate" hreflang="pl" href="{SITE}/pl/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:title" content="Party Queue">
<meta property="og:image" content="{SITE}/assets/img/screens/web-queue-dark.jpg">
<style>
body {{ margin:0; min-height:100vh; display:grid; place-items:center; background:#130a26; color:#f3ecff; font:18px/1.5 system-ui,sans-serif; text-align:center; padding:24px }}
img {{ width:96px; height:96px; border-radius:26px; box-shadow:0 10px 34px #7c3aed77 }}
h1 {{ margin:18px 0 6px; font-size:40px }}
a.b {{ display:inline-block; margin:8px; padding:10px 14px; border-radius:18px; background:linear-gradient(120deg,#ff2e93,#7c3aed 55%,#22b8ff); line-height:0 }}
.flag {{ width:84px; height:56px; border-radius:8px; box-shadow:0 0 0 2px #fff6; display:block }}
</style>
</head>
<body>
<div>
  <img src="assets/img/icon.svg" alt="">
  <h1>Party Queue</h1>
  <p>One phone. One queue. Everyone's songs.<br>Jeden telefon. Jedna kolejka. Piosenki wszystkich.</p>
  <p><a class="b" href="en/" hreflang="en" title="English" aria-label="English">{FLAG["en"].replace('width="30" height="20"', 'width="84" height="56"')}</a><a class="b" href="pl/" hreflang="pl" title="Polski" aria-label="Polski">{FLAG["pl"].replace('width="30" height="20"', 'width="84" height="56"')}</a></p>
</div>
<script>
  // Go straight to the visitor's language (the choice made on a page is remembered).
  try {{
    var saved = localStorage.getItem('pqLang');
    var l = saved || ((navigator.language || 'en').toLowerCase().indexOf('pl') === 0 ? 'pl' : 'en');
    if (location.search.indexOf('choose') < 0) location.replace(l + '/');
  }} catch (e) {{ /* the buttons above still work */ }}
</script>
</body>
</html>
''')

with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
    f.write('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>404 – Party Queue</title>'
            '<body style="margin:0;min-height:100vh;display:grid;place-items:center;background:#130a26;color:#f3ecff;font:18px system-ui;text-align:center">'
            '<div><h1>404</h1><p>This page does not exist. / Tej strony nie ma.</p><p><a style="color:#c4a3ff" href="/">Party Queue</a></p></div></body>')

with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "".join(f'  <url><loc>{SITE}/{L}/</loc><xhtml:link rel="alternate" hreflang="en" href="{SITE}/en/"/><xhtml:link rel="alternate" hreflang="pl" href="{SITE}/pl/"/></url>\n' for L in ("en", "pl"))
            + "</urlset>\n")
print("built")
