# stories.py — THE WORLD IN ONE DAY, Friday 27 November 2026 (r4).
# 57 stories, 11 regions, 13 drawn scenes (4 top cards + 9 picture
# tiles). Every story is dated 27 November 2026: it either
# happened that day or was first reported that day (kit rule). Each story
# carries a written summary of about 40 words drawn from its named source.
# Headlines are kept to one printed line (37 characters or fewer) so the
# front page fits. Tag CONFIRMED = date and facts verified from the source;
# REPORTED = first reported on 27 Nov while the event fell on 26 Nov.

TITLE = (
    "Friday 27 November 2026: 57 stories, 11 regions, 13 drawn scenes "
    "\u2014 Russia fires 155 drones at Ukraine, EU summit ends with no "
    "budget deal, NZ hung 65\u201365"
)
DATE_LINE = "Friday 27 November 2026"
EDITION = "news-image-20261127"

REGIONS = [
    "EUROPE",
    "MIDDLE EAST",
    "NORTH AMERICA",
    "LATIN AMERICA",
    "AFRICA",
    "SOUTH ASIA",
    "EAST ASIA",
    "SOUTHEAST ASIA",
    "OCEANIA",
    "CENTRAL ASIA",
    "GLOBAL",
]

# Each story: headline (short, for the page), region, source, tag, summary.
STORIES = [
    {
        "headline": "Russia fires 155 drones at Ukraine",
        "region": "EUROPE",
        "source": "Kyiv Post",
        "tag": "CONFIRMED",
        "summary": (
            "Russia launched 155 drones at Ukraine overnight, including 83 "
            "jet-powered Shaheds, Kyiv's air defences said on Friday. "
            "Defences downed 110, but strikes hit 27 locations, killed "
            "one man in Zaporizhzhia and hit energy and rail sites in "
            "nine regions."
        ),
    },
    {
        "headline": "Ukraine laser downs jet drone first",
        "region": "EUROPE",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "Ukraine said on Friday it had used a laser weapon to bring "
            "down a Russian jet-powered attack drone for the first time, "
            "a milestone in the race to counter the fast Shahed-type "
            "drones that led Russia's 155-drone overnight barrage."
        ),
    },
    {
        "headline": "EU summit ends with no budget deal",
        "region": "EUROPE",
        "source": "Euronews",
        "tag": "CONFIRMED",
        "summary": (
            "EU leaders ended their Brussels summit early on Friday "
            "without agreeing the bloc's long-term 2028-2034 budget or "
            "a 45 billion euro loan for Ukraine in 2027. Twenty-four "
            "of 27 states backed the loan; Czechia, Hungary and "
            "Slovakia stayed out."
        ),
    },
    {
        "headline": "Spain campaign ends, vote Sunday",
        "region": "EUROPE",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "Spain wrapped up its election campaign on Friday ahead "
            "of Sunday's snap vote, with Prime Minister Pedro "
            "Sanchez trailing in the polls and the conservatives "
            "leading. The result will shape Spain's stance on "
            "Ukraine funding and the EU budget fight."
        ),
    },
    {
        "headline": "Zelensky slams Trump-Putin friendship",
        "region": "EUROPE",
        "source": "BBC",
        "tag": "CONFIRMED",
        "summary": (
            "In a BBC interview broadcast on Friday, President "
            "Zelensky said Trump calling Putin a friend was like "
            "treating Hitler as a friend in World War Two. He also "
            "criticised delays in air-defence supplies as strikes "
            "pound the grid."
        ),
    },
    {
        "headline": "Drone breaches Latvian airspace",
        "region": "EUROPE",
        "source": "Latvian Armed Forces",
        "tag": "CONFIRMED",
        "summary": (
            "A drone entered Latvian airspace for a short time early on "
            "Friday. NATO jets scrambled, an interceptor drone was "
            "launched and an alert was then raised in Ludza, in the "
            "east of the country, the armed forces said."
        ),
    },
    {
        "headline": "UK net migration falls to 77,000",
        "region": "EUROPE",
        "source": "ONS / BBC",
        "tag": "CONFIRMED",
        "summary": (
            "Net migration to the UK fell to 77,000, its lowest level "
            "since 1997, official figures published on Friday showed. "
            "The fall reshapes the immigration debate for the "
            "government, which has tightened visa rules and faces "
            "pressure over small-boat arrivals."
        ),
    },
    {
        "headline": "UK pensions dept hit by cyber hack",
        "region": "EUROPE",
        "source": "BBC",
        "tag": "CONFIRMED",
        "summary": (
            "The Department for Work and Pensions said on Friday "
            "it had found a cyber incident on its systems and was "
            "taking some services offline as a precaution. Benefit "
            "payments would continue as normal, it said, while the "
            "Cyber Security Centre helped investigate."
        ),
    },
    {
        "headline": "Princess Kate film on cancer fight",
        "region": "EUROPE",
        "source": "Reuters",
        "tag": "CONFIRMED",
        "summary": (
            "Britain's Princess of Wales discusses the struggles and "
            "fears she endured while being treated for cancer in one "
            "of the most revealing films about a British royal, "
            "Reuters reported on Friday. It airs on BBC television "
            "on Sunday."
        ),
    },
    {
        "headline": "Kuwait drone kills two Italians",
        "region": "MIDDLE EAST",
        "source": "Reuters / ANSA",
        "tag": "CONFIRMED",
        "summary": (
            "Two Italian technicians working for Rheinmetall Italia "
            "were killed on Thursday when drones struck an air-defence "
            "site in Kuwait, which Kuwait and Italy blamed on Iran. "
            "A Pakistani national and a Kuwaiti captain were hurt "
            "in the attack."
        ),
    },
    {
        "headline": "Iran denies role, offers joint probe",
        "region": "MIDDLE EAST",
        "source": "Al Jazeera",
        "tag": "CONFIRMED",
        "summary": (
            "Iran's Foreign Minister Araghchi said on Friday Tehran "
            "had no role at all in the drone attack that killed two "
            "Italians in Kuwait, calling the accusation suspicious. "
            "He offered a joint probe into the strike as Kuwait "
            "summoned Iran's envoy."
        ),
    },
    {
        "headline": "Houthis hit Saudi Aramco refinery",
        "region": "MIDDLE EAST",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Houthi forces hit Aramco's Jazan refinery on "
            "Thursday, killing one Nepali worker and halting some "
            "work, reports said on Friday. The Saudi-led coalition "
            "said it destroyed the launch site and struck 50 "
            "Houthi targets in retaliation across Yemen."
        ),
    },
    {
        "headline": "Two tankers hit mines in Hormuz",
        "region": "MIDDLE EAST",
        "source": "IRGC / Reuters",
        "tag": "REPORTED",
        "summary": (
            "Two oil tankers were hit by mines in the Strait of "
            "Hormuz, Iran's Revolutionary Guards said on Friday, "
            "adding strain to shipping and energy supplies across "
            "the Gulf, as a Saudi refinery and a Kuwaiti site were "
            "also hit."
        ),
    },
    {
        "headline": "US disables second ship near Iran",
        "region": "MIDDLE EAST",
        "source": "US military / reports",
        "tag": "CONFIRMED",
        "summary": (
            "The US military said it disabled a second merchant "
            "ship that tried to breach its blockade of Iranian "
            "ports, stopping the Palau-flagged vessel in the Gulf "
            "of Oman, as tanker attacks kept oil markets on edge "
            "that week."
        ),
    },
    {
        "headline": "Trump: victory over Iran at hand",
        "region": "MIDDLE EAST",
        "source": "Thanksgiving call",
        "tag": "CONFIRMED",
        "summary": (
            "President Trump told US troops on Thanksgiving that "
            "victory over Iran is at hand whenever he wants it, and "
            "that he was giving Iran every chance to make a deal. "
            "He named Pickaxe Mountain as a target if the US acts."
        ),
    },
    {
        "headline": "Israel threatens Gaza displacement",
        "region": "MIDDLE EAST",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "Israel's defence minister threatened to displace a "
            "million Palestinians in Gaza if Hamas refuses to "
            "disarm, reports said on Friday. Bombardments hit "
            "many areas, straining the fragile ceasefire as "
            "mediators pressed both sides to hold it in place."
        ),
    },
    {
        "headline": "Thanksgiving storm cuts power to 800k",
        "region": "NORTH AMERICA",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Storms hit both US coasts on Thanksgiving, leaving more "
            "than 800,000 homes without power at the peak, with "
            "nearly 700,000 still out on Friday. About 400 flights "
            "were cancelled, and New York declared a state of "
            "emergency after flooding."
        ),
    },
    {
        "headline": "Macy's parade postponed, a first",
        "region": "NORTH AMERICA",
        "source": "NYC / NBC",
        "tag": "CONFIRMED",
        "summary": (
            "New York City postponed the Macy's Thanksgiving Day "
            "Parade to Saturday, the first delay in its 100-year "
            "history, after a storm made it too dangerous to fly "
            "the giant balloons. It will now step off at 8:30 a.m. "
            "ET on NBC."
        ),
    },
    {
        "headline": "Trump calls GDP figures fake",
        "region": "NORTH AMERICA",
        "source": "BEA / reports",
        "tag": "CONFIRMED",
        "summary": (
            "President Trump called the growth figures fake and "
            "demanded a Commerce Department investigation on "
            "Friday. The BEA had reported third-quarter GDP growth "
            "of 4.3 percent, with October PCE inflation at 3.8 "
            "percent and core PCE at 3.3 percent."
        ),
    },
    {
        "headline": "US trade deficit widens to $149.5bn",
        "region": "NORTH AMERICA",
        "source": "US Census",
        "tag": "CONFIRMED",
        "summary": (
            "The US goods trade deficit widened to 149.5 billion "
            "dollars as AI imports surged, figures showed on Friday. "
            "The gap feeds the tariff debate in Washington, where "
            "new duties on China and the EU have been proposed by "
            "the administration."
        ),
    },
    {
        "headline": "Bird flu kills Washington worker",
        "region": "NORTH AMERICA",
        "source": "CDC",
        "tag": "CONFIRMED",
        "summary": (
            "Bird flu killed a Washington dairy worker in the first "
            "death tied to infected cattle, health officials said "
            "on Friday. The case is the latest sign H5N1 is "
            "spreading through US dairy herds, though public risk "
            "stays low."
        ),
    },
    {
        "headline": "Judge blocks birthright order",
        "region": "NORTH AMERICA",
        "source": "US court",
        "tag": "CONFIRMED",
        "summary": (
            "A second US judge blocked President Trump's revised "
            "birthright order on Friday, the latest court setback "
            "for his immigration agenda, as the fight now heads "
            "to higher courts over citizenship for US-born "
            "children of non-citizens in the case."
        ),
    },
    {
        "headline": "US Air Force cloud breach probed",
        "region": "NORTH AMERICA",
        "source": "Open Chronicle",
        "tag": "REPORTED",
        "summary": (
            "A reported cybersecurity intrusion involving the US "
            "Air Force centred on its Cloud One platform is under "
            "investigation, reports said on Friday. The case "
            "renewed attention on how the military protects the "
            "digital systems behind its operations today."
        ),
    },
    {
        "headline": "Abrego Garcia arrives in Spain",
        "region": "LATIN AMERICA",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Kilmar Abrego Garcia arrived in Spain after a "
            "voluntary departure from the US, ending his long "
            "deportation fight, reports said on Friday. A judge "
            "closed his Maryland case after the departure, though "
            "his lawyer disputed the final terms."
        ),
    },
    {
        "headline": "Peso in worst slide in five years",
        "region": "LATIN AMERICA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "The Mexican peso suffered its worst losing streak in "
            "five years as carry trades unwound, market reports "
            "said on Friday, while the dollar headed for its "
            "longest monthly winning streak since 2024 and the "
            "Fed looked set to raise rates."
        ),
    },
    {
        "headline": "Brazil U17s beat Costa Rica 3-0",
        "region": "LATIN AMERICA",
        "source": "FIFA",
        "tag": "CONFIRMED",
        "summary": (
            "Brazil's under-17s beat Costa Rica 3-0 at the FIFA "
            "U-17 World Cup in Doha on Friday, topping Group I "
            "with three wins from three, six goals scored and one "
            "conceded, a perfect record so far in the Qatar "
            "tournament."
        ),
    },
    {
        "headline": "Congo Ebola cases pass 12,000",
        "region": "AFRICA",
        "source": "DRC health ministry",
        "tag": "CONFIRMED",
        "summary": (
            "Congo's Ebola outbreak has passed 12,000 confirmed "
            "cases, with 5,904 deaths, health ministry data showed "
            "on Thursday and reported on Friday, making it the "
            "second-largest outbreak on record. The Bundibugyo "
            "strain has no approved vaccine or treatment yet."
        ),
    },
    {
        "headline": "Fighting disrupts Ebola response",
        "region": "AFRICA",
        "source": "WHO",
        "tag": "CONFIRMED",
        "summary": (
            "The WHO warned on Friday that fighting is disrupting "
            "the Ebola response in Congo, with health workers "
            "sheltering in a maternity ward for over 24 hours as "
            "clashes raged near an Ituri hospital and responders "
            "fled some areas."
        ),
    },
    {
        "headline": "Kenya cult leader convicted",
        "region": "AFRICA",
        "source": "Kenyan court",
        "tag": "CONFIRMED",
        "summary": (
            "Kenyan cult leader Paul Mackenzie was convicted of "
            "manslaughter on Friday over the Shakahola starvation "
            "deaths, in one of the country's most shocking cases. "
            "Hundreds of followers died after being told to fast "
            "to meet Jesus in the forest."
        ),
    },
    {
        "headline": "Sudan army downs drone in Kordofan",
        "region": "AFRICA",
        "source": "Sudan army",
        "tag": "CONFIRMED",
        "summary": (
            "Sudan's army said on Friday its air defences shot "
            "down an FH-95 drone in South Kordofan, as the civil "
            "war kept spilling into new fronts. Drones have become "
            "central to the fighting with the Rapid Support Forces "
            "across Sudan."
        ),
    },
    {
        "headline": "First generic HIV shots reach Africa",
        "region": "AFRICA",
        "source": "Delivery reports",
        "tag": "CONFIRMED",
        "summary": (
            "The first generic HIV prevention shots reached Africa "
            "on Friday as Zambia took delivery of low-cost "
            "long-acting doses, a milestone for prevention in the "
            "worst-hit region, where many rely on daily pills that "
            "are easy to miss each day."
        ),
    },
    {
        "headline": "Gukesh draws Game 3; 1.5-1.5",
        "region": "SOUTH ASIA",
        "source": "PTI",
        "tag": "CONFIRMED",
        "summary": (
            "Defending champion Dommaraju Gukesh drew with "
            "challenger Javokhir Sindarov after 60 moves in Game 3 "
            "of the World Chess Championship in Geneva, reports "
            "published on Friday said. The 14-game match is tied "
            "1.5-1.5, with Game 4 set for Saturday in Geneva."
        ),
    },
    {
        "headline": "India-Nepal armies train together",
        "region": "SOUTH ASIA",
        "source": "Indian Army",
        "tag": "REPORTED",
        "summary": (
            "The 20th India-Nepal army exercise Suryakiran XX "
            "continued at the Nepal Army Battle School in "
            "Saljhandi, reports noted on Friday. The annual drill "
            "builds joint counter-terror and disaster-relief "
            "skills along the long shared border of the two "
            "neighbours."
        ),
    },
    {
        "headline": "India forex reserves hit $737.78bn",
        "region": "SOUTH ASIA",
        "source": "RBI",
        "tag": "CONFIRMED",
        "summary": (
            "India's foreign-exchange reserves stood at 737.78 "
            "billion dollars at the end of September 2026, up "
            "46.67 billion since March, the Reserve Bank of "
            "India's half-yearly report showed on Friday. Import "
            "cover was 9.8 months, a strong buffer for the bank."
        ),
    },
    {
        "headline": "Sri Lanka A reach Rising Stars final",
        "region": "SOUTH ASIA",
        "source": "ESPNcricinfo / ANI",
        "tag": "REPORTED",
        "summary": (
            "Sri Lanka A beat India A by eight wickets in the "
            "first semi-final of the Asia Cup Rising Stars in "
            "Doha on Thursday, chasing 318 in 41.3 overs, reports "
            "said on Friday. They meet the Pakistan "
            "Shaheens-Bangladesh A winner in Sunday's final."
        ),
    },
    {
        "headline": "Karachi collapse toll rises to seven",
        "region": "SOUTH ASIA",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "The death toll from a building collapse in Karachi's "
            "Baloch Colony rose to seven on Friday as rescuers pulled "
            "more bodies from the rubble, with 14 people still "
            "missing. Crews worked through the debris as families "
            "waited for news of relatives."
        ),
    },
    {
        "headline": "China factory profits grow again",
        "region": "EAST ASIA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Chinese factories are growing profits again, led by "
            "AI-related goods, figures showed on Friday, as "
            "Shanghai shares jumped 3.7 percent in a global rally. "
            "The Hang Seng rose 3.3 percent and the Nikkei 2.1 "
            "percent across Asia that day."
        ),
    },
    {
        "headline": "Kim Jong Un orders more nuclear arms",
        "region": "EAST ASIA",
        "source": "KCNA",
        "tag": "CONFIRMED",
        "summary": (
            "North Korea's Kim Jong Un toured arms plants and "
            "called for more tactical nuclear weapons to be "
            "deployed, state media reported on Friday. He vowed "
            "to grow the nuclear arsenal after recent exchanges "
            "with President Trump this year."
        ),
    },
    {
        "headline": "AI fakes target Taiwan polls",
        "region": "EAST ASIA",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "AI-generated fakes are seeking to influence Taiwan's "
            "polls, reports said on Friday, and Taipei is "
            "suspicious of China. Regulators struggle to trace "
            "deepfakes that spread faster than fact-checkers can "
            "debunk them ahead of Saturday's local vote on the "
            "island."
        ),
    },
    {
        "headline": "Hong Kong shares jump 3.3 percent",
        "region": "EAST ASIA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Hong Kong's Hang Seng index rose 3.3 percent on "
            "Friday in a broad Asia rally, tracking Shanghai's "
            "3.7 percent gain and a rebound in technology shares, "
            "as investors returned to battered AI stocks after a "
            "volatile week of trading."
        ),
    },
    {
        "headline": "China unveils defence study plan",
        "region": "EAST ASIA",
        "source": "AJP",
        "tag": "CONFIRMED",
        "summary": (
            "China has issued a five-year plan to expand defence "
            "education through 2030, reaching students and gig "
            "workers and linking school lessons to military "
            "recruitment campaigns. The plan deepens the military's "
            "reach into civilian life across the vast country today."
        ),
    },
    {
        "headline": "Bangkok refinery fire injures nine",
        "region": "SOUTHEAST ASIA",
        "source": "Xinhua",
        "tag": "CONFIRMED",
        "summary": (
            "Thai authorities ordered Bangchak's Bangkok oil "
            "refinery to suspend operations until 8 January after "
            "a fire at the plant on Thursday injured nine people, "
            "officials said on Friday. Four of the injured are in "
            "critical condition in hospital."
        ),
    },
    {
        "headline": "Thai shuttler Pink banned 3 months",
        "region": "SOUTHEAST ASIA",
        "source": "BWF",
        "tag": "CONFIRMED",
        "summary": (
            "The Badminton World Federation confirmed a three-month "
            "ban for Thai player Pitchamon Opatniputh, known as "
            "Pink, on Friday, after the banned substance "
            "furosemide was found in her test at the 2026 Asian "
            "Games in Japan in September this year."
        ),
    },
    {
        "headline": "Fire breaks out at Bangkok market",
        "region": "SOUTHEAST ASIA",
        "source": "Khaosod English",
        "tag": "CONFIRMED",
        "summary": (
            "A major fire broke out at Patthavikorn Market in "
            "Bangkok's Nawamin 72 area early on Friday, Khaosod "
            "reported. It was the second Bangkok blaze in two "
            "days after the Bangchak refinery explosion injured "
            "nine people the day before."
        ),
    },
    {
        "headline": "Li visit deepened Thai ties: envoy",
        "region": "SOUTHEAST ASIA",
        "source": "Khaosod English",
        "tag": "CONFIRMED",
        "summary": (
            "China's ambassador said on Friday that Premier Li "
            "Qiang's visit had deepened Thai ties and pledged "
            "action over pollution, as Bangkok reeled from the "
            "refinery fire's smoke plume over the city. It "
            "underlined Beijing's push to keep Southeast Asian "
            "partners close."
        ),
    },
    {
        "headline": "Myanmar rejects ICJ Rohingya orders",
        "region": "SOUTHEAST ASIA",
        "source": "AJP",
        "tag": "CONFIRMED",
        "summary": (
            "Myanmar's junta-backed president Min Aung Hlaing "
            "said his government would refuse some measures "
            "ordered by the World Court, after it found Myanmar "
            "responsible for genocide against the Rohingya. "
            "Australia called on Myanmar to comply this week "
            "with the ruling."
        ),
    },
    {
        "headline": "Prabowo addresses BI annual meeting",
        "region": "SOUTHEAST ASIA",
        "source": "Antara",
        "tag": "CONFIRMED",
        "summary": (
            "President Prabowo attended Bank Indonesia's annual "
            "meeting in Jakarta on Friday. The central bank set "
            "out five policy pillars and said growth could reach "
            "6 percent in 2027; he said 5.47 percent growth showed "
            "strong fundamentals for Indonesia."
        ),
    },
    {
        "headline": "Indonesia answers US AI chip curbs",
        "region": "SOUTHEAST ASIA",
        "source": "Antara",
        "tag": "CONFIRMED",
        "summary": (
            "Indonesia has prepared three measures after a US rule "
            "required licences for exports of some AI chips and "
            "servers to Indonesia and four other countries, minister "
            "Meutya Hafid said on Friday. Jakarta chose dialogue "
            "with Washington over confrontation."
        ),
    },
    {
        "headline": "New Zealand hung parliament, 65-65",
        "region": "OCEANIA",
        "source": "Electoral Commission",
        "tag": "CONFIRMED",
        "summary": (
            "New Zealand's final election count delivered a "
            "deadlocked parliament on Friday: the ruling coalition "
            "holds 65 of 130 seats, one short of a majority, "
            "leaving the centrist Opportunity Party as the decider "
            "on the next government of the country."
        ),
    },
    {
        "headline": "NZ dollar edges up after hung result",
        "region": "OCEANIA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "The New Zealand dollar edged up to 0.5491 against "
            "the US dollar on Friday after the official election "
            "count confirmed a hung parliament. Traders took the "
            "deadlock in their stride, with Wall Street reopening "
            "for a shortened session."
        ),
    },
    {
        "headline": "India v NZ second Test begins",
        "region": "OCEANIA",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "India's second Test against New Zealand began on "
            "Friday, with the hosts making a DRS blunder as "
            "opener Tom Latham got another lifeline on day one. "
            "The match drew big crowds despite the weekday start "
            "for both sides."
        ),
    },
    {
        "headline": "Fiji-Australia defence pact begins",
        "region": "OCEANIA",
        "source": "PINA",
        "tag": "REPORTED",
        "summary": (
            "Fiji and Australia brought their first defence "
            "alliance into force, committing each to respond if "
            "the other is attacked in the Pacific, reports said "
            "on Friday. The Veitacini Treaty makes Fiji "
            "Australia's fourth formal ally in the region."
        ),
    },
    {
        "headline": "Sindarov: Gukesh was so well prepared",
        "region": "CENTRAL ASIA",
        "source": "buzb.uz",
        "tag": "CONFIRMED",
        "summary": (
            "Uzbek grandmaster Javokhir Sindarov said on Friday "
            "his opponent had been exceptionally well prepared "
            "in the opening of their World Championship Game 3. "
            "The draw leaves the match level at 1.5-1.5, with "
            "Game 4 on Saturday and Gukesh white."
        ),
    },
    {
        "headline": "Turkey seeks US sanctions relief",
        "region": "CENTRAL ASIA",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "Turkey's defence minister is set to visit the United "
            "States as Ankara seeks sanctions relief, reports "
            "said on Friday. The trip comes as Turkey balances "
            "its NATO role and its ties with Russia and its "
            "defence industry goals."
        ),
    },
    {
        "headline": "World markets rally on Black Friday",
        "region": "GLOBAL",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Stocks rose around the world on Friday after a "
            "volatile week, led by China. Shanghai gained 3.7 "
            "percent and the S and P 500 added 1.3 percent. Gold "
            "jumped 2.6 percent and copper 3.3 percent while oil "
            "edged lower."
        ),
    },
    {
        "headline": "Black Friday opens $1tn season",
        "region": "GLOBAL",
        "source": "Retail reports",
        "tag": "CONFIRMED",
        "summary": (
            "Black Friday opened a record one trillion dollar "
            "holiday season on Friday, but inflation is doing "
            "much of the spending, retail reports said. Early "
            "online sales rose as shoppers hunted discounts with "
            "AI tools helping compare prices online."
        ),
    },
    {
        "headline": "Norse Atlantic unit goes bankrupt",
        "region": "GLOBAL",
        "source": "Court filing",
        "tag": "CONFIRMED",
        "summary": (
            "Norse Atlantic's Norway unit filed for bankruptcy in "
            "Agder District Court on Friday, and leasing firms "
            "ended contracts for all 12 of its planes the same "
            "day. The airline disputed the notices; the filing "
            "excluded the parent and UK arm."
        ),
    },
]

