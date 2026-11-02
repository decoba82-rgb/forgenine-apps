#!/usr/bin/env python3
# Gera privacy/dailyx/index.html e policies/dailyx/index.html (7 idiomas cada)
import os, html

EMAIL = "supportforge9@gmail.com"
DEV = "Forgenine"
APP = "DailyX"
DATE = {"en": "November 2, 2026", "pt-BR": "2 de novembro de 2026", "pt-PT": "2 de novembro de 2026",
        "es": "2 de noviembre de 2026", "fr": "2 novembre 2026", "de": "2. November 2026", "it": "2 novembre 2026"}
LANGS = [("en", "English"), ("pt-BR", "Português (Brasil)"), ("pt-PT", "Português (Portugal)"),
         ("es", "Español"), ("fr", "Français"), ("de", "Deutsch"), ("it", "Italiano")]
UI = {
 "en": ("Privacy Policy", "Terms of Use", "Last updated", "Language"),
 "pt-BR": ("Política de Privacidade", "Termos de Uso", "Última atualização", "Idioma"),
 "pt-PT": ("Política de Privacidade", "Termos de Utilização", "Última atualização", "Idioma"),
 "es": ("Política de Privacidad", "Términos de Uso", "Última actualización", "Idioma"),
 "fr": ("Politique de confidentialité", "Conditions d'utilisation", "Dernière mise à jour", "Langue"),
 "de": ("Datenschutzerklärung", "Nutzungsbedingungen", "Zuletzt aktualisiert", "Sprache"),
 "it": ("Informativa sulla privacy", "Termini di utilizzo", "Ultimo aggiornamento", "Lingua"),
}
M = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
GP = '<a href="https://policies.google.com/privacy">Google Privacy Policy</a>'
GT = '<a href="https://policies.google.com/technologies/partner-sites">'

