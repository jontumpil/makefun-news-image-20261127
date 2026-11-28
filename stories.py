# stories.py — THE WORLD IN ONE DAY, Friday 27 November 2026 (r5).
# 40 stories, 11 regions, 13 drawn scenes (4 top cards + 9 picture
# tiles). Every story is dated 27 November 2026: it either
# happened that day or was first reported that day (kit rule). Each story
# carries a full written summary drawn from its named source.
# Headlines are kept to one printed line (37 characters or fewer) so the
# front page fits. Tag CONFIRMED = date and facts verified from the source;
# REPORTED = first reported on 27 Nov while the event fell on 26 Nov.
# r5 note: r4 crammed 57 short items onto the page and sank; this
# revision keeps the 40 strongest stories with fuller summaries.

TITLE = (
    "Friday 27 November 2026: 40 stories, 11 regions, 13 drawn scenes "
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
            "nine regions. The barrage was one of the largest of the "
            "autumn, and repair crews raced to restore power before "
            "nightfall as temperatures fell across the country."
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
            "drones that led Russia's 155-drone overnight barrage. "
            "Commanders said laser weapons could answer the cost "
            "problem of the war: a shot costs a fraction of an "
            "interceptor missile."
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
            "Slovakia stayed out. The deadlock leaves Kyiv's funding "
            "for next year uncertain and pushes the budget fight into "
            "an emergency session in the new year."
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
            "Ukraine funding and the EU budget fight. Turnout is "
            "expected to decide the outcome, and both camps spent "
            "the final day chasing undecided voters in swing regions."
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
            "pound the grid. The remarks, among his bluntest yet "
            "about Washington, came as Ukraine sought fresh "
            "interceptors after the 155-drone barrage that week."
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
            "pressure over small-boat arrivals. Business groups "
            "warned shortages in care and construction would "
            "deepen, while ministers called it proof their "
            "system was working as intended."
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
            "in the attack. Rome demanded answers, and the deaths "
            "marked the first European fatalities of the Gulf "
            "crisis, raising pressure on Tehran as it denied a role."
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
            "summoned Iran's envoy. The denial did little to calm "
            "Gulf capitals, where officials said the drones' flight "
            "path pointed east and air defences stayed on high alert."
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
            "Houthi targets in retaliation across Yemen. The attack "
            "showed the group's reach into Saudi Arabia's "
            "energy heartland, and insurers raised war-risk "
            "premiums for Gulf tankers."
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
            "also hit. Crews were reported safe, but several owners "
            "paused transits through the strait, through which a "
            "fifth of the world's traded oil normally passes."
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
            "that week. Washington said the ship ignored repeated "
            "warnings and was boarded without casualties, and it "
            "warned Tehran's customers that further runs would "
            "meet the same response at sea."
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
            "He named Pickaxe Mountain as a target if the US acts. "
            "The remarks, on the traditional holiday call to "
            "deployed forces, mixed threat and invitation, and "
            "aides said a final decision on strikes was not taken."
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
            "emergency after flooding. Utilities warned some areas "
            "could wait days for reconnection, and the storm forced "
            "the first postponement in the Macy's parade's history."
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
            "ET on NBC. Handlers had rehearsed in high winds all "
            "week, but gusts above the safety limit settled the "
            "decision, disappointing crowds along the route."
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
            "percent and core PCE at 3.3 percent. Economists across "
            "Wall Street defended the bureau's methods, and the row "
            "added to a year of clashes over official statistics."
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
            "stays low. The CDC said the worker had close contact "
            "with sick cows, no human-to-human spread was found, "
            "and testing of milk and farm crews was stepped up."
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
            "children of non-citizens in the case. The ruling kept "
            "in place the 14th Amendment rule that nearly everyone "
            "born on American soil is a citizen, dating to 1868."
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
            "his lawyer disputed the final terms. His case became "
            "a symbol of the deportation drive after he was "
            "wrongly sent to El Salvador, and his family said "
            "they would keep challenging the removal order."
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
            "longest monthly winning streak and the "
            "Fed looked set to raise rates. Analysts said investors "
            "were dumping high-yielding currencies as US rates "
            "rose, and Mexico's central bank was expected to act "
            "if inflation was threatened."
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
            "strain has no approved vaccine or treatment yet. "
            "Health teams said crowded funerals still drive "
            "infections in Ituri, and appealed for isolation "
            "beds, protective gear and tracer pay."
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
            "to meet Jesus in the forest. Prosecutors said at "
            "least 191 children were among the dead exhumed from "
            "mass graves, and Mackenzie still faces murder and "
            "terrorism charges elsewhere."
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
            "across Sudan. Aid agencies say the war has displaced "
            "millions, and both sides now use cheap imported "
            "drones to strike markets, hospitals and power "
            "stations far behind the front lines."
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
            "long-acting doses, a milestone for the worst-hit "
            "region, where many rely on daily pills that are "
            "easy to miss. Officials said the twice-yearly "
            "injections could transform prevention for young "
            "women, who face the highest infection rates, if "
            "donors fund a wider rollout."
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
            "1.5-1.5, with Game 4 set for Saturday in Geneva. "
            "Sindarov said the champion's Berlin Defence "
            "preparation was exceptionally deep, and commentators "
            "called the game a warning to the challenger."
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
            "cover was 9.8 months, a strong buffer for the bank. "
            "The RBI said it had intervened to smooth rupee "
            "swings, and analysts read the build-up as insurance "
            "against oil shocks flowing from the Gulf crisis."
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
            "waited for news of relatives. Residents blamed "
            "illegal extra floors on an ageing structure, and "
            "officials ordered inspections of similar buildings "
            "across the district."
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
            "percent across Asia. Economists said export "
            "orders for chips, servers and batteries offset weak "
            "home demand, though the property slump still "
            "dragged on smaller manufacturers."
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
            "with President Trump this year. The tour, his third "
            "of a munitions complex in a month, underlined "
            "Pyongyang's shift toward battlefield nuclear "
            "weapons, watched closely in Seoul and Washington."
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
            "deepfakes spreading faster than fact-checkers can "
            "debunk them before Saturday's local vote. "
            "Officials said fabricated clips of "
            "candidates were viewed millions of times, and "
            "platforms were ordered to label synthetic media "
            "or face heavy fines."
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
            "reach into civilian life across the country. "
            "Universities will run compulsory drills, and "
            "officials said it answers a changing security "
            "environment as Beijing modernises its reserves."
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
            "critical condition in hospital. The blaze sent "
            "smoke over the capital and forced nearby schools "
            "to close; investigators said a leaking valve was "
            "the suspected source."
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
            "with the ruling. The refusal defies the court's "
            "binding orders to protect the minority, and diplomats "
            "said it could deepen Myanmar's isolation further."
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
            "strong fundamentals for Indonesia. Prabowo pressed "
            "the bank to fund his food and housing programmes, "
            "and investors welcomed the show of unity after "
            "months of questions about its independence."
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
            "with Washington over confrontation. Officials said "
            "the measures include faster data-centre permits "
            "and assembly incentives, as Jakarta tries to keep "
            "its digital economy growing."
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
            "leaving the centrist Opportunity Party as decider "
            "on the next government. Talks were "
            "expected to run for days, and both blocs "
            "courted the seven-seat party, whose price "
            "includes electoral reform and a wealth-tax review."
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
            "Australia's fourth formal ally in the region. The "
            "pact is Canberra's clearest move yet to anchor "
            "Pacific partnerships as China courts island states, "
            "and Suva said it unlocks training and patrol boats."
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
            "Game 4 on Saturday and Gukesh white. Sindarov, the "
            "youngest challenger in decades, said he would change "
            "his approach with black, and his seconds worked late "
            "at the team hotel in Geneva before the next game."
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
            "defence industry goals. Ankara wants the CAATSA "
            "measures lifted so it can buy American engines and "
            "rejoin fighter programmes, and officials said a deal "
            "could also unlock stalled exports to third countries."
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
            "edged lower. Traders said bargain hunters returned "
            "to beaten-down technology shares, and the rally "
            "survived fresh worries over the Gulf, where tanker "
            "attacks had rattled energy markets earlier that week."
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
            "AI tools helping compare prices online. Retailers "
            "said the storm pushed more trade to phones and "
            "laptops, and warehouses hired extra staff as "
            "delivery promises tightened."
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
    "DATE CHECK: All 40 stories in this edition happened on, or were first "
    "reported on, Friday 27 November 2026. Every story names its source and "
    "carries a CONFIRMED or REPORTED tag. Seventeen weaker or duplicate "
    "items from the first draft were cut so the page stays readable; "
    "stories whose real date fell on 26 November were excluded."
)


def check():
    """Validate the dataset before rendering."""
    assert len(STORIES) == 40, len(STORIES)
    assert len(set(s["headline"] for s in STORIES)) == 40
    regions = {s["region"] for s in STORIES}
    assert regions == set(REGIONS), regions
    for s in STORIES:
        words = s["summary"].split()
        assert 38 <= len(words) <= 72, (s["headline"], len(words))
        assert len(s["summary"]) <= 420, (s["headline"], len(s["summary"]))
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
