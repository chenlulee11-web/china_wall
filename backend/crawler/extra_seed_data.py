"""
Additional seed events (35 events) to reach 50+ total.
Combined with the 15 events in seed.py for a total of 50 events.
"""

EXTRA_SEED_EVENTS = [
    # ====== 1925: May 30th Movement ======
    {
        "date": "1925-05-30",
        "date_precision": "day",
        "category": "foreign_relations",
        "importance": 70,
        "tags": ["anti-imperialism", "nationalism", "protest"],
        "titles": {
            "zh_tw": "五卅運動",
            "en": "May 30th Movement",
            "ja": "五・三〇運動",
            "ko": "5·30 운동",
        },
        "descriptions": {
            "zh_tw": "上海公共租界英國巡捕開槍射殺抗議工人，引發全國性反帝國主義運動。此事件激發了中國民族主義情緒，並促進了中國共產黨的發展。",
            "en": "British police in Shanghai's International Settlement fired on protesting workers, triggering a nationwide anti-imperialist movement. The incident galvanized Chinese nationalism and boosted the CCP's growth.",
            "ja": "上海共同租界で英国警察が抗議労働者に発砲し、全国的な反帝国主義運動を引き起こした。中国のナショナリズムを刺激し、中国共産党の発展を促進した。",
            "ko": "상하이 공공조계에서 영국 경찰이 항의 노동자에게 발포, 전국적 반제국주의 운동을 촉발. 중국 민족주의를 자극하고 중국공산당의 성장을 촉진.",
        },
        "location": {"lat": 31.2400, "lng": 121.4700, "country": "CN", "names": {"zh_tw": "上海", "en": "Shanghai", "ja": "上海", "ko": "상하이"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/May_Thirtieth_Movement", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1927: Nanchang Uprising (PLA Founding) ======
    {
        "date": "1927-08-01",
        "date_precision": "day",
        "category": "military",
        "importance": 85,
        "tags": ["pla", "military", "civil war", "ccp"],
        "titles": {
            "zh_tw": "南昌起義（解放軍建軍節）",
            "en": "Nanchang Uprising (PLA Founding)",
            "ja": "南昌起義（人民解放軍建軍記念日）",
            "ko": "난창 봉기 (인민해방군 창건일)",
        },
        "descriptions": {
            "zh_tw": "中國共產黨在江西南昌領導武裝起義，打響了武裝反抗國民黨的第一槍。8月1日後來被定為中國人民解放軍建軍節。",
            "en": "The CCP led an armed uprising in Nanchang, Jiangxi, firing the first shot of armed resistance against the Nationalists. August 1 is celebrated as PLA Day.",
            "ja": "中国共産党が江西南昌で武装蜂起を指導し、国民党に対する武力抵抗の第一歩を記した。8月1日は後に人民解放軍建軍記念日とされた。",
            "ko": "중국공산당이 장시성 난창에서 무장 봉기를 주도, 국민당에 대한 무장 저항의 첫 걸음을 기록. 8월 1일은 후에 인민해방군 창건 기념일이 됨.",
        },
        "location": {"lat": 28.6822, "lng": 115.8579, "country": "CN", "names": {"zh_tw": "南昌", "en": "Nanchang", "ja": "南昌", "ko": "난창"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Nanchang_Uprising", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1935: Zunyi Conference ======
    {
        "date": "1935-01-15",
        "date_end": "1935-01-17",
        "date_precision": "day",
        "category": "politics",
        "importance": 80,
        "tags": ["ccp", "mao", "leadership", "long march"],
        "titles": {
            "zh_tw": "遵義會議",
            "en": "Zunyi Conference",
            "ja": "遵義会議",
            "ko": "쭌이 회의",
        },
        "descriptions": {
            "zh_tw": "長征途中在貴州遵義召開的關鍵會議，毛澤東進入中共領導核心，確立了在黨內和軍事的領導地位。被視為中共黨史的轉折點。",
            "en": "A pivotal CCP meeting during the Long March in Zunyi, Guizhou, where Mao Zedong entered the party's leadership core, establishing his military and political leadership. Seen as a turning point in CCP history.",
            "ja": "長征途中に貴州遵義で開かれた重要な会議で、毛沢東が中共指導部の中核に入り、軍事・政治的指導力を確立した。中共党史の転換点とされる。",
            "ko": "장정 도중 구이저우 쭌이에서 열린 중대한 회의로, 마오쩌둥이 당 지도부 핵심에 진입, 군사적·정치적 지도력을 확립. 중국공산당사의 전환점으로 평가됨.",
        },
        "location": {"lat": 27.6870, "lng": 106.9060, "country": "CN", "names": {"zh_tw": "遵義", "en": "Zunyi", "ja": "遵義", "ko": "쭌이"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Zunyi_Conference", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1937: Marco Polo Bridge Incident / Second Sino-Japanese War ======
    {
        "date": "1937-07-07",
        "date_precision": "day",
        "category": "military",
        "importance": 90,
        "tags": ["war", "japan", "world war ii", "invasion"],
        "titles": {
            "zh_tw": "七七事變（抗日戰爭全面爆發）",
            "en": "Marco Polo Bridge Incident (Second Sino-Japanese War begins)",
            "ja": "盧溝橋事件（日中戦争全面勃発）",
            "ko": "노구교 사건 (중일전쟁 전면 발발)",
        },
        "descriptions": {
            "zh_tw": "日本軍隊在北平西南盧溝橋附近演習時藉口一名士兵失蹤要求進城搜查，遭拒後發動進攻。此事件標誌著八年抗日戰爭的全面爆發。",
            "en": "Japanese forces near the Marco Polo Bridge southwest of Beijing demanded to search for a missing soldier. When refused, they attacked, marking the start of the full-scale Second Sino-Japanese War (1937-1945).",
            "ja": "北京郊外の盧溝橋で演習中の日本軍が兵士一名の行方不明を理由に市街への立ち入りを要求、拒否され攻撃を開始。この事件により八年にわたる日中戦争が全面勃発した。",
            "ko": "베이징 교외 루거우차오에서 훈련 중이던 일본군이 병사 한 명의 실종을 이유로 시내 진입을 요구, 거절당하자 공격을 개시. 이 사건으로 8년간의 중일전쟁이 전면 발발.",
        },
        "location": {"lat": 39.8480, "lng": 116.2130, "country": "CN", "names": {"zh_tw": "盧溝橋（北京）", "en": "Marco Polo Bridge, Beijing", "ja": "盧溝橋（北京）", "ko": "루거우차오 (베이징)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Marco_Polo_Bridge_Incident", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1945: Mao-Chiang Chongqing Negotiations ======
    {
        "date": "1945-08-28",
        "date_end": "1945-10-10",
        "date_precision": "day",
        "category": "politics",
        "importance": 70,
        "tags": ["ccp", "kmt", "civil war", "negotiation"],
        "titles": {
            "zh_tw": "重慶談判",
            "en": "Chongqing Negotiations (Mao-Chiang talks)",
            "ja": "重慶談判",
            "ko": "충칭 담판",
        },
        "descriptions": {
            "zh_tw": "毛澤東與蔣介石在重慶就戰後中國政治格局進行談判。雙方簽署了《雙十協定》，但不久即因軍事衝突而破裂，國共內戰全面爆發。",
            "en": "Mao Zedong and Chiang Kai-shek negotiated post-war China's political future in Chongqing. The Double Tenth Agreement was signed but soon collapsed amid military clashes, leading to full-scale civil war.",
            "ja": "毛沢東と蒋介石が重慶で戦後中国の政治体制について交渉。双十協定が締結されたが、まもなく軍事衝突により決裂し、国共内戦が全面化した。",
            "ko": "마오쩌둥과 장제스가 충칭에서 전후 중국의 정치 체제에 대해 협상. 쌍십협정이 체결되었으나 곧 군사 충돌로 결렬, 국공내전이 전면화됨.",
        },
        "location": {"lat": 29.5630, "lng": 106.5510, "country": "CN", "names": {"zh_tw": "重慶", "en": "Chongqing", "ja": "重慶", "ko": "충칭"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Chongqing_Negotiations", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1951: Tibet Annexation ======
    {
        "date": "1951-05-23",
        "date_precision": "day",
        "category": "politics",
        "importance": 85,
        "tags": ["tibet", "annexation", "seventeen point agreement", "military"],
        "titles": {
            "zh_tw": "西藏和平解放（十七條協議）",
            "en": "Annexation of Tibet (Seventeen Point Agreement)",
            "ja": "チベット併合（十七条協議）",
            "ko": "티베트 합병 (17개조 협정)",
        },
        "descriptions": {
            "zh_tw": "中國人民解放軍進入西藏，與西藏地方政府簽署《十七條協議》，宣布和平解放西藏。達賴喇嘛保留權力但實際控制權轉移至北京。1959年西藏抗暴後達賴流亡印度。",
            "en": "The PLA entered Tibet and signed the Seventeen Point Agreement with local authorities, declaring Tibet's 'peaceful liberation'. The Dalai Lama retained nominal authority but control shifted to Beijing. He fled to India after the 1959 Tibetan uprising.",
            "ja": "人民解放軍がチベットに入り、チベット地方政府と十七条協議を締結し「平和的解放」を宣言。ダライ・ラマは名目的権力を保持したが、実権は北京に移行。1959年のチベット蜂起後、インドに亡命。",
            "ko": "인민해방군이 티베트에 진입, 티베트 지방정부와 17개조 협정을 체결하고 '평화적 해방'을 선언. 달라이 라마는 명목상 권력을 유지했으나 실권은 베이징으로 이전. 1959년 티베트 봉기 후 인도로 망명.",
        },
        "location": {"lat": 29.6500, "lng": 91.1000, "country": "CN", "names": {"zh_tw": "拉薩", "en": "Lhasa", "ja": "ラサ", "ko": "라싸"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Seventeen_Point_Agreement", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1956-1957: Hundred Flowers / Anti-Rightist ======
    {
        "date": "1956-05-02",
        "date_end": "1957-12-31",
        "date_precision": "year",
        "category": "politics",
        "importance": 85,
        "tags": ["mao", "political campaign", "intellectuals", "repression"],
        "titles": {
            "zh_tw": "百花齊放／反右運動",
            "en": "Hundred Flowers Campaign / Anti-Rightist Movement",
            "ja": "百花斉放・百家争鳴／反右派闘争",
            "ko": "백화제방·백가쟁명 / 반우파 투쟁",
        },
        "descriptions": {
            "zh_tw": "毛澤東先號召知識分子「百花齊放、百家爭鳴」向黨提意見。當大量批評湧現後，隨即發動反右運動，將約55萬知識分子打成「右派」，遭受迫害。",
            "en": "Mao Zedong first invited intellectuals to 'Let a hundred flowers bloom' and criticize the Party. When criticism poured in, he launched the Anti-Rightist Movement, branding ~550,000 intellectuals as 'rightists' who faced persecution.",
            "ja": "毛沢東は知識人に「百花斉放、百家争鳴」を呼びかけ党への批判を求めた。批判が相次ぐと反右派闘争を開始し、約55万人の知識人が「右派」とされ迫害された。",
            "ko": "마오쩌둥이 지식인들에게 '백화제방, 백가쟁명'을 외치며 당 비판을 요구. 비판이 쏟아지자 반우파 투쟁을 시작, 약 55만 명의 지식인이 '우파'로 낙인찍혀 박해받음.",
        },
        "location": {"lat": 35.0, "lng": 105.0, "country": "CN", "names": {"zh_tw": "中國全國", "en": "All of China", "ja": "中国全土", "ko": "중국 전역"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Anti-Rightist_Movement", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1960: Sino-Soviet Split ======
    {
        "date": "1960-07-16",
        "date_precision": "day",
        "category": "foreign_relations",
        "importance": 80,
        "tags": ["soviet union", "split", "cold war", "ideology"],
        "titles": {
            "zh_tw": "中蘇分裂",
            "en": "Sino-Soviet Split",
            "ja": "中ソ対立",
            "ko": "중소 분쟁",
        },
        "descriptions": {
            "zh_tw": "蘇聯撤走在華全部專家，廢除數百個合作項目。意識形態和戰略利益分歧導致社會主義陣營兩大國關係破裂，深刻影響冷戰格局。",
            "en": "The USSR withdrew all advisors from China and terminated hundreds of cooperation projects. Ideological and strategic differences ruptured relations between the two communist giants, reshaping Cold War dynamics.",
            "ja": "ソ連が中国から全専門家を引き揚げ、数百の協力プロジェクトを廢止。イデオロギーと戦略的利益の相違により社会主義陣営の二大国が決裂し、冷戦構造に深刻な影響を与えた。",
            "ko": "소련이 중국에서 모든 전문가를 철수하고 수백 개의 협력 프로젝트를 폐기. 이데올로기와 전략적 이해 차이로 사회주의 진영의 두 대국이 결렬, 냉전 구도에 심각한 영향을 미침.",
        },
        "location": {"lat": 55.7558, "lng": 37.6173, "country": "RU", "names": {"zh_tw": "莫斯科（蘇聯）", "en": "Moscow (USSR)", "ja": "モスクワ（ソ連）", "ko": "모스크바 (소련)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Sino-Soviet_split", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1962: Sino-Indian War ======
    {
        "date": "1962-10-20",
        "date_end": "1962-11-21",
        "date_precision": "day",
        "category": "military",
        "importance": 75,
        "tags": ["india", "border war", "military", "territorial dispute"],
        "titles": {
            "zh_tw": "中印邊境戰爭",
            "en": "Sino-Indian War",
            "ja": "中印国境戦争",
            "ko": "중국-인도 국경 전쟁",
        },
        "descriptions": {
            "zh_tw": "中國與印度在喜馬拉雅邊境爆發短暫但激烈的戰爭。中國軍隊佔領阿克賽欽等地區，單方面宣布停火。邊界爭端至今未解決。",
            "en": "A brief but sharp war between China and India along the Himalayan border. Chinese forces captured Aksai Chin and other areas, then unilaterally declared a ceasefire. The border dispute remains unresolved.",
            "ja": "中国とインドの間でヒマラヤ国境で短期間だが激しい戦争が発生。中国軍がアクサイチンなどを占領し、一方的に停戦を宣言。国境紛争は現在も未解決。",
            "ko": "중국과 인도 간 히말라야 국경에서 짧지만 격렬한 전쟁 발생. 중국군이 악사이친 등 지역을 점령하고 일방적으로 휴전 선언. 국경 분쟁은 현재까지 미해결.",
        },
        "location": {"lat": 35.0, "lng": 79.0, "country": "CN", "names": {"zh_tw": "阿克賽欽（中印邊境）", "en": "Aksai Chin (Sino-Indian border)", "ja": "アクサイチン（中印国境）", "ko": "악사이친 (중인 국경)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Sino-Indian_War", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1964: First Atomic Bomb ======
    {
        "date": "1964-10-16",
        "date_precision": "day",
        "category": "science_tech",
        "importance": 85,
        "tags": ["nuclear", "weapon", "military", "technology"],
        "titles": {
            "zh_tw": "中國第一顆原子彈爆炸",
            "en": "China's first atomic bomb test (Project 596)",
            "ja": "中国初の原子爆弾実験（596計画）",
            "ko": "중국 최초 원자폭탄 실험 (596 프로젝트)",
        },
        "descriptions": {
            "zh_tw": "中國在新疆羅布泊成功試爆第一顆原子彈，成為世界第五個核武器國家。此舉極大提升了中國的國際地位和軍事威懾力。",
            "en": "China successfully detonated its first atomic bomb at Lop Nur, Xinjiang, becoming the world's fifth nuclear weapons state. This dramatically boosted China's international standing and military deterrence.",
            "ja": "中国が新疆ロプノールで初の原子爆弾の爆縮に成功し、世界で5番目の核兵器保有国となった。これにより中国の国際的地位と軍事抑止力が大幅に向上した。",
            "ko": "중국이 신장 뤄부포에서 최초 원자폭탄 폭발에 성공, 세계 5번째 핵무기 보유국이 됨. 이로써 중국의 국제적 지위와 군사 억지력이 크게 향상.",
        },
        "location": {"lat": 40.5000, "lng": 90.5000, "country": "CN", "names": {"zh_tw": "羅布泊（新疆）", "en": "Lop Nur, Xinjiang", "ja": "ロプノール（新疆）", "ko": "뤄부포 (신장)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/596_(nuclear_Test)", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1971: Lin Biao Incident ======
    {
        "date": "1971-09-13",
        "date_precision": "day",
        "category": "politics",
        "importance": 80,
        "tags": ["lin biao", "purge", "mao", "power struggle"],
        "titles": {
            "zh_tw": "林彪事件（九一三事件）",
            "en": "Lin Biao Incident (September 13 Incident)",
            "ja": "林彪事件（913事件）",
            "ko": "린뱌오 사건 (913 사건)",
        },
        "descriptions": {
            "zh_tw": "毛澤東指定的接班人林彪在疑似政變失敗後乘坐飛機外逃，墜毀於蒙古溫都爾汗。此事件震撼中共高層，導致對林彪路線的大規模批判。",
            "en": "Lin Biao, Mao's designated successor, fled by plane after an alleged coup attempt and died in a crash in Mongolia. The incident shocked the CCP leadership and led to a purge of Lin's associates.",
            "ja": "毛沢東の後継者とされた林彪がクーデター未遂の後、飛行機で逃亡中にモンゴルで墜落死。この事件は中共指導部を震撼させ、林彪派の大規模粛清につながった。",
            "ko": "마오쩌둥의 후계자로 지명된 린뱌오가 쿠데타 미수 후 비행기로 도주 중 몽골에서 추락사. 이 사건은 중국공산당 지도부를 충격에 빠뜨렸고 린뱌오 계열의 대규모 숙청으로 이어짐.",
        },
        "location": {"lat": 47.0000, "lng": 111.0000, "country": "MN", "names": {"zh_tw": "溫都爾汗（蒙古）", "en": "Öndörkhaan, Mongolia", "ja": "ウンドゥルハーン（モンゴル）", "ko": "온도르한 (몽골)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Lin_Biao_Incident", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1971: UN Resolution 2758 ======
    {
        "date": "1971-10-25",
        "date_precision": "day",
        "category": "foreign_relations",
        "importance": 85,
        "tags": ["un", "diplomacy", "international recognition", "china seat"],
        "titles": {
            "zh_tw": "聯合國第2758號決議（中國恢復聯合國席位）",
            "en": "UN General Assembly Resolution 2758 (PRC replaces ROC in UN)",
            "ja": "国連総会決議2758（中国の国連議席回復）",
            "ko": "유엔 총회 결의 2758호 (중화인민공화국 유엔 의석 회복)",
        },
        "descriptions": {
            "zh_tw": "聯合國大會以壓倒性多數通過第2758號決議，恢復中華人民共和國在聯合國的一切合法權利，並驅逐中華民國（台灣）代表。",
            "en": "The UN General Assembly voted overwhelmingly for Resolution 2758, recognizing the PRC as the sole legitimate representative of China and expelling the Republic of China (Taiwan) from the UN.",
            "ja": "国連総会が圧倒的多数で決議2758を採択し、中華人民共和国の国連におけるすべての合法的権利を回復、中華民国（台湾）の代表を追放した。",
            "ko": "유엔 총회가 압도적 다수로 결의 2758호를 채택, 중화인민공화국의 유엔 내 모든 합법적 권리를 회복하고 중화민국(대만) 대표를 축출.",
        },
        "location": {"lat": 40.7484, "lng": -73.9675, "country": "US", "names": {"zh_tw": "紐約聯合國總部", "en": "UN Headquarters, New York", "ja": "ニューヨーク国連本部", "ko": "뉴욕 유엔 본부"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/United_Nations_General_Assembly_Resolution_2758", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1972: Nixon Visit to China ======
    {
        "date": "1972-02-21",
        "date_end": "1972-02-28",
        "date_precision": "day",
        "category": "foreign_relations",
        "importance": 85,
        "tags": ["nixon", "us-china", "diplomacy", "ping pong", "shanghai communique"],
        "titles": {
            "zh_tw": "美國總統尼克森訪華",
            "en": "Nixon's visit to China",
            "ja": "ニクソン大統領の中国訪問",
            "ko": "닉슨 대통령의 중국 방문",
        },
        "descriptions": {
            "zh_tw": "美國總統尼克森訪問中國，與毛澤東、周恩來會晤，簽署《上海公報》。此訪打破中美長達23年的隔絕，標誌著兩國關係正常化的開端。",
            "en": "President Nixon visited China, meeting Mao and Zhou Enlai, signing the Shanghai Communiqué. The visit ended 23 years of isolation between the US and China, beginning the normalization of bilateral relations.",
            "ja": "ニクソン大統領が中国を訪問し、毛沢東や周恩来と会談し上海コミュニケに署名。23年にわたる米中の断絶に終止符を打ち、両国関係正常化の幕開けとなった。",
            "ko": "닉슨 대통령이 중국을 방문, 마오쩌둥과 저우언라이를 만나 상하이 코뮤니케에 서명. 23년간의 미중 단절에 종지부를 찍고 양국 관계 정상화의 서막이 됨.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京", "en": "Beijing", "ja": "北京", "ko": "베이징"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/1972_Nixon_visit_to_China", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1976: Mao Zedong's death ======
    {
        "date": "1976-09-09",
        "date_precision": "day",
        "category": "politics",
        "importance": 95,
        "tags": ["mao", "death", "gang of four", "end of era"],
        "titles": {
            "zh_tw": "毛澤東逝世與四人幫垮台",
            "en": "Mao Zedong's death and arrest of the Gang of Four",
            "ja": "毛沢東の死去と四人組の逮捕",
            "ko": "마오쩌둥 사망과 사인방 체포",
        },
        "descriptions": {
            "zh_tw": "中共創始人毛澤東逝世，結束長達27年的統治。一個月後華國鋒等逮捕「四人幫」（江青、張春橋、姚文元、王洪文），文化大革命宣告結束。",
            "en": "CCP founder Mao Zedong died, ending 27 years of rule. One month later, Hua Guofeng arrested the 'Gang of Four' (Jiang Qing, Zhang Chunqiao, Yao Wenyuan, Wang Hongwen), ending the Cultural Revolution.",
            "ja": "中国共産党創設者・毛沢東が死去し、27年にわたる統治が終了。1ヶ月後、華国鋒らが「四人組」（江青、張春橋、姚文元、王洪文）を逮捕し、文化大革命が終結した。",
            "ko": "중국공산당 창시자 마오쩌둥 사망, 27년간의 통치 종료. 한 달 후 화궈펑 등이 '사인방'(장칭, 장춘차오, 야오원위안, 왕훙원)을 체포, 문화대혁명 종결.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京", "en": "Beijing", "ja": "北京", "ko": "베이징"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Death_of_Mao_Zedong", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1979: One-Child Policy ======
    {
        "date": "1979-09-01",
        "date_precision": "year",
        "category": "society",
        "importance": 80,
        "tags": ["population", "birth control", "social policy", "demographics"],
        "titles": {
            "zh_tw": "一胎化政策實施",
            "en": "One-Child Policy introduced",
            "ja": "一人っ子政策の導入",
            "ko": "한 자녀 정책 도입",
        },
        "descriptions": {
            "zh_tw": "中國政府正式實施計劃生育政策，限制城鎮家庭只能生育一個孩子。該政策持續至2016年，導致性別比例失衡、人口老齡化等長期社會問題。",
            "en": "China formally introduced a family planning policy limiting urban couples to one child. The policy lasted until 2016, causing long-term social problems including gender imbalance and population aging.",
            "ja": "中国政府が正式に計画出産政策を実施し、都市部の家庭は子供一人に制限。2016年まで続き、性別不均衡や高齢化などの長期的な社会問題を引き起こした。",
            "ko": "중국 정부가 공식적으로 가족계획 정책을 시행, 도시 가정은 자녀 한 명으로 제한. 2016년까지 지속되어 성비 불균형, 고령화 등 장기적 사회 문제를 초래.",
        },
        "location": {"lat": 35.0, "lng": 105.0, "country": "CN", "names": {"zh_tw": "中國全國", "en": "All of China", "ja": "中国全土", "ko": "중국 전역"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/One-child_policy", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1979: Sino-Vietnamese War ======
    {
        "date": "1979-02-17",
        "date_end": "1979-03-16",
        "date_precision": "day",
        "category": "military",
        "importance": 75,
        "tags": ["vietnam", "war", "border", "punitive"],
        "titles": {
            "zh_tw": "中越邊境戰爭",
            "en": "Sino-Vietnamese War",
            "ja": "中越国境戦争",
            "ko": "중국-베트남 국경 전쟁",
        },
        "descriptions": {
            "zh_tw": "中國為「懲罰」越南入侵柬埔寨並驅逐在越華人而發動長約一個月的邊境戰爭。雙方均宣稱勝利，但傷亡慘重。中越邊境衝突持續至1990年代。",
            "en": "China launched a month-long punitive war against Vietnam for invading Cambodia and expelling ethnic Chinese. Both sides claimed victory with heavy casualties. Border skirmishes continued into the 1990s.",
            "ja": "中国がベトナムのカンボジア侵攻と華僑追放に対する「懲罰」として約1ヶ月の国境戦争を開始。双方が勝利を主張し死傷者は甚大。国境紛争は1990年代まで継続。",
            "ko": "중국이 베트남의 캄보디아 침공과 화교 추방에 대한 '징벌'로 약 한 달간의 국경 전쟁을 시작. 양측이 승리를 주장했으나 사상자는 막대. 국경 분쟁은 1990년대까지 지속.",
        },
        "location": {"lat": 22.5, "lng": 106.5, "country": "VN", "names": {"zh_tw": "中越邊境", "en": "Sino-Vietnamese border", "ja": "中越国境", "ko": "중국-베트남 국경"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Sino-Vietnamese_War", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1980: Special Economic Zones ======
    {
        "date": "1980-08-26",
        "date_precision": "day",
        "category": "economy",
        "importance": 85,
        "tags": ["reform", "sez", "deng xiaoping", "economic opening"],
        "titles": {
            "zh_tw": "經濟特區成立（深圳、珠海、汕頭、廈門）",
            "en": "Establishment of Special Economic Zones (Shenzhen, Zhuhai, Shantou, Xiamen)",
            "ja": "経済特区の設立（深圳、珠海、汕頭、厦門）",
            "ko": "경제특구 설립 (선전, 주하이, 산터우, 샤먼)",
        },
        "descriptions": {
            "zh_tw": "全國人大批准設立深圳、珠海、汕頭、廈門為經濟特區，實行市場經濟政策和外資優惠。深圳從漁村發展為人口超過2000萬的國際大都市，成為中國經濟奇蹟的象徵。",
            "en": "The NPC approved Shenzhen, Zhuhai, Shantou, and Xiamen as Special Economic Zones with market-oriented policies and foreign investment incentives. Shenzhen grew from a fishing village to a 20M+ population megacity, symbolizing China's economic miracle.",
            "ja": "全国人民代表大会が深圳、珠海、汕頭、厦門を経済特区に指定、市場経済政策と外資優遇措置を導入。深圳は漁村から人口2000万以上の国際都市に成長し、中国の経済奇跡を象徴した。",
            "ko": "전국인민대표대회가 선전, 주하이, 산터우, 샤먼을 경제특구로 지정, 시장경제 정책과 외국인 투자 우대 조치 도입. 선전은 어촌에서 인구 2000만 이상의 국제 도시로 성장, 중국 경제 기적을 상징.",
        },
        "location": {"lat": 22.5431, "lng": 114.0579, "country": "CN", "names": {"zh_tw": "深圳", "en": "Shenzhen", "ja": "深圳", "ko": "선전"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Special_Economic_Zones_of_China", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1992: Deng Xiaoping Southern Tour ======
    {
        "date": "1992-01-18",
        "date_end": "1992-02-21",
        "date_precision": "day",
        "category": "economy",
        "importance": 85,
        "tags": ["deng xiaoping", "southern tour", "reform", "market economy"],
        "titles": {
            "zh_tw": "鄧小平南巡講話",
            "en": "Deng Xiaoping's Southern Tour (Nanxun)",
            "ja": "鄧小平の南巡講話",
            "ko": "덩샤오핑 남순 강화",
        },
        "descriptions": {
            "zh_tw": "鄧小平在88歲高齡視察深圳、珠海等地，發表鼓勵改革開放的講話。南巡重申市場經濟改革方向，終結了1989年後的改革停滯期，推動了中國經濟再次高速增長。",
            "en": "The 88-year-old Deng Xiaoping toured Shenzhen and Zhuhai, delivering speeches reaffirming market reforms. The Southern Tour ended the post-Tiananmen reform stagnation, reigniting China's rapid economic growth.",
            "ja": "88歳の鄧小平が深圳や珠海を視察し、改革開放を推進する講話を行った。南巡は1989年以降の改革停滞に終止符を打ち、中国経済の高度成長を再始動させた。",
            "ko": "88세의 덩샤오핑이 선전과 주하이를 시찰, 개혁개방을 촉진하는 연설. 남순은 1989년 이후의 개혁 정체를 종식시키고 중국 경제의 고속 성장을 재가동시킴.",
        },
        "location": {"lat": 22.5431, "lng": 114.0579, "country": "CN", "names": {"zh_tw": "深圳", "en": "Shenzhen", "ja": "深圳", "ko": "선전"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Deng_Xiaoping%27s_Southern_Tour", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 1995-96: Taiwan Strait Missile Crisis ======
    {
        "date": "1995-07-21",
        "date_end": "1996-03-23",
        "date_precision": "month",
        "category": "military",
        "importance": 75,
        "tags": ["taiwan", "missile", "military", "us-china"],
        "titles": {
            "zh_tw": "台海飛彈危機",
            "en": "Taiwan Strait Missile Crisis",
            "ja": "台湾海峡ミサイル危機",
            "ko": "대만 해협 미사일 위기",
        },
        "descriptions": {
            "zh_tw": "中國在台灣附近海域進行導彈試射和軍事演習，美國派遣兩艘航空母艦戰鬥群前往台灣海峽。危機凸顯台海緊張局勢與中美對抗風險。",
            "en": "China conducted missile tests and military exercises near Taiwan. The US dispatched two aircraft carrier battle groups to the Taiwan Strait. The crisis highlighted cross-strait tensions and US-China confrontation risks.",
            "ja": "中国が台湾周辺海域でミサイル発射実験と軍事演習を実施。米国は空母2隻の戦闘群を台湾海峡に派遣。台湾海峡の緊張と米中対立のリスクが浮き彫りになった。",
            "ko": "중국이 대만 주변 해역에서 미사일 발사 실험과 군사 훈련을 실시. 미국은 항모 2척의 전투단을 대만 해협에 파견. 대만 해협의 긴장과 미중 대립 위험이 부각됨.",
        },
        "location": {"lat": 25.0, "lng": 120.0, "country": "TW", "names": {"zh_tw": "台灣海峽", "en": "Taiwan Strait", "ja": "台湾海峡", "ko": "대만 해협"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Third_Taiwan_Strait_Crisis", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "TW", "lang": "zh_tw", "viewpoint": "台灣方面視飛彈危機為中國武力威脅的直接證據，強化了台灣社會對國防自主和國際支持的需求。危機也促使台灣重新評估與美國的安全關係。"},
            {"country": "US", "lang": "en", "viewpoint": "The US dispatched two carrier battle groups to the Taiwan Strait in a show of force, reaffirming its commitment to Taiwan's security. The crisis underscored the potential for US-China military conflict over Taiwan."},
        ],
    },
    # ====== 1999: US bombing of Chinese Embassy in Belgrade ======
    {
        "date": "1999-05-08",
        "date_precision": "day",
        "category": "foreign_relations",
        "importance": 70,
        "tags": ["us", "nato", "embassy", "bombing", "protests"],
        "titles": {
            "zh_tw": "五八事件（美軍轟炸中國駐南斯拉夫大使館）",
            "en": "US bombing of the Chinese Embassy in Belgrade (May 8 Incident)",
            "ja": "中国大使館爆撃事件（五八事件）",
            "ko": "중국 대사관 폭격 사건 (5·8 사건)",
        },
        "descriptions": {
            "zh_tw": "北約（NATO）轟炸南斯拉夫期間，美軍B-2轟炸機精確打擊中國駐貝爾格勒大使館，造成3人死亡。中國發生大規模反美抗議，中美關係嚴重受損。",
            "en": "During NATO's bombing of Yugoslavia, US B-2 bombers struck the Chinese Embassy in Belgrade, killing 3. Massive anti-US protests erupted in China, severely damaging US-China relations.",
            "ja": "NATOのユーゴスラビア爆撃中、米軍B-2爆撃機が中国のベオグラード大使館を精密爆撃し、3人が死亡。中国で大規模な反米抗議が発生し、米中関係は深刻に悪化した。",
            "ko": "NATO의 유고슬라비아 폭격 중 미군 B-2 폭격기가 중국의 베오그라드 대사관을 정밀 타격, 3명 사망. 중국에서 대규모 반미 항의 발생, 미중 관계 심각히 악화.",
        },
        "location": {"lat": 44.8000, "lng": 20.4600, "country": "RS", "names": {"zh_tw": "貝爾格勒（南斯拉夫）", "en": "Belgrade, Yugoslavia", "ja": "ベオグラード（ユーゴスラビア）", "ko": "베오그라드 (유고슬라비아)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/United_States_bombing_of_the_Chinese_embassy_in_Belgrade", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2003: Shenzhou 5 / First Manned Spaceflight ======
    {
        "date": "2003-10-15",
        "date_precision": "day",
        "category": "science_tech",
        "importance": 75,
        "tags": ["space", "shenzhou", "manned spaceflight", "technology"],
        "titles": {
            "zh_tw": "神舟五號（首次載人航天）",
            "en": "Shenzhou 5 (First crewed spaceflight)",
            "ja": "神舟5号（初の有人宇宙飛行）",
            "ko": "선저우 5호 (최초 유인 우주비행)",
        },
        "descriptions": {
            "zh_tw": "中國成功發射神舟五號載人太空船，航天員楊利偉成為中國首位太空人。中國成為繼蘇聯和美國之後第三個獨立實現載人航天的國家。",
            "en": "China successfully launched Shenzhou 5 with astronaut Yang Liwei, who became China's first person in space. China became the third country to independently achieve crewed spaceflight after Russia and the US.",
            "ja": "中国が神舟5号の打ち上げに成功し、楊利偉飛行士が中国人初の宇宙飛行士となった。中国はロシア、米国に次いで3番目に有人宇宙飛行を達成した国となった。",
            "ko": "중국이 선저우 5호 발사에 성공, 양리웨이 우주비행사가 중국 최초의 우주인이 됨. 중국은 러시아, 미국에 이어 세 번째로 독자적 유인 우주비행을 달성한 국가가 됨.",
        },
        "location": {"lat": 40.9600, "lng": 100.2900, "country": "CN", "names": {"zh_tw": "酒泉衛星發射中心", "en": "Jiuquan Satellite Launch Center", "ja": "酒泉衛星発射センター", "ko": "주취안 위성발사센터"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Shenzhou_5", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2005: Anti-Japanese Protests ======
    {
        "date": "2005-04-09",
        "date_end": "2005-04-16",
        "date_precision": "day",
        "category": "society",
        "importance": 60,
        "tags": ["japan", "protests", "nationalism", "anti-japanese"],
        "titles": {
            "zh_tw": "2005年反日示威",
            "en": "2005 Anti-Japanese protests",
            "ja": "2005年反日デモ",
            "ko": "2005년 반일 시위",
        },
        "descriptions": {
            "zh_tw": "北京、上海、廣州等地爆發大規模反日示威，抗議日本教科書美化侵略歷史和日本試圖成為聯合國安理會常任理事國。部分示威演變為打砸日本商店和使領館。",
            "en": "Large-scale anti-Japanese protests erupted in Beijing, Shanghai, and Guangzhou against Japanese textbook whitewashing and Japan's UN Security Council bid. Some protests turned violent, targeting Japanese businesses and diplomatic missions.",
            "ja": "北京、上海、広州などで大規模な反日デモが発生し、日本の教科書問題や国連安保理常任理事国入りに抗議。一部は暴徒化し日本企業や在外公館を標的にした。",
            "ko": "베이징, 상하이, 광저우 등에서 대규모 반일 시위 발생, 일본의 교과서 왜곡 문제와 유엔 안보리 상임이사국 진출에 항의. 일부는 폭력적으로 변해 일본 기업과 외교 공관을 표적으로 삼음.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京（全國多城市）", "en": "Beijing (multiple cities)", "ja": "北京（全国複数都市）", "ko": "베이징 (전국 여러 도시)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/2005_anti-Japanese_demonstrations", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2008: Tibet Unrest (March 14) ======
    {
        "date": "2008-03-14",
        "date_precision": "day",
        "category": "human_rights",
        "importance": 75,
        "tags": ["tibet", "protest", "unrest", "crackdown"],
        "titles": {
            "zh_tw": "2008年西藏騷亂（314事件）",
            "en": "2008 Tibetan unrest (March 14 Incident)",
            "ja": "2008年チベット騒乱（314事件）",
            "ko": "2008년 티베트 소요 사태 (314 사건)",
        },
        "descriptions": {
            "zh_tw": "西藏拉薩發生大規模抗議活動，隨後蔓延至其他藏區。中國政府實施戒嚴和鎮壓，造成數十人死亡。事件引發國際強烈譴責，並導致北京奧運聖火傳遞受到大規模抗議。",
            "en": "Large-scale protests erupted in Lhasa, Tibet, spreading to other Tibetan areas. The Chinese government imposed martial law and a crackdown, resulting in dozens of deaths. International condemnation followed, and the Olympic torch relay faced massive protests.",
            "ja": "チベットのラサで大規模な抗議活動が発生し、他のチベット地域に拡大。中国政府は戒厳令を敷き弾圧を行い数十人が死亡。国際的な非難を浴び、北京五輪の聖火リレーは大規模な抗議に直面した。",
            "ko": "티베트 라싸에서 대규모 항의 시위 발생, 다른 티베트 지역으로 확산. 중국 정부는 계엄령을 선포하고 진압, 수십 명 사망. 국제적 비난을 받았고 베이징 올림픽 성화 봉송은 대규모 항의에 직면.",
        },
        "location": {"lat": 29.6500, "lng": 91.1000, "country": "CN", "names": {"zh_tw": "拉薩", "en": "Lhasa", "ja": "ラサ", "ko": "라싸"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/2008_Tibetan_unrest", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "TW", "lang": "zh_tw", "viewpoint": "台灣方面關注西藏人權狀況，認為中共的民族政策壓迫少數民族。西藏流亡政府設立在印度達蘭薩拉，持續爭取國際社會對西藏自治的支持。"},
            {"country": "US", "lang": "en", "viewpoint": "The US government expressed deep concern over the crackdown and called for dialogue between China and the Dalai Lama. The incident further strained US-China relations ahead of the Beijing Olympics."},
        ],
    },
    # ====== 2009: Xinjiang Unrest (July 5) ======
    {
        "date": "2009-07-05",
        "date_precision": "day",
        "category": "human_rights",
        "importance": 75,
        "tags": ["xinjiang", "uyghur", "protest", "unrest", "ethnic"],
        "titles": {
            "zh_tw": "2009年新疆騷亂（七五事件）",
            "en": "2009 Xinjiang unrest (July 5 Incident)",
            "ja": "2009年新疆騒乱（七一五事件）",
            "ko": "2009년 신장 소요 사태 (7·5 사건)",
        },
        "descriptions": {
            "zh_tw": "新疆烏魯木齊發生維吾爾族與漢族之間的嚴重種族衝突，造成近200人死亡，上千人受傷。事件後中國政府大幅加強對新疆的監控和管控措施。",
            "en": "Severe ethnic clashes between Uyghurs and Han Chinese in Urumqi, Xinjiang, left nearly 200 dead and thousands injured. The Chinese government subsequently intensified surveillance and control measures across Xinjiang.",
            "ja": "新疆ウルムチでウイグル族と漢族の間で深刻な民族衝突が発生し、約200人が死亡、数千人が負傷。中国政府はその後、新疆全体での監視と統制措置を大幅に強化した。",
            "ko": "신장 우루무치에서 위구르족과 한족 간 심각한 민족 충돌 발생, 약 200명 사망, 수천 명 부상. 중국 정부는 이후 신장 전역에서 감시와 통제 조치를 대폭 강화.",
        },
        "location": {"lat": 43.8250, "lng": 87.6000, "country": "CN", "names": {"zh_tw": "烏魯木齊", "en": "Urumqi", "ja": "ウルムチ", "ko": "우루무치"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/July_2009_%C3%9Cr%C3%BCmqi_riots", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2010: China becomes world's 2nd largest economy ======
    {
        "date": "2010-08-16",
        "date_precision": "month",
        "category": "economy",
        "importance": 85,
        "tags": ["economy", "gdp", "japan", "milestone"],
        "titles": {
            "zh_tw": "中國GDP超越日本成為世界第二大經濟體",
            "en": "China surpasses Japan as world's second-largest economy",
            "ja": "中国が日本を抜き世界第2位の経済大国に",
            "ko": "중국 GDP 일본 추월, 세계 2위 경제 대국으로 부상",
        },
        "descriptions": {
            "zh_tw": "中國第二季GDP正式超越日本，成為僅次於美國的世界第二大經濟體。這是自19世紀初以來中國首次重返世界經濟前列。",
            "en": "China's Q2 GDP officially surpassed Japan, making China the world's second-largest economy after the US. This marked China's return to the top tier of the global economy for the first time since the early 19th century.",
            "ja": "中国の第2四半期GDPが正式に日本を上回り、米国に次ぐ世界第2位の経済大国となった。19世紀初頭以来、中国が世界経済のトップ層に返り咲いたことを示す。",
            "ko": "중국의 2분기 GDP가 공식적으로 일본을 추월, 미국에 이은 세계 2위 경제 대국으로 부상. 19세기 초 이후 처음으로 중국이 세계 경제의 최상위권에 복귀했음을 의미.",
        },
        "location": {"lat": 35.0, "lng": 105.0, "country": "CN", "names": {"zh_tw": "中國", "en": "China", "ja": "中国", "ko": "중국"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/History_of_the_People%27s_Republic_of_China", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2012: Bo Xilai Scandal ======
    {
        "date": "2012-03-15",
        "date_precision": "day",
        "category": "politics",
        "importance": 70,
        "tags": ["bo xilai", "corruption", "purge", "power struggle"],
        "titles": {
            "zh_tw": "薄熙來事件",
            "en": "Bo Xilai scandal",
            "ja": "薄熙来事件",
            "ko": "보시라이 사건",
        },
        "descriptions": {
            "zh_tw": "重慶市委書記薄熙來因貪腐、濫用職權被調查，後被判無期徒刑。事件涉及薄熙來的妻子谷開來殺人案及王立軍叛逃案，凸顯中共高層權力鬥爭。",
            "en": "Chongqing party chief Bo Xilai was investigated for corruption and abuse of power, receiving a life sentence. The scandal involving his wife Gu Kailai's murder case and Wang Lijun's defection exposed elite power struggles.",
            "ja": "重慶市委書記・薄熙来が汚職と権力濫用で調査を受け、無期懲役の判決。妻・谷開来の殺人事件や王立軍の亡命事件も絡み、中共エリートの権力闘争を露呈した。",
            "ko": "충칭 시당 서기 보시라이가 부패와 권력 남용으로 조사받고 무기징역 선고. 아내 구카이라이의 살인 사건과 왕리쥔의 망명 사건이 얽히며 중국공산당 엘리트의 권력 투쟁을 드러냄.",
        },
        "location": {"lat": 29.5630, "lng": 106.5510, "country": "CN", "names": {"zh_tw": "重慶", "en": "Chongqing", "ja": "重慶", "ko": "충칭"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Bo_Xilai_scandal", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2012: Xi Jinping becomes CCP General Secretary ======
    {
        "date": "2012-11-15",
        "date_precision": "day",
        "category": "politics",
        "importance": 95,
        "tags": ["xi jinping", "leadership", "party congress", "18th congress"],
        "titles": {
            "zh_tw": "習近平出任中共中央總書記",
            "en": "Xi Jinping becomes CCP General Secretary",
            "ja": "習近平が中国共産党総書記に就任",
            "ko": "시진핑 중국공산당 총서기 취임",
        },
        "descriptions": {
            "zh_tw": "中共十八屆一中全會選舉習近平為中共中央總書記、中央軍委主席，正式接替胡錦濤成為中國最高領導人。習近平隨後提出「中國夢」理念，開啟強勢領導時代。",
            "en": "The 18th CCP Central Committee elected Xi Jinping as General Secretary and Chairman of the Central Military Commission, succeeding Hu Jintao as China's paramount leader. Xi soon introduced the 'Chinese Dream' vision, ushering in an era of assertive leadership.",
            "ja": "中国共産党第18期中央委員会第一回全体会議で、習近平が総書記と中央軍事委員会主席に選出され、胡錦濤の後継者として中国の最高指導者となった。習近平は「中国夢」理念を打ち出し、強力な指導力の時代を開始した。",
            "ko": "중국공산당 제18기 중앙위원회 제1차 전체회의에서 시진핑이 총서기와 중앙군사위원회 주석으로 선출, 후진타오의 후계자로 중국 최고 지도자가 됨. 시진핑은 '중국몽(中國夢)' 이념을 제시하며 강력한 지도력의 시대를 시작.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京人民大會堂", "en": "Great Hall of the People, Beijing", "ja": "北京人民大会堂", "ko": "베이징 인민대회당"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/18th_National_Congress_of_the_Chinese_Communist_Party", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2014: Hong Kong Umbrella Movement ======
    {
        "date": "2014-09-28",
        "date_end": "2014-12-15",
        "date_precision": "day",
        "category": "human_rights",
        "importance": 80,
        "tags": ["hong kong", "umbrella movement", "democracy", "occupy central"],
        "titles": {
            "zh_tw": "香港雨傘運動",
            "en": "Hong Kong Umbrella Movement (Occupy Central)",
            "ja": "香港雨傘運動",
            "ko": "홍콩 우산 혁명",
        },
        "descriptions": {
            "zh_tw": "香港學生和市民發起佔領中環運動，抗議全國人大對2017年普選方案的決定。抗議持續79天，最終被警方清場。運動標誌著香港人對北京干預自治的強烈反彈。",
            "en": "Hong Kong students and citizens launched Occupy Central, protesting the NPC's decision on 2017 election reform. The 79-day protest ended with a police clearance. The movement marked a strong backlash against Beijing's intervention in Hong Kong's autonomy.",
            "ja": "香港の学生と市民が中環占拠（Occupy Central）を開始し、全国人民代表大会の2017年選挙制度改革決定に抗議。79日間の抗議は警察による強制排除で終了。北京の香港自治への干渉に対する強い反発を示した。",
            "ko": "홍콩 학생과 시민이 중환 점거를 시작, 전국인민대표대회의 2017년 선거 개혁 결정에 항의. 79일간의 항의는 경찰에 의한 강제 진압으로 종료. 베이징의 홍콩 자치 간섭에 대한 강한 반발을 보여줌.",
        },
        "location": {"lat": 22.2796, "lng": 114.1593, "country": "HK", "names": {"zh_tw": "香港中環", "en": "Central, Hong Kong", "ja": "香港中環", "ko": "홍콩 중환"},
        },
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/2014_Hong_Kong_protests", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2016: South China Sea Arbitration ======
    {
        "date": "2016-07-12",
        "date_precision": "day",
        "category": "foreign_relations",
        "importance": 75,
        "tags": ["south china sea", "arbitration", "philippines", "international law"],
        "titles": {
            "zh_tw": "南海仲裁案裁決",
            "en": "South China Sea Arbitration ruling",
            "ja": "南シナ海仲裁裁判所判決",
            "ko": "남중국해 중재재판소 판결",
        },
        "descriptions": {
            "zh_tw": "海牙常設仲裁法院就菲律賓提出的南海仲裁案作出裁決，否定了中國的九段線主張。中國拒絕接受裁決，並加強南海島礁建設和軍事化。",
            "en": "The Permanent Court of Arbitration in The Hague ruled against China's nine-dash line claims in the South China Sea. China rejected the ruling and intensified island construction and militarization in the region.",
            "ja": "ハーグの常設仲裁裁判所がフィリピン提訴の南シナ海仲裁で中国の九段線主張を否定する判決。中国は判決を拒否し、南シナ海での島嶼建設と軍事化を強化した。",
            "ko": "헤이그 상설중재재판소가 필리핀 제기 남중국해 중재에서 중국의 구단선 주장을 부정하는 판결. 중국은 판결을 거부하고 남중국해에서 섬 건설과 군사화를 강화.",
        },
        "location": {"lat": 10.0, "lng": 115.0, "country": "PH", "names": {"zh_tw": "南海（菲律賓提起仲裁）", "en": "South China Sea", "ja": "南シナ海", "ko": "남중국해"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Philippines_v._China", "publisher": "Wikipedia", "reliability": 0.8},
        ],
        "perspectives": [
            {"country": "TW", "lang": "zh_tw", "viewpoint": "台灣雖然非仲裁案當事方，但南海爭議涉及太平島等台灣控制的島嶼。仲裁案裁決將太平島認定為『岩礁』而非『島嶼』，影響台灣的南海權益主張。"},
            {"country": "US", "lang": "en", "viewpoint": "The US urged China to abide by the arbitration ruling and has conducted Freedom of Navigation Operations to challenge China's expansive maritime claims. The South China Sea disputes remain a key flashpoint in US-China tensions."},
        ],
    },
    # ====== 2018: Xi term limit removal / Constitutional amendment ======
    {
        "date": "2018-03-11",
        "date_precision": "day",
        "category": "politics",
        "importance": 85,
        "tags": ["xi jinping", "constitution", "term limit", "authoritarianism"],
        "titles": {
            "zh_tw": "2018年修憲（取消國家主席任期限制）",
            "en": "2018 constitutional amendment (removal of presidential term limits)",
            "ja": "2018年憲法改正（国家主席任期制限撤廃）",
            "ko": "2018년 헌법 개정 (국가주석 임기 제한 철폐)",
        },
        "descriptions": {
            "zh_tw": "全國人大代表投票通過憲法修正案，取消國家主席和副主席「連續任職不得超過兩屆」的限制。此舉被視為習近平鞏固個人權力的關鍵步驟。",
            "en": "The NPC voted to pass a constitutional amendment removing the two-term limit for the president and vice president. The move was widely seen as a key step by Xi Jinping to consolidate personal power.",
            "ja": "全国人民代表大会が憲法改正を可決し、国家主席と副主席の「連続2期まで」の任期制限を撤廃。習近平による個人権力強化の重要な一歩と広く見なされた。",
            "ko": "전국인민대표대회가 헌법 개정안을 가결, 국가주석과 부주석의 '연속 2기' 임기 제한을 철폐. 시진핑의 개인 권력 강화를 위한 핵심 단계로 널리 평가됨.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京人民大會堂", "en": "Great Hall of the People, Beijing", "ja": "北京人民大会堂", "ko": "베이징 인민대회당"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/2018_Chinese_constitutional_amendment", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2018: China-US Trade War begins ======
    {
        "date": "2018-07-06",
        "date_precision": "day",
        "category": "economy",
        "importance": 80,
        "tags": ["trade war", "us-china", "tariffs", "trump", "economy"],
        "titles": {
            "zh_tw": "中美貿易戰爆發",
            "en": "US-China Trade War begins",
            "ja": "米中貿易戦争の勃発",
            "ko": "미중 무역 전쟁 발발",
        },
        "descriptions": {
            "zh_tw": "美國總統川普對中國340億美元商品加徵關稅，中國隨即報復。貿易戰持續多年，涵蓋技術封鎖（華為禁令）、供應鏈脫鉤等範疇，重塑全球經濟格局。",
            "en": "President Trump imposed tariffs on $34B of Chinese goods, prompting Chinese retaliation. The trade war expanded to tech decoupling (Huawei ban) and supply chain restructuring, reshaping the global economic order.",
            "ja": "トランプ大統領が中国から340億ドル相当の輸入品に関税を課し、中国が報復関税で応酬。貿易戦争は技術封鎖（ファーウェイ禁止）やサプライチェーン再編に拡大し、世界経済秩序を再編した。",
            "ko": "트럼프 대통령이 중국산 340억 달러 상품에 관세를 부과, 중국이 보복 관세로 응수. 무역 전쟁은 기술 봉쇄(화웨이 금지)와 공급망 재편으로 확대되어 세계 경제 질서를 재편.",
        },
        "location": {"lat": 35.0, "lng": 105.0, "country": "CN", "names": {"zh_tw": "中國（全球）", "en": "China (global)", "ja": "中国（全世界）", "ko": "중국 (전 세계)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/China%E2%80%93United_States_trade_war", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2020: Hong Kong National Security Law ======
    {
        "date": "2020-06-30",
        "date_precision": "day",
        "category": "politics",
        "importance": 85,
        "tags": ["hong kong", "national security law", "autonomy", "human rights"],
        "titles": {
            "zh_tw": "《香港國安法》實施",
            "en": "Hong Kong National Security Law imposed",
            "ja": "香港国家安全法の施行",
            "ko": "홍콩 국가안전법 시행",
        },
        "descriptions": {
            "zh_tw": "北京直接頒布《香港國安法》並在港實施，設立由特首任命法官的國安案件專門法庭。此法大幅限制香港的言論、集會和新聞自由，引發西方國家制裁。",
            "en": "Beijing directly imposed the National Security Law on Hong Kong, establishing a special court for national security cases. The law sharply curtailed freedoms of speech, assembly, and press, triggering Western sanctions.",
            "ja": "北京が直接香港国家安全法を制定・施行し、国家安全案件のための特別裁判所を設置。この法律は言論、集会、報道の自由を大幅に制限し、西側諸国の制裁を招いた。",
            "ko": "베이징이 직접 홍콩 국가안전법을 제정·시행, 국가안전 사건을 위한 특별 법원 설치. 이 법은 언론, 집회, 언론의 자유를 대폭 제한하고 서방 국가들의 제재를 초래.",
        },
        "location": {"lat": 22.3193, "lng": 114.1694, "country": "HK", "names": {"zh_tw": "香港", "en": "Hong Kong", "ja": "香港", "ko": "홍콩"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Hong_Kong_national_security_law", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2021: Evergrande Debt Crisis ======
    {
        "date": "2021-09-14",
        "date_precision": "day",
        "category": "economy",
        "importance": 70,
        "tags": ["evergrande", "debt crisis", "real estate", "financial"],
        "titles": {
            "zh_tw": "恒大債務危機",
            "en": "Evergrande debt crisis",
            "ja": "恒大（エバーグランデ）債務危機",
            "ko": "에버그란데 부채 위기",
        },
        "descriptions": {
            "zh_tw": "中國最大房地產開發商恒大集團未能按期支付債券利息，觸發中國房地產行業的全面債務危機。危機波及全球金融市場，凸顯中國「大到不能倒」的系統性風險。",
            "en": "China's largest developer Evergrande failed to make bond payments, triggering a debt crisis across the property sector. The crisis rippled through global markets, highlighting systemic risks in China's 'too big to fail' corporate landscape.",
            "ja": "中国最大の不動産デベロッパー恒大集団が社債利払いを滞り、不動産業界全体の債務危機を引き起こした。世界的な金融市場に波及し、「大きすぎて潰せない」中国企業のシステムリスクを露呈。",
            "ko": "중국 최대 부동산 개발업체 에버그란데가 회사채 이자 지급을 연체, 부동산 업계 전반의 부채 위기를 촉발. 위기는 글로벌 금융 시장에 파급되며 '너무 커서 무너뜨릴 수 없는' 중국 기업의 시스템 리스크를 노출.",
        },
        "location": {"lat": 23.1300, "lng": 113.2600, "country": "CN", "names": {"zh_tw": "深圳（恒大總部）", "en": "Shenzhen (Evergrande HQ)", "ja": "深圳（恒大本社）", "ko": "선전 (에버그란데 본사)"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/Evergrande_debt_crisis", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2021: CCP 100th Anniversary ======
    {
        "date": "2021-07-01",
        "date_precision": "day",
        "category": "politics",
        "importance": 80,
        "tags": ["ccp", "centenary", "propaganda", "xi jinping"],
        "titles": {
            "zh_tw": "中國共產黨成立100週年",
            "en": "100th Anniversary of the Chinese Communist Party",
            "ja": "中国共産党創立100周年",
            "ko": "중국공산당 창당 100주년",
        },
        "descriptions": {
            "zh_tw": "中共在北京盛大慶祝建黨百年，習近平發表重要講話，宣告「第一個百年奮鬥目標」實現——全面建成小康社會。慶祝活動包括大型文藝演出、頒授七一勳章等。",
            "en": "The CCP grandly celebrated its centenary in Beijing. Xi Jinping delivered a major speech declaring the 'First Centenary Goal' achieved — building a moderately prosperous society in all respects. Celebrations included a gala and the July 1 Medal awards.",
            "ja": "中国共産党が北京で盛大に創立100周年を祝賀。習近平が重要講話を述べ、「第一の百年奮闘目標」である「小康社会の全面的完成」を宣言。祝賀行事には大規模文芸公演や七一勲章授与などが含まれた。",
            "ko": "중국공산당이 베이징에서 창당 100주년을 성대히 축하. 시진핑이 중요 연설에서 '제1차 백년 분투 목표'인 전면적 샤오캉 사회 건설 완성을 선언. 축하 행사에는 대규모 문예 공연과 7·1 훈장 수여 등이 포함.",
        },
        "location": {"lat": 39.9042, "lng": 116.4074, "country": "CN", "names": {"zh_tw": "北京天安門廣場", "en": "Tiananmen Square, Beijing", "ja": "北京天安門広場", "ko": "베이징 톈안먼 광장"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/100th_Anniversary_of_the_Chinese_Communist_Party", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
    # ====== 2022: Shanghai COVID Lockdown ======
    {
        "date": "2022-03-28",
        "date_end": "2022-06-01",
        "date_precision": "day",
        "category": "society",
        "importance": 75,
        "tags": ["covid", "shanghai", "lockdown", "zero-covid", "protests"],
        "titles": {
            "zh_tw": "上海封城與白紙運動",
            "en": "Shanghai lockdown and Blank Paper Protests",
            "ja": "上海封鎖と白紙運動",
            "ko": "상하이 봉쇄와 백지 시위",
        },
        "descriptions": {
            "zh_tw": "上海因Omicron變種疫情實施兩個多月嚴格封城，居民生活嚴重受限。2022年11月全國多地爆發「白紙運動」抗議封控措施，最終迫使北京政府迅速放寬清零政策。",
            "en": "Shanghai endured over two months of strict lockdown due to Omicron. In November 2022, the 'Blank Paper Protests' erupted nationwide against zero-COVID policies, forcing Beijing to rapidly unwind the lockdown regime.",
            "ja": "上海がオミクロン株流行により2ヶ月以上にわたる厳格な封鎖を経験。2022年11月には全国で「白紙運動」が発生し、ゼロコロナ政策に抗議、北京は封鎖政策を急速に緩和せざるを得なかった。",
            "ko": "상하이가 오미크론 변이 유행으로 두 달 이상의 엄격한 봉쇄를 경험. 2022년 11월 전국에서 '백지 시위'가 발생, 제로코로나 정책에 항의, 베이징은 봉쇄 정책을 급속히 완화할 수밖에 없었음.",
        },
        "location": {"lat": 31.2304, "lng": 121.4737, "country": "CN", "names": {"zh_tw": "上海", "en": "Shanghai", "ja": "上海", "ko": "상하이"}},
        "sources": [
            {"lang": "en", "url": "https://en.wikipedia.org/wiki/2022_Shanghai_lockdown", "publisher": "Wikipedia", "reliability": 0.8},
        ],
    },
]
