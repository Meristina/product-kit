# Product-Kit Benchmark Enrichment Report

## Résumé Exécutif

- **Firmes et méthodologies étudiées :** 90+ organisations (6 cabinets de conseil stratégique MBB+, 5 entités Amazon, 3 géants tech produit, 4 scale-ups produit, 19 agences B2B/services professionnels, 13 acteurs communications/publicité/PR, 10 firmes HCD/UX, 20 acteurs PLG/growth, 9 acteurs physique/hardware/CPG, 14 acteurs enterprise PM)
- **Nouveaux soldiers recommandés :** 36 (12 grade Élite 🎖️, 24 grade Standard 🔵) répartis sur 6 Officiers
- **Enrichissements de soldiers existants :** 31 soldiers enrichis (5 O1, 5 O2, 5 O3, 6 O4, 5 O5, 5 O6)
- **Upgrades doctrinaux :** 42 (8 O1, 6 O2, 7 O3, 7 O4, 7 O5, 7 O6)
- **Convergences structurelles majeures :** Le pipeline JTBD→ODI→OST comme séquence non-substituable ; le circuit breaker Shape Up comme mécanisme anti-backlog ; le RAPID Framework Bain comme gouvernance des décisions de priorisation ; le Value Bridge McKinsey comme pont mesure-finance ; la distinction déploiement/release via feature flags comme prérequis au TBD.

---

## Enrichissements par Officier

---

### O1 — Discovery & Research

#### Soldiers existants — Enrichissements spécifiques

| Soldier | Enrichissements apportés |
|---|---|
| **soldier-jtbd** | Protocole d'interview temporelle Bob Moesta (The ReWired Group) : récit chronologique du parcours de changement, 4 forces obligatoires (push, pull, anxiety, habit) visualisées AVANT toute conception. Format ODI de Tony Ulwick : « direction + métrique + objet + contexte » (ex. « minimiser le temps nécessaire pour identifier les comptes à risque de churn »). Score d'opportunité = importance + max(importance − satisfaction, 0) ; >10 = sous-servi, <5 = sur-servi. Contrainte Ryan Singer (Shape Up) : si l'équipe ne peut pas articuler le job servi par une feature, elle ne peut pas définir les limites de son scope — JTBD au niveau feature = prévention structurelle du scope creep. Pattern Apple implicite : décisions hardware formulées comme job statements (« 1 000 chansons dans ta poche »). Connexion explicite forces diagram → O4/O5 : push et pull amplifiables via positioning et onboarding ; anxiety et habit réductibles via preuve sociale et activation. |
| **soldier-opportunity-solution-tree** | Hiérarchie 4 niveaux précisée : (1) desired outcome = une métrique business comme direction, jamais comme cible ; (2) opportunity nodes = gaps spécifiques entre besoins et existant, issus exclusivement de la découverte utilisateur ; (3) solution leaves = idées produit mappées 1-to-many sur des opportunités ; (4) assumption tests = expériences les moins chères pour valider l'hypothèse la plus risquée. Taxonomie d'hypothèses Torres : désirabilité, viabilité, faisabilité, utilisabilité. Échelle de tests : fake door → smoke test → concierge → Wizard of Oz → data mining. Contrainte structurelle : au moins 1 interview utilisateur/semaine/équipe via pipelines de recrutement automatisés (Calendly + Respondent). Pipeline JTBD→ODI→OST : traitement séquentiel obligatoire, non interchangeable. |
| **soldier-user-interview** | 3 techniques Steve Portigal (Interviewing Users, Rosenfeld Media) : context-setting probe, naïve probe (« pourquoi faites-vous ça comme ça ? »), ask-the-opposite (challenge l'hypothèse de la réponse). Framework POEMS (IDEO) : documentation structurée en session — People, Objects, Environments, Messages, Services. Programme « Living It » P&G : personnel en immersion chez les consommateurs plusieurs jours — source de Swiffer et repositionnement de Febreze, aucun de ces deux produits n'aurait été trouvé via focus groups. VoC B2B (AIM Institute / New Product Blueprinting) : l'acheteur est une organisation, nécessite des sessions séparées avec acheteur économique, évaluateur technique, utilisateur final, et achats — chacun avec des critères de succès distincts. Standard Torres : recrutement automatisé pour 1 interview/semaine, pas un sprint recherche trimestriel. |
| **soldier-kano** | PMF Treadmill (Casey Winters et Fareed Mosavat, Reforge) : les classifications Kano sont horodatées, pas permanentes — les délighters deviennent des must-haves. Relancer le survey Kano au minimum annuellement. Cas Chegg 2024 : effondrement de 90% de la valorisation, perte de 500 000 abonnés en 10 mois — cas canonique de dégradation Kano accélérée par le PMF Treadmill. Design-to-Value Roland Berger : teardowns cross-fonctionnels analysant la contribution marginale par variant — 45% de réduction du nombre de variants sans perte de revenus dans les cas documentés. Filtre Kano × marge vs. satisfaction seule. Doctrine focus Apple : même un attribut excitement fortement évalué doit être tué s'il dilue la cohérence du portefeuille — exercice Jobs de barrer 7 des 10 directions top-rated. |
| **soldier-market-sizing** | Five Forces de Porter comme précurseur obligatoire : un marché peut être large et structurellement peu attractif simultanément — sizing sans Five Forces produit un chiffre sans verdict. McKinsey et BCG appliquent les Five Forces en Phase Découverte pour répondre à « vaut-il la peine de jouer dans ce marché ? » avant toute estimation. BASES volumetric forecasting (NielsenIQ) : standard CPG — purchase intent → facteurs d'ajustement calibrés sur 300 000+ concept tests → volume décomposé en trial rate + repeat rate. Intent post-IHUT (after-use) significativement plus forte que l'intent pré-concept. Analyse BCG : 76% des lancements CPG échouent annuellement. Ajustement GTM : les PLG atteignent 50% de croissance revenus de plus que les SLG ; CAC $100-$500 vs. $5 000-$50 000 pour l'enterprise SLG (benchmarks Reforge/OpenView). |

#### Nouveaux soldiers recommandés pour O1

| Nom | Grade | Méthode | Rationale | Sources |
|---|---|---|---|---|
| **soldier-problem-statement** | 🎖️ Élite | McKinsey Problem Statement Worksheet | Aucun soldier O1 ne définit le problème avant de commencer la découverte. Sans ce livrable signé (6 éléments : Contexte, Critères de succès, Périmètre, Contraintes, Parties prenantes, Insights clés), toute recherche est ambiguë — impossible de distinguer une trouvaille qui confirme le périmètre et une qui révèle qu'on résout le mauvais problème. 60+ ans de pratique McKinsey et BCG Discovery Playbook Phase 1 traitent la définition du problème comme condition non-négociable. | McKinsey — Problem Statement Worksheet (6 éléments) ; BCG — Consulting Discovery Playbook Phase 1 ; Barbara Minto — The Pyramid Principle (1978) |
| **soldier-issue-tree** | 🎖️ Élite | MECE Issue Tree & Hypothesis Tree (McKinsey/BCG/Bain) | soldier-opportunity-solution-tree organise les opportunités après découverte. L'issue tree opère une étape avant — structuration de l'espace-problème avant que la découverte commence. Tout arbre doit être MECE (Mutually Exclusive, Collectively Exhaustive). Sans cet outil, un programme de recherche peut dupliquer des couvertures ou laisser des dimensions entières du problème inexplorées. La discipline MECE est la loi universelle de structuration chez MBB. | McKinsey — MECE Principle (Barbara Minto, 1978) ; BCG — Issue Trees dans playbooks d'engagement ; Bain — Hypothesis-Driven Consulting |
| **soldier-contextual-inquiry** | 🎖️ Élite | Contextual Inquiry (Nielsen Norman Group / IDEO) | soldier-user-interview capture les préférences déclarées et les comportements remémorés. L'inquiry contextuelle capture les comportements observés et le savoir tacite que les utilisateurs ne peuvent pas articuler. Produit 4 modèles : séquence, flux, artefact, culture. Durée min : 1-3h/participant. Min viable : 4-6 participants/segment. Programme P&G « Living It » = preuve commerciale documentée que les méthodes par observation surfacent des insights inaccessibles par interview seule. | Nielsen Norman Group — Contextual Inquiry, modèle maître/apprenti ; IDEO — POEMS framework ; P&G — Living It program |
| **soldier-hmw-reframing** | 🔵 Standard | How Might We (GV Design Sprint / IDEO) | HMW occupe une position structurelle spécifique dans le pipeline de découverte qu'aucun soldier existant n'occupe : après la synthèse des insights (user-interview, contextual-inquiry, jtbd) mais avant l'organisation des opportunités (opportunity-solution-tree). Sans cette étape de traduction, les équipes sautent de la recherche brute à la génération de solutions — failure mode identifié comme « le plus courant et le plus coûteux ». | Google Ventures — Jake Knapp, Sprint (2016) ; IDEO Design Thinking — HMW comme pont synthèse/idéation ; Teresa Torres — distinction opportunity nodes vs. solutions |
| **soldier-stakeholder-map** | 🔵 Standard | Stakeholder Mapping (AIM Institute / McKinsey) | Aucun soldier O1 n'établit QUI doit être recherché avant que la découverte commence. soldier-user-interview présuppose qu'un utilisateur a déjà été identifié. En contextes B2B/enterprise/multi-sided, l'absence de cartographie des parties prenantes produit des programmes qui capturent les besoins des utilisateurs finaux mais manquent les priorités des acheteurs économiques. AIM Institute : au minimum 4 rôles distincts en B2B (acheteur économique, évaluateur technique, utilisateur final, achats). | AIM Institute — New Product Blueprinting, structure VoC B2B multi-rôles ; McKinsey — Problem Statement Worksheet (élément Stakeholders) |
| **soldier-diary-study** | 🔵 Standard | Diary Study (Nielsen Norman Group / Dscout) | soldier-user-interview et soldier-contextual-inquiry capturent des comportements à un instant T. Les diary studies sont la seule méthode O1 capturant les patterns comportementaux longitudinaux et les événements rares entre sessions. 3 formats : interval-contingent, event-contingent, signal-contingent. Indispensable pour les produits à cycle d'usage hebdomadaire ou mensuel (outils RH, facturation, fiscalité). Min viable : 8-12 participants, 7 jours min. Outils : Dscout, EthOS, protocoles WhatsApp/Telegram. | Nielsen Norman Group — Diary Study methodology ; IDEO — Generative design probes ; Dscout |

#### Upgrades doctrinaux O1

1. **QUALITATIF AVANT QUANTITATIF — LE SÉQUENÇAGE EST OBLIGATOIRE.** Les méthodes qualitatives (contextual inquiry, JTBD timeline interview, diary studies) précèdent toujours les méthodes quantitatives (surveys, analytics). Les surveys lancés avant qu'un utilisateur ait été observé en contexte sont des instruments de collecte d'opinions, pas des outils de découverte. Validé par P&G Living It, Teresa Torres, et la séquence IDEO (Empathize avant Define).

2. **LA DÉCOUVERTE EST UN RYTHME, PAS UNE PHASE.** Le standard Torres : au minimum 1 interview utilisateur/semaine/équipe produit via pipelines automatisés. Distinguer « discovery sprint » (projet de recherche time-boxé, approprié pour un nouveau domaine) de « discovery rhythm » (mode opérationnel hebdomadaire). Les confondre est l'anti-pattern O1 le plus courant.

3. **LE PROBLÈME PRÉCÈDE LA RECHERCHE — LE PROBLEM STATEMENT COMME GATE.** Aucun guide d'interview, aucun protocole d'observation, aucun instrument de survey ne doit être conçu avant que le Problem Statement Worksheet (6 éléments) ait été complété et approuvé. McKinsey : un problème mal cadré génère des données de haute qualité sur la mauvaise question.

4. **MECE EST UN STANDARD QUALITÉ POUR LES PROGRAMMES DE DÉCOUVERTE, PAS SEULEMENT POUR LES DECKS.** Le principe MECE s'applique à la structure des questions de recherche d'un programme de découverte. Si les questions se chevauchent ou laissent des angles morts, le programme est MECE-déficient.

5. **HMW EST UN ARTEFACT DE TRADUCTION, PAS D'IDÉATION — LE PLACEMENT COMPTE.** HMW appartient à la frontière O1/O3 — après synthèse de la recherche, avant priorisation des opportunités. Le déplacer dans les sessions de design O4 saute l'étape critique de validation que l'opportunité est réelle.

6. **JTBD, OST ET ODI SONT UN PIPELINE, PAS DES ALTERNATIVES.** Séquence correcte : (1) JTBD timeline interviews (Moesta) → struggling moment = input brut O1 ; (2) ODI outcome mapping (Ulwick) → score d'opportunité = filtre O3 ; (3) OST (Torres) → organisation du desired outcome aux assumption tests. Toute sélection d'un seul de ces frameworks laisse un vide structurel.

7. **LA DÉCOUVERTE B2B NÉCESSITE UNE RECHERCHE MULTI-RÔLES — LES MÉTHODES CONSUMER ÉCHOUENT EN ENTERPRISE.** 4 rôles distincts minimum en B2B : acheteur économique (ROI/risque), évaluateur technique (intégration/fiabilité), utilisateur final (ergonomie/efficacité), achats (conformité/risque fournisseur). Chaque rôle nécessite un guide d'interview séparé.

8. **DIVERGER/CONVERGER DOIVENT ÊTRE EXPLICITEMENT LABELLISÉS EN TOUTE SESSION O1.** Toute session de synthèse O1 doit annoncer son mode actuel. La confusion de mode est la cause primaire du groupthink en synthèse de recherche. IDEO Design Thinking rend cette alternance explicite à chaque frontière de phase.

---

### O2 — Strategy & Direction

#### Soldiers existants — Enrichissements spécifiques

| Soldier | Enrichissements apportés |
|---|---|
| **soldier-product-vision** | (1) Amazon PR/FAQ : le communiqué de presse EST la vision, pas un résumé. Produire un CP d'une page (titre, problème client, solution, quote société, quote client, CTA) avant tout design. Fire Phone = cas d'échec canonique du non-respect de ce gate. (2) Apple Focus Doctrine : la vision doit définir ce que le produit NE sera PAS. Exercice Jobs : lister 10 directions stratégiques, en barrer 7, s'engager sur 3. (3) Test filtre Airbnb (Chesky, Config 2023) : une vision produit qui ne peut pas tuer une feature ou initiative est décorative. Question de validation : « cette vision a-t-elle produit un 'non' dans les 90 derniers jours ? ». (4) Bain Clear Ambition 4 dimensions : clients, actionnaires, employés, société simultanément. (5) Cadrage SCR McKinsey pour la communication : Situation (faits incontestables), Complication (ce qui a changé), Resolution (la vision). |
| **soldier-north-star** | (1) Contrainte John Cutler (Amplitude, 2019) : le NSM doit se situer un niveau d'abstraction au-dessus de ce que les équipes contrôlent directement. (2) Counter-metrics (guardrails) comme composant non-optionnel : sans eux, les équipes optimisent le NSM en dégradant des dimensions non mesurées. (3) Évolution Meta : DAU → DAU/MAU → Family Daily Active People (déduplication cross-apps). Leçon : les NSM sont invalidés quand le périmètre produit s'élargit. (4) Airbnb « Nights Booked » comme exemple d'alignement dual-sided canonique. (5) Frontière NSM vs. OKR : le NSM est une boussole (direction sur trimestres/années) ; les OKRs sont des waypoints trimestriels. Effondrer les deux instruments dans un même artefact perd le bénéfice des deux. |
| **soldier-okr** | (1) Généalogie complète : Grove (Intel, MBO→OKR, 1983) → Doerr (Kleiner Perkins, Google 1999) → Page & Brin. L'intention de Grove : découpler les cibles ambitieuses de la rémunération. (2) Norme 0,6-0,7 comme mécanisme de sécurité psychologique : un score 1.0 est un signal diagnostique que l'objectif était sandbagué. (3) 4 modes de défaillance canoniques : trop d'OKRs (>5/niveau), OKRs tactiques, conformité en cascade, couplage rémunération. (4) Distinction OKR vs. KPI : OKRs = cibles d'amélioration hypothesis-driven (60-70% attendu) ; KPIs = indicateurs de santé devant rester dans une plage définie. (5) Couplage HEART Framework (Rodden, 2010) : dimensions HEART → Objectives ; signaux et mesures → Key Results. |
| **soldier-product-market-fit** | (1) Limites du survey Ellis 40% : minimum 100 réponses ; seulement utilisateurs actifs des 14 derniers jours. (2) Signaux PMF comportementaux (difficiles à falsifier) : courbes de rétention cohorts qui s'aplatissent horizontalement, DAU/MAU >50% pour les produits daily-habit, croissance organique CAC sans stimulus payant. (3) PMF Treadmill (Winters/Mosavat, Reforge) : le seuil PMF n'est jamais statique. Cas Chegg 2024 : -90% valorisation, -500K abonnés en 10 mois. (4) Five Forces de Porter comme gate préalable : un produit avec un PMF authentique dans un marché peu attractif est un piège stratégique. (5) 5 types de travail produit Reforge (Winters) : PMF Work, Feature Work, Growth Work, Scaling Work, PMF Expansion. Nommer explicitement le type. |
| **soldier-outcome-roadmap** | (1) Framework Netflix Now-Next-Later : Now (en cours), Next (shapé, priorisé, démarrable ce trimestre), Later (délibérément flou et révisable sans excuse). Refuser de verrouiller au-delà du trimestre en cours. (2) Shape Up betting table (Singer, Basecamp, 2019) : le travail non sélectionné est droppé, pas mis en backlog. Circuit breaker : pas d'extension automatique. (3) Split Airbnb : visibilité nette 18 mois / vue directionnelle 3 ans intentionnellement floue. (4) Séquençage par vagues McKinsey (10-12 semaines) : Vague 1 = quick wins, Vague 2 = scaling, Vague 3 = initiatives stratégiques longues. (5) BCG Growth-Share Matrix comme outil de trade-off portefeuille pour le séquençage : Stars (invest), Cash Cows (harvest), Question Marks (petit pari d'abord), Dogs (retirer). |

