# -*- coding: utf-8 -*-
"""選修生物（Ⅱ）教材入口網站產生器：內容依翰林版《選修生物Ⅱ（全）》課本改寫。
修改網址、簡介或重點時，改本檔的 CHAPTERS 資料後重新執行即可。"""
import html, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
DRIVE = 'https://drive.google.com/file/d/{}/view?usp=drivesdk'

ICON_OUT = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_GO = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_ZOOM = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m16 16 4.5 4.5M8.5 11h5M11 8.5v5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
ICON_PLAY = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 8.5v7l6-3.5z" fill="currentColor"/></svg>'
ICON_BOOK = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5C6.5 4.5 9.5 4.5 12 6c2.5-1.5 5.5-1.5 8-.5v13c-2.5-1-5.5-1-8 .5-2.5-1.5-5.5-1.5-8-.5z M12 6v13.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'

E = html.escape

CHAPTERS = [
 dict(n=1, title='生物的起源與演化', en='Origin &amp; Evolution of Life', a='#0d9488', a2='#2dd4bf', t='#f0fdfa',
  lead='生命從何而來？本章從科學史上生源說與無生源說的經典論辯談起，探討雷迪、尼達姆、斯帕蘭札尼到巴斯德鵝頸瓶實驗如何以證據終結爭議；再循化學演化假說與米勒-尤里實驗追溯原始生命的誕生，最後透過內共生學說與三域系統認識生命形式的多樣化與演化大樹。',
  units=[
   dict(code='1-1', title='生源說與無生源說', web='生源論戰法庭', slug='ch1-1', vid='1tQ3aWW5F4WrJBRgr5rVs7dSD26uhW4cj', pages='P.8–14',
    fig='s1-1', cap='圖 1－4　巴斯德的鵝頸瓶實驗示意圖',
    intro='古代人們曾普遍相信無生源說（自然發生論），認為無生命的腐肉能生出蛆蟲。1668 年雷迪設計對照實驗打破腐肉生蛆之迷思；隨顯微鏡問世，尼達姆與斯帕蘭札尼就加熱肉汁中微生物的來源展開激烈論辯；直至 1860 年代法國微生物學家巴斯德設計精巧的「鵝頸瓶實驗」，證明空氣中的微生物沉降於彎曲頸部，肉汁不腐敗，唯有傾斜接觸塵埃才會滋生細菌，確立了「生源說」——生命只能由已存在的生命產生。',
    subs=['1-1.1 無生源說與生源說的爭議', '1-1.2 雷迪的腐肉生蛆實驗', '1-1.3 尼達姆與斯帕蘭札尼的肉汁加熱實驗', '1-1.4 巴斯德的鵝頸瓶實驗與生源說確立'],
    tags=['自然發生論', '雷迪對照實驗', '肉汁加熱爭辯', '鵝頸瓶實驗', '巴斯德', '生源說確立']),
   dict(code='1-2', title='生命的起源與化學演化', web='生命起源探索站', slug='ch1-2', vid='19nq8CJQzr84Bg38lkWrAvlI-wH14av-7', pages='P.15–21',
    fig='s1-2', cap='圖 1－8　米勒與尤里的化學演化模擬實驗裝置',
    intro='既然「生源說」確立生命來自生命，那地球上最初的生命又是如何誕生的？奧柏林與霍爾丹提出化學演化假說，認為原始地球在無游離氧的還原性大氣下，閃電與紫外線促成了無機物合成簡單有機分子。1953 年米勒與尤里以密閉循環裝置模擬原始大氣並放電，成功合成胺基酸等多種有機物；隨後有機單體聚合成高分子、形成具原始膜結構的原細胞，並由具催化與遺傳功能的 RNA 邁入「RNA 世界」，最終演化出以 DNA 儲存訊息的原始細胞。',
    subs=['1-2.1 化學演化假說與原始地球環境', '1-2.2 米勒與尤里的放電模擬實驗', '1-2.3 有機單體聚合與高分子形成', '1-2.4 原細胞與 RNA 世界假說'],
    tags=['化學演化', '原始大氣', '米勒-尤里實驗', '胺基酸合成', '原細胞', 'RNA 世界']),
   dict(code='1-3', title='生命形式的多樣化', web='生命多樣化探索站', slug='ch1-3', vid='1yQxcRxkJwWsJvvqNa9NNIUS3fmMlSANR', pages='P.22–31',
    fig='s1-3', cap='圖 1－12　原核生物演化為真核細胞的內共生學說歷程',
    intro='原始生命在演化洪流中不斷分化適應。從最早的厭氧異營原核生物，到發展出產氧光合作用的藍綠菌改變大氣組成；馬古利斯提出「內共生學說」，解釋原核生物如何透過吞噬好氧細菌與光合細菌，逐漸演化出含有粒線體與葉綠體的真核細胞。隨著細胞骨架與有絲分裂發展，真核生物進一步由單細胞邁向群體與多細胞個體，並依 rRNA 序列分化為細菌域、古菌域與真核生物域三域系統，展現出當今繽紛多樣的生物多樣性。',
    subs=['1-3.1 厭氧異營到光合自營的演化歷程', '1-3.2 內共生學說（粒線體與葉綠體的起源）', '1-3.3 單細胞到多細胞生物的演化', '1-3.4 生命之樹：三域系統（細菌、古菌、真核）'],
    tags=['藍綠菌產氧', '內共生學說', '雙層膜與獨立DNA', '多細胞演化', '三域系統', '生命之樹']),
  ],
  labs=[]),
 dict(n=2, title='植物體的構造與功能', en='Plant Structure &amp; Function', a='#059669', a2='#34d399', t='#ecfdf5',
  lead='植物是陸域生態系的主要生產者。本章從植物細胞的特化、分生組織與永久組織（保護、輸導與基本組織系統）的組成層次切入，接著剖析根、莖、葉等營養器官的解剖構造與初生、次級生長，並探討植物根莖葉為適應環境所演化出的多樣形態特化。',
  units=[
   dict(code='2-1', title='植物體的構造與組成層次', web='植物構造探索站', slug='ch2-1', vid='1BFsjv8pVswjHeq_xH8hGeaPPsQh3g9hN', pages='P.32–41',
    fig='s2-1', cap='圖 2－5　被子植物組織系統之微觀構造與組成層次',
    intro='植物體由細胞、組織、器官逐步構建而成。細胞具纖維素細胞壁，特化時初生壁外可加厚次生壁與木質化。組織分為具分裂能力的分生組織（頂端分生組織、側生分生組織）與分化完成的永久組織。依功能分為三大組織系統：表皮與周皮構成保護組織系統；木質部（導管、管胞）與韌皮部（篩管、伴細胞）構成輸導組織系統；薄壁、厚角與厚壁細胞則組成執行光合、儲藏與支持的基本組織系統。',
    subs=['2-1.1 植物細胞的構造特色與細胞壁特化', '2-1.2 分生組織（頂端與側生分生組織）', '2-1.3 永久組織與三大組織系統（保護、輸導、基本組織系統）', '2-1.4 導管、管胞、篩管與伴細胞的功能比較'],
    tags=['細胞壁木質化', '頂端分生組織', '形成層', '保護組織系統', '輸導組織系統', '基本組織系統']),
   dict(code='2-2', title='植物體的營養器官', web='植物器官探索站', slug='ch2-2', vid='11G1TJsSHEegGsTIRHUrVr-NMxULTbIBR', pages='P.42–57',
    fig='s2-2', cap='圖 2－13　雙子葉植物與單子葉植物根與莖橫切面解剖比較',
    intro='植物營養器官包括根、莖、葉。根尖由根冠保護，經細胞分裂區、延長區至成熟區分化出根毛，中柱內皮細胞具不透水卡氏帶；雙子葉根木質部呈星狀，單子葉根木質部與韌皮部環列中柱。莖具節與節間，雙子葉草本莖維管束環狀排列，木本莖經維管束形成層與木栓形成層次級生長形成木材與年輪；單子葉莖維管束則散生。葉片上下表皮具氣孔與保衛細胞，葉肉分為柵狀組織與海綿組織，葉脈維管束由維管束鞘包圍。',
    subs=['2-2.1 根的解剖構造（根尖分區、內皮卡氏帶與中柱構造）', '2-2.2 莖的初生與次級生長（木本莖、維管束形成層與年輪）', '2-2.3 葉的橫切面解剖（表皮、氣孔保衛細胞、葉肉與葉脈）', '2-2.4 根、莖、葉的形態特化與環境適應'],
    tags=['根尖構造', '卡氏帶', '雙子葉與單子葉比較', '形成層與年輪', '柵狀與海綿組織', '營養器官特化']),
  ],
  labs=[
   dict(code='活動 2-1', title='植物的細胞與組織', web='植物組織觀察站', slug='lab2-1', vid='1DDge5EBqNlULu5Cc8kdrJW_KOAEcIKGI', pages='P.58–61',
    fig='a2-1', cap='徒手切片法製作植物莖與葉之水埋玻片標本並進行顯微觀察',
    intro='透過徒手切片技巧，以保麗龍夾持芹菜葉柄、紫背萬年青葉或咸豐草莖，切出極薄橫切片並製作水埋玻片。以複式顯微鏡低倍及高倍鏡觀察保護組織（表皮、角質層、氣孔）、基本組織（薄壁細胞、厚角細胞、厚壁纖維）與輸導組織（導管、篩管），對比理論構造並繪製精確的生物繪圖。'),
   dict(code='活動 2-2', title='營養構造的形態適應與特化', web='植物特化探索站', slug='lab2-2', vid='1QW17Yi8IUm24ZDxIQBvC2UrO4XSIdSxq', pages='P.62–67',
    fig='a2-2', cap='觀察紅樹林水筆仔胎生苗、氣生根與多肉植物特化營養構造',
    intro='採集或觀察多樣特化器官實物：紅樹林氣生根與支持根、胡蘿蔔儲藏根；馬鈴薯塊莖、洋蔥鱗莖、黃金葛攀緣莖、仙人掌葉狀莖；豬籠草捕蟲葉、九重葛艷麗苞葉、洋蔥肉質鱗葉等，藉形態與內部構造分辨器官來源，探討植物對乾旱、淹水與攀爬等環境因子的形態適應。'),
  ]),
 dict(n=3, title='植物體內物質的吸收、合成及運輸', en='Plant Transport &amp; Photosynthesis', a='#16a34a', a2='#4ade80', t='#f0fdf4',
  lead='植物如何不靠心臟與幫浦將水分由數十公尺深的土壤抽至頂端？本章探索根部共質體與質外體途徑吸水、卡氏帶的把關，以及蒸散拉力與凝聚力-張力學說的運輸機制；接著深入葉綠體解析光反應（水裂解、電子傳遞、光合磷酸化）與卡爾文循環固碳，最後以壓力流假說解釋韌皮部篩管有機養分的跨器官調度。',
  units=[
   dict(code='3-1', title='植物體對水與無機鹽的吸收', web='植物吸收探索站', slug='ch3-1', vid='1rQZr96v_dlaQhxHZoVOGweLEjCWxbi_8', pages='P.70–73',
    fig='s3-1', cap='圖 3－2　水與無機鹽經質外體途徑與共質體途徑穿過內皮卡氏帶',
    intro='土壤中的水分藉滲透作用進入根毛，無機鹽則透過載體蛋白進行主動運輸。水分與離子橫向運送進入中柱有兩條路徑：沿著細胞壁與細胞間隙移動的「質外體途徑」，以及穿過細胞膜經由細胞質與原生質絲移動的「共質體途徑」。當水流抵達內皮層時，因卡氏帶含木質素與木栓質不透水，質外體水流被迫穿透內皮細胞膜轉入共質體，使內皮層扮演嚴格的選擇性關卡。',
    subs=['3-1.1 根毛的水分滲透與無機鹽主動運輸', '3-1.2 質外體途徑與共質體途徑', '3-1.3 內皮層與卡氏帶的選擇性把關機制', '3-1.4 菌根與根瘤菌之共生促吸收機制'],
    tags=['根毛吸收', '滲透與主動運輸', '質外體途徑', '共質體途徑', '卡氏帶', '菌根共生']),
   dict(code='3-2', title='植物體內水與無機鹽的運輸', web='植物運輸探索站', slug='ch3-2', vid='1CtaYB8slvF57P0Oyag53rGtRCJ0oyPo3', pages='P.74–77',
    fig='s3-2', cap='圖 3－4　水與無機鹽在木質部中向上運輸的綜合機制（凝聚力-張力學說）',
    intro='水與無機鹽在木質部導管與管胞中單向由下往上運送。運輸的主要原動力來自葉片蒸散作用產生的巨大拉力；水分子間因氫鍵產生的「凝聚力」，以及水分子與細胞壁間的「附著力」，維持了木質部內連續不中斷的水柱（凝聚力-張力學說）。此外，根部中柱主動吸收離子累積溶質產生的「根壓」可推動夜間水分上升並造成泌溢現象；而保衛細胞受光刺激累積 K⁺ 吸水膨脹使氣孔張開，調控蒸散速率。',
    subs=['3-2.1 木質部向上運輸的三大動力（蒸散拉力、水分子凝聚力、根壓）', '3-2.2 凝聚力-張力學說與毛細現象', '3-2.3 根壓的產生與泌溢現象', '3-2.4 保衛細胞膨壓變化與氣孔開閉調節機制'],
    tags=['蒸散拉力', '凝聚力-張力學說', '氫鍵凝聚力', '根壓與泌溢', '保衛細胞膨壓', '氣孔開閉']),
   dict(code='3-3', title='光合作用', web='光合作用探索站', slug='ch3-3', vid='12St3aSOE9k_h5AQESvvIerD2pdgZV4Lx', pages='P.78–88',
    fig='s3-3', cap='圖 3－10 &amp; 3－11　葉綠體內光反應與卡爾文循環固碳歷程全景',
    intro='光合作用在葉綠體進行，分為類囊體膜上的光反應與基質中的碳反應（卡爾文循環）。光系統由捕光複合體與反應中心構成，葉綠素 a/b 與類胡蘿蔔素吸收光能激發電子；水分子在光系統 Ⅱ 裂解釋出 O₂、H⁺ 與電子，電子沿電子傳遞鏈傳遞建立膜兩側 H⁺ 濃度差，驅動 ATP 合成酶進行光合磷酸化，並在光系統 Ⅰ 終端生成 NADPH。碳反應中，RuBisCO 酵素催化 CO₂ 與 RuBP 結合，消耗 ATP 與 NADPH 經還原與再生步驟合成三碳醣（G3P），進而轉變為葡萄糖與澱粉。',
    subs=['3-3.1 葉綠體構造與光合色素吸收光譜', '3-3.2 光系統 Ⅱ 與 Ⅰ 的組成與電子傳遞', '3-3.3 水裂解、化學滲透與光合磷酸化（ATP與NADPH生成）', '3-3.4 卡爾文循環的三階段（固碳、還原、RuBP再生）', '3-3.5 影響光合作用速率的環境因子（光照、CO₂、溫度）'],
    tags=['光系統Ⅱ與Ⅰ', '水裂解產氧', '電子傳遞鏈', '化學滲透磷酸化', '卡爾文循環', 'RuBisCO固碳']),
   dict(code='3-4', title='植物體內有機養分的運輸', web='有機養分運輸探索站', slug='ch3-4', vid='1a89RSmmqGO4Azfc6BbRcWu17XUWJDe4l', pages='P.89–91',
    fig='s3-4', cap='圖 3－14　韌皮部有機養分運輸機制的示意圖（壓力流假說）',
    intro='光合作用合成的醣類主要轉變成蔗糖，由韌皮部的篩管雙向運輸。蒙區提出「壓力流假說」解釋運輸機制：成熟葉等生產或釋放養分的部位稱為「供應中心（源）」，根、幼葉、果實等消耗或儲存養分的部位稱為「需求中心（庫）」。在源處，蔗糖被主動裝載進入篩管，造成水勢下降、鄰近木質部水分滲透進入使水壓升高；在庫處，蔗糖被主動卸載，水分滲出使水壓下降，兩端的膨壓梯度推動韌皮部汁液由源流向庫。',
    subs=['3-4.1 韌皮部篩管與伴細胞的構造特徵', '3-4.2 壓力流假說（Pressure-Flow Hypothesis）的原理', '3-4.3 供應中心（源）與需求中心（庫）的動態轉換', '3-4.4 蚜蟲吻針法在分析韌皮部汁液成分的應用'],
    tags=['韌皮部運輸', '壓力流假說', '源與庫', '蔗糖裝載與卸載', '膨壓梯度', '蚜蟲吻針實驗']),
  ],
  labs=[
   dict(code='活動 3-1', title='光合色素之層析分離', web='光合色素探索站', slug='lab3-1', vid='1few0bCQAFhgYs8aql5Jm2iuWMw-Wgtnj', pages='P.92–95',
    fig='a3-1', cap='濾紙層析分離菠菜葉綠體光合色素並計算各色素之 Rf 值',
    intro='利用菠菜葉研磨萃取光合色素，以展開液（石油醚：丙酮 = 9：1）進行濾紙層析。由於各色素對濾紙纖維素的吸附力與在展開液中的溶解度不同，由下而上依序分離出：葉綠素 b（黃綠色）、葉綠素 a（藍綠色）、葉黃素（黃色）與最前緣的胡蘿蔔素（橘黃色），藉量測移動距離計算移動比值（Rf 值）並探討其吸收光譜特徵。'),
   dict(code='活動 3-2', title='光反應的還原作用', web='光反應探索站', slug='lab3-2', vid='1o4FqsI5q-QbuHMXm-ehSo6qggODb0Iiu', pages='P.96–101',
    fig='a3-2', cap='希爾反應：分離葉綠體懸浮液並以 DCPIP 染劑褪色測定光反應還原速率',
    intro='分離菠菜新鮮葉綠體懸浮液，加入藍色人工電子接受者 DCPIP 染劑。在適當光照下，葉綠體光系統 Ⅱ 裂解水產生的電子經傳遞將藍色 DCPIP 還原為無色的 DCPIPH₂；藉由比色法觀察黑暗對照組、遮光組與隔熱水槽組的褪色速率，驗證光反應必須依賴光照激發電子傳遞。'),
  ]),
 dict(n=4, title='植物的生殖', en='Plant Reproduction', a='#e11d48', a2='#fb7185', t='#fff1f2',
  lead='開花植物繁衍後代的精密機制展現了演化的極致。本章從營養器官繁殖與組織培養的細胞全潛能性談起，認識被子植物的花朵構造、世代交替、花粉管萌發與特有的「雙重受精」歷程；再追蹤子房發育為果實、胚珠發育為種子的過程，並探討種子休眠打破與萌發機制。',
  units=[
   dict(code='4-1', title='被子植物的無性生殖', web='無性生殖探索站', slug='ch4-1', vid='1Fp5OOtb6TaTZjT0mOqb2m6ZqBIio0cGo', pages='P.108–110',
    fig='s4-1', cap='圖 4－3　蘭花植物組織培養過程與癒傷組織誘導分化',
    intro='被子植物可利用營養器官進行無性生殖，子代基因與親代完全相同，有利於保留優良農藝性狀。自然界常見落地生根的葉緣不定芽、草莓的匍匐莖、竹子地下莖等；農業上則廣泛應用扦插、稼接、壓條與分株技術。植物細胞具「全潛能性」，在無菌條件下取一小塊外植體置於含特定生長素與細胞分裂素比例的培養基中，可誘導形成未分化的「癒傷組織」，進一步誘導長出根與芽，實現大量無病毒健康種苗的快速繁殖。',
    subs=['4-1.1 自然界的營養繁殖方式（不定根、不定芽與特化莖）', '4-1.2 人工無性繁殖技術（扦插、稼接、壓條）', '4-1.3 植物細胞全潛能性（Totipotency）的發現', '4-1.4 組織培養技術、癒傷組織與種苗量產應用'],
    tags=['營養繁殖', '不定根與不定芽', '細胞全潛能性', '植物組織培養', '癒傷組織', '無病毒種苗']),
   dict(code='4-2', title='被子植物的有性生殖', web='有性生殖探索站', slug='ch4-2', vid='1d1UfsuVs1yvVY3ksKiCraev6e5xTY1K9', pages='P.111–121',
    fig='s4-2', cap='圖 4－7 &amp; 4－8　被子植物世代交替生活史與花粉管萌發雙重受精示意圖',
    intro='花是被子植物的有性生殖器官，典型完全花包含花萼、花瓣、雄蕊與雌蕊。雄蕊花藥內的小孢子母細胞經減數分裂與有絲分裂發育為含管核與生殖細胞的花粉粒；雌蕊子房胚珠內的大孢子母細胞經減數分裂與有絲分裂發育為具 7 個細胞、8 個細胞核的成熟胚囊（含 1 卵細胞、2 助細胞、3 反足細胞與 1 個含 2 極核的中央細胞）。傳粉後花粉萌發花粉管穿過花柱，生殖細胞分裂為 2 個精細胞，執行被子植物特有的「雙重受精」：一個精細胞與卵結合為合子（2n），另一個精細胞與 2 個極核結合成胚乳原核（3n）。',
    subs=['4-2.1 花的構造與類型（完全花、不完全花、單性花）', '4-2.2 雄配子體（花粉粒）與雌配子體（胚囊）的發育歷程', '4-2.3 傳粉媒介（風媒、蟲媒）與花部特徵之協同演化', '4-2.4 雙重受精（Double Fertilization）的歷程與演化優勢', '4-2.5 受精後花部構造之發育命運（胚、胚乳、種皮、果實）'],
    tags=['完全花與胚珠', '花粉發育', '胚囊（7細胞8核）', '雙重受精', '胚（2n）與胚乳（3n）', '世代交替']),
   dict(code='4-3', title='種子的構造與萌發', web='種子萌發探索站', slug='ch4-3', vid='1qxiBYgFXm_ytzPCJDHR7vWCfe5JV3Bpa', pages='P.122–125',
    fig='s4-3', cap='圖 4－12 &amp; 4－14　單子葉與雙子葉種子解剖及子葉出土與不出土萌發型態',
    intro='受精後胚珠發育為種子，珠被發育為堅韌的種皮，合子發育為胚（含胚芽、胚軸、胚根與子葉）。雙子葉無胚乳種子（如大豆、花生）的養分儲存於肥厚子葉中；單子葉種子（如玉米、水稻）具豐富胚乳，子葉特化為盾片傳遞養分，並具胚芽鞘與胚根鞘保護。種子成熟後脫水進入休眠期；當獲得充足水分、氧氣與適宜溫度後打破休眠，吸水膨脹使種皮破裂，胚根最先突破種皮向下扎根，隨後胚軸伸長帶動胚芽出土，展葉進行光合作用。',
    subs=['4-3.1 種子的構造（種皮、胚、胚乳）與雙子葉／單子葉比較', '4-3.2 有胚乳種子與無胚乳種子的養分儲藏部位', '4-3.3 種子休眠的生理意義與打破休眠條件', '4-3.4 種子萌發歷程（子葉出土型與子葉不出土型比較）'],
    tags=['種皮與胚', '有胚乳與無胚乳', '盾片與胚芽鞘', '休眠打破', '子葉出土', '子葉不出土']),
  ],
  labs=[
   dict(code='活動 4-1', title='花與果實的形態與構造', web='花果構造探索站', slug='lab4-1', vid='1f8TZ-5htN3YX00ZNBtJHtQeduo6KNt36', pages='P.126–131',
    fig='a4-1', cap='解剖觀察百合花或朱槿花各部構造，並比較單生果、聚合果與多花果',
    intro='以解剖針與刀片解剖百合花或朱槿花，辨認花萼、花瓣、雄蕊花藥與花絲、雌蕊柱頭、花柱與子房，切開子房以解剖顯微鏡觀察胚珠著生；採集花粉粒以複式顯微鏡觀察萌發孔與花粉壁紋飾。進一步觀察番茄、豌豆、草莓（聚合果）、鳳梨（多花果）等實物，對照果皮各層（外果皮、中果皮、內果皮）與真果、假果的發育來源。'),
  ]),
 dict(n=5, title='植物體的生長發育', en='Plant Growth &amp; Development', a='#d97706', a2='#fbbf24', t='#fffbeb',
  lead='植物無法移動，卻能以極其敏銳的方式感知四季更迭與環境刺激。本章介紹調節植物生長發育的五大經典植物激素（生長素、吉貝素、細胞分裂素、離層酸、乙烯）之生成、運輸與協同拮抗作用；進而探討植物的向性與傾性運動、光敏素對日照長度的感應與開花調控，以及面對逆境時的生理防禦策略。',
  units=[
   dict(code='5-1', title='植物體的生長發育受激素調節', web='植物激素探索站', slug='ch5-1', vid='1mnZ8IcXxYAhkFV476A4kIyLLxOX1mu3Y', pages='P.138–147',
    fig='s5-1', cap='圖 5－1 &amp; 5－6　生長素濃度生長反應曲線與吉貝素誘導大麥種子糊粉層合成澱粉酶',
    intro='植物體內的生長發育受微量植物激素協同調控。經典五大激素包括：生長素（IAA，促進細胞伸長、頂芽優勢、向光性，但高濃度抑制根生長）；吉貝素（GA，促進莖節伸長、打破種子休眠、誘導大麥糊粉層合成 α-澱粉酶）；細胞分裂素（CK，促進細胞分裂、延緩葉片老化、促進側芽萌發並與生長素拮抗）；離層酸（ABA，促進氣孔關閉以抗旱、維持種子休眠、促進葉片衰老）；乙烯（氣體激素，促進果實成熟、促進落葉離層形成、引發三重反應）。各激素間藉精密的濃度比率共同調控發育進程。',
    subs=['5-1.1 生長素（IAA）的生理功能（細胞伸長、頂芽優勢、不定根誘導）', '5-1.2 吉貝素（GA）與大麥糊粉層種子萌發機制', '5-1.3 細胞分裂素（CK）與頂芽優勢拮抗、組織培養根芽分化比例', '5-1.4 離層酸（ABA）的逆境防禦（抗旱保水與種子休眠）', '5-1.5 乙烯的氣體催熟效應、落葉離層形成與三聯反應'],
    tags=['五大植物激素', '生長素（IAA）', '吉貝素（GA）', '細胞分裂素（CK）', '離層酸（ABA）', '乙烯催熟']),
   dict(code='5-2', title='植物體對環境刺激的反應', web='植物感應探索站', slug='ch5-2', vid='1Rc0myKjmdddZKaYq-SR2s-e58IcEnBiu', pages='P.148–157',
    fig='s5-2', cap='圖 5－18　光敏素 Pr 與 Pfr 構形轉換及光週期調控長日照／短日照植物開花',
    intro='植物對環境刺激的反應分為生長運動與膨壓運動。受單向刺激引發具方向性生長者為「向性」（如莖向光性背重力性、根正向重力性，由澱粉體沉降與生長素橫向不均勻分布所驅動）；無生長方向性者為「傾性」（如含羞草葉枕細胞 K⁺ 流失引發觸發運動、氣孔開閉）。植物藉光敏素（Pr 吸收紅光轉為活化態 Pfr，Pfr 吸收遠紅光轉為 Pr）感應夜長（暗期長度），區分臨界夜長而調控長日照植物與短日照植物開花；葉片感受光週期後合成「開花素」（FT 蛋白）運送至莖頂誘導開花，部分植物亦需經低溫刺激之「春化作用」始能花芽分化。',
    subs=['5-2.1 向性運動（向光性、向重力性與澱粉體平衡石假說）', '5-2.2 傾性運動（含羞草觸發運動與葉枕膨壓變化）', '5-2.3 光週期現象與臨界夜長（長日照、短日照、中性日照植物）', '5-2.4 光敏素（Pr / Pfr）的轉換光譜與開花調控', '5-2.5 開花素（FT 蛋白）與春化作用（低溫誘導）'],
    tags=['向光性與向重力性', '平衡石假說', '葉枕與膨壓運動', '光週期與臨界夜長', '光敏素轉換', '開花素與春化']),
  ],
  labs=[
   dict(code='活動 5-1', title='發現植物的生長素', web='生長素實驗探索站', slug='lab5-1', vid='1GF6UyPZOas6q_cKMW9cRh053G_Y9tPZQ', pages='P.158–163',
    fig='a5-1', cap='達爾文、波森-詹森、佩爾至溫特探討燕麥胚芽鞘向光性實驗設計歷程',
    intro='追蹤科學史上發現植物生長素的嚴謹歷程：達爾文父子（1880）以不透光錫箔遮蓋燕麥胚芽鞘尖端與基部，推論尖端感光並產生訊號向下傳遞；波森-詹森（1913）插入明膠薄片與雲母片，證實傳遞訊號為水溶性化學物質；佩爾（1919）將切下的尖端偏置於一側，促成黑暗中彎曲生長；溫特（1928）將尖端置於瓊脂塊吸收化學物質，再將瓊脂塊偏放於去尖胚芽鞘，依彎曲角度量化物質濃度，成功命名並分離出「生長素」（Auxin）。'),
  ]),
]

