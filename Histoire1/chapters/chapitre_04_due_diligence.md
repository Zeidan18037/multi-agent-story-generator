# Chapitre 4 — La Due Diligence

Six mois après le séminaire, NovaScale était rachetée. Évidemment.

Sentinel Equity Partners, un fonds américain qui collectionnait les start-ups
européennes comme d'autres collectionnent les timbres, avait signé un chèque
à six chiffres que Moreau avait passé les jours suivants à encadrer dans
tous les sens — sur LinkedIn, sur son tableau de bord _Blind_, et, disait-on,
sur le miroir de sa salle de bain, au cas où il oublierait en se brossant
les dents qu'il était désormais, officiellement, quelqu'un d'important.
De cette importance discrète qui ne nécessite ni talent ni travail, juste
le bon moment et la bonne dose de vide bien calibré. Formidable.

L'acquisition fermait dans six semaines. La due diligence commençait
maintenant.

David Goldstein arriva de New York un lundi matin, débarquant dans le hall
de NovaScale avec une valise Cabas et l'air de quelqu'un qui avait déjà
vu assez de start-ups françaises pour savoir que le café serait buvable mais
que la techno serait probablement une arnaque. Costume bleu sombre, montre
discrète qui valait plus que le salaire annuel du stagiaire. Il parlait vite,
souriait rarement, et prenait des notes dans un carnet qui n'était pas là
pour le style. Visiblement, cet homme était dangereux : il ne disait pas
« synergies ». Il disait « *what's the codebase look like* ». Il ne disait
pas « *value proposition* ». Il disait « *show me the revenue* ». Et surtout,
il ne disait jamais « AI-native », ce qui, dans le paysage tech de 2026,
était la marque indiscutable d'un être potentiellement surnaturel.

Moreau, bien sûr, lui avait présenté Marc comme « l'architecte de notre vision
NovaVerse — un programme stratégique ambitieux porté par une approche compound
AI ».

Goldstein avait regardé Marc. Pas son costume. Pas son titre. Pas sa plaque
au mur. Ses yeux.

— Parfait. Montrez-moi le repo.

Le silence qui suivit fut de ceux qui ne s'oublient pas. Pas le petit silence
gêné de celui qui cherche ses mots. Le silence de celui qui cherche quelque
chose qui n'a jamais existé. Un silence épais, lourd, acoustiquement
remarquable, qui traversa la pièce comme une onde de choc inversée.

— Le repo ? répéta Marc.

— Le *repository* GitHub de votre NovaVerse. L'architecture, les _deploys_,
la base de code. On doit auditer ça avant le *closing*.

Marc sentit sa bouche devenir sèche. Il y avait un repo, naturellement.
Celui de l'API legacy qu'il était supposé avoir transformée en plateforme
agentic-native. Le refactoring qu'il n'avait jamais fait. Le code dont il
avait parlé pendant des mois sans en écrire une ligne. Le premier endroit
où la réalité viendrait crever le bullshit, et il arrivait maintenant,
dans un costard à 600 euros, devant un Américain au carnet Moleskine.

— On a une architecture un peu particulière, commença-t-il, les mots
sortant tout seuls comme un automate qu'il n'avait pas éteint. Le NovaVerse
n'est pas un *repo* unique. C'est un *écosystème distribué*. Un *maillage*
de *microservices* qui —

— Envoyez-moi le *diagramme d'architecture* et le *schéma de données*,
coupa Goldstein sans lever les yeux. On commencera par là. J'ai ça dans
deux heures.

Il se leva, serra la main de Moreau, ignora celle de Marc, et sortit.
Pas de « merci ». Pas de « à tout à l'heure ». Juste un dos bleu sombre
qui disparut dans le couloir en laissant derrière lui un vide encore plus
grand que ceux que Marc avait l'habitude de produire.

Marc resta seul avec Moreau dans la salle de conférence vitrée.

— Il faut lui montrer quelque chose, dit Moreau.

— Je sais.

— Je veux dire *vraiment* quelque chose. Pas une slide. Il va vérifier.
Le genre de vérification qu'on ne peut pas noyer dans du jargon.

— Je sais.

— Alors démerde-toi.

Moreau sortit. Marc resta seul. Le néon au plafond bourdonnait. Dehors,
quelqu'un riait — sans doute quelqu'un qui n'avait pas encore compris que
son poste dépendait d'une architecture qui n'existait pas.

Marc marcha jusqu'au bureau d'Edwina.

Elle était là, casque sur les oreilles, en train de coder. Vraiment coder.
Pas faire des slides. Pas aligner des boîtes sur PowerPoint. Coder. Ce
geste que Marc n'avait pas posé depuis trois mois et dont ses doigts avaient
déjà oublié la grammaire.

— Edwina.

Elle continua à taper.

— Edwina. J'ai besoin de toi.

Elle enleva son casque, lentement, comme quelqu'un qui s'apprêtait à écouter
une très mauvaise nouvelle qu'elle avait vue arriver de très, très loin.

— Non.

— Je n'ai pas fini ma phrase.

— Si. Tu as fini. Tu as fini quand tu as enfilé ce costume et que tu as
commencé à parler du NovaVerse. Tu as fini quand tu m'as regardée dans
les yeux et que tu m'as dit que tu étais devenu un bullshiteur, comme si
c'était une promotion. Maintenant le bullshit rencontre le mur. Et tu
veux que je le décale pour toi. La réponse est non.

— Edwina. Si je ne montre rien à Goldstein, l'acquisition tombe. Tout le
monde perd son job. Toi comprise.

Elle se leva. Elle le regarda. Pas de colère. Pas de pitié. Juste le
calme de quelqu'un qui avait fait son deuil.