PRIVACY = {
"en": [
 ("Who we are", f"{APP} is a daily puzzle game published by {DEV} (the “developer”, “we”). This policy explains what data is handled when you use the app and your choices. Contact: {M}."),
 ("Data we collect", "We do not ask for your name, e-mail or any account of our own. Your progress, streaks, stars, level choices and settings are stored only on your device."),
 ("Google Play Games (optional)", f"If you choose to sign in with Google Play Games, Google processes your Play Games profile (player name, avatar and player ID) and may store your progress as a saved game in your Google account. This is handled by Google under the {GP}. You can play without signing in."),
 ("Advertising", f"The app is free and shows ads through Google AdMob. AdMob may collect the advertising ID, device and app information, IP address (used for approximate location), ad interactions and diagnostic data to serve, measure and protect ads. Where the law requires it (for example in the EEA, UK and Switzerland), you will be asked for consent before personalized ads are shown. You can reset or delete your advertising ID in your Android settings. Learn more: {GT}how Google uses data</a>."),
 ("Purposes and legal bases", "Data is used to run the game, keep your progress, show and measure ads and prevent fraud. Legal bases: performance of the service, our legitimate interests and, where required, your consent (Brazilian LGPD, EU/UK GDPR and equivalent laws)."),
 ("Children", "The app is not directed to children under 13 and we do not knowingly collect their personal data. If you believe a child has provided data, contact us and we will take appropriate action."),
 ("Retention and deletion", "Local data stays on your device until you clear the app data or uninstall it. Data held by Google (Play Games, AdMob) follows Google's retention rules and can be managed in your Google account."),
 ("Your rights", f"Depending on where you live, you may request access, correction, deletion, portability or information about the use of your data, and withdraw consent. Write to {M}; we will reply within the legal deadlines. You may also contact your data protection authority (in Brazil, the ANPD)."),
 ("Security", "Data exchanged with third-party services is encrypted in transit. No method is 100% secure, but we use reasonable measures to protect it."),
 ("Changes", "We may update this policy. The date at the top shows the latest version; relevant changes will be announced in the app or store listing."),
],
"pt-BR": [
 ("Quem somos", f"O {APP} é um jogo de desafios diários publicado pela {DEV} (o “desenvolvedor”, “nós”). Esta política explica quais dados são tratados quando você usa o app e quais são as suas escolhas. Contato: {M}."),
 ("Dados que coletamos", "Não pedimos seu nome, e-mail nem cadastro próprio. Seu progresso, sequências, estrelas, níveis escolhidos e configurações ficam salvos apenas no seu aparelho."),
 ("Google Play Games (opcional)", f"Se você optar por entrar com o Google Play Games, o Google trata o seu perfil do Play Games (nome de jogador, avatar e ID de jogador) e pode guardar seu progresso como jogo salvo na sua conta Google. Esse tratamento é feito pelo Google conforme a <a href=\"https://policies.google.com/privacy?hl=pt-BR\">Política de Privacidade do Google</a>. Você pode jogar sem entrar."),
 ("Publicidade", f"O app é gratuito e exibe anúncios do Google AdMob. O AdMob pode coletar o ID de publicidade, informações do aparelho e do app, endereço IP (usado para localização aproximada), interações com anúncios e dados de diagnóstico para exibir, medir e proteger os anúncios. Onde a lei exigir (por exemplo, no Espaço Econômico Europeu, Reino Unido e Suíça), seu consentimento será solicitado antes de anúncios personalizados. Você pode redefinir ou excluir o ID de publicidade nas configurações do Android. Saiba mais: {GT}como o Google usa os dados</a>."),
 ("Finalidades e bases legais", "Os dados são usados para funcionar o jogo, manter seu progresso, exibir e medir anúncios e prevenir fraudes. Bases legais: execução do serviço, legítimo interesse e, quando exigido, consentimento (LGPD, RGPD/GDPR e leis equivalentes)."),
 ("Crianças", "O app não é direcionado a menores de 13 anos e não coletamos intencionalmente dados pessoais deles. Se você acredita que uma criança forneceu dados, fale conosco para tomarmos as providências cabíveis."),
 ("Retenção e exclusão", "Os dados locais ficam no seu aparelho até você limpar os dados do app ou desinstalá-lo. Os dados mantidos pelo Google (Play Games, AdMob) seguem as regras de retenção do Google e podem ser gerenciados na sua conta Google."),
 ("Seus direitos", f"Você pode solicitar confirmação, acesso, correção, eliminação, portabilidade e informações sobre o uso dos seus dados, além de revogar o consentimento (art. 18 da LGPD). Escreva para {M}; responderemos nos prazos legais. Você também pode recorrer à ANPD."),
 ("Segurança", "Os dados trocados com serviços de terceiros são criptografados em trânsito. Nenhum método é 100% seguro, mas adotamos medidas razoáveis de proteção."),
 ("Alterações", "Podemos atualizar esta política. A data no topo indica a versão mais recente; mudanças relevantes serão informadas no app ou na página da loja."),
],
"pt-PT": [
 ("Quem somos", f"O {APP} é um jogo de desafios diários publicado pela {DEV} (o “programador”, “nós”). Esta política explica que dados são tratados quando utiliza a aplicação e quais as suas opções. Contacto: {M}."),
 ("Dados que recolhemos", "Não pedimos o seu nome, e-mail nem registo próprio. O seu progresso, sequências, estrelas, níveis escolhidos e definições ficam guardados apenas no seu dispositivo."),
 ("Google Play Games (opcional)", f"Se optar por iniciar sessão com o Google Play Games, a Google trata o seu perfil do Play Games (nome de jogador, avatar e ID de jogador) e pode guardar o seu progresso como jogo guardado na sua conta Google, nos termos da <a href=\"https://policies.google.com/privacy?hl=pt-PT\">Política de Privacidade da Google</a>. Pode jogar sem iniciar sessão."),
 ("Publicidade", f"A aplicação é gratuita e apresenta anúncios do Google AdMob. O AdMob pode recolher o ID de publicidade, informações do dispositivo e da aplicação, endereço IP (para localização aproximada), interações com anúncios e dados de diagnóstico para apresentar, medir e proteger os anúncios. Quando a lei o exigir (por exemplo, no Espaço Económico Europeu, Reino Unido e Suíça), será pedido o seu consentimento antes de anúncios personalizados. Pode repor ou eliminar o ID de publicidade nas definições do Android. Saiba mais: {GT}como a Google utiliza os dados</a>."),
 ("Finalidades e fundamentos jurídicos", "Os dados são utilizados para o funcionamento do jogo, manter o progresso, apresentar e medir anúncios e prevenir fraudes. Fundamentos: execução do serviço, interesse legítimo e, quando exigido, consentimento (RGPD, LGPD e leis equivalentes)."),
 ("Crianças", "A aplicação não se destina a menores de 13 anos e não recolhemos intencionalmente os seus dados pessoais. Se considerar que uma criança forneceu dados, contacte-nos para tomarmos as medidas adequadas."),
 ("Conservação e eliminação", "Os dados locais permanecem no dispositivo até limpar os dados da aplicação ou desinstalá-la. Os dados mantidos pela Google (Play Games, AdMob) seguem as regras de conservação da Google e podem ser geridos na sua conta Google."),
 ("Os seus direitos", f"Pode pedir acesso, retificação, apagamento, portabilidade, limitação ou oposição ao tratamento e retirar o consentimento. Escreva para {M}; responderemos nos prazos legais. Pode também apresentar reclamação à CNPD."),
 ("Segurança", "Os dados trocados com serviços de terceiros são cifrados em trânsito. Nenhum método é 100% seguro, mas adotamos medidas razoáveis de proteção."),
 ("Alterações", "Podemos atualizar esta política. A data no topo indica a versão mais recente; alterações relevantes serão comunicadas na aplicação ou na página da loja."),
],
"es": [
 ("Quiénes somos", f"{APP} es un juego de desafíos diarios publicado por {DEV} (el “desarrollador”, “nosotros”). Esta política explica qué datos se tratan cuando usas la app y qué opciones tienes. Contacto: {M}."),
 ("Datos que recopilamos", "No pedimos tu nombre, correo ni una cuenta propia. Tu progreso, rachas, estrellas, niveles elegidos y ajustes se guardan solo en tu dispositivo."),
 ("Google Play Games (opcional)", f"Si eliges iniciar sesión con Google Play Games, Google trata tu perfil de Play Games (nombre de jugador, avatar e ID de jugador) y puede guardar tu progreso como partida guardada en tu cuenta de Google, según la <a href=\"https://policies.google.com/privacy?hl=es\">Política de Privacidad de Google</a>. Puedes jugar sin iniciar sesión."),
 ("Publicidad", f"La app es gratuita y muestra anuncios de Google AdMob. AdMob puede recopilar el ID de publicidad, información del dispositivo y de la app, la dirección IP (para ubicación aproximada), interacciones con anuncios y datos de diagnóstico para mostrar, medir y proteger los anuncios. Donde la ley lo exija (por ejemplo, en el Espacio Económico Europeo, Reino Unido y Suiza), se te pedirá consentimiento antes de mostrar anuncios personalizados. Puedes restablecer o eliminar tu ID de publicidad en los ajustes de Android. Más información: {GT}cómo usa Google los datos</a>."),
 ("Finalidades y bases legales", "Los datos se usan para que el juego funcione, conservar tu progreso, mostrar y medir anuncios y prevenir fraudes. Bases legales: ejecución del servicio, interés legítimo y, cuando se requiera, consentimiento (RGPD, LGPD y leyes equivalentes)."),
 ("Menores", "La app no está dirigida a menores de 13 años y no recopilamos intencionadamente sus datos personales. Si crees que un menor nos ha proporcionado datos, contáctanos y tomaremos las medidas oportunas."),
 ("Conservación y eliminación", "Los datos locales permanecen en tu dispositivo hasta que borres los datos de la app o la desinstales. Los datos que conserva Google (Play Games, AdMob) siguen las reglas de Google y puedes gestionarlos en tu cuenta de Google."),
 ("Tus derechos", f"Según dónde vivas, puedes solicitar acceso, rectificación, supresión, portabilidad, limitación u oposición, y retirar tu consentimiento. Escribe a {M}; responderemos en los plazos legales. También puedes acudir a tu autoridad de protección de datos."),
 ("Seguridad", "Los datos intercambiados con servicios de terceros se cifran en tránsito. Ningún método es 100 % seguro, pero aplicamos medidas razonables de protección."),
 ("Cambios", "Podemos actualizar esta política. La fecha superior indica la versión más reciente; los cambios relevantes se comunicarán en la app o en la ficha de la tienda."),
],
"fr": [
 ("Qui sommes-nous", f"{APP} est un jeu de défis quotidiens publié par {DEV} (le « développeur », « nous »). Cette politique explique quelles données sont traitées lorsque vous utilisez l'application et quels sont vos choix. Contact : {M}."),
 ("Données collectées", "Nous ne demandons ni votre nom, ni votre e-mail, ni la création d'un compte. Votre progression, vos séries, étoiles, niveaux choisis et réglages sont enregistrés uniquement sur votre appareil."),
 ("Google Play Jeux (facultatif)", f"Si vous choisissez de vous connecter avec Google Play Jeux, Google traite votre profil Play Jeux (nom de joueur, avatar et identifiant) et peut enregistrer votre progression comme partie sauvegardée dans votre compte Google, conformément aux <a href=\"https://policies.google.com/privacy?hl=fr\">Règles de confidentialité de Google</a>. Vous pouvez jouer sans vous connecter."),
 ("Publicité", f"L'application est gratuite et affiche des annonces Google AdMob. AdMob peut collecter l'identifiant publicitaire, des informations sur l'appareil et l'application, l'adresse IP (pour une localisation approximative), les interactions avec les annonces et des données de diagnostic afin de diffuser, mesurer et protéger les annonces. Lorsque la loi l'exige (par exemple dans l'Espace économique européen, au Royaume-Uni et en Suisse), votre consentement sera demandé avant toute publicité personnalisée. Vous pouvez réinitialiser ou supprimer votre identifiant publicitaire dans les paramètres Android. En savoir plus : {GT}comment Google utilise les données</a>."),
 ("Finalités et bases légales", "Les données servent à faire fonctionner le jeu, conserver votre progression, diffuser et mesurer les annonces et prévenir la fraude. Bases légales : exécution du service, intérêt légitime et, le cas échéant, consentement (RGPD, LGPD et lois équivalentes)."),
 ("Enfants", "L'application ne s'adresse pas aux enfants de moins de 13 ans et nous ne collectons pas sciemment leurs données personnelles. Si vous pensez qu'un enfant nous a fourni des données, contactez-nous."),
 ("Conservation et suppression", "Les données locales restent sur votre appareil jusqu'à ce que vous effaciez les données de l'application ou la désinstalliez. Les données détenues par Google (Play Jeux, AdMob) suivent les règles de Google et se gèrent dans votre compte Google."),
 ("Vos droits", f"Selon votre lieu de résidence, vous pouvez demander l'accès, la rectification, l'effacement, la portabilité, la limitation ou vous opposer au traitement, et retirer votre consentement. Écrivez à {M} ; nous répondrons dans les délais légaux. Vous pouvez aussi saisir votre autorité de protection des données (en France, la CNIL)."),
 ("Sécurité", "Les données échangées avec des services tiers sont chiffrées en transit. Aucune méthode n'est sûre à 100 %, mais nous appliquons des mesures raisonnables."),
 ("Modifications", "Nous pouvons mettre à jour cette politique. La date en haut indique la dernière version ; les changements importants seront signalés dans l'application ou sur la fiche du store."),
],
"de": [
 ("Wer wir sind", f"{APP} ist ein tägliches Rätselspiel, veröffentlicht von {DEV} („Entwickler“, „wir“). Diese Erklärung beschreibt, welche Daten bei der Nutzung der App verarbeitet werden und welche Wahlmöglichkeiten Sie haben. Kontakt: {M}."),
 ("Welche Daten wir erheben", "Wir fragen weder nach Ihrem Namen noch nach Ihrer E-Mail-Adresse oder einem eigenen Konto. Fortschritt, Serien, Sterne, gewählte Stufen und Einstellungen werden nur auf Ihrem Gerät gespeichert."),
 ("Google Play Spiele (optional)", f"Wenn Sie sich mit Google Play Spiele anmelden, verarbeitet Google Ihr Play-Spiele-Profil (Spielername, Avatar und Spieler-ID) und kann Ihren Fortschritt als gespeichertes Spiel in Ihrem Google-Konto ablegen. Dies erfolgt gemäß der <a href=\"https://policies.google.com/privacy?hl=de\">Datenschutzerklärung von Google</a>. Sie können auch ohne Anmeldung spielen."),
 ("Werbung", f"Die App ist kostenlos und zeigt Anzeigen über Google AdMob. AdMob kann die Werbe-ID, Geräte- und App-Informationen, die IP-Adresse (für den ungefähren Standort), Interaktionen mit Anzeigen und Diagnosedaten erfassen, um Anzeigen auszuliefern, zu messen und zu schützen. Wo gesetzlich vorgeschrieben (z. B. im EWR, im Vereinigten Königreich und in der Schweiz), werden Sie vor personalisierter Werbung um Ihre Einwilligung gebeten. Sie können Ihre Werbe-ID in den Android-Einstellungen zurücksetzen oder löschen. Mehr dazu: {GT}wie Google Daten verwendet</a>."),
 ("Zwecke und Rechtsgrundlagen", "Die Daten dienen dem Betrieb des Spiels, der Speicherung des Fortschritts, der Auslieferung und Messung von Anzeigen sowie der Betrugsprävention. Rechtsgrundlagen: Vertragserfüllung, berechtigtes Interesse und, soweit erforderlich, Ihre Einwilligung (DSGVO, LGPD und vergleichbare Gesetze)."),
 ("Kinder", "Die App richtet sich nicht an Kinder unter 13 Jahren, und wir erheben wissentlich keine personenbezogenen Daten von ihnen. Wenn Sie glauben, dass ein Kind Daten übermittelt hat, kontaktieren Sie uns."),
 ("Speicherdauer und Löschung", "Lokale Daten bleiben auf Ihrem Gerät, bis Sie die App-Daten löschen oder die App deinstallieren. Bei Google gespeicherte Daten (Play Spiele, AdMob) unterliegen den Regeln von Google und lassen sich in Ihrem Google-Konto verwalten."),
 ("Ihre Rechte", f"Sie haben je nach Wohnort das Recht auf Auskunft, Berichtigung, Löschung, Datenübertragbarkeit, Einschränkung und Widerspruch sowie auf Widerruf Ihrer Einwilligung. Schreiben Sie an {M}; wir antworten innerhalb der gesetzlichen Fristen. Sie können sich auch bei einer Datenschutzaufsichtsbehörde beschweren."),
 ("Sicherheit", "Mit Drittanbietern ausgetauschte Daten werden bei der Übertragung verschlüsselt. Keine Methode ist 100 % sicher, wir treffen jedoch angemessene Maßnahmen."),
 ("Änderungen", "Wir können diese Erklärung aktualisieren. Das Datum oben zeigt die aktuelle Fassung; wesentliche Änderungen werden in der App oder im Store-Eintrag mitgeteilt."),
],
"it": [
 ("Chi siamo", f"{APP} è un gioco di sfide quotidiane pubblicato da {DEV} (lo “sviluppatore”, “noi”). Questa informativa spiega quali dati vengono trattati quando usi l'app e quali sono le tue scelte. Contatto: {M}."),
 ("Dati raccolti", "Non chiediamo il tuo nome, la tua e-mail né un account nostro. Progressi, serie, stelle, livelli scelti e impostazioni sono salvati solo sul tuo dispositivo."),
 ("Google Play Giochi (facoltativo)", f"Se scegli di accedere con Google Play Giochi, Google tratta il tuo profilo Play Giochi (nome giocatore, avatar e ID giocatore) e può salvare i tuoi progressi come partita salvata nel tuo account Google, secondo le <a href=\"https://policies.google.com/privacy?hl=it\">Norme sulla privacy di Google</a>. Puoi giocare senza accedere."),
 ("Pubblicità", f"L'app è gratuita e mostra annunci tramite Google AdMob. AdMob può raccogliere l'ID pubblicità, informazioni su dispositivo e app, l'indirizzo IP (per la posizione approssimativa), le interazioni con gli annunci e dati diagnostici per mostrare, misurare e proteggere gli annunci. Dove la legge lo richiede (ad esempio nello Spazio economico europeo, nel Regno Unito e in Svizzera), ti verrà chiesto il consenso prima degli annunci personalizzati. Puoi reimpostare o eliminare l'ID pubblicità nelle impostazioni di Android. Maggiori informazioni: {GT}come Google utilizza i dati</a>."),
 ("Finalità e basi giuridiche", "I dati servono a far funzionare il gioco, conservare i progressi, mostrare e misurare gli annunci e prevenire frodi. Basi giuridiche: esecuzione del servizio, legittimo interesse e, ove richiesto, consenso (GDPR, LGPD e leggi equivalenti)."),
 ("Minori", "L'app non è rivolta a minori di 13 anni e non raccogliamo consapevolmente i loro dati personali. Se ritieni che un minore ci abbia fornito dati, contattaci."),
 ("Conservazione e cancellazione", "I dati locali restano sul dispositivo finché non cancelli i dati dell'app o la disinstalli. I dati conservati da Google (Play Giochi, AdMob) seguono le regole di Google e si gestiscono dal tuo account Google."),
 ("I tuoi diritti", f"In base a dove vivi, puoi chiedere accesso, rettifica, cancellazione, portabilità, limitazione od opposizione al trattamento e revocare il consenso. Scrivi a {M}; risponderemo nei termini di legge. Puoi anche rivolgerti al Garante per la protezione dei dati personali."),
 ("Sicurezza", "I dati scambiati con servizi di terze parti sono cifrati in transito. Nessun metodo è sicuro al 100%, ma adottiamo misure ragionevoli."),
 ("Modifiche", "Possiamo aggiornare questa informativa. La data in alto indica la versione più recente; le modifiche rilevanti saranno comunicate nell'app o nella scheda dello store."),
],
}