TOTAL_UNITS = sum(len(c['units']) for c in CHAPTERS)
TOTAL_LABS = sum(len(c['labs']) for c in CHAPTERS)

def url(u): return u['slug'] + '/'
def vurl(u): return DRIVE.format(u['vid'])

HEAD = '''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{theme}">
<link rel="icon" href="img/hanlin-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script>document.documentElement.classList.add('js')</script>
</head>
'''

FOOT = '''<footer class="foot">
  <div class="foot-in">
    <img src="img/hanlin-logo.png" alt="" width="34" height="34">
    <p>內容整理自翰林版高中《選修生物Ⅱ（全）》課本，簡介依課文重點改寫，圖片取自課本，僅供課堂教學使用。<br>各節互動教學網頁由臺北市立麗山高中生物科自編製作，發布於 GitHub Pages；教學影片存放於 Google 雲端硬碟。</p>
  </div>
</footer>
<div class="lightbox" id="lightbox" hidden>
  <button class="lb-close" aria-label="關閉">×</button>
  <figure><img alt=""><figcaption></figcaption></figure>
</div>
<script src="app.js"></script>
</body>
</html>
'''

def nav(current_n=None):
    items = ['<a href="index.html"' + (' class="cur"' if current_n is None else '') + '>全冊總覽</a>']
    for c in CHAPTERS:
        cls = ' class="cur"' if current_n == c['n'] else ''
        items.append(f'<a href="chapter{c["n"]}.html"{cls}>第 {c["n"]} 章</a>')
    items.append('<a href="../選生二網頁＿new/index.html" class="version-switch" title="切換至第二版優化版" style="margin-left:auto;color:#059669;font-weight:700;text-decoration:none;">✨ 第二版優化版 →</a>')
    return ''.join(items)

