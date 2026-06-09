"""
Seed the database with a curated initial set of key historical events
about the PRC and CCP, with multilingual titles and descriptions.
"""

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import SessionLocal, engine, Base
from app.models import (
    Event,
    EventTitle,
    EventDescription,
    EventLocation,
    EventSource,
    EventPerspective,
)
from crawler.extra_seed_data import EXTRA_SEED_EVENTS

SEED_EVENTS = [
    # ====== 1921: CCP Founding ======
    {
        "date": "1921-07-23",
        "date_precision": "day",
        "category": "politics",
        "importance": 100,
        "tags": ["ccp", "founding", "communist"],
        "titles": {
            "zh_tw": "中國共產黨第一次全國代表大會",
            "en": "First National Congress of the Chinese Communist Party",
            "ja": "中国共産党第一回全国代表大会",
            "ko": "중국공산당 제1차 전국대표대회",
        },
        "descriptions": {
            "zh_tw": "中國共產黨在上海法租界秘密成立，13名代表與會，代表全國50多名黨員。會議最後一天因密探搜查轉移至浙江嘉興南湖遊船舉行。",
            "en": "The Chinese Communist Party was founded in secret in Shanghai's French Concession, with 13 delegates representing 50+ party members. The final day moved to a pleasure boat on South Lake in Jiaxing, Zhejiang.",
            "ja": "中国共産党が上海フランス租界で秘密裡に結成。13人の代議員が出席し、全国50余名の党員を代表。最終日は浙江嘉興の南湖で開催。",
            "ko": "중국공산당이 상하이 프랑스 조계지에서 비밀리에 창당. 13명의 대표가 참석, 전국 50여명의 당원 대표. 마지막 날은 저장성 자싱의 남호에서 개최.",
        },
        "location": {"lat": 31.2245, "lng": 121.4683, "country": "CN", "names": {"zh_tw": "上海", "en": "Shanghai", "ja": "上海", "ko": "상하이"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/First_National_Congress_of_the_Chinese_Communist_Party", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1934-1935: Long March ======
    {
        "date": "1934-10-16",
        "date_end": "1935-10-20",
        "date_precision": "day",
        "category": "military",
        "importance": 95,
        "tags": ["ccp", "long march", "civil war"],
        "titles": {
            "zh_tw": "長征",
            "en": "Long March",
            "ja": "長征",
            "ko": "장정",
        },
        "descriptions": {
            "zh_tw": "中國工農紅軍為逃脫國民黨軍隊的圍剿，從江西瑞金出發，歷經一年徒步約12,500公里至陝西延安，途中經歷極度艱苦的條件。長征確立了毛澤東在黨內的領導地位。",
            "en": "The Chinese Red Army retreated from Nationalist forces, marching approximately 12,500 km from Ruijin, Jiangxi to Yan'an, Shaanxi over about a year. The march established Mao Zedong's leadership within the Party.",
            "ja": "中国赤軍が国民党軍の包囲を逃れ、江西省瑞金から陝西省延安まで約12,500kmを約1年かけて行軍。毛沢東の党内指導権が確立された。",
            "ko": "중국 홍군이 국민당군의 포위를 피해 장시성 루이진에서 산시성 옌안까지 약 12,500km를 1년에 걸쳐 행군. 마오쩌둥의 당내 지도력이 확립됨.",
        },
        "location": {"lat": 26.0, "lng": 116.0, "country": "CN", "names": {"zh_tw": "江西", "en": "Jiangxi", "ja": "江西省", "ko": "장시성"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Long_March", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1949: PRC Founding ======
    {
        "date": "1949-10-01",
        "date_precision": "day",
        "category": "politics",
        "importance": 100,
        "tags": ["prc", "founding", "mao"],
        "titles": {
            "zh_tw": "中華人民共和國成立",
            "en": "Proclamation of the People's Republic of China",
            "ja": "中華人民共和国の成立",
            "ko": "중화인민공화국 수립",
        },
        "descriptions": {
            "zh_tw": "毛澤東在北京天安門城樓上宣讀《中華人民共和國中央人民政府公告》，宣布中華人民共和國中央人民政府成立。自此中國共產黨正式取得全國政權。",
            "en": "Mao Zedong proclaimed the founding of the People's Republic of China from Tiananmen Gate in Beijing. The CCP formally took national power after defeating the Nationalist government.",
            "ja": "毛沢東が北京天安門城楼で中華人民共和国中央人民政府の成立を宣言。中国共産党が国民党政権に勝利し、全国政権を掌握。",
            "ko": "마오쩌둥이 베이징 톈안먼 성루에서 중화인민공화국 중앙인민정부 수립을 선언. 중국공산당이 국민당 정권을 꺾고 전국 정권을 장악.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京", "en": "Beijing", "ja": "北京", "ko": "베이징"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Proclamation_of_the_People%27s_Republic_of_China", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1950-1953: Korean War ======
    {
        "date": "1950-10-19",
        "date_end": "1953-07-27",
        "date_precision": "day",
        "category": "military",
        "importance": 90,
        "tags": ["korean war", "military", "foreign relations"],
        "titles": {
            "zh_tw": "韓戰（抗美援朝）",
            "en": "Korean War (China's intervention)",
            "ja": "朝鮮戦争（中国の介入）",
            "ko": "한국 전쟁 (중국 개입)",
        },
        "descriptions": {
            "zh_tw": "中國人民志願軍跨過鴨綠江參戰韓戰。中國官方稱之為「抗美援朝戰爭」，約有300萬中國軍人參戰，傷亡約40萬人。這場戰爭造成了朝鮮半島的長期分裂。",
            "en": "Chinese People's Volunteer Army crossed the Yalu River entering the Korean War. Officially called the 'War to Resist US Aggression and Aid Korea', approximately 3 million Chinese soldiers served with about 400,000 casualties.",
            "ja": "中国人民志願軍が鴨緑江を越え朝鮮戦争に参戦。中国公式名称は「抗米援朝戦争」。約300万人の中国兵が従軍し、約40万人の死傷者を出した。",
            "ko": "중국인민지원군이 압록강을 건너 한국전쟁에 참전. 중국 공식 명칭은 '항미원조 전쟁'. 약 300만 명의 중국 군인이 참전, 약 40만 명의 사상자 발생.",
        },
        "location": {"lat": 40.0, "lng": 127.0, "country": "KP", "names": {"zh_tw": "朝鮮半島", "en": "Korean Peninsula", "ja": "朝鮮半島", "ko": "한반도"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Korean_War", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "KR", "lang": "ko", "viewpoint": "한국 정부는 한국전쟁을 공산주의 세력의 남침으로 규정하며, 중국의 개입이 전쟁을 장기화하고 한반도 분단을 고착시켰다고 본다. 한국에서 중국은 전쟁 당시 적성국이었으며, 이는 한중 관계의 역사적 상처로 남아 있다."},
            {"country": "US", "lang": "en", "viewpoint": "The US viewed China's intervention in the Korean War as a major escalation of the Cold War. The conflict solidified US-ROK alliance and led to long-term US military presence in South Korea. China's 'volunteer army' was seen as a challenge to US hegemony."},
        ],
    },
    # ====== 1958-1962: Great Leap Forward ======
    {
        "date": "1958-01-01",
        "date_end": "1962-12-31",
        "date_precision": "year",
        "category": "economy",
        "importance": 95,
        "tags": ["great leap forward", "famine", "economic policy", "mao"],
        "titles": {
            "zh_tw": "大躍進",
            "en": "Great Leap Forward",
            "ja": "大躍進",
            "ko": "대약진 운동",
        },
        "descriptions": {
            "zh_tw": "毛澤東推動的大規模經濟及社會運動，旨在快速將中國從農業國轉變為工業國。政策失誤加上自然災害導致了中國歷史上最嚴重的饑荒，學術界估計約造成1500萬至4500萬人死亡。",
            "en": "Mao Zedong's massive economic and social campaign to rapidly transform China from an agrarian to an industrial society. Policy failures combined with natural disasters caused the deadliest famine in human history, with estimated 15-45 million excess deaths.",
            "ja": "毛沢東が推進した大規模な経済・社会運動で、農業国から工業国への急速な転換を目指した。政策の失敗と自然災害により史上最悪の飢饉が発生し、推定1500万〜4500万人の餓死者を出した。",
            "ko": "마오쩌둥이 추진한 대규모 경제·사회 운동으로, 농업국에서 공업국으로의 급속한 전환을 목표. 정책 실패와 자연재해로 사상 최악의 기근 발생, 추정 1500만~4500만 명의 사망자.",
        },
        "location": {"lat": 35.0, "lng": 105.0, "country": "CN", "names": {"zh_tw": "中國全國", "en": "All of China", "ja": "中国全土", "ko": "중국 전역"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Great_Leap_Forward", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1966-1976: Cultural Revolution ======
    {
        "date": "1966-05-16",
        "date_end": "1976-10-06",
        "date_precision": "day",
        "category": "politics",
        "importance": 100,
        "tags": ["cultural revolution", "mao", "red guard", "political violence"],
        "titles": {
            "zh_tw": "文化大革命",
            "en": "Cultural Revolution",
            "ja": "文化大革命",
            "ko": "문화대혁명",
        },
        "descriptions": {
            "zh_tw": "毛澤東發起的社會政治運動，旨在清除資本主義和傳統文化元素，鞏固個人權力。造成大規模的政治迫害、知識分子迫害、文物破壞，估計數百萬人死亡。",
            "en": "Mao Zedong's socio-political movement to purge capitalist and traditional elements, and to re-assert his power. Resulted in widespread political persecution, targeting of intellectuals, destruction of cultural artifacts, and millions of deaths.",
            "ja": "毛沢東が発起した社会政治運動で、資本主義的・伝統的文化要素の排除と個人権力の強化を目的とした。大規模な政治的弾圧、知識人迫害、文化財破壊を引き起こし、数百万人が死亡した。",
            "ko": "마오쩌둥이 발기한 사회정치 운동으로, 자본주의적·전통적 문화 요소 제거와 개인 권력 강화를 목표. 대규모 정치 탄압, 지식인 박해, 문화재 파괴 초래, 수백만 명 사망.",
        },
        "location": {"lat": 35.0, "lng": 105.0, "country": "CN", "names": {"zh_tw": "中國全國", "en": "All of China", "ja": "中国全土", "ko": "중국 전역"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Cultural_Revolution", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "JP", "lang": "ja", "viewpoint": "日本では文化大革命を狂気の社会実験と見る向きが強く、日本のマスコミは紅衛兵の暴力的行為を克明に報道。この経験は日本の中国観に長く影を落とした。"},
            {"country": "US", "lang": "en", "viewpoint": "The US viewed the Cultural Revolution as a catastrophic social upheaval that destabilized China and led to widespread human rights abuses. It reinforced US skepticism about communist governance."},
        ],
    },
    # ====== 1978: Reform and Opening Up ======
    {
        "date": "1978-12-18",
        "date_end": "1978-12-22",
        "date_precision": "day",
        "category": "economy",
        "importance": 100,
        "tags": ["reform", "deng xiaoping", "economic reform", "opening up"],
        "titles": {
            "zh_tw": "十一屆三中全會（改革開放）",
            "en": "3rd Plenary Session of the 11th Central Committee (Reform and Opening-up)",
            "ja": "中国共産党第十一期三中全会（改革開放）",
            "ko": "중국공산당 제11기 3중전회 (개혁개방)",
        },
        "descriptions": {
            "zh_tw": "鄧小平主導的十一屆三中全會決定終止「以階級鬥爭為綱」，將工作重心轉移到經濟建設，開啟改革開放政策。此後中國開始了從計劃經濟向市場經濟的轉型。",
            "en": "Deng Xiaoping's landmark plenum decided to shift focus from class struggle to economic construction, launching the Reform and Opening-up policy. China began its historic transition from a planned to a market-oriented economy.",
            "ja": "鄧小平主導の三中全会が「階級闘争を綱とする」ことを停止し、経済建設に重点を移す改革開放政策を開始。中国は計画経済から市場経済への歴史的転換を始めた。",
            "ko": "덩샤오핑 주도의 3중전회가 '계급투쟁을 강령으로' 하는 것을 중단하고 경제 건설에 중점을 두는 개혁개방 정책을 시작. 중국은 계획경제에서 시장경제로의 역사적 전환을 시작함.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京", "en": "Beijing", "ja": "北京", "ko": "베이징"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Reform_and_opening_up", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1989: Tiananmen Square protests ======
    {
        "date": "1989-04-15",
        "date_end": "1989-06-04",
        "date_precision": "day",
        "category": "human_rights",
        "importance": 100,
        "tags": ["tiananmen", "protest", "democracy", "crackdown", "human rights"],
        "titles": {
            "zh_tw": "六四天安門事件",
            "en": "Tiananmen Square protests and massacre",
            "ja": "天安門事件",
            "ko": "톈안먼 사건",
        },
        "descriptions": {
            "zh_tw": "1989年4月起長達七週的學生主導民主抗議運動，聚集在北京天安門廣場。6月4日解放軍武力鎮壓，造成數千人死亡。事件後中共加強了對言論和集會自由的限制。",
            "en": "A seven-week student-led pro-democracy protest in Beijing's Tiananmen Square. On June 4, the People's Liberation Army violently suppressed the protests, resulting in thousands of deaths. The CCP subsequently intensified political control.",
            "ja": "1989年4月からの学生主導による民主化抗議運動。6月4日未明、人民解放軍が武力鎮圧し、数千人が死亡。中国共産党はその後、言論・集会の自由をさらに制限した。",
            "ko": "1989년 4월부터 7주간 베이징 톈안먼 광장에서 학생 주도 민주화 항의 운동. 6월 4일 인민해방군이 무력 진압, 수천 명 사망. 중국공산당은 이후 언론·집회의 자유를 더욱 제한.",
        },
        "location": {"lat": 39.9054, "lng": 116.3976, "country": "CN", "names": {"zh_tw": "北京天安門廣場", "en": "Tiananmen Square, Beijing", "ja": "北京天安門広場", "ko": "베이징 톈안먼 광장"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Tiananmen_Square_protests_of_1989", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "TW", "lang": "zh_tw", "viewpoint": "臺灣方面將此事件視為中共政權壓迫人權的象徵，每年舉辦追悼活動。事件是台灣社會對中國共產黨負面認同的重要因素之一。"},
            {"country": "JP", "lang": "ja", "viewpoint": "日本政府はこの事件を受け、对中国経済協力の見直しを行った。マスコミは連日大々的に報道し、日本の中国観に大きな影響を与えた。"},
            {"country": "KR", "lang": "ko", "viewpoint": "한국 언론은 톈안먼 사건을 대대적으로 보도했으며, 이는 한국 사회의 중국 인식에 중요한 전환점이 되었다. 1992년 한중 수교 과정에서도 배경 요인으로 작용했다."},
            {"country": "US", "lang": "en", "viewpoint": "The US government imposed sanctions including arms sales ban and visa restrictions. The event fundamentally altered US-China relations for decades. Media coverage was extensive and critical."},
        ],
    },
    # ====== 1997: Hong Kong Handover ======
    {
        "date": "1997-07-01",
        "date_precision": "day",
        "category": "politics",
        "importance": 90,
        "tags": ["hong kong", "handover", "one country two systems"],
        "titles": {
            "zh_tw": "香港主權移交",
            "en": "Handover of Hong Kong",
            "ja": "香港返還",
            "ko": "홍콩 반환",
        },
        "descriptions": {
            "zh_tw": "香港由英國移交給中華人民共和國，結束156年英國殖民統治。香港成為中國首個特別行政區，實行「一國兩制」，承諾50年內保持資本主義制度和生活方式。",
            "en": "Hong Kong was handed over from the United Kingdom to the People's Republic of China, ending 156 years of British colonial rule. Hong Kong became China's first Special Administrative Region under 'One Country, Two Systems'.",
            "ja": "香港がイギリスから中華人民共和国に返還され、156年の英国植民地支配が終了。香港は中国初の特別行政区となり、「一国二制度」の下で資本主義制度と生活様式が50年間維持されることが約束された。",
            "ko": "홍콩이 영국에서 중화인민공화국으로 반환되어 156년의 영국 식민 통치 종료. 홍콩은 중국 최초의 특별행정구가 되어 '일국양제' 아래 자본주의 제도와 생활 방식이 50년간 유지될 것을 약속받음.",
        },
        "location": {"lat": 22.3193, "lng": 114.1694, "country": "HK", "names": {"zh_tw": "香港", "en": "Hong Kong", "ja": "香港", "ko": "홍콩"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Handover_of_Hong_Kong", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "TW", "lang": "zh_tw", "viewpoint": "台灣方面密切關注香港移交後的發展，視其為『一國兩制』的試驗場。香港的民主萎縮強化了台灣社會對中國承諾的不信任。"},
            {"country": "GB", "lang": "en", "viewpoint": "The UK government viewed the handover as the end of empire but maintained a moral commitment to Hong Kong's democratic development. Post-handover concerns grew over the erosion of judicial independence."},
        ],
    },
    # ====== 2001: WTO Accession ======
    {
        "date": "2001-12-11",
        "date_precision": "day",
        "category": "economy",
        "importance": 85,
        "tags": ["wto", "trade", "globalization"],
        "titles": {
            "zh_tw": "中國加入世界貿易組織",
            "en": "China's accession to the WTO",
            "ja": "中国のWTO加盟",
            "ko": "중국의 WTO 가입",
        },
        "descriptions": {
            "zh_tw": "中國正式加入世界貿易組織(WTO)，歷經15年談判。此後中國經濟快速融入全球體系，出口大幅成長，成為「世界工廠」，GDP在十年內超越日本成為世界第二。",
            "en": "China formally joined the World Trade Organization after 15 years of negotiations. This accelerated China's integration into the global economy, making it the 'World's Factory'. China's GDP surpassed Japan within a decade, becoming the world's second-largest economy.",
            "ja": "中国が15年にわたる交渉を経てWTOに正式加盟。これを機に中国経済は世界経済に急速に統合され、「世界の工場」に。GDPは10年以内に日本を抜き世界第2位となった。",
            "ko": "중국이 15년에 걸친 협상 끝에 WTO에 정식 가입. 이후 중국 경제는 세계 경제에 급속히 통합되어 '세계의 공장'이 됨. GDP는 10년 내에 일본을 추월하여 세계 2위가 됨.",
        },
        "location": {"lat": 35.0, "lng": 105.0, "country": "CN", "names": {"zh_tw": "中國", "en": "China", "ja": "中国", "ko": "중국"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/China_and_the_World_Trade_Organization", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2008: Beijing Olympics ======
    {
        "date": "2008-08-08",
        "date_end": "2008-08-24",
        "date_precision": "day",
        "category": "society",
        "importance": 80,
        "tags": ["olympics", "sports", "international"],
        "titles": {
            "zh_tw": "2008年北京奧運會",
            "en": "2008 Beijing Summer Olympics",
            "ja": "2008年北京オリンピック",
            "ko": "2008년 베이징 하계 올림픽",
        },
        "descriptions": {
            "zh_tw": "第29屆夏季奧運會在北京舉行，被視為中國改革開放30年成就的展示。開幕式盛大空前，但同時西藏抗議、人權問題在國際上引發爭議。",
            "en": "The 29th Summer Olympics in Beijing, seen as China's coming-out party showcasing 30 years of reform. The opening ceremony was spectacular, but the Games were also shadowed by Tibet protests and human rights concerns.",
            "ja": "第29回夏季オリンピックが北京で開催され、改革開放30年の成果を示す場となった。開会式は前例のない規模で開催されたが、チベット抗議や人権問題が国際的な議論を呼んだ。",
            "ko": "제29회 하계 올림픽이 베이징에서 개최, 개혁개방 30년의 성과를 과시하는 장이 됨. 개회식은 전례 없는 규모였으나 티베트 항의와 인권 문제가 국제적 논란을 불러일으킴.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京", "en": "Beijing", "ja": "北京", "ko": "베이징"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/2008_Summer_Olympics", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2013: Belt and Road Initiative ======
    {
        "date": "2013-09-01",
        "date_precision": "month",
        "category": "foreign_relations",
        "importance": 85,
        "tags": ["belt and road", "xi jinping", "foreign policy", "infrastructure"],
        "titles": {
            "zh_tw": "一帶一路倡議",
            "en": "Belt and Road Initiative",
            "ja": "一带一路構想",
            "ko": "일대일로 이니셔티브",
        },
        "descriptions": {
            "zh_tw": "習近平提出的全球基礎設施發展戰略，涵蓋數十個國家。被視為中國擴大國際影響力和經濟外交的核心工具，同時也被批評為「債務陷阱外交」。",
            "en": "Xi Jinping's global infrastructure development strategy involving dozens of countries. Seen as China's core tool for expanding international influence and economic diplomacy, but also criticized as 'debt-trap diplomacy'.",
            "ja": "習近平が提唱した世界的なインフラ開発戦略で数十カ国が関与。中国の国際的影響力と経済外交の拡大の核心的手段とされる一方、「債務の罠外交」としても批判されている。",
            "ko": "시진핑이 제안한 글로벌 인프라 개발 전략으로 수십 개국이 참여. 중국의 국제적 영향력과 경제 외교 확대의 핵심 수단으로 평가되지만 '부채 함정 외교'로도 비판받음.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京（總部）", "en": "Beijing (headquarters)", "ja": "北京（本部）", "ko": "베이징 (본부)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Belt_and_Road_Initiative", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "US", "lang": "en", "viewpoint": "The US has criticized BRI as a debt-trap diplomacy strategy that undermines recipient nations' sovereignty. Washington has countered with alternative infrastructure initiatives like the G7's Build Back Better World."},
            {"country": "JP", "lang": "ja", "viewpoint": "日本はBRIに対し懐疑的で、透明性や持続可能性の欠如を批判。同時に日本主導の『自由で開かれたインド太平洋』構想や質の高いインフラ投資で対抗している。"},
        ],
    },
    # ====== 2019: Hong Kong Protests ======
    {
        "date": "2019-03-01",
        "date_end": "2020-01-01",
        "date_precision": "month",
        "category": "human_rights",
        "importance": 90,
        "tags": ["hong kong", "protests", "extradition bill", "democracy"],
        "titles": {
            "zh_tw": "2019年香港反送中運動",
            "en": "2019 Hong Kong protests",
            "ja": "2019年香港反送中運動",
            "ko": "2019년 홍콩 시위",
        },
        "descriptions": {
            "zh_tw": "香港百萬人上街抗議《逃犯條例》修正草案，後擴大為追求民主與反對北京干預的運動。最終北京政府通過《香港國安法》並大幅收緊香港自治。",
            "en": "Millions in Hong Kong protested against the extradition bill, which escalated into a movement for democracy and against Beijing's encroachment. Beijing ultimately imposed the National Security Law, sharply curtailing Hong Kong's autonomy.",
            "ja": "香港で百万人以上が逃亡犯条例改正案に抗議し、民主化と北京の干渉反対運動に発展。最終的に北京は香港国家安全法を制定し、香港の自治を大幅に制限した。",
            "ko": "홍콩에서 백만 명 이상이 범죄인 인도 조례 개정안에 항의, 이후 민주화와 베이징의 간섭 반대 운동으로 발전. 베이징은 결국 홍콩 국가안전법을 제정, 홍콩의 자치를 대폭 제한.",
        },
        "location": {"lat": 22.3193, "lng": 114.1694, "country": "HK", "names": {"zh_tw": "香港", "en": "Hong Kong", "ja": "香港", "ko": "홍콩"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/2019_Hong_Kong_protests", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "TW", "lang": "zh_tw", "viewpoint": "台灣社會高度關注香港反送中運動，擔憂香港的『一國兩制』失敗將成為台灣未來的一面鏡子。台灣朝野普遍聲援香港抗議者。"},
            {"country": "US", "lang": "en", "viewpoint": "The US viewed the protests as a legitimate expression of democratic aspirations and imposed sanctions on Chinese and Hong Kong officials. The subsequent National Security Law was condemned as a betrayal of Hong Kong's autonomy."},
        ],
    },
    # ====== 2020: COVID-19 / Wuhan Lockdown ======
    {
        "date": "2020-01-23",
        "date_end": "2020-04-08",
        "date_precision": "day",
        "category": "society",
        "importance": 90,
        "tags": ["covid-19", "wuhan", "lockdown", "pandemic"],
        "titles": {
            "zh_tw": "COVID-19疫情與武漢封城",
            "en": "COVID-19 pandemic and Wuhan lockdown",
            "ja": "COVID-19パンデミックと武漢封鎖",
            "ko": "코로나19 팬데믹과 우한 봉쇄",
        },
        "descriptions": {
            "zh_tw": "武漢因COVID-19疫情實施史無前例的封城，影響1100萬居民。中國的零容忍防疫政策包括大規模檢測、封鎖和健康碼系統。疫情起源與初期隱瞞引發國際爭議。",
            "en": "Wuhan was placed under an unprecedented lockdown affecting 11 million residents. China's zero-COVID policy included mass testing, lockdowns, and a health code system. The pandemic's origins and initial cover-up sparked international controversy.",
            "ja": "武漢がCOVID-19流行により1100万人の住民を対象に前例のない封鎖を実施。中国のゼロコロナ政策は大規模検査、封鎖、健康コードシステムを含んだ。パンデミックの起源と初期の隠蔽が国際的な論争を引き起こした。",
            "ko": "우한이 COVID-19 팬데믹으로 1100만 명의 주민을 대상으로 전례 없는 봉쇄를 시행. 중국의 제로코로나 정책은 대규모 검사, 봉쇄, 건강 코드 시스템을 포함. 팬데믹의 기원과 초기 은폐가 국제적 논란을 불러일으킴.",
        },
        "location": {"lat": 30.5928, "lng": 114.3055, "country": "CN", "names": {"zh_tw": "武漢", "en": "Wuhan", "ja": "武漢", "ko": "우한"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_mainland_China", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "US", "lang": "en", "viewpoint": "The US and many countries criticized China's initial cover-up of the outbreak and called for transparent investigation into the virus's origins. China's zero-COVID policy was seen as draconian yet effective in controlling case numbers."},
            {"country": "JP", "lang": "ja", "viewpoint": "日本は武漢封鎖や中国の情報隠蔽に強い懸念を示した。中国からの渡航制限を実施し、ワクチン外交や水際対策で独自の対応を取った。中国のゼロコロナ政策は日本経済にも影響を与えた。"},
        ],
    },
    # ====== 2022: Xi Jinping Third Term ======
    {
        "date": "2022-10-16",
        "date_end": "2022-10-22",
        "date_precision": "day",
        "category": "politics",
        "importance": 85,
        "tags": ["xi jinping", "party congress", "third term"],
        "titles": {
            "zh_tw": "中共二十大（習近平第三任期）",
            "en": "20th National Congress of the CCP (Xi's third term)",
            "ja": "中国共産党第二十回全国代表大会（習近平三期目）",
            "ko": "중국공산당 제20차 전국대표대회 (시진핑 3기)",
        },
        "descriptions": {
            "zh_tw": "中國共產黨第二十次全國代表大會，習近平打破慣例獲得第三任期，進一步鞏固個人權力。大會確立了「習近平新時代中國特色社會主義思想」的指導地位。",
            "en": "The 20th CCP National Congress where Xi Jinping broke convention to secure an unprecedented third term, further consolidating personal power. The Congress enshrined 'Xi Jinping Thought on Socialism with Chinese Characteristics for a New Era'.",
            "ja": "中国共産党第二十回全国代表大会で、習近平が慣例を破り異例の三期目を獲得、個人権力をさらに強化。大会は「習近平の新時代の中国の特色ある社会主義思想」の指導的地位を確立した。",
            "ko": "중국공산당 제20차 전국대표대회에서 시진핑이 관례를 깨고 전례 없는 3기를 확보, 개인 권력을 더욱 강화. 대회는 '시진핑 신시대 중국특색사회주의 사상'의 지도적 지위를 확립.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京人民大會堂", "en": "Great Hall of the People, Beijing", "ja": "北京人民大会堂", "ko": "베이징 인민대회당"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/20th_National_Congress_of_the_Chinese_Communist_Party", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
]

SEED_EVENTS.extend(EXTRA_SEED_EVENTS)


def seed_database():
    """Import seed events into the database."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    existing = db.query(Event).count()
    if existing > 0:
        print(f"Database already has {existing} events, skipping seed.")
        db.close()
        return

    count = 0
    for ev_data in SEED_EVENTS:
        ev = Event(
            date=ev_data["date"] if isinstance(ev_data["date"], date) else date.fromisoformat(ev_data["date"]),
            date_end=date.fromisoformat(ev_data["date_end"]) if ev_data.get("date_end") else None,
            date_precision=ev_data.get("date_precision", "day"),
            category=ev_data.get("category"),
            tags=ev_data.get("tags", []),
            importance=ev_data.get("importance", 0),
        )
        db.add(ev)
        db.flush()

        for lang, title in ev_data.get("titles", {}).items():
            db.add(EventTitle(event_id=ev.id, language=lang, title=title))

        for lang, desc in ev_data.get("descriptions", {}).items():
            db.add(EventDescription(event_id=ev.id, language=lang, summary=desc[:500] if desc else None, content=desc))

        loc = ev_data.get("location")
        if loc:
            db.add(EventLocation(event_id=ev.id, lat=loc.get("lat"), lng=loc.get("lng"), country=loc.get("country"), names=loc.get("names", {})))

        for src in ev_data.get("sources", []):
            db.add(EventSource(event_id=ev.id, language=src.get("lang", "en"), url=src["url"], publisher=src.get("publisher", "Wikipedia"), reliability=src.get("reliability", 0.7)))

        for persp in ev_data.get("perspectives", []):
            db.add(EventPerspective(event_id=ev.id, country_code=persp.get("country", ""), language=persp.get("lang", "en"), viewpoint=persp.get("viewpoint", "")))

        count += 1

    db.commit()
    db.close()
    print(f"Seeded {count} events into database.")


if __name__ == "__main__":
    seed_database()