TERMS = {
"en": [
 ("Acceptance", f"By downloading or using {APP}, published by {DEV}, you agree to these Terms. If you do not agree, do not use the app."),
 ("The service", "DailyX offers free daily puzzles, the same for every player each day, supported by advertising. Features, modes and puzzles may change, be added or be removed over time."),
 ("License", "We grant you a personal, non-exclusive, non-transferable and revocable license to use the app on your devices for non-commercial purposes."),
 ("Acceptable use", "You agree not to copy, modify, decompile or reverse engineer the app, use bots or automated tools, manipulate results or rankings, interfere with ads, or use the app for any unlawful purpose."),
 ("Third-party services", "The app relies on Google Play, Google Play Games and Google AdMob, which are governed by their own terms and policies. We are not responsible for third-party services."),
 ("Intellectual property", f"The app, its puzzles, design, texts, logo and the {APP} name belong to {DEV} or its licensors. Nothing in these Terms transfers ownership to you."),
 ("Progress and availability", "Progress is stored on your device and, if you sign in, in Google Play Games. We do not guarantee that the app will be uninterrupted or error-free, or that streaks and progress will never be lost."),
 ("Disclaimer", "The app is provided “as is” and “as available”, without warranties of any kind, to the extent permitted by law."),
 ("Limitation of liability", "To the extent permitted by law, we are not liable for indirect, incidental or consequential damages arising from the use of the app. Nothing in these Terms limits rights that consumer law grants you and that cannot be waived."),
 ("Termination", "You may stop using the app at any time by uninstalling it. We may suspend or end access in case of a breach of these Terms."),
 ("Governing law", "These Terms are governed by the laws of Brazil. If you are a consumer, you keep the mandatory protections and venue of your country of residence."),
 ("Changes and contact", f"We may update these Terms; the date at the top shows the latest version. Continued use after changes means acceptance. Questions: {M}. See also our <a href=\"../../privacy/dailyx/\">Privacy Policy</a>."),
],
"pt-BR": [
 ("Aceitação", f"Ao baixar ou usar o {APP}, publicado pela {DEV}, você concorda com estes Termos. Se não concordar, não use o app."),
 ("O serviço", "O DailyX oferece desafios diários gratuitos, iguais para todos os jogadores a cada dia, mantidos por publicidade. Recursos, modos e desafios podem mudar, ser incluídos ou retirados com o tempo."),
 ("Licença", "Concedemos a você uma licença pessoal, não exclusiva, intransferível e revogável para usar o app nos seus aparelhos, para fins não comerciais."),
 ("Uso aceitável", "Você concorda em não copiar, modificar, descompilar ou fazer engenharia reversa do app, usar robôs ou ferramentas automatizadas, manipular resultados ou rankings, interferir nos anúncios ou usar o app para fins ilícitos."),
 ("Serviços de terceiros", "O app depende do Google Play, do Google Play Games e do Google AdMob, que têm termos e políticas próprios. Não nos responsabilizamos por serviços de terceiros."),
 ("Propriedade intelectual", f"O app, os desafios, o design, os textos, o logotipo e o nome {APP} pertencem à {DEV} ou a seus licenciantes. Nada nestes Termos transfere a propriedade a você."),
 ("Progresso e disponibilidade", "O progresso fica salvo no seu aparelho e, se você entrar, no Google Play Games. Não garantimos que o app funcione sem interrupções ou erros, nem que sequências e progresso nunca sejam perdidos."),
 ("Isenção de garantias", "O app é fornecido “no estado em que se encontra” e “conforme disponível”, sem garantias de qualquer tipo, na medida permitida pela lei."),
 ("Limitação de responsabilidade", "Na medida permitida pela lei, não respondemos por danos indiretos, incidentais ou consequentes decorrentes do uso do app. Nada nestes Termos limita os direitos assegurados pelo Código de Defesa do Consumidor."),
 ("Encerramento", "Você pode deixar de usar o app a qualquer momento, desinstalando-o. Podemos suspender ou encerrar o acesso em caso de violação destes Termos."),
 ("Lei aplicável", "Estes Termos são regidos pelas leis do Brasil. Se você for consumidor, mantém as proteções obrigatórias e o foro do seu domicílio."),
 ("Alterações e contato", f"Podemos atualizar estes Termos; a data no topo indica a versão mais recente. Continuar usando o app após mudanças significa concordar com elas. Dúvidas: {M}. Veja também a <a href=\"../../privacy/dailyx/?lang=pt-BR\">Política de Privacidade</a>."),
],
"pt-PT": [
 ("Aceitação", f"Ao transferir ou utilizar o {APP}, publicado pela {DEV}, aceita estes Termos. Se não concordar, não utilize a aplicação."),
 ("O serviço", "O DailyX oferece desafios diários gratuitos, iguais para todos os jogadores em cada dia, suportados por publicidade. Funcionalidades, modos e desafios podem ser alterados, adicionados ou removidos ao longo do tempo."),
 ("Licença", "Concedemos-lhe uma licença pessoal, não exclusiva, intransmissível e revogável para utilizar a aplicação nos seus dispositivos, para fins não comerciais."),
 ("Utilização aceitável", "Compromete-se a não copiar, modificar, descompilar ou fazer engenharia inversa da aplicação, utilizar bots ou ferramentas automáticas, manipular resultados ou classificações, interferir com os anúncios ou utilizar a aplicação para fins ilícitos."),
 ("Serviços de terceiros", "A aplicação utiliza o Google Play, o Google Play Games e o Google AdMob, sujeitos a termos e políticas próprios. Não somos responsáveis por serviços de terceiros."),
 ("Propriedade intelectual", f"A aplicação, os desafios, o design, os textos, o logótipo e o nome {APP} pertencem à {DEV} ou aos seus licenciantes. Nada nestes Termos lhe transfere a propriedade."),
 ("Progresso e disponibilidade", "O progresso fica guardado no seu dispositivo e, se iniciar sessão, no Google Play Games. Não garantimos que a aplicação funcione sem interrupções ou erros, nem que sequências e progresso nunca se percam."),
 ("Exclusão de garantias", "A aplicação é fornecida “tal como está” e “conforme disponível”, sem garantias de qualquer tipo, na medida permitida por lei."),
 ("Limitação de responsabilidade", "Na medida permitida por lei, não somos responsáveis por danos indiretos, acidentais ou consequenciais resultantes da utilização da aplicação. Nada nestes Termos limita os direitos que a lei de defesa do consumidor lhe confere."),
 ("Cessação", "Pode deixar de utilizar a aplicação a qualquer momento, desinstalando-a. Podemos suspender ou terminar o acesso em caso de violação destes Termos."),
 ("Lei aplicável", "Estes Termos regem-se pela lei brasileira. Se for consumidor, mantém as proteções imperativas e o foro do seu país de residência."),
 ("Alterações e contacto", f"Podemos atualizar estes Termos; a data no topo indica a versão mais recente. Continuar a utilizar a aplicação após alterações significa aceitá-las. Dúvidas: {M}. Consulte também a <a href=\"../../privacy/dailyx/?lang=pt-PT\">Política de Privacidade</a>."),
],
"es": [
 ("Aceptación", f"Al descargar o usar {APP}, publicado por {DEV}, aceptas estos Términos. Si no estás de acuerdo, no uses la app."),
 ("El servicio", "DailyX ofrece desafíos diarios gratuitos, iguales para todos los jugadores cada día, financiados con publicidad. Las funciones, modos y desafíos pueden cambiar, añadirse o retirarse con el tiempo."),
 ("Licencia", "Te otorgamos una licencia personal, no exclusiva, intransferible y revocable para usar la app en tus dispositivos con fines no comerciales."),
 ("Uso aceptable", "Te comprometes a no copiar, modificar, descompilar ni aplicar ingeniería inversa a la app, usar bots o herramientas automatizadas, manipular resultados o clasificaciones, interferir con los anuncios ni usar la app con fines ilícitos."),
 ("Servicios de terceros", "La app utiliza Google Play, Google Play Games y Google AdMob, que se rigen por sus propios términos y políticas. No somos responsables de los servicios de terceros."),
 ("Propiedad intelectual", f"La app, sus desafíos, diseño, textos, logotipo y el nombre {APP} pertenecen a {DEV} o a sus licenciantes. Nada en estos Términos te transfiere su propiedad."),
 ("Progreso y disponibilidad", "El progreso se guarda en tu dispositivo y, si inicias sesión, en Google Play Games. No garantizamos que la app funcione sin interrupciones ni errores, ni que las rachas y el progreso nunca se pierdan."),
 ("Exención de garantías", "La app se ofrece “tal cual” y “según disponibilidad”, sin garantías de ningún tipo, en la medida permitida por la ley."),
 ("Limitación de responsabilidad", "En la medida permitida por la ley, no respondemos por daños indirectos, incidentales o consecuentes derivados del uso de la app. Nada en estos Términos limita los derechos irrenunciables que te otorga la legislación de consumo."),
 ("Terminación", "Puedes dejar de usar la app en cualquier momento desinstalándola. Podemos suspender o cancelar el acceso si se incumplen estos Términos."),
 ("Ley aplicable", "Estos Términos se rigen por las leyes de Brasil. Si eres consumidor, conservas las protecciones obligatorias y la jurisdicción de tu país de residencia."),
 ("Cambios y contacto", f"Podemos actualizar estos Términos; la fecha superior indica la versión más reciente. Seguir usando la app tras los cambios implica aceptarlos. Consultas: {M}. Consulta también la <a href=\"../../privacy/dailyx/?lang=es\">Política de Privacidad</a>."),
],
"fr": [
 ("Acceptation", f"En téléchargeant ou en utilisant {APP}, publié par {DEV}, vous acceptez les présentes Conditions. Si vous ne les acceptez pas, n'utilisez pas l'application."),
 ("Le service", "DailyX propose des défis quotidiens gratuits, identiques pour tous les joueurs chaque jour, financés par la publicité. Les fonctionnalités, modes et défis peuvent évoluer, être ajoutés ou retirés."),
 ("Licence", "Nous vous accordons une licence personnelle, non exclusive, non transférable et révocable pour utiliser l'application sur vos appareils à des fins non commerciales."),
 ("Utilisation acceptable", "Vous vous engagez à ne pas copier, modifier, décompiler ou désosser l'application, utiliser des robots ou outils automatisés, manipuler les résultats ou classements, perturber les annonces ou utiliser l'application à des fins illicites."),
 ("Services tiers", "L'application s'appuie sur Google Play, Google Play Jeux et Google AdMob, régis par leurs propres conditions et règles. Nous ne sommes pas responsables des services tiers."),
 ("Propriété intellectuelle", f"L'application, ses défis, son design, ses textes, son logo et le nom {APP} appartiennent à {DEV} ou à ses concédants. Les présentes Conditions ne vous en transfèrent pas la propriété."),
 ("Progression et disponibilité", "La progression est enregistrée sur votre appareil et, si vous vous connectez, dans Google Play Jeux. Nous ne garantissons pas un fonctionnement ininterrompu ou sans erreur, ni que les séries et la progression ne seront jamais perdues."),
 ("Exclusion de garanties", "L'application est fournie « en l'état » et « selon disponibilité », sans garantie d'aucune sorte, dans la mesure permise par la loi."),
 ("Limitation de responsabilité", "Dans la mesure permise par la loi, nous ne sommes pas responsables des dommages indirects, accessoires ou consécutifs liés à l'utilisation de l'application. Rien dans ces Conditions ne limite les droits impératifs que vous confère le droit de la consommation."),
 ("Résiliation", "Vous pouvez cesser d'utiliser l'application à tout moment en la désinstallant. Nous pouvons suspendre ou mettre fin à l'accès en cas de violation des présentes Conditions."),
 ("Droit applicable", "Les présentes Conditions sont régies par le droit brésilien. Si vous êtes consommateur, vous conservez les protections impératives et la juridiction de votre pays de résidence."),
 ("Modifications et contact", f"Nous pouvons mettre à jour ces Conditions ; la date en haut indique la dernière version. Continuer à utiliser l'application après une modification vaut acceptation. Questions : {M}. Voir aussi notre <a href=\"../../privacy/dailyx/?lang=fr\">Politique de confidentialité</a>."),
],
"de": [
 ("Zustimmung", f"Mit dem Herunterladen oder Nutzen von {APP}, veröffentlicht von {DEV}, stimmen Sie diesen Bedingungen zu. Wenn Sie nicht zustimmen, nutzen Sie die App nicht."),
 ("Der Dienst", "DailyX bietet kostenlose tägliche Rätsel, an jedem Tag für alle Spieler gleich, finanziert durch Werbung. Funktionen, Modi und Rätsel können sich mit der Zeit ändern, ergänzt oder entfernt werden."),
 ("Lizenz", "Wir gewähren Ihnen eine persönliche, nicht ausschließliche, nicht übertragbare und widerrufliche Lizenz zur Nutzung der App auf Ihren Geräten für nicht kommerzielle Zwecke."),
 ("Zulässige Nutzung", "Sie verpflichten sich, die App nicht zu kopieren, zu verändern, zu dekompilieren oder zurückzuentwickeln, keine Bots oder automatisierten Tools zu verwenden, keine Ergebnisse oder Ranglisten zu manipulieren, die Anzeigen nicht zu stören und die App nicht rechtswidrig zu nutzen."),
 ("Dienste Dritter", "Die App nutzt Google Play, Google Play Spiele und Google AdMob, für die eigene Bedingungen und Richtlinien gelten. Für Dienste Dritter übernehmen wir keine Verantwortung."),
 ("Geistiges Eigentum", f"Die App, ihre Rätsel, das Design, die Texte, das Logo und der Name {APP} gehören {DEV} oder ihren Lizenzgebern. Diese Bedingungen übertragen Ihnen kein Eigentum daran."),
 ("Fortschritt und Verfügbarkeit", "Der Fortschritt wird auf Ihrem Gerät und, wenn Sie sich anmelden, in Google Play Spiele gespeichert. Wir garantieren weder einen unterbrechungs- oder fehlerfreien Betrieb noch, dass Serien und Fortschritt nie verloren gehen."),
 ("Gewährleistungsausschluss", "Die App wird, soweit gesetzlich zulässig, „wie besehen“ und „wie verfügbar“ ohne jegliche Gewährleistung bereitgestellt."),
 ("Haftungsbeschränkung", "Soweit gesetzlich zulässig, haften wir nicht für indirekte, zufällige oder Folgeschäden aus der Nutzung der App. Zwingende Verbraucherrechte, insbesondere die Haftung für Vorsatz und grobe Fahrlässigkeit, bleiben unberührt."),
 ("Beendigung", "Sie können die Nutzung jederzeit durch Deinstallation beenden. Bei Verstößen gegen diese Bedingungen können wir den Zugang sperren oder beenden."),
 ("Anwendbares Recht", "Diese Bedingungen unterliegen brasilianischem Recht. Als Verbraucher behalten Sie die zwingenden Schutzvorschriften und den Gerichtsstand Ihres Wohnsitzlandes."),
 ("Änderungen und Kontakt", f"Wir können diese Bedingungen aktualisieren; das Datum oben zeigt die aktuelle Fassung. Die weitere Nutzung nach Änderungen gilt als Zustimmung. Fragen: {M}. Siehe auch unsere <a href=\"../../privacy/dailyx/?lang=de\">Datenschutzerklärung</a>."),
],
"it": [
 ("Accettazione", f"Scaricando o usando {APP}, pubblicato da {DEV}, accetti i presenti Termini. Se non li accetti, non usare l'app."),
 ("Il servizio", "DailyX offre sfide quotidiane gratuite, uguali per tutti i giocatori ogni giorno, sostenute dalla pubblicità. Funzioni, modalità e sfide possono cambiare, essere aggiunte o rimosse nel tempo."),
 ("Licenza", "Ti concediamo una licenza personale, non esclusiva, non trasferibile e revocabile per usare l'app sui tuoi dispositivi per scopi non commerciali."),
 ("Uso consentito", "Ti impegni a non copiare, modificare, decompilare o decodificare l'app, non usare bot o strumenti automatici, non manipolare risultati o classifiche, non interferire con gli annunci e non usare l'app per scopi illeciti."),
 ("Servizi di terze parti", "L'app si basa su Google Play, Google Play Giochi e Google AdMob, regolati da termini e norme propri. Non siamo responsabili dei servizi di terze parti."),
 ("Proprietà intellettuale", f"L'app, le sfide, il design, i testi, il logo e il nome {APP} appartengono a {DEV} o ai suoi licenzianti. Questi Termini non ti trasferiscono alcuna proprietà."),
 ("Progressi e disponibilità", "I progressi sono salvati sul tuo dispositivo e, se accedi, in Google Play Giochi. Non garantiamo che l'app funzioni senza interruzioni o errori, né che serie e progressi non vadano mai persi."),
 ("Esclusione di garanzie", "L'app è fornita “così com'è” e “come disponibile”, senza garanzie di alcun tipo, nei limiti consentiti dalla legge."),
 ("Limitazione di responsabilità", "Nei limiti consentiti dalla legge, non rispondiamo di danni indiretti, incidentali o consequenziali derivanti dall'uso dell'app. Nulla nei presenti Termini limita i diritti inderogabili che ti riconosce il Codice del consumo."),
 ("Cessazione", "Puoi smettere di usare l'app in qualsiasi momento disinstallandola. Possiamo sospendere o terminare l'accesso in caso di violazione dei presenti Termini."),
 ("Legge applicabile", "I presenti Termini sono regolati dalla legge brasiliana. Se sei un consumatore, mantieni le tutele inderogabili e il foro del tuo paese di residenza."),
 ("Modifiche e contatti", f"Possiamo aggiornare questi Termini; la data in alto indica la versione più recente. Continuare a usare l'app dopo le modifiche equivale ad accettarle. Domande: {M}. Vedi anche la nostra <a href=\"../../privacy/dailyx/?lang=it\">Informativa sulla privacy</a>."),
],
}