def chstyle(c):
    return f"--a:{c['a']};--a2:{c['a2']};--t:{c['t']};"

def figure(name, cap, extra_class=''):
    cls = (' ' + extra_class) if extra_class else ''
    full = f"img/{name}.jpg"
    return (
        f'<button class="fig-btn{cls}" type="button" data-full="{full}" data-cap="{E(cap)}" aria-label="點擊放大圖解：{E(cap)}">'
        f'<img src="{full}" alt="{E(cap)}" loading="lazy">'
        f'<span class="fig-zoom">{ICON_ZOOM} 點擊放大圖解</span>'
        f'</button>'
    )

def build_index():
    o = [HEAD.format(title='翰林版 選修生物（Ⅱ）｜互動教學網站',
        desc=f'翰林版高中選修生物Ⅱ（全）五章 {TOTAL_UNITS} 節與 {TOTAL_LABS} 個探討活動的互動教學網頁與教學影片入口', theme='#059669')]
    o.append('''<body class="home">
<header class="hero">
  <!-- Botanical chloroplast & foliage geometric motif -->
  <svg class="globe" viewBox="0 0 600 600" aria-hidden="true">
    <g fill="none" stroke="currentColor" stroke-width="1.3">
      <circle cx="300" cy="300" r="280" stroke-dasharray="12 8" opacity=".4"/>
      <path d="M300 40 C140 160 140 440 300 560 C460 440 460 160 300 40 Z" opacity=".7"/>
      <path d="M40 300 C160 140 440 140 560 300 C440 460 160 460 40 300 Z" opacity=".5"/>
      <path d="M300 70 L300 530" stroke-dasharray="6 6" opacity=".6"/>
      <path d="M70 300 L530 300" stroke-dasharray="6 6" opacity=".6"/>
      <circle cx="300" cy="300" r="160" opacity=".35"/>
      <circle cx="300" cy="300" r="70" opacity=".4"/>
    </g>
  </svg>
  <div class="hero-in">
    <div style="display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;margin-bottom:8px;">
      <span style="display:inline-flex;align-items:center;gap:6px;background:#e2e8f0;color:#334155;padding:5px 14px;border-radius:999px;font-size:13px;font-weight:700;">第一版・原始版</span>
      <a href="../選生二網頁＿new/index.html" style="display:inline-flex;align-items:center;gap:6px;background:#ecfdf5;color:#065f46;border:1.5px solid #34d399;border-radius:999px;padding:5px 16px;font-size:13px;font-weight:700;text-decoration:none;box-shadow:0 2px 6px rgba(5,150,105,0.15);">✨ 前往第二版（質感優化版：288dpi 超清圖＋貼標籤練習＋原題詳解） →</a>
    </div>
    <img class="hero-logo" src="img/hanlin-logo-wide.png" alt="翰林出版 HAN LIN PUBLISHING" width="1240" height="324">
    <div class="hero-rule"><span></span><em>自然科學領域　加深加廣選修</em><span></span></div>
    <h1>選修生物（Ⅱ）<span>互動教學網站</span></h1>
    <p class="hero-sub">翰林版《選修生物Ⅱ（全）》· 生命的起源與演化歷程、植物組織器官與水鹽光合運輸、被子植物繁衍與生長激素調節，每一節皆配備專屬互動教學網頁與雲端影片</p>
    <ul class="stats">
''' + f'''      <li><b>5</b><span>大章節</span></li><li><b>{TOTAL_UNITS}</b><span>節正課</span></li><li><b>{TOTAL_LABS}</b><span>個探討活動</span></li><li><b>{TOTAL_UNITS+TOTAL_LABS}</b><span>個互動網頁</span></li>
    </ul>
  </div>
</header>
<main>
  <section class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">CHAPTERS</span><h2>選擇章節，探索生命與植物之美</h2><p>點選章節封面進入章節，瀏覽每一節的課本概念圖解、重點引導、互動教學網頁與教學影片。</p></div>
    <div class="ch-grid">
''')
    for c in CHAPTERS:
        lis = ''.join(f"<li><span>{u['code']}</span>{E(u['title'])}</li>" for u in c['units'])
        meta = f"<span>{len(c['units'])} 節正課</span>" + (f"<span>{len(c['labs'])} 個探討活動</span>" if c['labs'] else '')
        o.append(f'''      <a class="ch-card reveal" href="chapter{c['n']}.html" style="{chstyle(c)}">
        <div class="ch-cover"><img src="img/cover{c['n']}.jpg" alt="第{c['n']}章 {c['title']} 章節封面" loading="lazy" width="900" height="1020"></div>
        <div class="ch-body">
          <div class="ch-kicker">CHAPTER 0{c['n']} · {c['en']}</div>
          <h2>第 {c['n']} 章　{c['title']}</h2>
          <ul class="ch-list">{lis}</ul>
          <div class="ch-meta">{meta}</div>
          <span class="ch-go">進入本章 {ICON_GO}</span>
        </div>
      </a>
''')
    o.append('''    </div>
  </section>
  <section class="wrap labs-home">
    <div class="sec-head reveal"><span class="eyebrow">INQUIRY ACTIVITIES</span><h2>全冊探討活動專區</h2><p>從徒手切片、色素層析、希爾反應到生長素發現史，以實驗數據與科學證據深化探究與實作素養。</p></div>
    <div class="lab-grid">
''')
    for c in CHAPTERS:
        for l in c['labs']:
            o.append(f'''      <article class="lab reveal" style="{chstyle(c)}">
        {figure(l['fig'], l['cap'], 'lab-fig fig-btn')}
        <div class="lab-body">
          <div class="unit-top"><span class="code sm">{l['code']}</span><span class="web-pill">{E(l['web'])}</span><span class="pg-pill">{ICON_BOOK}課本 {l['pages']}</span></div>
          <h3>{E(l['title'])}</h3>
          <a class="intro" href="{url(l)}" target="_blank" rel="noopener"><p>{E(l['intro'])}</p><span class="intro-hint">開啟教學網頁 {ICON_OUT}</span></a>
          <div class="btn-row">
            <a class="btn" href="{url(l)}" target="_blank" rel="noopener">進入「{E(l['web'])}」{ICON_OUT}</a>
            <a class="btn ghost vid" href="{vurl(l)}" target="_blank" rel="noopener">{ICON_PLAY}教學影片</a>
          </div>
        </div>
      </article>
''')
    o.append('''    </div>
  </section>
</main>
''' + FOOT)
    return ''.join(o)