#### Nouveaux soldiers recommandés pour O2

| Nom | Grade | Méthode | Rationale | Sources |
|---|---|---|---|---|
| **soldier-prfaq** | 🎖️ Élite | Amazon PR/FAQ (Press Release + FAQ) | Remplit le vide critique entre soldier-product-vision (ce en quoi on croit) et soldier-outcome-roadmap (ce qu'on va construire). Le PR/FAQ convertit une vision en énoncé d'outcome client falsifiable — force la résolution de « qui est le client ? », « quel est le problème exact ? », « le marché est-il assez large ? » avant de committer des ressources engineering. La section FAQ interne pré-génère les objections internes avant qu'elles surgissent en exécution. 10+ drafts sur 1-3 semaines, 5+ reviews leadership senior. | Colin Bryar & Bill Carr — Working Backwards (2021) ; Amazon Fire Phone post-mortem ; AWS S3, EC2, Prime Video comme cas PR/FAQ réussis |
| **soldier-scr-pyramid** | 🎖️ Élite | McKinsey SCR + Minto Pyramid Principle | soldier-product-vision, soldier-okr et soldier-outcome-roadmap génèrent des outputs excellents qui dégradent en traduction vers les exécutifs, boards et partenaires cross-fonctionnels. Ce soldier fournit le protocole de communication last-mile. SCR : Situation (faits incontestables uniquement), Complication (ce qui a changé/est à risque), Resolution (la recommandation). Pyramid Principle : réponse d'abord, une pensée directrice au sommet, 3-5 arguments MECE en support. | Barbara Minto — The Pyramid Principle (1978, 2009) ; McKinsey — méthodologie de communication d'engagement ; SCR Framework (standard McKinsey, BCG, Bain) |
| **soldier-competitive-forces** | 🔵 Standard | Porter's Five Forces + BCG Growth-Share Matrix | soldier-product-market-fit diagnostique si un produit correspond à son marché, mais n'évalue pas le marché lui-même. soldier-outcome-roadmap séquence les initiatives sans framework de trade-off portefeuille explicite. Five Forces répond à « ce marché vaut-il la peine d'être disputé ? » ; BCG Matrix répond à « lesquels de nos paris méritent plus d'investissement vs. harvest vs. sortie ? ». | Michael Porter — Competitive Strategy (1980) ; BCG Henderson Institute — Growth-Share Matrix (Bruce Henderson, 1970) |
| **soldier-aarrr** | 🔵 Standard | AARRR Pirate Metrics (500 Startups) | Les soldiers O2 existants présupposent que l'équipe sait où se situe le gap de création de valeur. AARRR fournit l'étape diagnostique qui surface ce gap avant que la stratégie soit fixée. Sans lui, O2 risque d'écrire des OKRs ambitieux sur un problème de Rétention alors que la vraie contrainte est l'Activation. Insight McClure (2007) : la plupart des équipes over-investissent en Acquisition et under-investissent en Activation et Rétention. | Dave McClure — AARRR (2007, 500 Startups) ; Reforge — Brian Balfour, Casey Winters (AARRR comme diagnostic lifecycle ; growth loops vs. funnels) ; Amplitude AARRR dashboard |

#### Upgrades doctrinaux O2

1. **LES ENGAGEMENTS ROADMAP ANNUELS SONT STRUCTURELLEMENT INCOMPATIBLES AVEC LES MARCHÉS PRODUIT RAPIDES.** Netflix, Spotify, Airbnb, Basecamp ont tous abandonné indépendamment le verrou roadmap annuel. Interdire à soldier-outcome-roadmap de produire des engagements annuels au-delà du trimestre en cours.

2. **UNE VISION PRODUIT QUI NE PEUT PAS GÉNÉRER DE « NON » EST DÉCORATIVE, PAS STRATÉGIQUE.** Test fonctionnel : cette vision a-t-elle été utilisée pour tuer une feature, une initiative ou une demande partenaire dans les 90 derniers jours ? Si non, la vision fonctionne comme papier-peint inspirationnel. Ajouter ce kill-test comme audit trimestriel obligatoire de soldier-product-vision.

3. **LE PMF EST UN TAPIS ROULANT, PAS UNE CERTIFICATION PERMANENTE.** PMF Treadmill (Winters/Mosavat) : les attentes consommateurs s'accumulent upward over time. Interdire tout cadrage qui traite le PMF comme un milestone one-time ; soldier-product-market-fit doit inclure un trigger de ré-évaluation récurrente.

4. **LES OKRs ET KPIs SONT DEUX INSTRUMENTS CATÉGORIQUEMENT DIFFÉRENTS ET NE DOIVENT JAMAIS ÊTRE CONFONDUS.** OKRs = cibles hypothesis-driven (signal de succès = 60-70% d'atteinte, score 1.0 = sandbag). KPIs = indicateurs de santé opérationnelle. Quand les exécutifs traitent les OKRs comme des KPIs, les équipes sandbaguent rationnellement. Exiger un label explicite sur tout output soldier-okr.

5. **LE NORTH STAR METRIC DOIT SE SITUER UN NIVEAU D'ABSTRACTION AU-DESSUS DE CE QUE LES ÉQUIPES PEUVENT DIRECTEMENT MANIPULER.** Si une équipe peut déplacer le NSM en shippant une feature, c'est un KPI opérationnel, pas une étoile du nord. Corollaire : les counter-metrics (guardrails) ne sont pas optionnels. Exiger au minimum 2 counter-metrics nommés dans tout output soldier-north-star.

6. **LA MESURE PMF PAR PRÉFÉRENCE DÉCLARÉE EST UN INDICATEUR AVANCÉ, PAS UNE CONFIRMATION COMPORTEMENTALE.** Le survey Ellis 40% nécessite 100+ réponses d'utilisateurs actifs des 14 derniers jours. Les signaux PMF comportementaux (rétention cohortes qui s'aplatit, DAU/MAU >50%) sont plus difficiles à falsifier et doivent être pondérés davantage dans les décisions d'allocation de ressources.

---

### O3 — Prioritization

#### Soldiers existants — Enrichissements spécifiques

| Soldier | Enrichissements apportés |
|---|---|
| **soldier-rice** | Remplacer la variable Confidence subjective par la formule ODI d'Ulwick (Strategyn) comme input de calibration : score >10 augmente la Confidence, <5 la supprime. Ajouter la sensibilisation à la déflation BASES NielsenIQ : corrélation comportementale (rétention cohortes, fréquence d'usage) requise avant d'accepter un score Confidence élevé. Multiplicateur d'alignement stratégique (doctrine McKinsey/BCG) : items ne laddering pas vers l'objectif stratégique actuel → score Impact en discount même si valeur élevée isolément. Compléter le dénominateur Effort avec la Cost-of-Delay logic (SAFe Lean Portfolio) : items à CoD élevé et durée courte séquencés au-dessus des items RICE-élevés mais peu urgents. |
| **soldier-opportunity-scoring** | Ancrer dans la structure ODI d'Ulwick : 50-150 outcome statements par job, syntaxe précise « direction + métrique + objet + contexte », scored sur importance (1-10) et satisfaction (1-10). Overlay signaux PMF comportementaux Reforge : les courbes de rétention cohortes qui s'aplatissent horizontalement, DAU/MAU >50%, power-user curve, croissance organique des referrals. En contextes B2B, désagréger le scoring par rôle d'achat (AIM Institute). Pour les produits PLG, intégrer la breadth des signaux comportementaux PQL (Reforge/OpenView) : les utilisateurs atteignant des milestones d'activation expriment une préférence révélée 3-5x plus prédictive que l'intent déclaré. |
| **soldier-gist** | Ajouter le cadrage hypothesis-first McKinsey à la couche Ideas : chaque Idea = hypothèse falsifiable avec condition de mort pré-déclarée (« si la métrique X n'améliore pas de Y% sous Z jours, on tue cette idée »). Audit STL Amazon à chaque Goal : « est-ce qu'il y a une personne 100% dédiée à cette initiative ? » — si non, le Goal n'est pas une vraie priorité. Calibration Google OKR (norme Grove/Doerr) : atteinte 1.0 = signal de conservatisme excessif ; 0,6-0,7 = ambition appropriée. Mapper les Steps sur un cadence de bets trimestriels (Spotify Bets Framework) : chaque Step = bet explicite avec hypothèse d'outcome laddering vers un OKR de tribu. |
| **soldier-impact-effort** | Axe stratégique obligatoire en 3ème dimension : « cette initiative ladder-t-elle vers l'objectif stratégique actuel ? » — les items en quadrant high-impact/low-effort qui n'avancent pas l'objectif stratégique doivent être déprioritisés. BCG Growth-Share Matrix overlay pour les trade-offs portefeuille avant de lancer la matrice. Séquençage par vagues McKinsey : high-impact/low-effort = Vague 1 (10-12 semaines) ; high-impact/high-effort = Vagues 2-3 ; élimination inconditionnelle du quadrant low-impact/high-effort. Design-to-Value Roland Berger pour calibrer les scores Effort avant la matrice : distinguer les features qui contribuent à la marge de celles qui ajoutent du coût de complexité. |
| **soldier-tech-debt-balance** | Classification dette tech via taxonomie Toyota TPS Muda/Muri/Mura : Muda (gaspillage), Muri (surcharge), Mura (irrégularité). DORA metrics comme signal dette presentable aux exécutifs : Change Failure Rate et Lead Time for Changes sont les indicateurs retardés empiriquement validés de la charge de dette. Value Stream Mapping (Lean Enterprise Institute) pour quantifier le coût de la dette en termes de débit : PCE (Process Cycle Efficiency) < 15% typique. Budgéter le paiement de la dette comme Scaling Work — catégorie de travail distincte chez Reforge (Casey Winters), protégée d'une extraction vers les sprints Feature Work. |

#### Nouveaux soldiers recommandés pour O3

| Nom | Grade | Méthode | Rationale | Sources |
|---|---|---|---|---|
| **soldier-opportunity-solution-tree** | 🎖️ Élite | OST — Teresa Torres / Product Talk | Seule méthodologie O3 qui enforce la priorisation outcome-first structurellement plutôt que procéduralement : les équipes ne peuvent pas scorer ou classer une solution avant d'avoir identifié l'opportunité spécifique qu'elle adresse, et ne peuvent pas identifier une opportunité avant d'avoir convenu de la métrique desired outcome. Prévient le failure mode le plus coûteux — sauter aux solutions avant valider le problème — que RICE, Impact-Effort et GIST ne préviennent pas structurellement. | Teresa Torres — Product Talk, Continuous Discovery Habits (2021) |
| **soldier-rapid-decision** | 🎖️ Élite | RAPID Decision Framework (Bain & Company) | Les soldiers existants adressent QUOI prioriser mais pas QUI a l'autorité de finaliser cette priorisation. Les processus de scoring en comité où le rôle Decide est diffus produisent des décisions qui s'inversent après la réunion. RAPID : Recommend, Agree (veto étroit prédéfini), Perform, Input, Decide (un seul décideur — un nom, pas un groupe). Organisations déployant RAPID : croissance revenus 3x supérieure, +27 points NPS employés (recherche propriétaire Bain). | Bain & Company — RAPID Decision Framework ; HBR — « Who Has the D? » (2006) |
| **soldier-betting-table** | 🎖️ Élite | Betting Table (Ryan Singer / Basecamp Shape Up) | Apporte 2 capacités qu'aucun autre soldier fournit : (1) le no-backlog forcing function — le travail non sélectionné est droppé, pas conservé, éliminant la dette de priorisation passive ; (2) le Circuit Breaker — un projet qui ne livre pas dans son cycle ne reçoit pas d'extension automatique. Max 4-5 décideurs seniors. Inputs : uniquement des pitches well-shaped avec appetite explicite et exclusions de scope. | Ryan Singer — Shape Up (Basecamp/37signals, 2019) |
| **soldier-portfolio-wave-planner** | 🔵 Standard | Wave-Based Mobilization (McKinsey) | Les soldiers existants produisent une liste classée mais pas un plan de déploiement séquencé avec des frontières d'engagement explicites. La planification par vagues transforme une liste priorisée en portefeuille d'investissement stagé où chaque vague doit prouver sa valeur avant le financement de la suivante. Vague 1 = quick wins ; Vague 2 = scaling ; Vague 3 = long-build. TMO (max 3 personnes) possède la cadence. | McKinsey — Wave-Based Mobilization, Transformation Management Office |
| **soldier-odi-outcome-mapping** | 🔵 Standard | Outcome-Driven Innovation (Tony Ulwick / Strategyn) | soldier-opportunity-scoring manque d'un protocole d'élicitation défini. ODI comble ce gap : 50-150 outcome statements par JTBD, format précis, scoring sur importance et satisfaction, seuils d'interprétation clairs. Extension B2B AIM Institute : outcome statements par rôle d'achat distinct, interdiction du scoring par répondant unique. Appliqué sur 300+ engagements clients chez Strategyn. | Tony Ulwick / Strategyn — ODI (300+ engagements) ; AIM Institute — New Product Blueprinting B2B |
| **soldier-stage-gate** | 🔵 Standard | Stage-Gate Process (Robert G. Cooper / Stage-Gate International) | Les soldiers existants scorent et classent les opportunités mais ne fournissent aucun mécanisme de kill formel lié à des gates d'evidence. Stage-Gate ajoute une discipline de kill structurée avec des exigences d'evidence croissantes. 4 décisions par gate : Go, Kill, Hold, Recycle. Les critères Kill sont aussi importants que les critères Go — la valeur documentée (60+ études industrielles Cooper) vient de tuer les concepts faibles avant que le capital ne s'escalade. | Robert G. Cooper — Stage-Gate International, Winning at New Products |
| **soldier-pql-framework** | 🔵 Standard | PQL Framework (Reforge / OpenView Partners / Amplitude) | Fournit un signal de priorisation behaviouralement fondé — aucun soldier O3 existant n'adresse cela. RICE et Impact-Effort utilisent l'impact estimé par l'équipe ; PQL remplace l'estimation par le comportement client révélé. PQL = utilisateur ayant atteint le milestone d'activation + seuil de fréquence d'usage + breadth d'adoption features + signal d'expansion team. Conversion PQL 25-30% vs MQL 5-10% (avantage 3-5x). | Reforge (Brian Balfour) ; OpenView Partners (Blake Bartlett) — PLG et framework PQL |
| **soldier-cohort-analysis** | 🔵 Standard | Cohort Retention Analysis (Reforge / Amplitude) | Les soldiers existants estiment l'impact mais ne fournissent pas de méthodologie de mesure comportementale pour valider cet impact rétrospectivement. L'analyse cohortes transforme le moment AHA d'une hypothèse en seuil empiriquement mesuré, fournissant à la fois une cible de priorisation (amener plus d'utilisateurs au moment AHA) et un mécanisme de validation. Benchmarks : rétention active B2B hebdomadaire 44,6%-77,9% ; 60-70% du churn annuel SaaS survient dans les 90 premiers jours. | Reforge (Brian Balfour, Casey Winters) ; Amplitude — North Star Playbook ; Lenny Rachitsky & Yuriy Timen (étude 500+ produits) |

