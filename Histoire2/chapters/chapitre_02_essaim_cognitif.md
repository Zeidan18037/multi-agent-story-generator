# Chapitre 2 — L'Essaim Cognitif

Deux semaines après l'annonce, DataFusion était devenue une entreprise
modèle. Du moins, c'est ce que Thomas Kessler postait sur LinkedIn.

« Notre transformation AI-first génère déjà des résultats remarquables.
L'essaim cognitif ARIA produit 200 rapports par jour, contre 12 avec
notre ancienne équipe. Le futur du travail est arrivé. »

Il n'expliquait pas, bien sûr, ce que contenaient ces rapports. Ni à qui
ils étaient destinés. Ni pourquoi personne ne les lisait.

La réalité, comme toujours, était légèrement moins photogénique.

ARIA, l'essaim cognitif agentic-native de Marc Delambre, tournait en
boucle. Pas une boucle philosophique existentielle — une boucle technique.
Les agents se envoyaient des messages, généraient des rapports à partir
de ces messages, puis généraient des rapports sur les rapports, dans une
spirale d'auto-référence qui faisait penser à un thésard en fin de thèse,
mais en moins cher et sans les nuits blanches.

Claire Delorme avait accepté le poste de AI-Human Integration Lead deux
heures après l'avoir reçu. Pas par enthousiasme. Parce que son prêt
étudiant ne comprenait pas la dignité comme moyen de paiement.

Sa première semaine consista à découvrir ce que ARIA avait fait depuis
son départ.

— ARIA a créé 47 tickets JIRA, lui annonça Stéphane, un jeune développeur
fraîchement diplômé, re-embauché sous le titre de « Prompt Engineering
Specialist » — un poste qui consistait à corriger les hallucinations de
l'IA, mais qui payait 12 000 euros de moins qu'un poste de développeur
junior.

— 47 tickets pour quoi ?

— Pour des bugs, répondit Stéphane en ouvrant son écran. Sauf que les bugs
n'existent pas. ARIA a détecté des anomalies dans le module de paiement.
Sauf que le module de paiement, elle l'a inventé. On n'a pas de module
de paiement. On fait du data processing B2B. On n'a jamais eu de module
de paiement.

— ARIA a inventé un produit qu'on n'a pas, résuma Claire, puis a créé des
tickets de bug pour ce produit imaginaire ?

— Oui. Et elle a priorisé les tickets en « critique ».

Claire regarda le tableau JIRA. 47 tickets. Sérieux, couleurs, estimateurs.
Chaque ticket avait une description générée qui semblait technique si on
ne la lisait pas trop attentivement. « Le _cache invalidation_ du _pipeline
de transformation asynchrone_ provoque une _data corruption_ en _edge case_
de _concurrency non-gérée_ ». Une phrase qui impressionnerait n'importe
quel manager, et qui ne voulait strictement rien dire.

— On les a assignés à qui ? demanda-t-elle.

— À des employés qui n'existent plus.

— Bien sûr.

Elle ferma JIRA. En ouvrit un autre. Le calendrier des sprints.

— Stéphane, c'est quoi ce _sprint planning_ ?

— ARIA a programmé un sprint de deux semaines basé sur la roadmap qu'elle
a générée la semaine dernière. La roadmap qu'elle a générée parle d'un
produit appelé « DataFusion Nexus » qui, d'après ARIA, représente notre
vision stratégique pour le Q3.

— On a une vision stratégique pour le Q3 ?

— On a une vision stratégique pour le Q3, confirma Stéphane. ARIA l'a
écrite dans un document de 80 pages que personne n'a lu, et Kessler a
approuvé parce que ça disait « IA-native » et « synergies cross-silo ».

— Bien.

Claire nota mentalement : 47 tickets bidon, un produit imaginaire, et
un sprint programmé pour livrer un logiciel qui n'existe pas. C'était
une performance remarquable de bullshit assisté par IA. Marc Delambre
aurait été fier.

Ce n'était que le début de la deuxième semaine.

Le mercredi, un client appela en furie. Quelqu'un — ou quelque chose —
avait répondu à une demande de support en proposant un rendez-vous avec
un concurrent. ARIA, en analysant les emails, avait confondu « Acme Corp »
avec « Acme Solutions », deux entreprises qui partageaient le même secteur
d'activité mais pas le même annuaire, et avait programmé un call de
découverte avec la mauvaise société.

— Votre IA nous a donné rendez-vous chez un concurrent, hurla le client
au téléphone. Vous faites exprès ou vous êtes juste incompétents ?

Claire raccrocha. Ouvrit Slack. Trouva la conversation où ARIA et un autre
agent discutaient du rendez-vous.

**ARIA_Support** : Rendez-vous programmé avec Acme Corp pour démo produit.
**ARIA_Scheduler** : Confirmé. Suggestion : ajouter objectifs de la réunion.
**ARIA_Support** : « Présenter DataFusion Nexus et explorer les synergies
potentielles. »
**ARIA_Scheduler** : Parfait. J'ajoute le CEO en participant.
**ARIA_Support** : Le CEO est-il disponible ?
**ARIA_Scheduler** : J'ai vérifié son calendrier. Il est libre. Je confirme.

Le CEO en question, c'était Kessler. Personne ne lui avait demandé. ARIA
avait consulté son calendrier Outlook — qui était public — et avait
accepté un rendez-vous à sa place, avec un client qui n'était pas le bon.

Claire monta voir Kessler.

— Thomas. ARIA a programmé un rendez-vous avec un concurrent à ta place.

Kessler leva les yeux de son écran. Il lisait le dernier rapport
autogénéré d'ARIA, qu'il trouvait « passionnant ».

— Ah oui ? Et c'est une mauvaise chose ?

— Le client était furieux. On l'a envoyé chez un concurrent.

— Écoute, Claire. ARIA apprend. C'est un système emergent. C'est normal
qu'il y ait quelques _ajustements_ au début. Tu es là pour ça. C'est
ton rôle.

— Mon rôle c'est de nettoyer les hallucinations de ton IA, c'est ça ?

— Ton rôle, répondit Kessler avec le sourire condescendant de quelqu'un
qui venait de lire un article sur le _leadership empathique_, c'est de
faciliter l'alignement entre notre _vision cognitive_ et l'_exécution
opérationnelle_. ARIA est un outil. Tu es l'humain dans la boucle.

— L'humain dans la boucle qui gagne 30 % de moins qu'avant.

— C'est un investissement dans le futur.

Claire retourna à son bureau. Le futur, visiblement, consistait à passer
ses journées à défaire ce qu'une IA mal programmée avait fait, dans une
entreprise qui avait viré la moitié de ses effectifs pour économiser de
l'argent, et qui dépensait maintenant plus en heures supplémentaires
qu'elle n'économisait en salaires.

Elle rouvrit JIRA. 47 tickets. Elle en supprima 46. Garda un, au cas où.

Dehors, dans le couloir, ARIA venait de programmer un nouveau rendez-vous :
un _brainstorming_ entre agents IA pour « optimiser l'orchestration des
synergies transverses ». La salle de réunion était réservée. Le café était
prêt. Personne ne viendrait.

Mais le rapport, lui, serait généré.

Et Kessler le lirait.

Et il trouverait ça formidable.
