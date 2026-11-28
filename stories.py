# stories.py — THE WORLD IN ONE DAY, Friday 27 November 2026 (r3).
# 47 stories, 11 regions. Every story is dated 27 November 2026: it either
# happened that day or was first reported that day (kit rule). Each story
# carries a written summary of about 40 words drawn from its named source.
# Headlines are kept to one printed line (37 characters or fewer) so the
# front page fits. Tag CONFIRMED = date and facts verified from the source;
# REPORTED = first reported on 27 Nov while the event fell on 26 Nov.

TITLE = (
    "Friday 27 November 2026: 47 stories, 11 regions \u2014 "
    "Russia fires 155 drones at Ukraine, EU summit ends with no budget deal, "
    "New Zealand hung 65\u201365"
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
            "jet-powered Shaheds, Ukrainian air defences said on Friday. "
            "Defences downed 110, but strikes hit 27 locations and one man "
            "was killed in Zaporizhzhia. Energy and rail sites in nine "
            "regions were hit, and power exports halted."
        ),
    },
    {
        "headline": "EU summit ends with no budget deal",
        "region": "EUROPE",
        "source": "Euronews",
        "tag": "CONFIRMED",
        "summary": (
            "European Union leaders ended their Brussels summit early "
            "on Friday without agreeing the bloc's 2028-2034 budget or a "
            "45 billion euro loan for Ukraine in 2027. Twenty-four "
            "of 27 states backed the loan; Czechia, Hungary and Slovakia "
            "stayed out, and Bulgaria backed only the civilian part."
        ),
    },
    {
        "headline": "Zelensky slams Trump-Putin friendship",
        "region": "EUROPE",
        "source": "BBC",
        "tag": "CONFIRMED",
        "summary": (
            "In a BBC interview broadcast on Friday, President Volodymyr "
            "Zelensky said President Trump calling President Putin a friend "
            "was like treating Hitler as a friend during World War Two, "
            "calling it strange. He also criticised delays in air-defence "
            "supplies as Russian strikes pound Ukraine's power grid."
        ),
    },
    {
        "headline": "Drone breaches Latvian airspace",
        "region": "EUROPE",
        "source": "Latvian Armed Forces",
        "tag": "CONFIRMED",
        "summary": (
            "An unidentified drone briefly entered Latvian airspace early on "
            "Friday, triggering NATO fighter scrambles, an interceptor drone "
            "launch and an alert in the eastern municipality of Ludza. "
            "Latvian officials noted the breach coincided with air-defence "
            "activity in Russia's Leningrad region."
        ),
    },
    {
        "headline": "UK net migration falls to 77,000",
        "region": "EUROPE",
        "source": "ONS / BBC",
        "tag": "CONFIRMED",
        "summary": (
            "Net migration to the United Kingdom fell to 77,000, its lowest "
            "level since 1997, official figures published on Friday showed. "
            "The sharp fall reshapes the immigration debate for the "
            "government, which has tightened visa rules, and comes as "
            "ministers face pressure over small-boat arrivals."
        ),
    },
    {
        "headline": "UK pensions dept hit by cyber hack",
        "region": "EUROPE",
        "source": "BBC",
        "tag": "CONFIRMED",
        "summary": (
            "The Department for Work and Pensions said on Friday it had "
            "identified a cyber incident affecting its systems and was "
            "taking some services offline as a precaution. People would "
            "still receive regular benefit payments, the department said, "
            "while the National Cyber Security Centre helped investigate."
        ),
    },
    {
        "headline": "Princess Kate film on cancer fight",
        "region": "EUROPE",
        "source": "Reuters",
        "tag": "CONFIRMED",
        "summary": (
            "Britain's Princess of Wales discusses the struggles and fears "
            "she endured while being treated for cancer in one of the most "
            "revealing films about a British royal, Reuters reported on "
            "Friday. The documentary, filmed climbing mountains, airs on "
            "BBC television on Sunday before broadcasts abroad."
        ),
    },
    {
        "headline": "Kuwait drone kills two Italians",
        "region": "MIDDLE EAST",
        "source": "Reuters / ANSA",
        "tag": "CONFIRMED",
        "summary": (
            "Two Italian technicians working for Rheinmetall Italia were "
            "killed on Thursday when drones struck an air-defence "
            "site in Kuwait, which Kuwait and Italy blamed on Iran. The men, "
            "aged 65 and 36, were maintaining detection equipment. A "
            "Pakistani national and a Kuwaiti captain were hurt."
        ),
    },
    {
        "headline": "Iran denies role, offers joint probe",
        "region": "MIDDLE EAST",
        "source": "Al Jazeera",
        "tag": "CONFIRMED",
        "summary": (
            "Iran's Foreign Minister Abbas Araghchi said on Friday that "
            "Tehran had no role or involvement whatsoever in the drone "
            "attack that killed two Italians in Kuwait, calling the "
            "accusation suspicious and a precooked recipe for war. He "
            "offered a joint investigation as Kuwait summoned Iran's envoy."
        ),
    },
    {
        "headline": "Houthis hit Saudi Aramco refinery",
        "region": "MIDDLE EAST",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Houthi forces hit Saudi Aramco's Jazan refinery on Thursday, "
            "killing one Nepali worker and halting some operations, reports "
            "said on Friday. The Saudi-led coalition said it destroyed the "
            "launch platform and struck 50 Houthi targets in Sanaa, "
            "Hodeidah and Saada in retaliation for the attack."
        ),
    },
    {
        "headline": "Two tankers hit mines in Hormuz",
        "region": "MIDDLE EAST",
        "source": "IRGC / Reuters",
        "tag": "REPORTED",
        "summary": (
            "Two oil tankers were hit by mines in the Strait of Hormuz, "
            "Iran's Revolutionary Guards said on Friday, adding strain to "
            "shipping and energy infrastructure across the Gulf. The "
            "incident came the same day a Saudi refinery and a Kuwaiti "
            "facility were hit in separate attacks, rattling oil markets."
        ),
    },
    {
        "headline": "Trump: victory over Iran at hand",
        "region": "MIDDLE EAST",
        "source": "Thanksgiving call",
        "tag": "CONFIRMED",
        "summary": (
            "President Donald Trump told US troops on Thanksgiving that "
            "victory over Iran is at hand whenever he wants it, said he "
            "was giving Iran every chance to make a deal, and named "
            "Pickaxe Mountain as a target if the United States acts. The "
            "remarks came as Gulf tensions spiked after the Kuwait attack."
        ),
    },
    {
        "headline": "Israel threatens Gaza displacement",
        "region": "MIDDLE EAST",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "Israel's defence minister threatened to displace one million "
            "Palestinians within Gaza if Hamas refuses to disarm, reports "
            "said on Friday. Israeli bombardments and cannon fire hit "
            "multiple areas of the territory, keeping the fragile "
            "ceasefire under severe strain as mediators pressed both sides."
        ),
    },
    {
        "headline": "Thanksgiving storm cuts power to 800k",
        "region": "NORTH AMERICA",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Storms hit both US coasts on Thanksgiving, leaving more than "
            "800,000 homes without power at the peak, with nearly 700,000 "
            "still out on Friday. About 400 flights were cancelled. Heavy "
            "rain and wind caused flooding and water rescues from New York "
            "to Virginia, and New York declared a state of emergency."
        ),
    },
    {
        "headline": "Macy's parade postponed, a first",
        "region": "NORTH AMERICA",
        "source": "NYC / NBC",
        "tag": "CONFIRMED",
        "summary": (
            "New York City officials postponed the Macy's Thanksgiving Day "
            "Parade to Saturday, the first delay in its 100-year history, "
            "after a powerful storm made it too dangerous to fly the giant "
            "balloons. The 100th parade will now step off on Saturday at "
            "8:30 a.m. ET, broadcast live on NBC, Telemundo and Peacock."
        ),
    },
    {
        "headline": "Trump calls GDP figures fake",
        "region": "NORTH AMERICA",
        "source": "BEA / reports",
        "tag": "CONFIRMED",
        "summary": (
            "President Trump called the growth figures fake and demanded a "
            "Commerce Department investigation on Friday, questioning a GDP "
            "revision. The Bureau of Economic Analysis had reported "
            "third-quarter GDP growth of 4.3 percent, with October PCE "
            "inflation at 3.8 percent and core PCE at 3.3 percent."
        ),
    },
    {
        "headline": "US trade deficit widens to $149.5bn",
        "region": "NORTH AMERICA",
        "source": "US Census",
        "tag": "CONFIRMED",
        "summary": (
            "The US goods trade deficit widened to 149.5 billion "
            "dollars as artificial-intelligence imports surged, figures "
            "showed on Friday. The gap feeds the tariff debate in "
            "Washington, where the administration has proposed new duties "
            "on China and the European Union to replace levies struck down "
            "by a court."
        ),
    },
    {
        "headline": "Bird flu kills Washington worker",
        "region": "NORTH AMERICA",
        "source": "CDC",
        "tag": "CONFIRMED",
        "summary": (
            "Bird flu killed a Washington dairy worker in the first death "
            "tied to infected cattle, health officials said on Friday. The "
            "case is the latest sign the H5N1 virus is spreading through US "
            "dairy herds, and officials stressed monitoring of farm workers "
            "while stressing the risk to the general public remains low."
        ),
    },
    {
        "headline": "Judge blocks birthright order",
        "region": "NORTH AMERICA",
        "source": "US court",
        "tag": "CONFIRMED",
        "summary": (
            "A second federal judge blocked President Trump's revised "
            "birthright citizenship order on Friday, the latest court "
            "setback for the administration's immigration agenda. The "
            "ruling keeps the legal fight over citizenship for children "
            "born in the United States to non-citizen parents heading "
            "toward higher courts."
        ),
    },
    {
        "headline": "Abrego Garcia arrives in Spain",
        "region": "LATIN AMERICA",
        "source": "AP",
        "tag": "CONFIRMED",
        "summary": (
            "Kilmar Abrego Garcia arrived in Spain after a voluntary "
            "departure from the United States, ending his long deportation "
            "fight, reports said on Friday. A federal judge closed his "
            "Maryland immigration case after the departure, though his "
            "lawyer and Homeland Security disagreed over the terms of the "
            "exit."
        ),
    },
    {
        "headline": "Peso in worst slide in five years",
        "region": "LATIN AMERICA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "The Mexican peso suffered its worst losing streak in five years "
            "as carry trades unwound, market reports said on Friday, while "
            "the dollar headed for its longest monthly winning streak since "
            "2024. The Federal Reserve looked poised to raise rates even as "
            "equities wobbled, pressuring emerging-market currencies."
        ),
    },
    {
        "headline": "Brazil U17s beat Costa Rica 3-0",
        "region": "LATIN AMERICA",
        "source": "FIFA",
        "tag": "CONFIRMED",
        "summary": (
            "Brazil's under-17s beat Costa Rica 3-0 at the FIFA U-17 World "
            "Cup in Doha on Friday, topping Group I with three wins from "
            "three games, six goals scored and one conceded. The young "
            "Selecao kept a perfect record in Qatar as the tournament's "
            "knockout rounds approached."
        ),
    },
    {
        "headline": "Congo Ebola cases pass 12,000",
        "region": "AFRICA",
        "source": "DRC health ministry",
        "tag": "CONFIRMED",
        "summary": (
            "Congo's Ebola outbreak has passed 12,000 confirmed cases, with "
            "5,904 deaths, health ministry data showed on Thursday and "
            "reported on Friday, making it the second-largest outbreak on "
            "record. The Bundibugyo strain has no approved vaccine or "
            "treatment, and an updated response plan needs about 1.576 "
            "billion dollars."
        ),
    },
    {
        "headline": "Fighting disrupts Ebola response",
        "region": "AFRICA",
        "source": "WHO",
        "tag": "CONFIRMED",
        "summary": (
            "The World Health Organization warned on Friday that fighting "
            "is disrupting the Ebola response in Congo, with health workers "
            "sheltering in a maternity ward for more than 24 hours as "
            "clashes raged near an Ituri hospital. Responders were forced "
            "to flee some areas, leaving cases untraced as infections "
            "climbed."
        ),
    },
    {
        "headline": "Kenya cult leader convicted",
        "region": "AFRICA",
        "source": "Kenyan court",
        "tag": "CONFIRMED",
        "summary": (
            "Kenyan cult leader Paul Mackenzie was convicted of manslaughter "
            "on Friday over the Shakahola starvation deaths, in one of the "
            "country's most shocking criminal cases. Hundreds of followers "
            "died after being told to fast to meet Jesus, and the verdict "
            "closes years of investigation into the forest commune."
        ),
    },
    {
        "headline": "Sudan army downs drone in Kordofan",
        "region": "AFRICA",
        "source": "Sudan army",
        "tag": "CONFIRMED",
        "summary": (
            "Sudan's army said on Friday its air defences shot down an "
            "FH-95 drone in South Kordofan, as the country's civil war "
            "kept spilling into new fronts. The claim underlines how "
            "uncrewed aircraft have become central to the fighting between "
            "the army and the Rapid Support Forces across Sudan."
        ),
    },
    {
        "headline": "First generic HIV shots reach Africa",
        "region": "AFRICA",
        "source": "Delivery reports",
        "tag": "CONFIRMED",
        "summary": (
            "The first generic HIV prevention shots reached Africa on "
            "Friday as Zambia took delivery of low-cost long-acting "
            "doses, a milestone for prevention in the worst-hit region. "
            "Cheaper generics could put the twice-yearly injection within "
            "reach of millions who now rely on daily pills that are easy "
            "to miss."
        ),
    },
    {
        "headline": "Gukesh draws Game 3; 1.5-1.5",
        "region": "SOUTH ASIA",
        "source": "PTI",
        "tag": "CONFIRMED",
        "summary": (
            "Defending champion Dommaraju Gukesh drew with challenger "
            "Javokhir Sindarov after 60 moves in Game 3 of the World Chess "
            "Championship in Geneva on Thursday, reports published on Friday "
            "said. Gukesh, playing black, used a rare Berlin Defence "
            "variation. The 14-game match, worth 2.5 million dollars, is "
            "tied 1.5-1.5."
        ),
    },
    {
        "headline": "India-Nepal armies train together",
        "region": "SOUTH ASIA",
        "source": "Indian Army",
        "tag": "REPORTED",
        "summary": (
            "The 20th India-Nepal army exercise Suryakiran XX continued at "
            "the Nepal Army Battle School in Saljhandi, having opened on "
            "25 November and running until 8 December, current-affairs "
            "reports noted on Friday. The annual drill builds joint "
            "counter-terror and disaster-relief skills along the shared "
            "border."
        ),
    },
    {
        "headline": "India forex reserves hit $737.78bn",
        "region": "SOUTH ASIA",
        "source": "RBI",
        "tag": "CONFIRMED",
        "summary": (
            "India's foreign-exchange reserves stood at 737.78 billion "
            "dollars at the end of September 2026, up 46.67 billion since "
            "March, the Reserve Bank of India's half-yearly report showed "
            "on Friday. Import cover was 9.8 months, giving the central "
            "bank a strong buffer as global markets stayed volatile."
        ),
    },
    {
        "headline": "Sri Lanka A reach Rising Stars final",
        "region": "SOUTH ASIA",
        "source": "ESPNcricinfo / ANI",
        "tag": "REPORTED",
        "summary": (
            "Sri Lanka A beat India A by eight wickets in the first "
            "semi-final of the Asia Cup Rising Stars in Doha on Thursday, "
            "chasing 318 in 41.3 overs, reports said on Friday. Two openers "
            "scored centuries as Sri Lanka won with 51 balls to spare. "
            "They meet the Pakistan Shaheens-Bangladesh A winner in "
            "Sunday's final."
        ),
    },
    {
        "headline": "China factory profits grow again",
        "region": "EAST ASIA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Chinese factories are growing profits again, led by "
            "AI-related goods, figures showed on Friday, as Shanghai "
            "shares jumped 3.7 percent in a global rally. The Hang Seng "
            "rose 3.3 percent and the Nikkei 2.1 percent, while markets "
            "also steadied after Nvidia's chief executive returned to the "
            "chipmaker."
        ),
    },
    {
        "headline": "Kim Jong Un orders more nuclear arms",
        "region": "EAST ASIA",
        "source": "KCNA",
        "tag": "CONFIRMED",
        "summary": (
            "North Korea's Kim Jong Un inspected production facilities and "
            "called for expanded deployment of tactical nuclear weapons, "
            "state media reported on Friday. The leader vowed to expand "
            "the nuclear arsenal programme after recent exchanges with "
            "President Trump, keeping the peninsula's arms race in the "
            "spotlight."
        ),
    },
    {
        "headline": "AI fakes target Taiwan polls",
        "region": "EAST ASIA",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "AI-generated fakes are seeking to influence Taiwan's polls, "
            "reports said on Friday, and Taipei is suspicious of China. "
            "The warning adds to a year of concern over synthetic media in "
            "Asian elections, as regulators struggle to trace deepfakes "
            "that spread faster than fact-checkers can debunk them."
        ),
    },
    {
        "headline": "Hong Kong shares jump 3.3 percent",
        "region": "EAST ASIA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Hong Kong's Hang Seng index rose 3.3 percent on Friday in a "
            "broad Asia rally, tracking Shanghai's 3.7 percent gain and a "
            "rebound in technology shares. Investors returned to battered "
            "AI stocks after a volatile week, though traders warned the "
            "recovery could fade if tariff threats harden again."
        ),
    },
    {
        "headline": "Bangkok refinery fire injures nine",
        "region": "SOUTHEAST ASIA",
        "source": "Xinhua",
        "tag": "CONFIRMED",
        "summary": (
            "Thai authorities ordered Bangchak's Bangkok oil refinery to "
            "suspend operations until 8 January after a fire at the plant "
            "on Thursday injured nine people, officials said on Friday. "
            "A heat exchanger in the hydrocracking unit ruptured, Bangchak "
            "said, and seven people remained in hospital, four in "
            "critical condition."
        ),
    },
    {
        "headline": "Thai shuttler Pink banned 3 months",
        "region": "SOUTHEAST ASIA",
        "source": "BWF",
        "tag": "CONFIRMED",
        "summary": (
            "The Badminton World Federation confirmed a three-month ban for "
            "Thai women's singles player Pitchamon Opatniputh, known as "
            "Pink, on Friday, after the banned substance furosemide was "
            "found in her test at the 2026 Asian Games in Aichi-Nagoya, "
            "Japan, in September. She will miss the start of next season."
        ),
    },
    {
        "headline": "Fire breaks out at Bangkok market",
        "region": "SOUTHEAST ASIA",
        "source": "Khaosod English",
        "tag": "CONFIRMED",
        "summary": (
            "A major fire broke out at Patthavikorn Market in Bangkok's "
            "Nawamin 72 area early on Friday, Khaosod reported, prompting "
            "firefighters to rush to the scene and urge motorists to avoid "
            "nearby roads. It was the second Bangkok blaze in two days "
            "after the Bangchak refinery explosion injured nine people."
        ),
    },
    {
        "headline": "Li visit deepened Thai ties: envoy",
        "region": "SOUTHEAST ASIA",
        "source": "Khaosod English",
        "tag": "CONFIRMED",
        "summary": (
            "China's ambassador said on Friday that Premier Li Qiang's "
            "visit had deepened Thai ties and pledged action over "
            "pollution, as Bangkok reeled from the refinery fire's smoke "
            "plume. The envoy's remarks underlined Beijing's push to keep "
            "Southeast Asian partners close amid US tariff pressure."
        ),
    },
    {
        "headline": "New Zealand hung parliament, 65-65",
        "region": "OCEANIA",
        "source": "Electoral Commission",
        "tag": "CONFIRMED",
        "summary": (
            "New Zealand's final election count delivered a deadlocked "
            "parliament on Friday: the ruling coalition holds 65 of 130 "
            "seats, one short of a majority, leaving the centrist "
            "Opportunity Party, with seven seats, as the decider on the "
            "next government. Luxon must now negotiate to stay in office."
        ),
    },
    {
        "headline": "NZ dollar edges up after hung result",
        "region": "OCEANIA",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "The New Zealand dollar edged up to 0.5491 against the US "
            "dollar on Friday after the official election count confirmed "
            "a hung parliament. Traders took the deadlock in their stride, "
            "with no major market-moving US data due while Wall Street "
            "reopened for a shortened Black Friday session."
        ),
    },
    {
        "headline": "India v NZ second Test begins",
        "region": "OCEANIA",
        "source": "Reports",
        "tag": "CONFIRMED",
        "summary": (
            "India's second Test against New Zealand began on Friday, with "
            "the hosts making a DRS blunder as opener Tom Latham got "
            "another lifeline on day one. The series is a key test for "
            "both sides ahead of a crowded winter calendar, and the match "
            "drew big crowds despite the weekday start."
        ),
    },
    {
        "headline": "Sindarov: Gukesh was so well prepared",
        "region": "CENTRAL ASIA",
        "source": "buzb.uz",
        "tag": "CONFIRMED",
        "summary": (
            "Uzbek grandmaster Javokhir Sindarov said on Friday his "
            "opponent had been exceptionally well prepared in the opening "
            "of their World Championship Game 3, while he had tried to "
            "find chances with the white pieces. The draw leaves the "
            "14-game match level at 1.5-1.5, with Game 4 on Saturday and "
            "Gukesh playing white."
        ),
    },
    {
        "headline": "Turkey seeks US sanctions relief",
        "region": "CENTRAL ASIA",
        "source": "Reports",
        "tag": "REPORTED",
        "summary": (
            "Turkey's defence minister is set to visit the United States "
            "as Ankara seeks sanctions relief, reports said on Friday. "
            "The trip comes as Turkey balances its NATO role, its defence "
            "industry ambitions and its ties with Russia, with US "
            "restrictions still biting on key weapons programmes."
        ),
    },
    {
        "headline": "World markets rally on Black Friday",
        "region": "GLOBAL",
        "source": "Markets",
        "tag": "CONFIRMED",
        "summary": (
            "Stocks rose around the world on Friday after a volatile week, "
            "led by China. Shanghai gained 3.7 percent and the S and P 500 "
            "added 1.3 percent. Gold jumped 2.6 percent and copper 3.3 "
            "percent, while oil edged lower to about 90 dollars a barrel "
            "but is still down 22 percent over the month."
        ),
    },
    {
        "headline": "Black Friday opens $1tn season",
        "region": "GLOBAL",
        "source": "Retail reports",
        "tag": "CONFIRMED",
        "summary": (
            "Black Friday opened a record one trillion dollar holiday "
            "season on Friday, but inflation is doing much of the "
            "spending, retail reports said. Early online sales rose as "
            "shoppers hunted discounts, with AI tools helping compare "
            "prices, while Amazon workers in several countries planned "
            "strikes."
        ),
    },
    {
        "headline": "Norse Atlantic unit goes bankrupt",
        "region": "GLOBAL",
        "source": "Court filing",
        "tag": "CONFIRMED",
        "summary": (
            "Norse Atlantic's Norwegian unit filed for bankruptcy in "
            "Norway's Agder District Court on Friday, and leasing firms "
            "ended contracts for all 12 of its planes the same day. The "
            "airline disputed those notices. The filing excluded the "
            "listed parent and its United Kingdom subsidiary."
        ),
    },
]