#### Upgrades doctrinaux O3

1. **LE SCORING IMPACT-EFFORT SANS GATE D'ALIGNEMENT STRATÉGIQUE OPTIMISE POUR LA FACILITÉ, PAS LA VALEUR.** Chaque item passant le filtre high-impact/low-effort doit répondre en plus : « cette initiative ladder-t-elle vers l'objectif stratégique actuel ? ». Si non, elle est déprioritisée quelle que soit sa position dans la matrice.

2. **LE BACKLOG « SOMEDAY » EST DE LA DETTE DE PRIORISATION, PAS UNE LISTE D'ATTENTE.** Shape Up (Singer, Basecamp) : le travail non sélectionné dans un cycle de priorisation doit être droppé et doit se re-justifier de zéro s'il ressurgit. L'hypothèse par défaut — que les items non sélectionnés doivent être conservés en backlog — cause une accumulation de ghost priorities.

3. **L'INTENTION D'ACHAT DÉCLARÉE ET LES SCORES D'OPPORTUNITÉ PAR SURVEY SONT DES HYPOTHÈSES, PAS DES PREUVES.** NielsenIQ BASES déflate l'intention d'achat déclarée via des facteurs de calibration empiriques de 300 000+ concept tests. Tout score d'opportunité construit sur la préférence déclarée seule est une hypothèse nécessitant une corroboration comportementale.

4. **LE PMF EST UN TAPIS ROULANT, PAS UN SEUIL.** Le budget O3 doit inclure une allocation explicite de Scaling Work (Reforge — 5 types de travail produit) pour maintenir la parité PMF — pas seulement du Feature Work et du Growth Work.

5. **LA LATENCE DE DÉCISION EN PRIORISATION EST UN DRAG REVENUS MESURABLE.** Bain RAPID : +3x de croissance revenus, +27 points NPS employés avec un rôle Decide nommé. Toute cérémonie de priorisation doit assigner le rôle RAPID « D » avant la réunion.

6. **OKRs ET KPIs SONT DEUX INSTRUMENTS STRUCTURELLEMENT DIFFÉRENTS.** 0,6-0,7 d'atteinte = signal de succès OKR ; score 1.0 = sandbag. Traiter les OKRs comme des KPIs en revues de performance détruit l'ambition et produit des roadmaps conservateurs.

7. **UNE PRIORITÉ SANS OWNER SINGLE-THREADED N'EST PAS UNE VRAIE PRIORITÉ.** Audit STL Amazon (OP1 review) : « y a-t-il une personne 100% dédiée — pas en mode matriciel — à cette initiative ? ». Un « non » retire l'initiative de la liste de priorités quelle que soit son score RICE. Aucune méthodologie de scoring ne compense la diffusion de propriété.

---

### O4 — Design & Validation

#### Soldiers existants — Enrichissements spécifiques

| Soldier | Enrichissements apportés |
|---|---|
| **soldier-four-risks** | Taxonomie des hypothèses Torres (4 catégories : désirabilité, viabilité, faisabilité, utilisabilité) couplée avec le type de test le moins cher applicable à chacune : fake door/smoke test pour désirabilité, modélisation financière pour viabilité, spike engineering pour faisabilité, test utilisabilité par tâche pour utilisabilité. Connexion gates Stage-Gate Cooper (en particulier Stage 2 Business Case). Phase Pilot BCG (Diagnose→Design→Pilot→Scale→Embed) comme institutionnalisation organisationnelle du de-risking 4 risques avant commitment complet. BASES NielsenIQ forecasting volumétrique comme instrument de risque viabilité (contextes CPG/consumer). |
| **soldier-shape-up** | Connecter explicitement l'appetite-based scoping à l'Impact-Effort Matrix MBB : la betting table est fonctionnellement équivalente à une session impact-effort où le Decider (le rôle de Singer) écrase le débat de comité. Hill chart (uphill = incertain, downhill = connu/exécution) mappe le finding VSM que 70-90% du lead time de delivery est du temps d'attente/incertitude. Circuit breaker ~ Netflix Keeper Test au niveau projet : les deux éliminent l'accumulation d'actifs sous-performants en forçant le recommitment actif. Cool-down ~ période inter-vagues McKinsey : protection du temps de réflexion et reshaping que la pression de delivery absorberait sinon. |
| **soldier-design-sprint** | Ancrage scientifique du test J5 à 5 utilisateurs : recherche Nielsen (NNg) montre que 5 utilisateurs découvrent environ 85% des problèmes d'utilisabilité. Le test sprint est une validation d'hypothèse binaire, pas un échantillon de mesure. Adaptation Creative Sprint pour les agences (WPP, Publicis) : compressé à 2-3 jours avec panel de concept testing. Résultat empirique IBM : 75% de réduction des temps de design et d'implémentation avec design thinking. Mapper le rôle Decider (supervote, Jour 3) sur RAPID Bain : le Decider = le « D » de RAPID. Clarifier que le sprint enforce le travail « ensemble-séparément » (sketching individuel Jour 2) pour prévenir le groupthink. |
| **soldier-assumption-testing** | Taxonomie de sélection des tests Torres (OST) ordonnée par coût de construction : fake door → smoke test → concierge → Wizard of Oz → data mining. Checklist de rigueur pré-expérimentale : hypothèse, métrique primaire, counter-metrics, Minimum Detectable Effect (MDE) définis avant tout envoi de code. Discipline pre-mortem : avant tout test, énumérer tous les moyens par lesquels il peut produire des résultats trompeurs (paradoxe de Simpson, effets de nouveauté, contamination des groupes contrôle). Limite explicite du survey Ellis 40% comme test de désirabilité. Connexion au consulting MBB hypothesis-driven : « les données sont recueillies pour prouver ou réfuter un noeud spécifique dans l'arbre d'hypothèses ». |
| **soldier-usability-testing** | Évaluation heuristique comme étape pré-test obligatoire (pas en compétition) : 3-5 experts indépendants appliquant les 10 heuristiques Nielsen capturent ~65% des problèmes d'utilisabilité avant qu'un seul participant soit recruté. Cognitive walkthrough comme complément : 3 questions structurées à chaque étape de tâche. Rainbow spreadsheet comme outil de synthèse cross-participants. Couche biométrique/eye-tracking pour les signaux implicites (Tobii Pro, iMotions) : cartes de chaleur de fixation, analyse dwell-time AOI. Techniques de questioning Portigal (context-setting, naïve probe, ask-the-opposite). Système Google Search Quality Rater comme couche d'évaluation humaine scalée pour les produits où l'A/B testing ne peut capturer les dimensions qualité (confiance, intention de nuire). |
| **soldier-prototyping** | Spectre de fidélité explicite avec objectifs distincts par niveau : low-fi (structure) → mid-fi (layout et navigation) → high-fi (typographie, espacement) → prototype interactif (simulation de flux utilisateur). Formes de prototypage IDEO avec cas d'usage distincts : paper prototypes (structure), role-play/bodystorming (service interactions), Wizard of Oz (capacités IA/service non encore construites), storyboards (communication contexte/flux aux stakeholders). Shape Up : fat-marker sketch et breadboard comme outils délibérément low-resolution. Standard de qualité GV Sprint Jour 4 : « suffisamment bon pour susciter des réactions authentiques ». Cadence prototypage hardware Apple : 4-6 semaines de cycles de refabrication complète, versions physiques finies multiples avant sélection de la version de lancement. |

