# Aelio
AELIO_1 = ("統制型ドールズ討伐戦", (24, 112))
AELIO_2 = ("ネクス・ヴェラ討伐戦", (24, 131))
AELIO_3 = ("資源採掘リグ防衛戦", (67, 203))
AELIO_4 = ("ダークファルス迎撃戦", (56, 195))
AELIO_5 = ("戦変万花のエネミー掃討戦", (0, 0))
AELIO_6 = ("ハルフィリア湖の戦い", (159, 46))
AELIO_6_ALT = ("ハルフィリア湖の戦い", (163, 39))
# AELIO_6 = ("第二次ハルフィリア湖要撃戦", (159, 46))
# AELIO_6_ALT = ("第二次ハルフィリア湖要撃戦", (163, 39))
AELIO_7 = ("ハッピーラッピー大作戦", (35, 169))
AELIO = [AELIO_1, AELIO_2, AELIO_3, AELIO_4, AELIO_5, AELIO_6, AELIO_6_ALT, AELIO_7]

# Retem
RETEM_1 = ("スナイダル・ヴェラ討伐戦", (215, 152))
RETEM_2 = ("レヌス・ヴェラ討伐戦", (208, 169))
RETEM_3 = ("資源採掘リグ防衛戦", (179, 202))
RETEM_4 = ("ホーンテッドドメイン", (196, 186))
RETEM_5 = ("星滅の予兆", (189, 193))
RETEM = [RETEM_1, RETEM_2, RETEM_3, RETEM_4, RETEM_5]

# Kvaris
KVARIS_1 = ("クロコダラス・ヴェラ討伐戦", (98, 31))
KVARIS_2 = ("アムス・ヴェラ討伐戦", (71, 42))
KVARIS_3 = ("資源採掘リグ防衛戦", (63, 51))
KVARIS_4 = ("野望の残滓", (53, 61))
KVARIS = [KVARIS_1, KVARIS_2, KVARIS_3, KVARIS_4]

# Stia
STIA_1 = ("ドルドリス・ヴェラ討伐戦", (190, 54))
STIA_2 = ("ニルス・ヴェラ討伐戦", (181, 49))
STIA = [STIA_1, STIA_2]

# Halpha
HALPHA = [AELIO, RETEM, KVARIS, STIA]

# Others
FAILED = "データ取得失敗"
NODATA = "データ無し"

def is_incomplete(determined: list) -> bool:
    return ((FAILED in determined) or (NODATA in determined))

def is_all_nodata(determined: list) -> bool:
    return all(quest_name == NODATA for quest_name in determined)
