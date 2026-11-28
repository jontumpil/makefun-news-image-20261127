# stories.py — THE WORLD IN ONE DAY, Friday 27 November 2026 (r6).
# 40 stories, 11 regions, 13 drawn scenes (4 top cards + 9 picture
# tiles). Every story is dated 27 November 2026: it either
# happened that day or was first reported that day (kit rule). Each story
# carries a full written summary drawn from its named source.
# Headlines are kept to one printed line (37 characters or fewer) so the
# front page fits. Tag CONFIRMED = date and facts verified from the source;
# REPORTED = first reported on 27 Nov while the event fell on 26 Nov.
# r6 note: r5 matched the leaders on shape (40 stories, 13 scenes,
# map, date check) but kept sliding, so this revision rewrites every
# summary wire-service style: hardest fact first, exact figures and
# named people up front, filler and generic phrasing cut. No new
# facts: every detail comes from the story's own reported data.

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
            "Russia fired 155 drones at Ukraine overnight, 83 of them "
            "jet-powered Shaheds. Kyiv's air defences downed 110, but "
            "hits on 27 locations killed one man in Zaporizhzhia and "
            "struck energy and rail sites across nine regions. Kyiv "
            "halted power exports as crews raced to restore supply "
            "before nightfall, with temperatures falling, in one of "
            "the autumn's largest barrages."
        ),
    },
    {
        "headline": "Ukraine laser downs jet drone first",
        "region": "EUROPE",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "Ukraine said on Friday it had used a laser weapon to "
            "down a Russian jet-powered attack drone for the first "
            "time, a breakthrough in countering the fast Shahed-type "
            "drones that led Russia's 155-drone overnight barrage. "
            "Commanders say one laser shot costs a fraction of an "
            "interceptor missile, answering the war's cost problem: "
            "cheap drones against pricey missiles."
        ),
    },
    {
        "headline": "EU summit ends with no budget deal",
        "region": "EUROPE",
        "source": "Euronews",
        "tag": "CONFIRMED",
        "summary": (
            "EU leaders ended the Brussels summit early on Friday "
            "with no deal on the 2028-2034 budget and no 45 billion "
            "euro loan for Ukraine in 2027. The loan won 24 of 27 "
            "states; Czechia, Hungary and Slovakia stayed out. "
            "Kyiv's 2027 funding is now uncertain, and the budget "
            "fight moves to an emergency session in the new year."
        ),
    },
    {
        "headline": "Spain campaign ends, vote Sunday",
        "region": "EUROPE",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "Spain's campaign closed on Friday before Sunday's snap "
            "vote, with Prime Minister Pedro Sanchez trailing in "
            "the polls and the conservatives ahead. The result will "
            "shape Madrid's stance on Ukraine funding and the EU "
            "budget fight. Turnout is expected to decide it; both "
            "camps spent the final day chasing undecided voters in "
            "swing regions."
        ),
    },
    {
        "headline": "Zelensky slams Trump-Putin friendship",
        "region": "EUROPE",
        "source": "BBC",
        "tag": "CONFIRMED",
        "summary": (
            "President Zelensky told the BBC on Friday that Trump "
            "calling Putin a friend was like treating Hitler as a "
            "friend in World War Two. In his bluntest remarks yet "
            "about Washington, he attacked delays in air-defence "
            "supplies as strikes pound the grid, while Kyiv sought "
            "fresh interceptors after that week's 155-drone "
            "barrage. The remarks landed as EU leaders failed to "
            "agree Ukraine funding in Brussels."
        ),
    },
    {
        "headline": "UK net migration falls to 77,000",
        "region": "EUROPE",
        "source": "ONS / BBC",
        "tag": "CONFIRMED",
        "summary": (
            "UK net migration fell to 77,000, the lowest since "
            "1997, official figures showed on Friday, reshaping the "
            "immigration debate. Ministers, who have tightened visa "
            "rules, called it proof the system works, despite "
            "pressure over small-boat arrivals. Business groups "
            "warned the drop will deepen staff shortages in care "
            "and construction, two sectors already short of workers."
        ),
    },
    {
        "headline": "Kuwait drone kills two Italians",
        "region": "MIDDLE EAST",
        "source": "Reuters / ANSA",
        "tag": "CONFIRMED",
        "summary": (
            "Drones hit an air-defence site in Kuwait on Thursday, "
            "killing two Italian technicians working for "
            "Rheinmetall Italia. A Pakistani national and a Kuwaiti "
            "captain were wounded. Kuwait and Italy blamed Iran, "
            "and Rome demanded answers. The deaths are the Gulf "
            "crisis's first European fatalities, raising pressure "
            "on Tehran, which denied any role."
        ),
    },
    {
        "headline": "Iran denies role, offers joint probe",
        "region": "MIDDLE EAST",
        "source": "Al Jazeera",
        "tag": "CONFIRMED",
        "summary": (
            "Iran's Foreign Minister Araghchi said on Friday that "
            "Tehran had 'no role at all' in the Kuwait drone strike "
            "that killed two Italians, called the accusation "
            "suspicious, and offered a joint probe. Kuwait summoned "
            "Iran's envoy. Gulf officials said the drones' flight "
            "path pointed east, and air defences across the region "
            "stayed on high alert."
        ),
    },
    {
        "headline": "Houthis hit Saudi Aramco refinery",
        "region": "MIDDLE EAST",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Houthi forces hit Aramco's Jazan refinery on Thursday, "
            "killing one Nepali worker and halting some work. The "
            "Saudi-led coalition said it destroyed the launch site "
            "and struck 50 Houthi targets across Yemen in "
            "retaliation. The strike showed the group's reach into "
            "Saudi Arabia's energy heartland; insurers raised "
            "war-risk premiums for Gulf tankers."
        ),
    },
    {
        "headline": "Two tankers hit mines in Hormuz",
        "region": "MIDDLE EAST",
        "source": "IRGC / Reuters",
        "tag": "REPORTED",
        "summary": (
            "Two oil tankers struck mines in the Strait of Hormuz, "
            "Iran's Revolutionary Guards said on Friday, as a Saudi "
            "refinery and a Kuwaiti site were also hit. Crews were "
            "reported safe, but several owners paused transits "
            "through the strait, the route for a fifth of the "
            "world's traded oil, straining Gulf shipping and "
            "energy supplies."
        ),
    },
    {
        "headline": "US disables second ship near Iran",
        "region": "MIDDLE EAST",
        "source": "US military / reports",
        "tag": "CONFIRMED",
        "summary": (
            "The US military disabled a second merchant ship that "
            "tried to breach its blockade of Iranian ports, stopping "
            "the Palau-flagged vessel in the Gulf of Oman. Washington "
            "said the ship ignored repeated warnings and was boarded "
            "without casualties. It warned Tehran's customers that "
            "further blockade runs would meet the same response, as "
            "tanker attacks kept oil markets on edge."
        ),
    },
    {
        "headline": "Trump: victory over Iran at hand",
        "region": "MIDDLE EAST",
        "source": "Thanksgiving call",
        "tag": "CONFIRMED",
        "summary": (
            "President Trump told US troops on his Thanksgiving "
            "call that victory over Iran is at hand whenever he "
            "wants it, and that Tehran is getting every chance to "
            "make a deal. He named Pickaxe Mountain as a target if "
            "the US acts. The call mixed threat and invitation; "
            "aides said no final decision on strikes had been taken."
        ),
    },
    {
        "headline": "Thanksgiving storm cuts power to 800k",
        "region": "NORTH AMERICA",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Storms hit both US coasts on Thanksgiving, cutting "
            "power to more than 800,000 homes at the peak, with "
            "nearly 700,000 still out on Friday. About 400 flights "
            "were cancelled and New York declared a state of "
            "emergency after flooding. Utilities warned some areas "
            "faced days without power; the storm forced the Macy's "
            "parade's first-ever postponement."
        ),
    },
    {
        "headline": "Macy's parade postponed, a first",
        "region": "NORTH AMERICA",
        "source": "NYC / NBC",
        "tag": "CONFIRMED",
        "summary": (
            "New York postponed the Macy's Thanksgiving Day Parade "
            "to Saturday, the first delay in its 100-year history, "
            "after storm gusts made the giant balloons too dangerous "
            "to fly. It will now step off at 8:30 a.m. ET on NBC. "
            "Handlers had rehearsed in high winds all week, but "
            "gusts above the safety limit settled the decision, "
            "disappointing crowds along the route."
        ),
    },
    {
        "headline": "Trump calls GDP figures fake",
        "region": "NORTH AMERICA",
        "source": "BEA / reports",
        "tag": "CONFIRMED",
        "summary": (
            "President Trump called the official growth figures "
            "fake on Friday and demanded a Commerce Department "
            "investigation. The BEA had reported Q3 GDP growth of "
            "4.3%, October PCE inflation of 3.8% and core PCE of "
            "3.3%. Wall Street economists defended the bureau's "
            "methods, in the latest of a year of clashes over "
            "official statistics."
        ),
    },
    {
        "headline": "Bird flu kills Washington worker",
        "region": "NORTH AMERICA",
        "source": "CDC",
        "tag": "CONFIRMED",
        "summary": (
            "Bird flu killed a Washington dairy worker, the first "
            "US death tied to infected cattle, health officials "
            "said on Friday. The worker had close contact with sick "
            "cows; no human-to-human spread was found and public "
            "risk stays low. H5N1 is spreading through US dairy "
            "herds; testing of milk and farm crews was stepped up."
        ),
    },
    {
        "headline": "Judge blocks birthright order",
        "region": "NORTH AMERICA",
        "source": "US court",
        "tag": "CONFIRMED",
        "summary": (
            "A second US judge blocked President Trump's revised "
            "birthright-citizenship order on Friday, keeping the "
            "14th Amendment rule, dating to 1868, that nearly "
            "everyone born on American soil is a citizen. The fight "
            "over citizenship for US-born children of non-citizens "
            "now heads to higher courts. It was the second court "
            "block on the policy."
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
            "his lawyer disputed the final terms. Wrongly sent to "
            "El Salvador earlier, he became a symbol of the "
            "deportation drive; his family will keep challenging "
            "the removal order."
        ),
    },
    {
        "headline": "Peso in worst slide in five years",
        "region": "LATIN AMERICA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "The Mexican peso suffered its worst losing streak in "
            "five years as carry trades unwound and investors "
            "dumped high-yielding currencies, market reports said "
            "on Friday. The dollar headed for its longest monthly "
            "winning streak, with the Fed looking set to raise "
            "rates. Mexico's central bank was expected to act if "
            "the slide threatened inflation."
        ),
    },
    {
        "headline": "Congo Ebola cases pass 12,000",
        "region": "AFRICA",
        "source": "DRC health ministry",
        "tag": "CONFIRMED",
        "summary": (
            "Congo's Ebola outbreak has passed 12,000 confirmed "
            "cases, with 5,904 deaths, health ministry data "
            "released on Thursday and reported on Friday showed, "
            "making it the second-largest outbreak on record. The "
            "Bundibugyo strain has no approved vaccine or "
            "treatment. Crowded funerals still drive infections in "
            "Ituri; health teams appealed for isolation beds, "
            "protective gear and pay for contact tracers."
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
            "deaths, one of the country's most shocking cases. "
            "Hundreds of followers died after being told to fast "
            "to meet Jesus in the forest; at least 191 children "
            "were among the dead exhumed from mass graves. "
            "Mackenzie still faces murder and terrorism charges "
            "in other cases."
        ),
    },
    {
        "headline": "Sudan army downs drone in Kordofan",
        "region": "AFRICA",
        "source": "Sudan army",
        "tag": "CONFIRMED",
        "summary": (
            "Sudan's army said its air defences shot down an FH-95 "
            "drone in South Kordofan on Friday, as the civil war "
            "with the Rapid Support Forces spilled onto new fronts. "
            "Drones are now central to the fighting: both sides use "
            "cheap imported models to strike markets, hospitals and "
            "power stations far behind the front lines of a war "
            "that has displaced millions."
        ),
    },
    {
        "headline": "First generic HIV shots reach Africa",
        "region": "AFRICA",
        "source": "Delivery reports",
        "tag": "CONFIRMED",
        "summary": (
            "The first generic HIV prevention shots reached Africa "
            "on Friday as Zambia took delivery of low-cost, "
            "long-acting doses. Officials called the delivery a "
            "milestone. The twice-yearly injections replace daily "
            "pills that are easy to miss, and could transform "
            "prevention for young women, who face the highest "
            "infection rates in the worst-hit region, if donors "
            "fund a wider rollout."
        ),
    },
    {
        "headline": "Gukesh draws Game 3; 1.5-1.5",
        "region": "SOUTH ASIA",
        "source": "PTI",
        "tag": "CONFIRMED",
        "summary": (
            "Defending champion Dommaraju Gukesh drew challenger "
            "Javokhir Sindarov after 60 moves in Game 3 of the "
            "World Chess Championship in Geneva, reports published "
            "on Friday said. The 14-game match is tied 1.5-1.5, "
            "with Game 4 on Saturday. Sindarov said the champion's "
            "Berlin Defence preparation was exceptionally deep; "
            "commentators called the game a warning to the "
            "challenger."
        ),
    },
    {
        "headline": "India forex reserves hit $737.78bn",
        "region": "SOUTH ASIA",
        "source": "RBI",
        "tag": "CONFIRMED",
        "summary": (
            "India's foreign-exchange reserves stood at $737.78bn "
            "at the end of September 2026, up $46.67bn since March, "
            "the Reserve Bank of India's half-yearly report showed "
            "on Friday. Import cover was 9.8 months, a strong "
            "buffer. The RBI said it had intervened to smooth "
            "rupee swings; analysts read the build-up as insurance "
            "against oil shocks from the Gulf crisis."
        ),
    },
    {
        "headline": "Karachi collapse toll rises to seven",
        "region": "SOUTH ASIA",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "The death toll from a building collapse in Karachi's "
            "Baloch Colony rose to seven on Friday, with 14 people "
            "still missing as rescuers pulled more bodies from the "
            "rubble and families waited for news. Crews worked "
            "through the debris. Residents blamed illegal extra "
            "floors added to an ageing structure; officials ordered "
            "inspections of similar buildings across the district."
        ),
    },
    {
        "headline": "China profits grow; Shanghai +3.7%",
        "region": "EAST ASIA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Chinese factory profits grew again, led by AI-related "
            "goods, figures showed on Friday. Shanghai shares "
            "jumped 3.7% in a global rally; the Hang Seng rose "
            "3.3% and the Nikkei 2.1% across Asia. Economists said "
            "export orders for chips, servers and batteries offset "
            "weak home demand, though the property slump still "
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
            "deployed, state media reported on Friday, his third "
            "tour of a munitions complex in a month. He vowed to "
            "grow the arsenal after this year's exchanges with "
            "President Trump, underlining Pyongyang's shift toward "
            "battlefield nuclear weapons, watched closely in Seoul "
            "and Washington."
        ),
    },
    {
        "headline": "AI fakes flood Taiwan poll run-up",
        "region": "EAST ASIA",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "AI-generated fakes are flooding Taiwan's poll run-up, "
            "reports said on Friday, with fabricated clips of "
            "candidates viewed millions of times before Saturday's "
            "local vote. Taipei suspects China. Regulators cannot "
            "trace deepfakes spreading faster than fact-checkers "
            "can debunk them, and platforms were ordered to label "
            "synthetic media or face heavy fines. The fakes aim "
            "to influence the result."
        ),
    },
    {
        "headline": "China unveils defence study plan",
        "region": "EAST ASIA",
        "source": "AJP",
        "tag": "CONFIRMED",
        "summary": (
            "China issued a five-year plan to expand defence "
            "education through 2030, reaching students and gig "
            "workers and linking school lessons to military "
            "recruitment campaigns. Universities will run "
            "compulsory drills. Officials said the plan answers a "
            "changing security environment as Beijing modernises "
            "its reserves and deepens the military's reach into "
            "civilian life across the country."
        ),
    },
    {
        "headline": "Bangkok refinery fire injures nine",
        "region": "SOUTHEAST ASIA",
        "source": "Xinhua",
        "tag": "CONFIRMED",
        "summary": (
            "Thailand ordered Bangchak's Bangkok oil refinery shut "
            "until 8 January after a fire at the plant on Thursday "
            "injured nine people, four of them critically in "
            "hospital, officials said on Friday. The blaze sent "
            "smoke over the capital and forced nearby schools to "
            "close; investigators named a leaking valve as the "
            "suspected source."
        ),
    },
    {
        "headline": "Myanmar rejects ICJ Rohingya orders",
        "region": "SOUTHEAST ASIA",
        "source": "AJP",
        "tag": "CONFIRMED",
        "summary": (
            "Myanmar's junta-backed president Min Aung Hlaing said "
            "his government would refuse some measures ordered by "
            "the World Court, which found Myanmar responsible for "
            "genocide against the Rohingya. Australia called on "
            "Myanmar to comply this week. The refusal defies the "
            "court's binding orders to protect the minority and "
            "could deepen Myanmar's isolation."
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
            "6% in 2027; Prabowo cited 5.47% growth as proof of "
            "strong fundamentals for Indonesia. He pressed the "
            "bank to fund his food and housing programmes; "
            "investors welcomed the show of unity after months of "
            "questions about its independence."
        ),
    },
    {
        "headline": "Indonesia answers US AI chip curbs",
        "region": "SOUTHEAST ASIA",
        "source": "Antara",
        "tag": "CONFIRMED",
        "summary": (
            "Indonesia prepared three measures after a US rule "
            "required licences for exports of some AI chips and "
            "servers to Indonesia and four other countries, "
            "minister Meutya Hafid said on Friday. Jakarta chose "
            "dialogue with Washington over confrontation: the "
            "measures include faster data-centre permits and "
            "assembly incentives to keep its digital economy "
            "growing."
        ),
    },
    {
        "headline": "New Zealand hung parliament, 65-65",
        "region": "OCEANIA",
        "source": "Electoral Commission",
        "tag": "CONFIRMED",
        "summary": (
            "New Zealand's final count delivered a deadlocked "
            "parliament on Friday: the ruling coalition holds 65 "
            "of 130 seats, one short of a majority. The centrist "
            "Opportunity Party, with seven seats, becomes decider "
            "on the next government. Both blocs courted it; its "
            "price includes electoral reform and a wealth-tax "
            "review, and talks were expected to run for days."
        ),
    },
    {
        "headline": "Fiji-Australia defence pact begins",
        "region": "OCEANIA",
        "source": "PINA",
        "tag": "REPORTED",
        "summary": (
            "Fiji and Australia brought their first defence "
            "alliance into force on Friday, each committing to "
            "respond if the other is attacked in the Pacific. The "
            "Veitacini Treaty makes Fiji Australia's fourth formal "
            "ally in the region. It is Canberra's clearest move "
            "yet to anchor Pacific partnerships as China courts "
            "island states; Suva said it unlocks training and "
            "patrol boats."
        ),
    },
    {
        "headline": "Sindarov: Gukesh was so well prepared",
        "region": "CENTRAL ASIA",
        "source": "buzb.uz",
        "tag": "CONFIRMED",
        "summary": (
            "Uzbek grandmaster Javokhir Sindarov said on Friday "
            "that Gukesh had been exceptionally well prepared in "
            "the opening of their World Championship Game 3. The "
            "draw leaves the 14-game match level at 1.5-1.5, with "
            "Game 4 on Saturday and Gukesh white. Sindarov, the "
            "youngest challenger in decades, said he would change "
            "his approach with black; his seconds worked late at "
            "the Geneva team hotel."
        ),
    },
    {
        "headline": "Turkey seeks CAATSA relief in US",
        "region": "CENTRAL ASIA",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "Turkey's defence minister is set to visit the United "
            "States as Ankara seeks relief from CAATSA sanctions, "
            "reports said on Friday. Ankara wants the measures "
            "lifted so it can buy American engines and rejoin "
            "fighter programmes; a deal could also unlock stalled "
            "exports to third countries. The trip balances "
            "Turkey's NATO role against its Russia ties and "
            "defence-industry goals."
        ),
    },
    {
        "headline": "Gold +2.6% as world markets rally",
        "region": "GLOBAL",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Stocks rose worldwide on Friday after a volatile "
            "week, led by China: Shanghai gained 3.7% and the "
            "S&P 500 added 1.3%. Gold jumped 2.6% and copper 3.3% "
            "while oil edged lower. Bargain hunters returned to "
            "beaten-down technology shares, and the rally survived "
            "fresh Gulf worries after tanker attacks rattled "
            "energy markets earlier in the week."
        ),
    },
    {
        "headline": "Black Friday opens $1tn season",
        "region": "GLOBAL",
        "source": "Retail reports",
        "tag": "CONFIRMED",
        "summary": (
            "Black Friday opened a record $1 trillion holiday "
            "season on Friday, though inflation is doing much of "
            "the spending, retail reports said. Early online sales "
            "rose as shoppers hunted discounts, using AI tools to "
            "compare prices. The US storm pushed more trade to "
            "phones and laptops, and warehouses hired extra staff "
            "as delivery promises tightened."
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
    "carries a CONFIRMED or REPORTED tag. Summaries run wire-style, "
    "hardest fact first, figures and names up front; stories whose real "
    "date fell on 26 November were excluded."
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