CSS = """
:root{--bg:#f7f7f5;--fg:#1d1d1f;--muted:#666;--card:#fff;--line:#e4e4e0;--accent:#5b4bdb}
@media (prefers-color-scheme:dark){:root{--bg:#121214;--fg:#ececee;--muted:#a0a0a6;--card:#1c1c20;--line:#2c2c32;--accent:#9d92ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:24px 16px 64px}
header{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:16px;margin-bottom:8px}
.brand{font-weight:700;letter-spacing:.04em}.brand span{color:var(--accent)}
select{font:inherit;padding:6px 10px;border-radius:8px;border:1px solid var(--line);background:var(--card);color:var(--fg)}
h1{font-size:1.7rem;line-height:1.25;margin:24px 0 4px}.date{color:var(--muted);margin:0 0 24px;font-size:.92rem}
h2{font-size:1.1rem;margin:28px 0 6px}p{margin:0 0 8px}a{color:var(--accent)}
section[lang]{display:none}section[lang].on{display:block}
footer{margin-top:40px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:.88rem}
"""

JS = """
(function(){var codes=%s;var sel=document.getElementById('lang');
function pick(){var q=new URLSearchParams(location.search).get('lang');if(q&&codes.indexOf(q)>=0)return q;
var nav=(navigator.languages||[navigator.language||'en']);for(var i=0;i<nav.length;i++){var l=nav[i];
if(codes.indexOf(l)>=0)return l;var b=l.split('-')[0];if(b==='pt')return l.toLowerCase()==='pt-pt'?'pt-PT':'pt-BR';
if(codes.indexOf(b)>=0)return b;}return 'en';}
function show(c){document.querySelectorAll('section[lang]').forEach(function(s){s.classList.toggle('on',s.getAttribute('lang')===c)});
document.documentElement.lang=c;sel.value=c;var t=document.querySelector('section[lang="'+c+'"] h1');if(t)document.title=t.textContent+' · DailyX';}
sel.addEventListener('change',function(){show(sel.value);var u=new URL(location);u.searchParams.set('lang',sel.value);history.replaceState(null,'',u);});
show(pick());})();
"""

