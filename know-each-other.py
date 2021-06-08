from functools import reduce
from random import shuffle

QUESTIONS_COUNT = 2

family_names = ["趙", "錢", "孫", "李", "週", "吳", "鄭", "王", "馮", "陳", "褚", "衛", "蔣", "沈", "韓", "楊", "朱", "秦", "尤",
                "許", "何", "呂", "施", "張", "孔", "曹", "嚴", "華", "金", "魏", "陶", "姜", "戚", "謝", "鄒", "喻", "柏", "水",
                "竇", "章", "雲", "蘇", "潘", "葛", "奚", "範", "彭", "郎", "魯", "韋", "昌", "馬", "苗", "鳳", "花", "方", "俞",
                "任", "袁", "柳", "酆", "鮑", "史", "唐", "費", "廉", "岑", "薛", "雷", "賀", "倪", "湯", "滕", "殷", "羅", "畢",
                "郝", "鄔", "安", "常", "樂", "於", "時", "傅", "皮", "卞", "齊", "康", "伍", "餘", "元", "卜", "顧", "孟", "平",
                "黃", "和", "穆", "蕭", "尹", "姚", "邵", "湛", "汪", "祁", "毛", "禹", "狄", "米", "貝", "明", "臧", "計", "伏",
                "成", "戴", "談", "宋", "茅", "龐", "熊", "紀", "舒", "屈", "項", "祝", "董", "梁", "杜", "阮", "藍", "閔", "席",
                "季", "麻", "強", "賈", "路", "婁", "危", "江", "童", "顏", "郭", "梅", "盛", "林", "刁", "鐘", "徐", "邱", "駱",
                "高", "夏", "蔡", "田", "樊", "胡", "凌", "霍", "虞", "萬", "支", "柯", "昝", "管", "盧", "莫", "經", "房", "裘",
                "繆", "幹", "解", "應", "宗", "丁", "宣", "賁", "鄧", "鬱", "單", "杭", "洪", "包", "諸", "左", "石", "崔", "吉",
                "鈕", "龔", "程", "嵇", "邢", "滑", "裴", "陸", "榮", "翁", "荀", "羊", "於", "惠", "甄", "曲", "家", "封", "芮",
                "羿", "儲", "靳", "汲", "邴", "糜", "松", "井", "段", "富", "巫", "烏", "焦", "巴", "弓", "牧", "隗", "山", "谷",
                "車", "侯", "宓", "蓬", "全", "郗", "班", "仰", "秋", "仲", "伊", "宮", "寧", "仇", "欒", "暴", "甘", "鈄", "厲",
                "戎", "祖", "武", "符", "劉", "景", "詹", "束", "龍", "葉", "幸", "司", "韶", "郜", "黎", "薊", "溥", "印", "宿",
                "白", "懷", "蒲", "邰", "從", "鄂", "索", "咸", "籍", "賴", "卓", "藺", "屠", "蒙", "池", "喬", "陰", "鬱", "胥",
                "能", "蒼", "雙", "聞", "莘", "黨", "翟", "譚", "貢", "勞", "逄", "姬", "申", "扶", "堵", "冉", "宰", "酈", "雍",
                "卻", "璩", "桑", "桂", "濮", "牛", "壽", "通", "邊", "扈", "燕", "冀", "浦", "尚", "農", "溫", "別", "莊", "晏",
                "柴", "瞿", "閻", "充", "慕", "連", "茹", "習", "宦", "艾", "魚", "容", "向", "古", "易", "慎", "戈", "廖", "庾",
                "終", "暨", "居", "衡", "步", "都", "耿", "滿", "弘", "匡", "國", "文", "寇", "廣", "祿", "闕", "東", "歐", "殳",
                "沃", "利", "蔚", "越", "夔", "隆", "師", "鞏", "厙", "聶", "晁", "勾", "敖", "融", "冷", "訾", "辛", "闞", "那",
                "簡", "饒", "空", "曾", "毋", "沙", "乜", "養", "鞠", "須", "豐", "巢", "關", "蒯", "相", "查", "後", "荊", "紅",
                "遊", "郟", "竺", "權", "逯", "蓋", "益", "桓", "公", "仉", "督", "岳", "帥", "緱", "亢", "況", "郈", "有", "琴",
                "歸", "海", "晉", "楚", "閆", "法", "汝", "鄢", "塗", "欽", "商", "牟", "佘", "佴", "伯", "賞", "墨", "哈", "譙",
                "篁", "年", "愛", "陽", "佟", "言", "福", "南", "火", "鐵", "遲", "漆", "官", "冼", "真", "展", "繁", "檀", "祭",
                "密", "敬", "揭", "舜", "樓", "疏", "冒", "渾", "摯", "膠", "隨", "高", "皋", "原", "種", "練", "彌", "倉", "眭",
                "蹇", "覃", "阿", "門", "惲", "來", "綦", "召", "儀", "風", "介", "巨", "木", "京", "狐", "郇", "虎", "枚", "抗",
                "達", "杞", "萇", "折", "麥", "慶", "過", "竹", "端", "鮮", "皇", "亓", "老", "是", "秘", "暢", "鄺", "還", "賓", ]


class Player:
    def __init__(self):
        self.own = {}
        self.other = {}
        self.familiarity = 0


questions = []
player1 = Player()
player2 = Player()
players = [player1, player2]


def percent_formatter(num):
    return f"{round(num * 100, 2)} %"


def reset_game():
    global questions

    questions = []

    for _ in range(QUESTIONS_COUNT):
        shuffle(family_names)
        questions.append(family_names.pop())


def start_game():
    for index, player in enumerate(players):
        nth_round = 0
        print(f'Player {index + 1}')
        print('以第一直覺回答一個人名: ')
        while nth_round < QUESTIONS_COUNT:
            family_name = questions[nth_round]
            player.own[family_name] = input(f'{family_name}: ')
            nth_round += 1

        nth_round = 0
        print('猜對方會回答什麼人名: ')
        while nth_round < QUESTIONS_COUNT:
            family_name = questions[nth_round]
            player.other[family_name] = input(f'{family_name}: ')
            nth_round += 1


def analyze_game():
    total = len(questions)

    similarity_correct = 0
    familiarity_correct1 = 0
    familiarity_correct2 = 0

    for family_name in questions:
        if player1.own[family_name] == player2.own[family_name]:
            similarity_correct += 1
        if player1.other[family_name] == player2.own[family_name]:
            familiarity_correct1 += 1
        if player2.other[family_name] == player1.own[family_name]:
            familiarity_correct2 += 1

    similarity = similarity_correct / total
    player1.familiarity = familiarity_correct1 / total
    player2.familiarity = familiarity_correct2 / total

    print(f"兩位的相似程度: {percent_formatter(similarity)}")
    print(
        f"Player 1 對 Player 2 的熟悉度: {percent_formatter(player1.familiarity)}")
    print(
        f"Player 2 對 Player 1 的熟悉度: {percent_formatter(player2.familiarity)}")


def main():
    reset_game()
    start_game()
    analyze_game()


main()
