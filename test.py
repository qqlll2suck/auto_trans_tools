from googletrans import Translator
import asyncio


text = 'Some Android Auto navigation apps are not designed for commercial vehicles and may not be used for navigation.'

async def translate_text():
    #  async with Translator() as translator:
    async with Translator() as translator:

        result = await translator.translate(text=text, src='en', dest='tr')
        # * 原文
        # print(result.origin)
        # * 翻译后的文本
        print(result.text)

asyncio.run(translate_text())