def page(kind, data, title_idx):
    codes = [c for c, _ in LANGS]
    opts = "".join(f'<option value="{c}">{html.escape(n)}</option>' for c, n in LANGS)
    secs = []
    for c, _ in LANGS:
        t = UI[c][title_idx]
        body = "".join(f"<h2>{i}. {html.escape(h)}</h2><p>{p}</p>" for i, (h, p) in enumerate(data[c], 1))
        cls = ' class="on"' if c == "en" else ""
        secs.append(f'<section lang="{c}"{cls}><h1>{APP} — {html.escape(t)}</h1>'
                    f'<p class="date">{UI[c][2]}: {DATE[c]}</p>{body}</section>')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{APP} — {UI['en'][title_idx]}</title><meta name="robots" content="index,follow">
<style>{CSS}</style></head><body><main>
<header><div class="brand">FORGE<span>NINE</span> · {APP}</div>
<label>🌐 <select id="lang" aria-label="Language">{opts}</select></label></header>
{''.join(secs)}
<footer>© 2026 {DEV} · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</main><script>{JS % str(codes).replace("'", '"')}</script></body></html>
"""

out = os.path.dirname(os.path.abspath(__file__)) + "/forgenine-apps"
for kind, data, idx in (("privacy", PRIVACY, 0), ("policies", TERMS, 1)):
    d = f"{out}/{kind}/dailyx"; os.makedirs(d, exist_ok=True)
    open(f"{d}/index.html", "w", encoding="utf-8").write(page(kind, data, idx))

open(f"{out}/.nojekyll", "w").write("")
open(f"{out}/index.html", "w", encoding="utf-8").write(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Forgenine Apps</title><style>{CSS}</style></head>
<body><main><header><div class="brand">FORGE<span>NINE</span></div></header><h1>Forgenine Apps — Legal</h1>
<h2>DailyX</h2><p><a href="privacy/dailyx/">Privacy Policy</a> · <a href="policies/dailyx/">Terms of Use</a></p>
<footer>© 2026 {DEV} · <a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>
""")
open(f"{out}/README.md", "w", encoding="utf-8").write("""# forgenine-apps

Páginas legais dos apps Forgenine, publicadas via GitHub Pages.

| App | Privacidade | Termos de Uso |
|---|---|---|
| DailyX | `privacy/dailyx/` | `policies/dailyx/` |

Cada página tem 7 idiomas (en, pt-BR, pt-PT, es, fr, de, it). O idioma é escolhido pelo aparelho,
pelo seletor ou pelo parâmetro `?lang=` (ex.: `privacy/dailyx/?lang=pt-BR`).

Para editar os textos, altere `gen.py` e rode `python3 gen.py`.
""")
print("ok", out)
