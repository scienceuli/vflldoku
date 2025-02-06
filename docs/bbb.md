# Meetings mit BigBlueButton

Das KollTool stellt für Video-Meetings die Open Source Software [BigBlueButton](https://bigbluebutton.org) zur Verfügung. Sie wird auf einem eigenen leistungsfähigen Server gehostet. Dadurch sind jederzeit Videokonferenzen mit (theoretisch) beliebig vielen Teilnehmenden möglich.

Videokonferenzen innerhalb von BigBlueButton (BBB) sind in *Räumen* organisiert; jeder Raum steht für ein Meeting. Erst wenn ein Raum „geöffnet“ wird und ein\*e User\*in eingetreten ist, läuft das Meeting. 

Jedem Team im KollTool steht (mindestens) ein Raum/Meeting zur Verfügung. Darüber hinaus gibt es offene Räume/Meetings, die keinem Team zugeordnet sind. Zusätzlich kann der Zugang zu einem Raum so geregelt werden, dass auch Gäste, die nicht als User\*innen des KollTools registriert sind, an einem Videomeeting teilnehmen können.

*Hinweis*: Die Aufzeichnung von Meetings ist nicht möglich, auch wenn es oben im Meeting-Fenster angeboten wird! Die Funktion ist deaktiviert.

## Wo finde ich die Meetings?

Aus der Navigationsleiste des KollTools gelangt man über *Meetings* → *BigBlueButton* zu einer Übersicht aller Räume, aufgeteilt in **Offene Meetings/Räume** (ohne Teamzuordnung) und **Team-Meetings/Räume** (jeweils einem Team zugeordnet). User\*innen sehen neben den Offenen Räumen nur die Räume der Teams, zu denen sie gehören. 

Das Anlegen der Räume geschieht im Backend; besteht der Wunsch nach einem weiteren Raum, wendet euch bitte an den [Admin](mailto:kolltooladmin@vfll.de). 

## Wie wird ein Meeting gestartet?

Ein Meeting/Raum kann drei Zustände haben:

+ Meetings, die nicht gestartet sind, werden <span style="text-color: red;">rot</span> dargestellt.
+ Meetings, deren Raum geöffnet ist, die aber noch keine\*n Teilnehmer\*in haben, werden <span style="text-color: yellow;">gelb</span> dargestellt.
+ Meetings, die gestartet sind und mindestens eine\*n Teilnehmer\*in haben, werden <span style="text-color: green;">grün</span> dargestellt. 

Zum **Starten** eines Meetings muss der Button *Start* angeklickt werden. Das Recht dazu besitzen alle Team-Mitglieder (Team-Meetings) bzw. alle User\*innen (offene Meetings).

Anschließend tritt man dem Meeting durch Anklicken von *Beitreten* bei; die Farbe der Meeting-Kachel ändert sich zu grün. Weitere User\*innen des KoolTools können nun ebenfalls dem Meeting beitreten.

## Können auch Nicht-User\*innen des KollTools an einem Meeting teilnehmen?

Ja, das ist möglich. Jede Meeting-Kachel zeigt an, ob der Gastzugang aktiviert ist \(*Gastzugang: ja*\) oder nicht \(*Gastzugang: nein*\). Der Status kann durch Anklicken von *Ändern* umgeschaltet werden.

![Meeting-Kachel im Detail](attachments/bbb_meeting_details.png)

Gäste können nun per Code oder per Link an einem Meeting teilnehmen:

1. **Teilnahme per Code**: Ist der Gastzugang freigeschaltet, wird in der Kachel zusätzlich ein achtstelliger Code angezeigt, den Nicht-User\*innen benötigen, um einem Meeting beizutreten.
2. **Teilnahme per Link**: Zusätzlich wird ein Meeting-Link angezeigt, der sich in die Zwischenablage kopieren lässt.

Code oder Link können an Gäste weitergegeben werden. 

## Wie nehmen Nicht-User an einem Meeting teil?

1. **Zugang mit Code**: Meetings, bei denen der Gastzugang aktiviert ist, die gestartet wurden und mindestens eine\*n Teilnehmer\*in haben, werden beim Aufruf von <kolltool.vfll.de> links unter *Laufende Meetings* angezeigt. Über das Tür-Symbol gelangen die Besucher\*innen zu einer Eingabemaske, in die sie ihren Namen und den Code des Meetings eingeben. Wird der Code akzeptiert, bringt sie *Teilnehmen* direkt zum Meeting.
2. **Zugang mit Link**: Der Link führt auf eine Eingabemaske, in die der Gast seinen Namen eingibt. Anschließend wird er zum Meeting weitergeleitet.

Als Name bitte immer Vor- und Nachname angeben. Ist der Kreis der Teilnehmenden größer und kennen sich nicht alle, ist es sinnvoll, zusätzlich Ort und/oder Regionalgruppe und ggf. Funktion im VFLL anzugeben.

## Wie wird ein Meeting beendet?

Ein BigBlueButton-Meeting kann innerhalb von BigBlueButton beendet werden:

Anklicken von ⋮ öffnet dieses Menü

![Meeting beenden|250](attachments/stop_bbb.png)

mit den Optionen *Konferenz verlassen* und *Konferenz beenden*.

Falls sich die Meetingraum-Kachel nach Beenden einer Konferenz nicht rot färbt, hilft *Stop*.

## Meetings planen

Über den Button ![BBB-Kalender-Icon|20](attachments/button_plan_bbb.png) lassen sich Meetings planen. Jedes geplante Meeting besteht aus: Beginn (Datum und Uhrzeit) – Dauer (in Minuten) – Titel – Beschreibung (optional).

Die geplanten Meetings werden zum vorgesehenen Startpunkt gestartet und automatisch nach der vorgesehenen Dauer beendet, falls sich keine Teilnehmenden mehr im Meeting befinden. 
Eine Übersicht der geplanten Meetings findet sich auf jeder Meeting-Kachel im Reiter *Kalender*. Dort können geplante Meetings auch geändert oder gelöscht werden.

![Übersicht Meetings|350](attachments/meeting_calendar.png)


## Weitere Informationen zu BBB

Wer sich detailliert über die Möglichkeiten von BBB informieren möchte findet [hier](https://www.youtube.com/playlist?list=PLeSl48Y1rgh9Cta0kM7IjjHarLRFeXlCF) Videotutorials. 

Auf ein paar Details wird im Folgenden eingegangen.

### Mikrofon und Kamera einschalten

Beim Eintritt in ein BBB-Meeting wird man zunächst gefragt, ob man der Konferenz mit Mikrofon beitreten oder nur zuhören möchte. 

![BigBlueButton-Konferenz beitreten|250](attachments/bbb_konferenz_beitreten.png)

Um mit Webcambild am Meeting teilzunehmen, muss man nun die Kamera freigeben. Dazu klickt man auf das (noch durchgestrichene) Kamerasymbol in der Leiste unten und wählt dann die Option „Webcam freigeben“. Hier hat man auch die Möglichkeit, einen Hintergrund einzustellen.

![Webcam-Freigabe|350](attachments/bbb_webcam-freigabe_1.png)

![Hintergrund einstellen|350](attachments/bbb_webcam-freigabe_2.png)


### Die einzelnen Bereiche des BBB-Bildschirms

In der **Menüleiste** links finden sich neben der Teilnehmendenliste die Bereiche Nachrichten \(Öffentlicher Chat\) und \(Geteilte\) Notizen.

![BigBlueButton Menüleiste|250](attachments/bbb_menueleiste.png)


In der **Teilnehmerliste** werden alle Teilnehmenden in Form von Kacheln mit Namen angezeigt. Die Symbole geben an, wie jemand an dem Meeting teilnimmt: mit Mikrofon, nur zuhörend, mit Webcam.

![Liste der Konferenzteilnehmer|250](attachments/bbb_teilnehmendenliste.png)


Der **Chat** ermöglicht zum einen Teilnehmenden mit Mikrofonproblemen die aktive Konferenzteilnahme, zum anderen eignet er sich zur Weitergabe von Links oder anderen Informationen, die im aktuellen Zusammenhang von Bedeutung sind.

![Chatbeispiel|300](attachments/bbb_chat_beispiel.png)

Speichern kann man den Chatverlauf über das Kontextmenü, das sich rechts oben hinter den drei Punkten verbirgt.


![Chat speichern|300](attachments/bbb_chat_menu.png)

Der *Export* ist nur als .txt möglich.

Unter **Geteilte Notizen** können beispielsweise Diskussionsergebnisse, getroffene Vereinbarungen oder Tagesordnungspunkte für die nächste Konferenz festgehalten werden.

![Geteilte Notizen|300](attachments/bbb_geteilte-Notizen.png)

Hinter dem Pfeilsymbol oben rechts verbergen die Exportmöglichkeiten, die dann unten im Notizenfenster angezeigt werden.

![Export geteilter Notizen|300](attachments/bbb_geteilte-notizen_export.png)

Im **Hauptfenster** ist die **Präsentationsfläche** zu sehen, die mit Klick auf den zweiten Button von rechts in der Fußleiste minimiert werden kann. 

![Fußleiste des BigBlueButton-Bildschirms](attachments/bbb_fussleiste.png)
 
Hinter dem rechten Button in Buttongruppe in der Mitte (in der Abbildung schwarz) verbirgt sich die **Bildschirmfreigabe**.

Dafür benötigt man Präsentatorrechte. Alle Teilnehmenden können sich entweder mit Klick auf das Pluszeichen in der Fußleiste oder über das Kontextmenü der Kachel zum Präsentator machen. 

![Zum Präsentator werden|150](attachments/bbb_praesentator_werden.png)

Alternativ geht das über die Teilnehmerliste:

![Über die Teilnehmerliste zum Präsentator werden|300](attachments/bbb_praesentator_werden_alternative.png)

Klickt man auf *Bildschirm freigeben*, erscheint folgendes Fenster:

![Bildschirm freigeben|350](attachments/bbb_bildschirmfreigabe.png)

Hier kann man auswählen, was freigegeben werden soll, und muss die Freigabe bestätigen.

![Bildschirmteilung erlauben|350](attachments/bbb_bildschirm-teilen_erlauben.png)

*Wichtig*: Es können nur Browserfenster freigegeben werden, keine Browsertabs.

Nützlich ist die **Umfragefunktion**, die auch zu Abstimmungen genutzt werden kann und von mehreren Regionalgruppen für Wahlen genutzt wird.

*Bitte beachten*: Die Person, die eine Umfrage stellt, kann an dieser Umfrage nicht teilnehmen. Ihr Votum muss zur Ermittlung des Endergebnisses addiert werden.

Klickt man auf *Umfrage starten*, öffnet sich das folgende Fenster:

![Umfragetypen|300](attachments/bbb_umfragen_uebersicht.png)

Wichtig ist das Feld *Teilnehmerantwort*. Standardmäßig sind die Umfragen nicht anonym. Über den Schieberegler kann das geändert werden.

![Anonyme Umfragen|300](attachments/bbb_umfrage_teilnehmerantwort.png)

Der Umfragetyp Ja / Nein / Enthaltung lässt sich für Wahlen in den RG nutzen (nicht vergessen, die Teilnehmerantwort auf anonym zu setzen!).

In dem folgenden Beispiel wurde danach gefragt, ob das KollTool nützlich ist.

![Umfrage Ja, Nein, Enthaltung|300](attachments/bbb_umfrage_ja-nein-enthaltung.png)

Sobald die Umfrage gestartet ist, sieht man als Ersteller\*in der Umfrage folgendes Fenster:

![Laufende Umfrage|300](attachments/bbb_umfrage_ja-nein-enthaltung_fertig.png)

Ist die Umfrage abgeschlossen, kann das Ergebnis veröffentlicht werden. Es erscheint für alle Teilnehmenden sichtbar in der rechten unteren Ecke des Präsentationsfensters:

![Umfrageergebnis anzeigen|300](attachments/bbb_umfrage_veroeffentlicht.png)

## Zoom Meetings

siehe [[zoom]]



