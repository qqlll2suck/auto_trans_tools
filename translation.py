import asyncio
from googletrans import Translator


# * 自定义服务url
# translator = Translator(service_urls=[
#       'translate.google.com',
#     ])

translator = Translator(service_urls=[
      'translate.googleapis.com'
    ])


# * 基本用法
# * 如果没有给出源语言，谷歌翻译会尝试检测源语言。
async def translate_text():
    #  async with Translator() as translator:
    async with translator:
        result = await translator.translate('안녕하세요.')
        print(result)  # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>

        result = await translator.translate('안녕하세요.', dest='ja')
        print(result)  # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>

        result = await translator.translate('안녕하세요', src='ko', dest='zh-cn')
        # * 原文
        print(result.origin)
        # * 翻译后的文本
        print(result.text)

asyncio.run(translate_text())

# * 高级用法（批量）
# * 数组可用于在单个方法调用和单个 HTTP 会话中批量转换字符串。上述方法同样适用于数组。

async def translate_bulk():
    async with Translator() as translator:
        translations = await translator.translate(
            ['The quick brown fox', 'jumps over', 'the lazy dog'], dest='zh-cn'
        )
        # 返回翻译对象列表
        return [(t.origin, t.text) for t in translations]

# 获取返回值
result = asyncio.run(translate_bulk())
print(result)


'''
语言检测
检测方法，顾名思义，就是识别给定句子中使用的语言。
'''
async def detect_languages():
    async with Translator() as translator:
        result = await translator.detect('이 문장은 한글로 쓰여졌습니다.')
        print(result)  # <Detected lang=ko confidence=0.27041003>

        result = await translator.detect('この文章は日本語で書かれました。')
        print(result)  # <Detected lang=ja confidence=0.64889508>

        result = await translator.detect('This sentence is written in English.')
        print(result)  # <Detected lang=en confidence=0.22348526>

        result = await translator.detect('Tiu frazo estas skribita en Esperanto.')
        print(result)  # <Detected lang=eo confidence=0.10538048>
asyncio.run(detect_languages())