import hanlp

# 加载中文句子切分模型
split_sent = hanlp.load(hanlp.pretrained.eos.UD_CTB_EOS_MUL)

# 中文测试文本
text = """月光轻轻洒落，林中传来阵阵狼嚎，夜色悄然笼罩一切。
树叶在微风中沙沙作响，影子在地面上摇曳不定。
一只猫头鹰静静地眨了眨眼，从枝头注视着四周……
远处的小溪哗啦啦地流淌，仿佛在向石头倾诉着什么！
“咔嚓”一声，某处的树枝突然断裂，然后恢复了寂静。
空气中弥漫着松树与湿土的气息，令人心安。
一只狐狸悄然出现，又迅速消失在灌木丛中。
天上的星星闪烁着，仿佛在诉说古老的故事。
时间仿佛停滞了……
万物静候，聆听着夜的呼吸！"""

# 分句
sentences = split_sent(text)

results = []
start = 0
for sentence in sentences:
    start = text.find(sentence, start)
    end = start + len(sentence)
    results.append({
        'sentence': sentence + '\n',  
        'start': start,
        'end': end
    })
    start = end

# 打印结果
from pprint import pprint
pprint(results, width=120)