def build_chapter(c):
    n = c['n']
    o = [HEAD.format(title=f"第 {n} 章 {c['title']}｜翰林版 選修生物（Ⅱ）", desc=E(c['lead']), theme=c['a'])]
    jumps = ''.join(f'<a href="#u{u["code"]}"><b>{u["code"]}</b>{E(u["title"])}</a>' for u in c['units'])
    if c['labs']: jumps += f'<a href="#labs" class="j-lab"><b>探討</b>活動 × {len(c["labs"])}</a>'
    o.append(f'''<body class="chapter" style="{chstyle(c)}">
<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="index.html" aria-label="回到首頁">
      <img src="img/hanlin-logo.png" alt="翰林出版" width="40" height="40">
      <span class="brand-t"><small>翰林版</small>選修生物（Ⅱ）</span>
    </a>
    <nav class="nav">{nav(n)}</nav>
  </div>
</header>
<header class="ch-hero">
  <div class="ch-hero-in">
    <div class="ch-hero-text">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
        <span style="display:inline-flex;align-items:center;gap:6px;background:#e2e8f0;color:#334155;padding:5px 12px;border-radius:999px;font-size:13px;font-weight:700;">第一版第 {n} 章</span>
        <a href="../選生二網頁＿new/chapter{n}.html" style="display:inline-flex;align-items:center;gap:6px;background:#ecfdf5;color:#065f46;border:1.5px solid #34d399;border-radius:999px;padding:5px 14px;font-size:13px;font-weight:700;text-decoration:none;">✨ 切換至第二版第 {n} 章優化版 →</a>
      </div>
      <div class="ch-kicker">CHAPTER 0{n} · {c['en']}</div>
      <h1><span class="big">{n}</span><span class="t">第 {n} 章<br><strong>{c['title']}</strong></span></h1>
      <p class="lead">{E(c['lead'])}</p>
      <div class="jump">{jumps}</div>
    </div>
    <div class="ch-hero-cover"><img src="img/cover{n}.jpg" alt="第 {n} 章 章節封面" width="900" height="1020"></div>
  </div>
</header>
<main class="wrap units">
''')
    for i, u in enumerate(c['units']):
        subs = ''.join(f'<li>{E(s)}</li>' for s in u['subs'])
        tags = ''.join(f'<span>{E(t)}</span>' for t in u['tags'])
        o.append(f'''    <article class="unit reveal{' flip' if i % 2 else ''}" id="u{u['code']}">
      <figure class="fig">
        {figure(u['fig'], u['cap'])}
        <figcaption>{E(u['cap'])}</figcaption>
      </figure>
      <div class="unit-body">
        <div class="unit-top"><span class="code">{u['code']}</span><span class="web-pill">互動網頁｜{E(u['web'])}</span><span class="pg-pill">{ICON_BOOK}課本 {u['pages']}</span></div>
        <h2>{E(u['title'])}</h2>
        <a class="intro" href="{url(u)}" target="_blank" rel="noopener" title="開啟「{E(u['web'])}」教學網頁">
          <p>{E(u['intro'])}</p>
          <span class="intro-hint">點選文字即可開啟教學網頁 {ICON_OUT}</span>
        </a>
        <div class="subs"><h3>本節重點</h3><ol>{subs}</ol></div>
        <div class="tags">{tags}</div>
        <div class="btn-row">
          <a class="btn" href="{url(u)}" target="_blank" rel="noopener">進入「{E(u['web'])}」{ICON_OUT}</a>
          <a class="btn ghost vid" href="{vurl(u)}" target="_blank" rel="noopener">{ICON_PLAY}教學影片</a>
        </div>
      </div>
    </article>
''')
    if c['labs']:
        one = ' one' if len(c['labs']) == 1 else ''
        o.append(f'''  <section class="labs" id="labs">
    <div class="sec-head reveal"><span class="eyebrow">HANDS-ON LAB</span><h2>探討活動</h2><p>動手操作、記錄變因與數據，把課文中的概念轉化為自己的實驗證據。</p></div>
    <div class="lab-grid{one}">
''')
        for l in c['labs']:
            o.append(f'''      <article class="lab reveal" id="{l['slug']}">
        {figure(l['fig'], l['cap'], 'lab-fig fig-btn')}
        <div class="lab-body">
          <div class="unit-top"><span class="code sm">{l['code']}</span><span class="web-pill">{E(l['web'])}</span><span class="pg-pill">{ICON_BOOK}課本 {l['pages']}</span></div>
          <h3>{E(l['title'])}</h3>
          <a class="intro" href="{url(l)}" target="_blank" rel="noopener"><p>{E(l['intro'])}</p><span class="intro-hint">開啟教學網頁 {ICON_OUT}</span></a>
          <div class="btn-row">
            <a class="btn ghost" href="{url(l)}" target="_blank" rel="noopener">進入「{E(l['web'])}」{ICON_OUT}</a>
            <a class="btn ghost vid" href="{vurl(l)}" target="_blank" rel="noopener">{ICON_PLAY}教學影片</a>
          </div>
        </div>
      </article>
''')
        o.append('    </div>\n  </section>\n')
    prev = f'<a class="pg" href="chapter{n-1}.html"><small>PREVIOUS</small>← 第 {n-1} 章　{CHAPTERS[n-2]["title"]}</a>' if n > 1 else '<a class="pg" href="index.html"><small>HOME</small>← 回首頁總覽</a>'
    nxt = f'<a class="pg next" href="chapter{n+1}.html"><small>NEXT CHAPTER</small>第 {n+1} 章　{CHAPTERS[n]["title"]} →</a>' if n < len(CHAPTERS) else '<a class="pg next" href="index.html"><small>HOME</small>回首頁總覽 →</a>'
    o.append(f'  <nav class="pager">\n    {prev}\n    {nxt}\n  </nav>\n</main>\n' + FOOT)
    return ''.join(o)

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(build_index())
for c in CHAPTERS:
    open(os.path.join(OUT, f'chapter{c["n"]}.html'), 'w', encoding='utf-8').write(build_chapter(c))
print(f'Build finished: {TOTAL_UNITS} units, {TOTAL_LABS} labs across 5 chapters.')