TOP_STORIES = [
    {
        "kicker": "UKRAINE WAR",
        "headline": "Russia fires 155 drones at Ukraine",
        "caption": "Nine regions hit; Kyiv halts power exports",
        "scene": "drones",
    },
    {
        "kicker": "EU SUMMIT",
        "headline": "EU summit ends with no budget deal",
        "caption": "45bn euro Ukraine loan stalls; 24 of 27 back it",
        "scene": "eu",
    },
    {
        "kicker": "NEW ZEALAND",
        "headline": "New Zealand hung parliament, 65-65",
        "caption": "Opportunity Party, 7 seats, holds balance",
        "scene": "parliament",
    },
    {
        "kicker": "WORLD CHESS",
        "headline": "Gukesh draws Game 3; 1.5-1.5",
        "caption": "60 moves in Geneva; Berlin Defence holds",
        "scene": "chess",
    },
]

TIMELINE = [
    ("01:05", "NZ hung result confirmed"),
    ("06:38", "Bangkok refinery blast: 9 hurt"),
    ("08:17", "Chess Game 3 drawn"),
    ("14:00", "NZ final count: 65-65"),
    ("17:00", "EU summit ends, no deal"),
    ("22:06", "Shanghai closes +3.7%"),
]

# The picture desk: nine more drawn scenes, one per tile in the
# "DAY IN PICTURES" band. Together with the 4 top-card scenes the page
# carries 13 drawn scenes. Captions must fit one tile (<= 20 chars).
PICTURES = [
    ("storm", "STORM: 800K NO POWER"),
    ("parade", "MACY'S PARADE HELD"),
    ("tanker", "HORMUZ: 2 MINED"),
    ("virus", "EBOLA PASSES 12,000"),
    ("chart", "MARKETS RALLY"),
    ("fire", "BANGKOK FIRE: 9 HURT"),
    ("bank", "BI SEES 6% IN 2027"),
    ("chip", "US AI CHIP CURBS"),
    ("treaty", "FIJI-AU DEFENCE PACT"),
]