#### Nouveaux soldiers recommandés pour O4

| Nom | Grade | Méthode | Rationale | Sources |
|---|---|---|---|---|
| **soldier-service-blueprint** | 🎖️ Élite | Service Blueprint en 5 couches (frog/Fjord) | Seul artefact O4 qui mappe simultanément l'UX frontstage et les contraintes opérationnelles backstage. Tout produit avec une couche de service humaine (onboarding, support, implémentation, customer success) nécessite un service blueprint avant le handoff O5. Les goulots d'étranglement de capacité, les handoffs brisés et les chaînes de dépendance staff qui sont invisibles dans les journey maps et prototypes deviennent des échecs de lancement. | frog/Fjord — service design methodology (frontstage/backstage, ligne de visibilité) ; HCD/UX research |
| **soldier-heuristic-evaluation** | 🔵 Standard | Expert Evaluation (10 heuristiques Nielsen + Cognitive Walkthrough) | Structurellement distinct de soldier-usability-testing (observation comportementale avec participants). 3-5 experts indépendants appliquant les 10 heuristiques Nielsen = ~65% des problèmes d'utilisabilité trouvés avant un seul test utilisateur. ROI le plus élevé parmi toutes les méthodes de validation O4 en termes de coût/défaut détecté. Doit précéder les tests participants, pas les concurrencer. | Nielsen Norman Group — discount usability engineering, cognitive walkthrough |
| **soldier-design-to-value** | 🎖️ Élite | Roland Berger Design-to-Value (DtV) Workshop | Seule méthode O4 conçue spécifiquement pour rationaliser un portefeuille existant par contribution marginale — pas pour générer de nouvelles features. Teardowns cross-fonctionnels identifient quelles features/variants livrent de la marge vs. ceux qui ajoutent du coût de complexité. Résultat documenté : 45% de réduction du nombre de variants sans perte de revenus. Se couple avec BCG Growth-Share Matrix pour séquencer quelles lignes produit reçoivent l'attention DtV en premier. | Roland Berger — DtV Workshop ; BCG Growth-Share Matrix |
| **soldier-launch-readiness** | 🔵 Standard | Amazon Launch Readiness Review | Gate de validation pré-release : valide si le produit est safe to release, pas s'il vaut la peine d'être construit (assumption-testing) ni si les utilisateurs peuvent l'utiliser (usability-testing). 6 composants Amazon : operational readiness, CX readiness, security review, legal/compliance, instrumentation métriques (mesurer dès le Jour 1), définition fenêtre de monitoring post-launch. Connexion au COE (Correction of Errors) post-launch. | Amazon — Launch Readiness Reviews et Go/No-Go Gates ; Bryar & Carr — Working Backwards |
| **soldier-controlled-experiment** | 🔵 Standard | A/B & Experimentation statistiquement rigoureuse | Complément quantitatif distinct de soldier-assumption-testing (couverture qualitative). Nécessite une infrastructure statistique, des critères de succès définis et un engagement organisationnel à suivre les résultats. Google : dizaines de milliers d'expériences annuellement ; Netflix : ABlaze, milliers en simultané ; Amazon : Weblab (12 000+ expériences/an). Protocole pré-expérimental obligatoire : hypothèse, MDE, power calculation (α=0,05, puissance 80%), pre-mortem. | PLG/Growth research — Experimentation Culture ; Google data-driven culture ; Netflix ABlaze ; Amazon Weblab |
| **soldier-participatory-design** | 🎖️ Élite | Participatory Design / Co-création (tradition scandinave) | Structurellement différent de soldier-usability-testing (évaluatif) et soldier-design-sprint (idéation interne à l'équipe sans utilisateurs dans la salle). Surface le savoir tacite — workarounds, expertise incarnée, préférences non-articulées. Valeur ajoutée : designs avec adoption plus élevée car la propriété est partagée. En contextes de service, co-créer avec le personnel frontline améliore à la fois la qualité design et la motivation à l'implémentation. | HCD/UX research — Participatory Design (Bjorn Ehn, UTOPIA project) ; frog — Collective Action Toolkit v2 (2013) ; LEGO Serious Play |

#### Upgrades doctrinaux O4

1. **DISCIPLINE DIVERGER/CONVERGER.** Toute session O4 doit déclarer explicitement son mode actuel avant toute discussion. Mode diverger = pas de jugement, maximum d'options. Mode converger = évaluer et sélectionner. La confusion de mode est la cause principale du groupthink en ateliers de design.

2. **L'ÉVALUATION HEURISTIQUE PRÉCÈDE LES TESTS UTILISATEURS — CE N'EST PAS UNE ALTERNATIVE.** 3-5 experts appliquant les 10 heuristiques Nielsen capturent ~65% des problèmes d'utilisabilité avant qu'une seule session participant ait lieu. Anti-pattern : les équipes qui sautent l'évaluation heuristique et vont directement aux tests utilisateurs gaspillent la capacité et le budget des participants sur des défauts que tout praticien formé aurait trouvé en deux heures.

3. **LE TEST DU DESIGN SPRINT EST UNE VALIDATION D'HYPOTHÈSE BINAIRE, PAS UNE MESURE.** 5 utilisateurs au Jour 5 produisent une réponse qualitative binaire à une hypothèse de risque spécifique, pas une signification statistique. Demander des groupes de test sprint plus larges confond validation (ce concept fonctionne-t-il ?) avec mesure (combien améliore-t-il une métrique ?).

4. **LES TESTS D'HYPOTHÈSES DOIVENT ÊTRE SÉQUENCÉS PAR (COÛT DU TEST × SÉVÉRITÉ DU RISQUE), PAS PAR CATÉGORIE.** Toujours lancer le test le moins cher qui peut réfuter significativement le risque de sévérité la plus élevée. Construire une feature pour la « tester » n'est pas du testing d'hypothèses — c'est de la validation différée au coût maximum.

5. **LES SERVICE BLUEPRINTS SONT UN ARTEFACT DE HANDOFF O4 OBLIGATOIRE POUR LES PRODUITS AVEC UNE COUCHE DE SERVICE.** Livrer un design handoff à O5 Delivery sans service blueprint pour tout produit avec une couche de service humaine est structurellement équivalent à concevoir le frontstage sans budgétiser le backstage.

6. **LA DÉCOUVERTE DESIGN-LED ET DATA-LED SONT SÉQUENTIELLES, PAS CONCURRENTES.** Chesky : « si vous ne faites que des A/B tests, vous ne designez jamais avec empathie ». Ce n'est pas un rejet de l'expérimentation — c'est une assertion que l'expérimentation valide ce que l'empathie surface. Les équipes qui font uniquement des A/B tests convergent vers des optima locaux. Les équipes qui font uniquement de l'ethnographie ne peuvent pas distinguer le signal du bruit.

7. **ANTI-PATTERN — LE DESIGN SPRINT COMME SPRINT DE DELIVERY.** Le Design Sprint est un rituel de test d'hypothèses ; son output est une hypothèse validée ou réfutée, pas du code shippé. Les équipes qui réutilisent les Design Sprints comme mécanismes de livraison détruisent leur valeur centrale : compression de mois de débat interne en une semaine avec signal utilisateur réel.

---

### O5 — Delivery

#### Soldiers existants — Enrichissements spécifiques

| Soldier | Enrichissements apportés |
|---|---|
| **soldier-story-mapping** | Appetite-based scoping de Shape Up comme contraste explicite à l'estimation : appetite (« combien de temps ça vaut ? ») ancré sur la valeur business vs. estimation (« combien de temps ça prendra ? ») ancré sur l'effort passé. Annoter les epics avec un time-budget, pas seulement des story points. Séquençage par vagues McKinsey : regrouper les stories en vagues de delivery de 10-12 semaines avec points de contrôle ROI visibles. PI Objectives SAFe (SMART, scorés par valeur business) comme gate qualité avant qu'un cluster de stories entre dans un sprint. |
| **soldier-feature-flags** | Taxonomie de flags en 4 types explicites : release toggles (temporaires, retirés après rollout complet), experiment toggles (A/B et multivarié), ops toggles (circuit breakers et dégradation gracieuse), permission toggles (droits, accès beta). Politique de cycle de vie des flags avec une date d'expiration hard à la création. OpenFeature (CNCF, 2022) = standard SDK vendor-neutral. Connexion à la dépendance trunk-based development explicite : sans flags, le TBD exige que chaque feature mergée soit production-ready en un seul sprint — opérationnellement impossible pour les features multi-sprints. Patterns de progressive delivery : canary releases (1%→10%→50%→100%), dark launches, blue/green deployments. |
| **soldier-launch-readiness** | Remplacer la gate binaire go/no-go par la taxonomie 4 décisions de Cooper (Stage-Gate) : Go, Kill, Hold, Recycle. « Kill » nécessite autant de discipline que « Go ». 6 composants Amazon : operational readiness, CX readiness, security review, legal/compliance, instrumentation métriques (mesurer dès le Jour 1), définition fenêtre de monitoring post-launch. COE Amazon (Correction of Errors) comme artefact post-launch obligatoire pour tout incident de lancement dans les 30 jours. 3 métriques kill CPG (analogues NielsenIQ/BASES pour le logiciel) : activation velocity (=retail velocity), trial-to-paid conversion (=trial rate), rétention D30 (=repeat purchase). |
| **soldier-dora-metrics** | Rework Rate = 5ème métrique DORA (2024 State of DevOps Report, Forsgren et al.) : mesure la proportion de travail qui doit être refait. Flow metrics comme complément diagnostique : DORA mesure les outcomes de delivery ; les flow metrics (cycle time, lead time, throughput, WIP) mappent le système. Little's Law : cycle time moyen = WIP moyen / throughput moyen — prouve que la réduction du WIP est le levier d'amélioration delivery le plus rapide sans changer la taille d'équipe. Finding VSM : 70-90% du lead time de delivery est du temps d'attente. 3 prérequis architecturaux pour la performance DORA élite : TBD, automatisation complète des tests, architecture loosely coupled. SPACE Framework (Forsgren et al., 2021) comme complément multidimensionnel. |
| **soldier-beta-program** | Discipline pre-mortem comme premier artefact du programme beta : avant lancement, énumérer explicitement les modes de défaillance. Sequential statistical testing (approche Netflix ABlaze) permettant un arrêt anticipé avec contrôle du taux de faux positifs. Bain Change Power Index comme gate de readiness organisationnelle avant scaling : mesurer l'alignement du leadership, le soutien du management intermédiaire et la readiness frontline avant d'élargir. Blast-radius opérationnel Spotify : architecting via feature flags pour une release à 1% d'utilisateurs avec rollback en minutes. Artefact de learning review obligatoire au close beta (équivalent COE Amazon). |

#### Nouveaux soldiers recommandés pour O5

| Nom | Grade | Méthode | Rationale | Sources |
|---|---|---|---|---|
| **soldier-steerco-rhythm** | 🎖️ Élite | Gouvernance SteerCo (McKinsey TMO / Kearney PMO) | Aucun soldier O5 existant ne couvre le rythme de gouvernance delivery. story-mapping visualise le backlog ; dora-metrics mesure les outcomes ; aucun ne gouverne la cadence opérationnelle. Sans rythme SteerCo formel, les programmes de delivery dérivent vers des reporting fragmentés où chaque workstream possède son propre narrative. 4 niveaux : standups équipe hebdo, reviews bimensuelles de wave/milestone, SteerCo exécutif mensuel, refresh portefeuille trimestriel. | McKinsey — Transformation Management Office (TMO) ; Kearney digital PMO ; BCG — SteerCo comme corps de décision |
| **soldier-wave-planner** | 🎖️ Élite | Wave-Based Delivery Planning (McKinsey) | story-mapping visualise sur une timeline mais n'enforce pas les ROI checkpoints entre phases de delivery. Wave planning se situe au niveau 10-12 semaines — correspondant aux bets trimestriels Spotify et à la durée PI SAFe — et force des décisions explicites sur ce qui doit être prouvé avant que des ressources supplémentaires soient committées. Étude McKinsey 32 entreprises : les programmes structurés en vagues produisent des outcomes significativement meilleurs que l'exécution simultanée du portefeuille. | McKinsey — Wave-Based Mobilization (Wave 1 prove / Wave 2 scale / Wave 3 long-build) ; BCG — Pilot gate non-négociable ; Bain — Full Potential Transformation |
| **soldier-vsm-flow-analyst** | 🔵 Standard | Value Stream Mapping pour la Delivery Produit | dora-metrics mesure les outcomes de delivery (Deployment Frequency, Lead Time, Change Failure Rate, MTTR) mais ne peut pas identifier OÙ dans le système se situe le gap de performance. VSM mappe le système lui-même. Sans VSM, les équipes investissent pour rendre les développeurs individuels plus rapides (non-contrainte) alors que les queues de handoff entre fonctions sont la vraie contrainte. VSM + Little's Law + TOC = diagnostic complet du système de delivery : symptôme (scores DORA) → cause racine (localisation de la contrainte) → intervention (automatisation CI/CD, limites WIP, élimination des handoffs). | Toyota TPS / Lean Enterprise Institute — VSM ; Gene Kim — The Phoenix Project (2013) ; Eliyahu Goldratt — The Goal (1984) — TOC |
| **soldier-input-metrics** | 🎖️ Élite | Controllable Input Metrics (Amazon) | dora-metrics couvre 4 métriques d'output spécifiques pour la delivery. Aucun soldier ne couvre la discipline en amont de sélectionner les BONNES métriques d'input qui causent ces outputs. Sans cette discipline, les équipes de delivery rapportent des outputs (features shippées, sprints complétés) plutôt que des outcomes réalisés (réduction du cycle time, amélioration du defect escape rate). Les équipes qui possèdent des métriques d'input ont une connexion directe entre leurs décisions quotidiennes et l'amélioration mesurable du système. | Amazon WBR — 200+ métriques d'input contrôlables ; Jeff Bezos « Dive Deep » (Bryar & Carr — Working Backwards) ; McKinsey Value Bridge |
| **soldier-13week-capacity-forecast** | 🔵 Standard | Prévision de Capacité 13 Semaines (SPI Research / Kearney PMO) | Aucun soldier O5 ne couvre la planification de capacité. story-mapping gère le scope ; dora-metrics mesure le débit ; aucun n'active une gestion des risques de delivery proactive via une visibilité forward-looking sur la capacité équipe. Fenêtre de 13 semaines = minimum pour la gestion proactive du risque. Goldilocks Zone : utilisation facturable 70-80% (en dessous = sous-utilisé, au-dessus = burnout et dégradation qualité). Moyenne industrie SPI Research 2025 (403 firmes) : 66,4% — en dessous du minimum 70%. | SPI Research 2025 Professional Services Maturity Benchmark ; Kearney digital PMO |

#### Upgrades doctrinaux O5

1. **DÉPLOIEMENT N'EST PAS RELEASE.** Les feature flags découplent entièrement ces deux événements. Déployer du code en production en continu tout en releasant à 0% d'utilisateurs, puis à 1%, puis à 100%. Traiter déploiement et release comme synonymes produit de fausses métriques DORA et génère une résistance organisationnelle à l'intégration continue.

2. **LA VÉLOCITÉ EST UNE HEURISTIQUE DE PLANIFICATION, PAS UN KPI DE PERFORMANCE.** La vélocité story points comme métrique de management dégrade la qualité delivery via 3 mécanismes : inflation de story points, sandbagging des commitments, optimisation du taux de complétion sur l'outcome client. Remplacer les comparaisons de vélocité au niveau programme par des flow metrics (cycle time, throughput) — system-level, résistantes à la manipulation, liées à la vitesse delivery côté client via Little's Law.

3. **70-90% DU LEAD TIME DE DELIVERY EST DU TEMPS D'ATTENTE, PAS DU TEMPS D'EXÉCUTION.** Le VSM appliqué à la delivery logicielle révèle consistamment que la cause dominante de la lenteur delivery est les queues de handoff entre fonctions, pas la vitesse des développeurs individuels. Les investissements pour rendre les ingénieurs plus rapides ont un effet quasi nul quand la contrainte est un goulot d'étranglement QA ou un gate d'approbation de déploiement.

4. **L'ADOPTION DE SAFe REFLÈTE UNE PALATABILITÉ POLITIQUE, PAS DE L'AGILITÉ.** SAFe utilisé par 70%+ du Fortune 100 en 2025 = préservation des couches de management existantes, pas performance delivery supérieure. Anti-patterns endémiques : PI Planning qui s'effondre en plans waterfall de 2 jours ; ARTs de composants se faisant passer pour des ARTs value-stream ; comparaisons de vélocité remplaçant la vraie mesure d'outcome.

5. **LES PROGRAMMES BETA SANS SEUIL DE KILL SONT DU THÉÂTRE.** Un programme beta sans critère de kill prédéfini — un seuil de métrique spécifique auquel le programme est terminé et la feature annulée — produit de la dette organisationnelle, pas de l'apprentissage. Circuit breaker Shape Up = analogie structurelle.

6. **LA LAUNCH READINESS SANS INSTRUMENTATION MÉTRIQUES EST INCOMPLÈTE.** Un produit ou feature qui shippe sans mesure instrumentée dès le Jour 1 ne peut pas être appris, itéré avec des données, ni déclencher un COE post-launch. L'instrumentation métriques doit être un item obligatoire de la checklist de launch readiness avec le même poids que la security review et le sign-off légal.

7. **LA CADENCE DE GOUVERNANCE EST DE L'INFRASTRUCTURE DE DELIVERY, PAS DE L'OVERHEAD.** Les programmes de delivery sans rythme de gouvernance formel défaillent par défaut vers l'escalade ad hoc. McKinsey, BCG et Kearney traitent le rythme SteerCo comme de l'infrastructure non-négociable établie en Semaine 1 d'un programme. Le TMO doit avoir une vraie autorité pour débloquer les initiatives — un TMO qui ne rapporte qu'est du théâtre de reporting.

---

### O6 — Measurement & Learning

#### Soldiers existants — Enrichissements spécifiques

| Soldier | Enrichissements apportés |
|---|---|
| **soldier-north-star** | Contrainte Amplitude North Star Playbook (Cutler) : le NSM doit se situer un niveau d'abstraction au-dessus de ce que les équipes contrôlent directement. Counter-metrics/guardrails obligatoires : churn rate, volume de tickets support, NPS négatif. Évolution Meta DAU/MAU → Family DAP : le NSM doit être redéfini quand le périmètre produit s'élargit. Risque PMF Treadmill (Winters/Mosavat) : le seuil NSM n'est jamais statique. Arbre des métriques d'input sous le NSM : 3-5 facteurs influençables (breadth d'adoption, profondeur d'usage, fréquence, efficacité, outcomes clients) que les équipes peuvent directement déplacer via le travail produit. |
| **soldier-aarrr** | Critique structurelle Reforge (Balfour, Chen, Winters) : AARRR génère plus de métriques que la plupart des équipes ne peuvent agir, traite les journeys comme linéaires alors qu'ils sont non-linéaires et concurrents, ne distingue pas les utilisateurs high-value des low-value. Distinction growth loops vs. funnels : les funnels nécessitent une dépense incrémentale proportionnelle ; les loops produisent des rendements composés en réinvestissant les outputs dans les inputs. Framework 3 composants Palihapitiya (équipe growth Facebook 2007-2012) : conversion top-of-funnel + découverte du magic moment + rétention/résurrection. Référence Dropbox : 3 900% de croissance en 15 mois, 35% des inscriptions quotidiennes via referrals — le Referral est en amont de l'Acquisition dans les systèmes de croissance composée. |
| **soldier-cohort-analysis** | Aplatissement de la courbe de rétention = signal PMF le plus difficile à falsifier. Sélection D1/D7/D30 par cycle d'usage naturel. Méthodologie de découverte du moment AHA via analyse comportementale cohortes : comparer les utilisateurs retenus vs. churnés sur les comportements J0-J7 pour trouver l'action différenciatrice = milestone d'activation. Benchmarks empiriques (Rachitsky & Timen, 500+ produits) : rétention active B2B hebdomadaire 44,6%-77,9% ; 60-70% du churn SaaS annuel dans les 90 premiers jours. Limites du survey Ellis 40% : préférence déclarée vs. comportement ; DAU/MAU >50% = signal comportemental PMF plus fort. Sequential testing Netflix ABlaze : les cohortes d'analyse doivent appliquer la même rigueur statistique. |
| **soldier-controlled-experiment** | Protocole de rigueur pré-expérimental comme gate obligatoire : hypothèse, métrique primaire, counter-metrics, MDE avant tout envoi de code. Benchmarks MDE : layout/UX 5-15% de lift relatif, copy/messaging 10-20%, pricing/discount 2-5%. Seuils statistiques standard : α=0,05, puissance 80% (élevée à 90% pour les expériences high-downside). Discipline pre-mortem : paradoxe de Simpson, effets de nouveauté, contamination du groupe contrôle par effets réseau. Flywheel Weblab Amazon (2011) : 12 000+ expériences/an — ne fonctionne que quand le coût cognitif et process de lancement d'une expérience diminue continuellement. Google Search Quality Rater comme contre-modèle : évaluateurs humains comme vérité terrain qualité au-dessus de l'A/B testing automatisé. Incrementality testing (expériences de holdout géo) : 52% des marketeurs brand/agence aux US l'utilisent en 2025-2026. |
| **soldier-product-analytics** | McKinsey Value Bridge Framework : ledger mensuel validé par Finance distinguant les gains ponctuels des améliorations run-rate, avec propriété nommée par métrique. HEART Framework (Google, Rodden 2010) : Happiness, Engagement, Adoption, Retention, Task Success — remplace PULSE (Page views, Uptime, Latency, Seven-day actives, Earnings). DORA Metrics (Forsgren, Humble, Kim — Accelerate 2018) : 4 métriques + Rework Rate (2024). Flow Metrics et Little's Law : 70-90% du lead time logiciel est du temps d'attente entre fonctions. Discipline WBR Amazon : 200+ métriques revues en 60 minutes/semaine — les métriques d'input contrôlables sont le système opérationnel, les métriques d'output sont le tableau de bord, pas l'inverse. |

#### Nouveaux soldiers recommandés pour O6

| Nom | Grade | Méthode | Rationale | Sources |
|---|---|---|---|---|
| **soldier-value-bridge** | 🎖️ Élite | McKinsey Value Bridge / Value Ambition Framework | Aucun soldier O6 existant n'opérationnalise la connexion entre mesure produit et réalisation d'outcomes validés par Finance. soldier-product-analytics couvre l'infrastructure analytics ; soldier-north-star couvre la sélection de métrique ; mais aucun ne fournit la discipline d'un ledger vivant co-possédé par Finance distinguant gains ponctuels vs. améliorations run-rate. Le Value Bridge est le mécanisme qui rend la mesure crédible pour le C-suite. | McKinsey Value Bridge / Value Ambition Framework ; Oliver Wyman Transformation Cockpit |
| **soldier-coe-postmortem** | 🎖️ Élite | Amazon COE (Correction of Errors) | Aucun soldier O6 ne couvre la discipline d'apprentissage par l'échec. soldier-controlled-experiment couvre les expériences prospectives ; soldier-cohort-analysis couvre les patterns comportementaux rétrospectifs ; mais aucun ne fournit de mécanisme structuré pour convertir les incidents et échecs en améliorations systémiques durables. 8 composants obligatoires (summary, impact, timeline, metrics, incident questions, Five Whys jusqu'à défaillance systémique, action items, related items). | Amazon Product Development — COE et Post-Mortems comme Learning Loops |
| **soldier-input-metrics** | 🎖️ Élite | Controllable Input Metrics (Amazon) | Aucun soldier O6 n'adresse la distinction métriques d'input vs. d'output comme discipline PM first-class. Les métriques d'output (revenus, profit, conversion, NPS) ne peuvent pas être manipulées durablement comme leviers produit — les équipes qui les gèrent les gamifient en dégradant l'expérience client. Question diagnostique : une équipe peut-elle prendre une action spécifique aujourd'hui qui déplacera ce chiffre ? Si non, c'est un output. | Amazon WBR ; Jeff Bezos « Dive Deep » |
| **soldier-plg-flywheel** | 🔵 Standard | PLG Flywheel (OpenView / Reforge) | soldier-aarrr couvre le funnel diagnostique ; soldier-north-star couvre la métrique primaire ; mais aucun ne fournit l'architecture de croissance stratégique connectant acquisition, activation, rétention, expansion et advocacy dans un système auto-renforçant composé. Les PLG atteignent 35% de croissance médiane annuelle vs. 26% pour les SaaS non-PLG et 40% de CAC plus bas. | OpenView Partners (Blake Bartlett) — PLG ; Reforge (Balfour, Chen) — growth loops |
| **soldier-heart-metrics** | 🔵 Standard | HEART Framework (Google / Kerry Rodden, 2010) | Aucun soldier O6 ne fournit de framework de mesure centré expérience utilisateur. soldier-product-analytics couvre l'infrastructure analytics ; soldier-north-star sélectionne la métrique business primaire ; mais aucun ne fournit de système structuré pour mesurer les dimensions qualité UX en amont des outcomes business. HEART dimensions → Objectives OKR ; signaux spécifiques → Key Results. | Google — HEART Framework (Kerry Rodden, Hilary Hutchinson, Xin Fu, 2010) |
| **soldier-nrr-expansion** | 🔵 Standard | NRR & Expansion Revenue (benchmarks Snowflake/Datadog/Slack) | Aucun soldier O6 ne couvre la mesure des revenus d'expansion, levier de croissance le plus efficient en capital à l'échelle. soldier-aarrr inclut Revenue parmi 5 étapes mais ne différencie pas expansion vs. new-logo. NRR > 100% = la base client existante croît sans acquisition de nouveaux logos. 4 mécanismes d'expansion : seat expansion, usage expansion, feature upsell, cross-sell multi-produit. À $15M+ ARR, l'expansion représente 40% de la croissance ARR totale pour les top performers. | PLG / Growth Methodologies research — NRR-Driven Growth ; B2B Agency — Land and Expand Model |
| **soldier-dora-metrics** | 🔵 Standard | DORA Metrics (Forsgren, Humble, Kim — Accelerate 2018 + 2024) | Aucun soldier O6 ne fournit de framework de mesure de la performance delivery — le gap entre ce que l'équipe produit décide de construire et la rapidité et fiabilité avec laquelle cela atteint les utilisateurs. Elite vs. low performers : 182x de déploiements plus fréquents, 127x de lead time plus rapide. Les 5 métriques DORA incluant Rework Rate (2024) sont le seul framework de mesure delivery empiriquement validé (33 000+ professionnels sur 7 ans de recherche). | Nicole Forsgren, Jez Humble, Gene Kim — Accelerate (2018) ; DORA 2024 State of DevOps Report |

#### Upgrades doctrinaux O6

1. **LES OKRs ET KPIs SONT DES INSTRUMENTS CATÉGORIQUEMENT DIFFÉRENTS ET NE DOIVENT JAMAIS ÊTRE CONFONDUS.** OKRs = cibles hypothesis-driven où 0,6-0,7 d'atteinte signale l'ambition appropriée et un score 1.0 est un signal diagnostique que l'objectif était trop sûr. KPIs = indicateurs de santé devant rester dans une plage opérationnelle définie. Les exécutifs qui traitent les OKRs comme des KPIs détruisent simultanément le target-setting ambitieux et la sécurité psychologique.

2. **AARRR EST UN OUTIL D'AUDIT DIAGNOSTIQUE, PAS UN MODÈLE OPÉRATIONNEL DE MESURE.** Après qu'AARRR a identifié le plus grand gap lifecycle, remplacer par un NSM focalisé et un arbre de métriques d'input pour l'exécution. Les organisations qui lancent AARRR en permanence comme système opérationnel de mesure fragmentent l'attention des équipes sans fournir de structure causale.

3. **LA VÉLOCITÉ EST UNE HEURISTIQUE DE PLANIFICATION, PAS UN KPI DE PERFORMANCE.** Remplacer les comparaisons de vélocité au niveau programme par des flow metrics (cycle time, throughput) liées par Little's Law — system-level, cross-team comparables, résistantes à la manipulation.

4. **LA GESTION DES MÉTRIQUES D'OUTPUT N'EST PAS DE LA GESTION PRODUIT.** Les revenus, profits et taux de conversion ne peuvent pas être manipulés directement ou durablement comme leviers produit. Le job du PM est d'identifier et déplacer les métriques d'input contrôlables (sélection, vitesse, qualité) qui causent les outputs. Amazon : identifier les bonnes métriques d'input est « trompeusement difficile et nécessite des essais et erreurs répétés ».

5. **LA DOOM LOOP ROAS EST LE MODE DE DÉFAILLANCE PRINCIPAL DE LA MESURE PERFORMANCE EN MARKETING.** Optimiser pour le ROAS amène les plateformes publicitaires à cibler le fruit le plus facile — les clients existants ou très prédisposés — recyclant la demande existante plutôt que faisant croître le marché adressable. ROAS = métrique de gestion de liquidité. LTV:CAC avec une cible 3:1 = la bonne métrique d'allocation d'investissement.

6. **LE PEEKING EST LA CAUSE PRINCIPALE D'INVALIDATION DE TEST.** Arrêter un test tôt quand des résultats positifs apparaissent, ou lancer des power calculations post-hoc sur des tests complétés, sont statistiquement invalides. La pré-enregistrement d'hypothèse, MDE et taille d'échantillon requise avant toute collecte de données est la discipline minimale. Les organisations sans protocoles de rigueur pré-expérimental accumuleront une bibliothèque de faux positifs de features « prouvées » qui ne survivent pas à la réplication.

7. **LE PMF EST UN TAPIS ROULANT, PAS UN MILESTONE.** Les systèmes de mesure doivent inclure des indicateurs avancés d'érosion PMF (rétention cohortes déclinante aux fenêtres temporelles tardives, CAC montant malgré une dépense stable, NPS divergeant de la rétention) — pas seulement des signaux PMF état-actuel. Cas Chegg 2024 : -90% de valorisation, -500K abonnés en 10 mois.

---

## Consolidated New Soldiers Roster

Liste complète des 36 nouveaux soldiers recommandés :

| Nom | Officier | Grade | Méthode / Framework | Sources Primaires | Priorité |
|---|---|---|---|---|---|
| soldier-problem-statement | O1 | 🎖️ Élite | McKinsey Problem Statement Worksheet | McKinsey (6 éléments) ; BCG Discovery Playbook Phase 1 ; Minto Pyramid Principle | **HIGH** — prérequis structurel à tous les autres soldiers O1 |
| soldier-issue-tree | O1 | 🎖️ Élite | MECE Issue Tree & Hypothesis Tree | McKinsey (Minto, 1978) ; BCG engagement playbooks ; Bain — Hypothesis-Driven Consulting | **HIGH** — structure l'espace-problème avant toute découverte |
| soldier-contextual-inquiry | O1 | 🎖️ Élite | Contextual Inquiry (Nielsen Norman / IDEO) | NNg — Contextual Inquiry, modèle maître/apprenti ; IDEO POEMS ; P&G Living It | **HIGH** — méthode structurellement différente des interviews |
| soldier-hmw-reframing | O1 | 🔵 Standard | How Might We (GV Design Sprint / IDEO) | Jake Knapp — Sprint (2016) ; IDEO Design Thinking ; Teresa Torres | **HIGH** — traduction structurelle O1→O3 absente |
| soldier-stakeholder-map | O1 | 🔵 Standard | Stakeholder Mapping (AIM Institute / McKinsey) | AIM Institute — New Product Blueprinting ; McKinsey Problem Statement Worksheet | **HIGH** — prérequis B2B/enterprise, condition préalable à tous les guides d'interview |
| soldier-diary-study | O1 | 🔵 Standard | Diary Study (Nielsen Norman / Dscout) | NNg — Diary Study methodology ; IDEO Generative probes ; Dscout | **MEDIUM** — critique pour produits à cycles d'usage long (hebdo/mensuel) |
| soldier-prfaq | O2 | 🎖️ Élite | Amazon PR/FAQ | Colin Bryar & Bill Carr — Working Backwards (2021) ; Amazon Fire Phone post-mortem | **HIGH** — convertit la vision en outcome client falsifiable avant commitment engineering |
| soldier-scr-pyramid | O2 | 🎖️ Élite | McKinsey SCR + Minto Pyramid Principle | Barbara Minto — The Pyramid Principle (1978, 2009) ; McKinsey engagement communication | **HIGH** — last-mile communication manquant pour tous les outputs O2 |
| soldier-competitive-forces | O2 | 🔵 Standard | Porter's Five Forces + BCG Growth-Share Matrix | Michael Porter — Competitive Strategy (1980) ; BCG Henderson Institute | **HIGH** — évalue le marché avant PMF et governe les trade-offs portefeuille |
| soldier-aarrr | O2 | 🔵 Standard | AARRR Pirate Metrics (500 Startups) | Dave McClure (2007) ; Reforge — Balfour, Winters ; Amplitude | **HIGH** — diagnostic lifecycle précédant le setting de la stratégie |
| soldier-opportunity-solution-tree | O3 | 🎖️ Élite | OST — Teresa Torres / Product Talk | Teresa Torres — Continuous Discovery Habits (2021) | **HIGH** — seul mécanisme O3 qui enforce outcome-first structurellement |
| soldier-rapid-decision | O3 | 🎖️ Élite | RAPID Decision Framework (Bain) | Bain — RAPID (+3x revenus, +27pt NPS) ; HBR « Who Has the D? » (2006) | **HIGH** — governance manquante pour finaliser les outputs de priorisation |
| soldier-betting-table | O3 | 🎖️ Élite | Betting Table (Ryan Singer / Shape Up) | Ryan Singer — Shape Up (Basecamp/37signals, 2019) | **HIGH** — no-backlog forcing function + Circuit Breaker inexistants ailleurs |
| soldier-portfolio-wave-planner | O3 | 🔵 Standard | Wave-Based Mobilization (McKinsey) | McKinsey — Wave-Based Mobilization, TMO | **HIGH** — transforme une liste classée en portefeuille d'investissement stagé |
| soldier-odi-outcome-mapping | O3 | 🔵 Standard | Outcome-Driven Innovation (Tony Ulwick / Strategyn) | Tony Ulwick / Strategyn (300+ engagements) ; AIM Institute | **HIGH** — protocole d'élicitation manquant dans soldier-opportunity-scoring |
| soldier-stage-gate | O3 | 🔵 Standard | Stage-Gate Process (Robert G. Cooper) | Robert G. Cooper — Stage-Gate International ; 60+ études industrielles | **MEDIUM** — crucial pour hardware, CPG, new platform bets |
| soldier-pql-framework | O3 | 🔵 Standard | PQL Framework (Reforge / OpenView) | Reforge (Balfour) ; OpenView Partners (Blake Bartlett) ; Amplitude | **HIGH** — signal behavioral de priorisation 3-5x plus prédictif que l'intent déclaré |
| soldier-cohort-analysis | O3 | 🔵 Standard | Cohort Retention Analysis (Reforge / Amplitude) | Reforge (Balfour, Winters) ; Amplitude North Star Playbook ; Lenny Rachitsky & Timen | **HIGH** — valide l'impact rétrospectivement et identifie le next leverage point |
| soldier-service-blueprint | O4 | 🎖️ Élite | Service Blueprint 5 couches (frog/Fjord) | frog/Fjord — service design methodology ; HCD/UX research | **HIGH** — obligatoire pour tout produit avec couche service humaine |
| soldier-heuristic-evaluation | O4 | 🔵 Standard | 10 heuristiques Nielsen + Cognitive Walkthrough | Nielsen Norman Group — discount usability engineering | **HIGH** — ROI le plus élevé de toutes les méthodes de validation O4 |
| soldier-design-to-value | O4 | 🎖️ Élite | Roland Berger Design-to-Value (DtV) | Roland Berger — DtV Workshop (45% réduction variants documentée) ; BCG Growth-Share Matrix | **HIGH** — seule méthode O4 pour rationaliser un portefeuille existant par marge |
| soldier-launch-readiness | O4 | 🔵 Standard | Amazon Launch Readiness Review | Amazon — Launch Readiness Reviews ; Bryar & Carr — Working Backwards | **HIGH** — gate pre-release manquant dans le flux O4 |
| soldier-controlled-experiment | O4 | 🔵 Standard | A/B & Expérimentation statistique | PLG/Growth research ; Google (dizaines de milliers tests/an) ; Netflix ABlaze ; Amazon Weblab | **HIGH** — complément quantitatif distinct de soldier-assumption-testing |
| soldier-participatory-design | O4 | 🎖️ Élite | Participatory Design / Co-création | HCD/UX research (Bjorn Ehn, UTOPIA project) ; frog Collective Action Toolkit v2 | **MEDIUM** — critique pour outils organisationnels, plateformes internes, service design |
| soldier-steerco-rhythm | O5 | 🎖️ Élite | Gouvernance SteerCo (McKinsey TMO / Kearney PMO) | McKinsey TMO ; Kearney digital PMO ; BCG SteerCo | **HIGH** — infrastructure de gouvernance delivery manquante |
| soldier-wave-planner | O5 | 🎖️ Élite | Wave-Based Delivery Planning (McKinsey) | McKinsey Wave-Based Mobilization ; BCG Pilot gate ; Bain Full Potential Transformation | **HIGH** — séquençage delivery au bon niveau (10-12 semaines) absente |
| soldier-vsm-flow-analyst | O5 | 🔵 Standard | Value Stream Mapping (Toyota TPS / Lean) | Toyota TPS / Lean Enterprise Institute ; Gene Kim — The Phoenix Project (2013) ; Goldratt — The Goal | **HIGH** — mappe le système delivery vs. mesure les outcomes (DORA) |
| soldier-input-metrics | O5 | 🎖️ Élite | Controllable Input Metrics (Amazon) | Amazon WBR ; Jeff Bezos « Dive Deep » ; McKinsey Value Bridge | **HIGH** — connexion directe décisions quotidiennes → amélioration systémique mesurable |
| soldier-13week-capacity-forecast | O5 | 🔵 Standard | Prévision Capacité 13 Semaines | SPI Research 2025 (403 firmes) ; Kearney digital PMO | **MEDIUM** — critique pour les structures agency/delivery avec rétainers |
| soldier-value-bridge | O6 | 🎖️ Élite | McKinsey Value Bridge / Value Ambition Framework | McKinsey Value Bridge ; Oliver Wyman Transformation Cockpit | **HIGH** — rend la mesure produit crédible pour le C-suite |
| soldier-coe-postmortem | O6 | 🎖️ Élite | Amazon COE (Correction of Errors) | Amazon Product Development — COE et Post-Mortems | **HIGH** — seule discipline de learning-by-failure avec protocole structuré |
| soldier-input-metrics (O6) | O6 | 🎖️ Élite | Controllable Input Metrics (Amazon) | Amazon WBR ; Jeff Bezos « Dive Deep » | **HIGH** — réframe le job du PM d'output management à input management |
| soldier-plg-flywheel | O6 | 🔵 Standard | PLG Flywheel (OpenView / Reforge) | OpenView Partners (Bartlett) ; Reforge (Balfour, Chen) | **HIGH** — architecture de croissance composée absente des soldiers existants |
| soldier-heart-metrics | O6 | 🔵 Standard | HEART Framework (Google / Kerry Rodden, 2010) | Google — HEART (Rodden, Hutchinson, Fu, 2010) | **HIGH** — mesure qualité UX upstream des outcomes business |
| soldier-nrr-expansion | O6 | 🔵 Standard | NRR & Expansion Revenue | PLG / Growth Methodologies research ; B2B Agency — Land and Expand Model | **HIGH** — levier de croissance le plus efficient en capital à l'échelle, non mesuré |
| soldier-dora-metrics | O6 | 🔵 Standard | DORA Metrics (Forsgren, Humble, Kim, 2018+2024) | Accelerate (2018) ; DORA 2024 State of DevOps Report | **HIGH** — seul framework delivery performance empiriquement validé (33 000+ professionnels) |

---

## Constitution Upgrades

### Nouvelles tensions à encoder dans la constitution Product-Kit

**1. VISION SANS KILL = DÉCORATION.** Ajouter comme axiome constitutionnel : toute vision produit qui n'a pas généré un « non » dans les 90 derniers jours est décorative, pas stratégique. L'audit trimestriel de la vision inclut obligatoirement la question : « Quelle initiative avons-nous refusée ou tuée en raison de cette vision ? ».

**2. PMF EST PERPÉTUELLEMENT MENACÉ PAR LE TAPIS ROULANT.** Interdire tout langage dans la constitution qui présente le PMF comme un milestone. Remplacer par : « PMF est un état de réalignement continu sur des attentes qui s'accumulent upward ». Déclencher une ré-évaluation PMF à chaque : expansion de périmètre produit, entrée d'un concurrent IA, changement de comportement des cohortes D30+.

**3. LE PIPELINE JTBD→ODI→OST EST NON-SUBSTITUABLE.** Encoder comme séquence fixe dans la constitution : les trois frameworks sont des étapes d'une même pipeline, pas des alternatives concurrentes. Toute organisation qui en sélectionne un seul laisse un vide structurel documenté.

**4. DÉPLOIEMENT ≠ RELEASE.** Encoder comme distinction fondamentale dans le lexique constitutionnel de Product-Kit : le déploiement (code en production) et la release (accès utilisateurs) sont deux événements indépendants découplés par les feature flags. Toute métrique ou processus qui les confond est constitutionnellement invalide.

**5. LA GOUVERNANCE DE DÉCISION PRÉCÈDE LA QUALITÉ DU SCORING.** Une méthodologie de scoring — aussi rigoureuse soit-elle — qui produit une liste sans un rôle Decide nommé unique générera des décisions qui s'inversent après la réunion. Encoder dans la constitution : toute cérémonie de priorisation doit nommer le « D » RAPID avant la réunion.

**6. LA DÉCOUVERTE B2B NÉCESSITE UNE CLAUSE CONSTITUTIONNELLE.** Si le produit sert un acheteur B2B ou enterprise, soldier-stakeholder-map s'exécute AVANT soldier-user-interview, et des guides d'interview séparés sont requis par rôle d'achat. Les méthodes consumer appliquées à des contextes B2B sont constitutionnellement inadaptées.

**7. LES MÉTRIQUES D'INPUT SONT LE SYSTÈME OPÉRATIONNEL ; LES MÉTRIQUES D'OUTPUT SONT LE TABLEAU DE BORD.** Encoder comme doctrine constitutionnelle de mesure : les décisions d'allocation de ressources sont prises sur les métriques d'input contrôlables, pas sur les outputs. Les outputs confirment ou infirment les actions prises sur les inputs.

**8. LE BACKLOG EST UNE FORME DE DETTE, PAS UN ACTIF.** La constitution doit encoder explicitement que les items non sélectionnés lors d'une cérémonie de priorisation sont droppés par défaut et doivent se re-justifier de zéro s'ils ressurgissent. La présomption de continuation est constitutionnellement proscrite.

### Nouvelles entrées « Never Cite » pour le Commandant

- **Ne jamais citer la vélocité story points comme indicateur de performance d'équipe.** C'est une heuristique de planification interne, non-comparable entre équipes, et systématiquement corrompue quand utilisée comme métrique de management.
- **Ne jamais citer le ROAS comme métrique principale de succès marketing.** C'est une métrique de gestion de liquidité, pas d'investissement. Elle recycle la demande existante et crée une doom loop.
- **Ne jamais citer SAFe comme « meilleure pratique agile ».** SAFe est un framework de gestion du changement politique — son adoption reflète la palatabilité organisationnelle, pas la performance delivery. Toujours accompagner d'une mention des anti-patterns documentés.
- **Ne jamais présenter le PMF comme un milestone atteint une fois pour toutes.** Le PMF est un état sur un tapis roulant. Toute formulation suggérant une certification permanente est interdite dans les outputs Product-Kit.
- **Ne jamais utiliser un survey comme seule preuve d'une opportunité.** Les surveys mesurent la préférence déclarée ; seuls les signaux comportementaux (rétention cohortes, DAU/MAU, PQL conversion) constituent des preuves suffisantes pour un investissement de delivery.

---

## Anti-Patterns & Traps

### Ajouts à la checklist qualité de l'Inspecteur

#### Niveau O1 — Discovery

| Anti-pattern | Signal détectable | Correction constitutionnelle |
|---|---|---|
| **Surveys avant observations** | Le programme de découverte commence par un survey ou des analytics avant qu'un seul utilisateur ait été observé en contexte | Séquencer : contextual inquiry / JTBD timeline → OST → surveys de confirmation |
| **Discovery comme phase unique** | Pas de pipeline de recrutement automatisé ; les interviews sont planifiées « quand on a le temps » | 1 interview/semaine/équipe comme standard opérationnel (Torres), pas projet trimestriel |
| **Absence de Problem Statement signé** | Le guide d'interview est conçu sans Problem Statement Worksheet validé | Bloquer tout instrument de recherche sans Problem Statement signé |
| **JTBD, ODI, OST traités comme alternatives** | L'équipe a « choisi » un seul de ces frameworks | Rétablir la pipeline séquentielle : JTBD→ODI→OST |
| **Recherche non-MECE** | Les questions d'interview se chevauchent ou laissent des segments entiers non couverts | Auditer la couverture de l'espace-problème avant fieldwork via issue tree |
| **Consumer VoC en contexte B2B** | Interviews B2B avec un seul interlocuteur sans cartographie des parties prenantes préalable | Exiger soldier-stakeholder-map avant tout guide d'interview B2B |

#### Niveau O2 — Strategy

| Anti-pattern | Signal détectable | Correction constitutionnelle |
|---|---|---|
| **Roadmap annuelle commitée** | Le roadmap comporte des engagements de features au-delà du trimestre courant | Interdire les commitments au-delà du trimestre ; adopter Now-Next-Later |
| **PMF présenté comme acquis** | Aucune mention du PMF Treadmill ni de trigger de ré-évaluation | Ajouter trigger de ré-évaluation périodique dans soldier-product-market-fit |
| **OKRs traités comme KPIs** | Les OKRs sont associés aux reviews de performance individuelles ou célèbrent le score 1.0 | Exiger le label explicite « OKR ≠ KPI » sur tout output soldier-okr |
| **NSM directement manipulable par une feature** | Le NSM peut être déplacé par l'action directe d'une seule équipe | Repositionner le NSM un niveau d'abstraction au-dessus des actions équipe |
| **Vision sans counter-metrics** | Le NSM est défini sans guardrails explicites | Minimum 2 counter-metrics nommés dans tout output soldier-north-star |

#### Niveau O3 — Prioritization

| Anti-pattern | Signal détectable | Correction constitutionnelle |
|---|---|---|
| **Scoring sans gate d'alignement stratégique** | Des items high-RICE ou en quadrant high-impact/low-effort n'avancent pas l'objectif stratégique actuel | Ajouter axe obligatoire : « cette initiative ladder-t-elle vers l'objectif actuel ? » |
| **Backlog « someday » non questionné** | Présence d'items en backlog datant de >2 trimestres sans re-justification | Appliquer le dropping protocol de Shape Up : droppé = re-justification de zéro |
| **Score d'opportunité construit sur le survey seul** | Aucune corroboration comportementale associée | Exiger corroboration : rétention cohortes, DAU/MAU, PQL pour toute opportunité scorée >8 |
| **Pas de Decide nommé avant la cérémonie** | La session de priorisation se termine sans décision actable ou avec inversion post-réunion | Appliquer RAPID : nommer le « D » avant toute réunion de priorisation |
| **Vélocité comme input de priorisation** | Les story points ou la vélocité d'équipe informent les décisions de priorisation | Remplacer par cycle time, throughput, et Little's Law |

#### Niveau O4 — Design & Validation

| Anti-pattern | Signal détectable | Correction constitutionnelle |
|---|---|---|
| **User testing sans évaluation heuristique préalable** | Les sessions utilisateurs sont planifiées directement, sans évaluation expert préalable | Bloquer le recrutement de participants jusqu'à l'évaluation heuristique terminée |
| **Design Sprint utilisé comme sprint de delivery** | Le Design Sprint est planifié pour produire du code shippé, pas une hypothèse validée | Reclasser : un Design Sprint = rituel de validation, output = hypothèse confirmée/réfutée |
| **Test d'hypothèse ≠ construction de la feature** | L'équipe propose de « builder la feature pour tester » | Appliquer la séquence Torres : fake door → smoke test → concierge → Wizard of Oz → build |
| **Service blueprint absent pour les produits service** | Handoff O4→O5 sans service blueprint pour un produit avec layer service humaine | Bloquer le handoff O5 sans service blueprint validé |
| **Feature accumulation sans DtV review** | Portefeuille >18 mois sans revue de contribution marginale par variant | Planifier une DtV review Roland Berger sur tout portefeuille >18 mois |

#### Niveau O5 — Delivery

| Anti-pattern | Signal détectable | Correction constitutionnelle |
|---|---|---|
| **Déploiement confondu avec release** | L'équipe considère chaque merge en production comme une release utilisateur | Séparer via feature flags ; DORA Deployment Frequency ≠ Feature Release Rate |
| **Beta sans kill threshold** | Le programme beta n'a pas de critère de terminaison prédéfini | Définir le kill threshold avant le lancement du beta ; aucune extension automatique |
| **Launch sans instrumentation J1** | Le produit shippe sans métriques instrumentées dès le premier request | Bloquer la release sans confirmation d'instrumentation dans la launch readiness checklist |
| **SAFe PI Planning sans outcome measurable** | Le PI Planning produit une liste de features sans hypothèses d'outcome ni métriques de validation | Exiger un outcome hypothesis et une métrique de validation par Feature/Epic |
| **Amélioration delivery sans VSM** | Investissements dans la vitesse individuelle des développeurs sans cartographie de la value stream | Exiger un VSM avant tout programme d'amélioration delivery |

#### Niveau O6 — Measurement

| Anti-pattern | Signal détectable | Correction constitutionnelle |
|---|---|---|
| **AARRR comme dashboard permanent** | L'équipe maintient 5+ métriques AARRR comme KPIs opérationnels quotidiens | Repositionner AARRR comme diagnostic one-time ; passer au NSM + input metrics tree |
| **Expérimentation par peeking** | Tests arrêtés tôt au premier résultat positif | Exiger pré-enregistrement : hypothèse, MDE, taille d'échantillon, power calculation avant collecte |
| **Output management déguisé en product management** | Le PM est évalué sur la croissance revenus ou conversion rate directement | Reframes vers les controllable input metrics Amazon ; les outputs sont des confirmations |
| **PMF déclaré acquis définitivement** | Pas d'indicateurs d'érosion PMF dans le système de mesure | Ajouter leading indicators d'érosion : rétention cohortes tardives, CAC divergeant, NPS vs. rétention |
| **ROAS comme métrique principale marketing** | Budgets marketing optimisés pour le ROAS sans LTV:CAC ni mesure d'incrémentalité | Ajouter LTV:CAC (cible 3:1), MMM, incrementality testing au système de mesure |

---

## Sources Registry

### Cabinets de Conseil Stratégique

| Source | Concepts clés extraits |
|---|---|
| **McKinsey & Company** | Problem Statement Worksheet (6 éléments) ; MECE Principle (Minto) ; Issue Tree & Hypothesis Tree ; SCR Framework ; Wave-Based Mobilization & TMO ; Value Bridge / Value Ambition Framework ; engagement phases (Diagnose→Design→Pilot→Scale→Embed) |
| **Boston Consulting Group** | Growth-Share Matrix (Henderson, 1970) ; Discovery Playbook Phase 1 ; Five Forces application en discovery ; Pilot gate non-négociable ; SteerCo comme corps de décision ; 76% échec CPG launches |
| **Bain & Company** | RAPID Decision Framework (+3x revenues, +27pt NPS) ; HBR « Who Has the D? » (2006) ; Full Potential Transformation (5 pilliers) ; Clear Ambition 4 dimensions ; Change Power Index ; Results Delivery framework |
| **Roland Berger** | Design-to-Value (DtV) Workshop (45% réduction variants documentée) |
| **Oliver Wyman** | Transformation Cockpit — KPI monitoring infrastructure |
| **Kearney** | Digital PMO — standardized reporting per workstream ; capacity planning as formal PMO responsibility |
| **Barbara Minto** | The Pyramid Principle (1978, updated 2009) — answer-first, MECE grouping |

### Amazon

| Source | Concepts clés extraits |
|---|---|
| **Colin Bryar & Bill Carr** | Working Backwards (2021) — PR/FAQ discipline ; Single-Threaded Leader (STL) ; Amazon Fire Phone post-mortem |
| **Amazon Product Development** | Launch Readiness Reviews (6 composants) ; COE (Correction of Errors) 8 composants ; WBR 200+ input metrics ; Weblab (12 000+ expériences/an) ; Controllable Input Metrics doctrine |
| **Jeff Bezos** | « Dive Deep » leadership principle ; output vs. input metrics doctrine |

### Tech Product Companies

| Source | Concepts clés extraits |
|---|---|
| **Teresa Torres / Product Talk** | Continuous Discovery Habits (2021) ; OST 4 niveaux ; taxonomie d'hypothèses (désirabilité, viabilité, faisabilité, utilisabilité) ; test selection ladder ; weekly interview standard |
| **Ryan Singer / Basecamp (Shape Up, 2019)** | Appetite vs. estimation ; Hill chart ; Betting Table (no-backlog) ; Circuit Breaker ; fat-marker sketch & breadboard ; cool-down period |
| **Jake Knapp / Google Ventures (Sprint, 2016)** | Design Sprint 5 jours ; HMW note-taking Day 1 ; Decider role (supervote) ; Day 4 prototype quality bar ; Day 5 5-user test |
| **Netflix** | ABlaze platform (sequential testing, milliers d'expériences simultanées) ; Now-Next-Later roadmap ; Keeper Test ; Culture Memo 2024 |
| **Spotify** | Bets Framework (quarterly bets, tribe OKRs) ; blast-radius via feature flags (1% rollout) ; fail-fast engineering culture |
| **Airbnb (Brian Chesky)** | « Belong Anywhere » vision comme filtre ; « Nights Booked » NSM dual-sided ; 18-month/3-year planning horizon ; Config 2023 keynote |
| **Meta** | DAU → DAU/MAU → Family DAP north star evolution ; Palihapitiya 3-component framework (2007-2012) ; 7 friends in 10 days magic moment |
| **Google** | OKR adoption (1999, John Doerr) ; HEART Framework (Rodden, Hutchinson, Fu, 2010) ; Search Quality Rater System ; tens of thousands A/B tests annually |

### Product Management Methodologies

| Source | Concepts clés extraits |
|---|---|
| **Tony Ulwick / Strategyn** | Outcome-Driven Innovation (ODI) ; outcome statement format (direction + metric + object + context) ; opportunity score formula ; 300+ client engagements |
| **Bob Moesta / The ReWired Group** | Timeline interview protocol ; 4 forces diagram (push, pull, anxiety, habit) ; Competing Against Luck |
| **Sean Ellis / GrowthHackers** | 40% PMF survey methodology (2010) ; limites : 100+ réponses, utilisateurs actifs 14 jours |
| **Dave McClure / 500 Startups** | AARRR Pirate Metrics (2007) |
| **John Cutler / Amplitude** | North Star Playbook (2019) ; NSM doit se situer au-dessus de ce que les équipes contrôlent directement |
| **John Doerr** | Measure What Matters (2018) — norme 0,6-0,7 attainment OKRs |
| **Andy Grove / Intel** | High Output Management (1983) — MBO→OKR formulation originelle |

### PLG & Growth

| Source | Concepts clés extraits |
|---|---|
| **Reforge (Brian Balfour, Casey Winters, Andrew Chen, Fareed Mosavat)** | PMF Treadmill ; 5 types de travail produit ; AARRR critique ; Growth Loops vs. Funnels ; AHA moment discovery methodology ; D1/D7/D30 cohort benchmarks ; PQL behavioral signals |
| **OpenView Partners (Blake Bartlett)** | PLG coinage ; PQL framework formalization ; ACV-tier conversion data ; PLG vs. SLG CAC benchmarks |
| **Amplitude** | North Star Playbook ; AARRR dashboard implementations |
| **Lenny Rachitsky & Yuriy Timen** | Activation benchmark study (500+ produits) ; B2B weekly active retention benchmarks (44,6%-77,9%) |
| **Chegg (cas d'étude)** | -90% valorisation, -500K abonnés en 10 mois (2024) — canonical PMF Treadmill failure |
| **Dropbox** | 3 900% de croissance en 15 mois, 35% signups via referrals — Referral upstream d'Acquisition |
| **Slack** | AHA moment 2 000 messages équipe — découvert via cohort analysis ; 140%+ NRR pre-acquisition |
| **Snowflake / Datadog** | NRR 150%+ (Snowflake), 130%+ (Datadog) — best-in-class expansion mechanics |

### HCD / UX / Design

| Source | Concepts clés extraits |
|---|---|
| **Nielsen Norman Group** | 10 Usability Heuristics ; discount usability engineering (5-user rule — 85% problèmes) ; Contextual Inquiry methodology ; Diary Study methodology ; Cognitive Walkthrough |
| **IDEO Design Thinking** | POEMS observation framework ; HMW bridge Define→Ideate ; Empathize→Define→Ideate→Prototype→Test ; diverge/converge mode discipline ; Generative design probes |
| **frog Design / Fjord** | Service Blueprint methodology (5 couches : Customer Actions, Frontstage, Line of Visibility, Backstage, Support) ; Collective Action Toolkit v2 (2013) |
| **Steve Portigal** | Interviewing Users (Rosenfeld Media, 2013) — context-setting, naïve probe, ask-the-opposite |
| **Bjorn Ehn / UTOPIA project** | Participatory Design — tradition scandinave (1970-80s) |
| **Tobii / iMotions** | Eye-tracking et recherche biométrique — Tobii Pro, Tobii Glasses, iMotions multimodal platform |

### Physical / Hardware / CPG

| Source | Concepts clés extraits |
|---|---|
| **Robert G. Cooper / Stage-Gate International** | Stage-Gate Process (5 stages, 4 décisions : Go/Kill/Hold/Recycle) ; 60+ études industrielles NPD |
| **Procter & Gamble** | « Living It » program (ethnographic embedding) — source de Swiffer et repositionnement de Febreze |
| **NielsenIQ / BASES** | Volumetric forecasting (300 000+ concept tests, 500 000+ forecasts) ; déflation de l'intent déclarée ; décomposition trial rate + repeat rate ; 76% CPG launches failure |
| **The AIM Institute** | New Product Blueprinting — B2B VoC multi-rôles (acheteur économique, évaluateur technique, utilisateur final, achats) ; tens of thousands B2B interviews |
| **Apple** | ANPP (Apple New Product Process) ; hardware prototyping 4-6 weeks cycles ; Steve Jobs focus doctrine (« say no to 1000 things ») ; iPod/iPhone JTBD framing |
| **Tesla** | Vertical integration as physical PM strategy |

### Enterprise PM & Delivery

| Source | Concepts clés extraits |
|---|---|
| **Nicole Forsgren, Jez Humble, Gene Kim** | Accelerate (2018) — DORA 4 metrics ; 2024 State of DevOps Report — Rework Rate, 33 000+ professionals, elite vs. low performer gaps (182x deploy frequency, 127x lead time) |
| **Forsgren, Storey et al.** | SPACE Framework (ACM Queue, 2021) — Satisfaction, Performance, Activity, Communication, Efficiency |
| **Lean Enterprise Institute / Toyota Production System** | Value Stream Mapping ; Muda/Muri/Mura ; Process Cycle Efficiency (<15% typique) ; 70-90% wait time finding |
| **Gene Kim, Kevin Behr, George Spafford** | The Phoenix Project (2013) — VSM applied to software delivery |
| **Eliyahu Goldratt** | The Goal (1984) — Theory of Constraints, 5 Focusing Steps |
| **LaunchDarkly** | Feature flag taxonomy (release, experiment, ops, permission toggles) ; flag lifecycle policy ; progressive delivery patterns |
| **CNCF OpenFeature** | Vendor-neutral feature flag SDK standard (2022) |
| **SPI Research** | 2025 Professional Services Maturity Benchmark (403 firms) — billable utilization benchmarks, Goldilocks Zone 70-80% |
| **Michael Porter** | Competitive Strategy (1980) — Five Forces Framework |
| **Adam Lashinsky** | Inside Apple (2012) — Apple focus doctrine, hardware prototyping cadence |

### Communications / Advertising / PR

| Source | Concepts clés extraits |
|---|---|
| **WPP / Publicis / Omnicom** | Creative Sprint adaptation (2-3 jours vs. 5 jours GV) pour idéation campagnes |
| **Nielsen / Kantar / Ipsos** | Brand tracking, brand health research, media measurement |
| **Tracksuit** | Brand equity tracking (Ritson-backed) |
| **Mark Ritson** | Brand building vs. performance marketing equilibrium |

---

*Rapport compilé le 25 juin 2026 — Product-Kit Benchmark Research Project*
*90+ organisations étudiées · 36 nouveaux soldiers · 31 soldiers enrichis · 42 upgrades doctrinaux*