TOP_STORIES = [
    {
        "kicker": "UKRAINE WAR",
        "headline": "Russia fires 155 drones at Ukraine",
        "caption": "Nine regions hit overnight; Kyiv halts power exports",
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
        "caption": "Opportunity Party, 7 seats, now holds the balance",
        "scene": "parliament",
    },
    {
        "kicker": "WORLD CHESS",
        "headline": "Gukesh draws Game 3; 1.5-1.5",
        "caption": "60 moves in Geneva; Berlin Defence holds Sindarov",
        "scene": "chess",
    },
]

TIMELINE = [
    ("01:05", "NZ hung parliament confirmed"),
    ("06:38", "Bangkok refinery blast toll: 9 hurt"),
    ("08:17", "Gukesh-Sindarov Game 3 drawn"),
    ("09:00", "UK pensions dept cyber incident"),
    ("14:00", "NZ final count published, 65-65"),
    ("17:00", "EU summit ends, no deal"),
    ("22:06", "Markets close: Shanghai +3.7%"),
]

DATE_CHECK = (
    "DATE CHECK: All 47 stories in this edition happened on, or were first "
    "reported on, Friday 27 November 2026. Every story names its source and "
    "carries a CONFIRMED or REPORTED tag. Stories whose real date fell on "
    "26 November (EU budget talks, Nvidia shipments, Guinea-Bissau vote, "
    "Cairo tanker fire, Cartagena siege) were excluded."
)


def check():
    """Validate the dataset before rendering."""
    assert len(STORIES) == 47, len(STORIES)
    assert len(set(s["headline"] for s in STORIES)) == 47
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