— Tu te souviens quand je t'ai dit « tu deviens eux » ? C'était pas une
insulte. C'était un diagnostic. Le problème, Marc, c'est que tu les as
tellement bien imités que tu en as aussi adopté la croyance : que ton
problème est le problème de tout le monde. Que ton urgence est l'urgence
collective. Que si tu tombes, on tombe tous. Mais c'est faux. C'est
toujours faux. *Tu* as construit ce château de cartes. *Tu* assumes.

Elle se rassit, remit son casque, et tourna son écran. La conversation
était finie.

Marc resta planté là une minute, puis deux, cherchant une réplique, un
argument, un mot. Il ne trouva rien. Il tourna les talons.

De retour dans son bureau, Marc fit quelque chose qu'il n'avait pas fait
depuis trois mois.

Il ouvrit Visual Studio Code.

L'interface lui parut étrangère. Les dossiers. Les fichiers. Les extensions.
Il avait oublié les racourcis clavier. Il tapa `git st` au lieu de
`git status`. Il essaya de lancer le serveur de dev — une erreur Node.js
qu'il ne comprit pas, une _stack trace_ qui lui parut plus absurde qu'un
slide de Delacourte. Il écrivit trois lignes, les effaça, les réécrivit,
les effaça encore.

Ses doigts ne répondaient plus. Les réflexes étaient morts. Les muscles
qui autrefois enchaînaient les _pull requests_ comme des gammes refusaient
de coopérer. Il était rouillé. Pire : il n'était plus développeur. Il
était quelqu'un qui avait oublié ce que c'était que de construire quelque
chose, et qui avait remplacé ce vide par des mots.

Il referma VS Code.

Il regarda par la fenêtre. Les bureaux vides. La plante verte qui agonisait.
Le néon DISRUPT qui clignotait — un clignement d'œil ironique de l'univers
qui semblait dire : *« On avait prévenu. »*

Il prit son téléphone. Il écrivit un mail. Pas à Goldstein. À lui-même,
d'abord, pour vérifier que les mots sonnaient juste.

*« Delambre Strategic Consulting — Partenaire de votre transformation. »*

Il relut. C'était parfait. C'était vide. C'était beau. Ça ne voulait rien
dire, et justement, ça pouvait tout vouloir dire. C'était le même vide que
Delacourte, le même vide que Delacourte avait vendu douze mille euros l'heure,
un an plus tôt, dans cette même entreprise. La boucle était bouclée.

---

Deux heures plus tard, Marc se tenait devant Goldstein dans la petite salle
de réunion vitrée.

— Alors, ce diagramme d'architecture ? demanda Goldstein sans lever les yeux
de son carnet.

Marc inspira.

— Il n'y a pas de diagramme d'architecture, David.

Goldstein leva les yeux.

— Comment ça ?

— Il n'y a pas d'architecture non plus. Ni de NovaVerse. Ni de couche
d'optimisation Q*. Ni de benchmark interne à 340 %. Il n'y a rien. J'ai
tout inventé.

Goldstein le regarda. Pas de surprise. Pas de colère. Une espèce de
fascination tranquille, comme un médecin qui entend un patient décrire
des symptômes qu'il a déjà vus cent fois.

— D'accord, dit-il. Merci pour l'honnêteté. L'acquisition se fera quand
même — on rachète la base clients, pas la techno. Mais vous êtes viré,
évidemment.

— Je ne suis pas viré, répondit Marc en sortant une carte de visite de
sa poche intérieure. Je démissionne.

Il posa la carte sur la table.

*Delambre Strategic Consulting*
*Marc Delambre — Founder & CEO*
*Transformation digitale, accompagnement stratégique, optimisation des processus*

Goldstein prit la carte. La retourna. La lut deux fois.

— Vous voulez devenir consultant, dit-il. C'est une blague ?

— Je veux devenir *votre* consultant. Vous rachetez NovaScale. Vous allez
passer six mois à intégrer une boîte dont vous ne comprenez ni la culture,
ni les process, ni les gens. Moi si. Je connais tout le monde. Je connais
les dossiers. Je connais les cadavres dans les placards. Vous me payez en
mission. Pas de salaire. Pas de charges. Pas de complication. Juste une
facture et du *deliverable*.

Goldstein ne rit pas. Il réfléchit.

— Vous êtes en train de me dire que vous avez passé six mois à bullshiter
votre propre boîte, et que maintenant vous voulez qu'on vous paie pour
bullshiter notre intégration ?

— Je vous propose de vous faire gagner du temps. Vous déciderez si c'est
du bullshit ou pas.

Goldstein le regarda longtemps. Puis il fit une chose que Marc n'avait
pas anticipée.

Il glissa la carte dans son carnet.

— Envoyez-moi une proposition. On verra.

---

Trois semaines plus tard, Marc Delambre s'installa dans un espace de
coworking loué à l'heure, rue du Faubourg Saint-Honoré. Le même quartier
que le séminaire. Le même type de salle. Le même frigo à bières. Le même
babyfoot délabré. Rien n'avait changé, sauf que la facture était maintenant
pour lui.

Son nouveau bureau était plus petit que l'ancien. Mais c'était le sien.
Pas de plaque vissée au mur. Pas de titre officiel. Rien que du vide,
bien emballé, avec une facture mensuelle et un numéro de TVA
intracommunautaire.

Il ouvrit son MacBook. Un mail trônait dans sa boîte : Goldstein.

« *Please send the strategic roadmap for the NovaScale integration
by Friday. Keep it high-level — board presentation.* »

Marc sourit.

Il ouvrit PowerPoint.

Il se remit au travail.