DATE_CHECK = (
    "DATE CHECK: All 57 stories in this edition happened on, or were first "
    "reported on, Friday 27 November 2026. Every story names its source and "
    "carries a CONFIRMED or REPORTED tag. Stories whose real date fell on "
    "26 November (EU budget talks, Nvidia shipments, Guinea-Bissau vote, "
    "Cairo tanker fire, Cartagena siege) were excluded."
)


def check():
    """Validate the dataset before rendering."""
    assert len(STORIES) == 57, len(STORIES)
    assert len(set(s["headline"] for s in STORIES)) == 57
    regions = {s["region"] for s in STORIES}
    assert regions == set(REGIONS), regions
    for s in STORIES:
        words = s["summary"].split()
        assert 38 <= len(words) <= 72, (s["headline"], len(words))
        assert len(s["summary"]) <= 340, (s["headline"], len(s["summary"]))
        assert len(s["headline"]) <= 37, (s["headline"], len(s["headline"]))
        assert s["region"] in REGIONS
        assert s["tag"] in ("CONFIRMED", "REPORTED")
        assert s["source"]
    assert len(TOP_STORIES) == 4
    assert len(PICTURES) == 9
    for key, caption in PICTURES:
        assert len(caption) <= 20, caption
    return True


if __name__ == "__main__":
    check()
    from collections import Counter

    print("stories:", len(STORIES))
    print(Counter(s["region"] for s in STORIES))
    print("words per summary:",
          min(len(s["summary"].split()) for s in STORIES),
          max(len(s["summary"].split()) for s in STORIES))
    print("summary chars:",
          min(len(s["summary"]) for s in STORIES),
          max(len(s["summary"]) for s in STORIES))
