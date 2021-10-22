@bot.command()
async def hangman(ctx):
  text=rastgele seçimler dizisi, like ['seçim 1', 'seçim 2', 'vb']
  text=random.seçim(text)
  text=text.lower()
  tries=0
  lettersdone=[]
  sendtext=""
  win="false"
  for i in text:
    if i.isspace():
      sendtext=f'{sendtext} '
    else:
      sendtext=f'{sendtext}🟦'
  messageid=await ctx.send(f"**{ctx.author}**, adam asmaca oyunu başladı! **{len(text)}** harf var: `{sendtext}`")
  while tries<6:
    def check(m):
      return m.channel==ctx.channel
    content=await bot.wait_for('message', check=check)
    content=content.content.lower()
    if len(content)!=1:
      continue
    else:
      if content in text:
        if content in lettersdone:
          sendlettersdone=", ".join(lettersdone).upper()
          await ctx.send(f"Zaten "{sendlettersdone}" tahmin ettiniz ve "{content}" buna dahil!")
        else:
          lettersdone.append(content)
          sendtext=list(sendtext)
          for i in range(len(text)):
            if text[i]==content:
              sendtext[i]=content
          sendtext="".join(sendtext)
          sendlettersdone=", ".join(lettersdone).upper()
          if sendtext.replace(text, " ").isspace():
            await messageid.edit(content=f"**__Kaybettin__**\nFinal Text: `{sendtext}`\nGuessed Letters: `{sendlettersdone}`\nWrong Guess Chances Left: `{6-tries}`")
            win="true"
            break
          else:
            await messageid.edit(content=f"Bu doğruydu, Adam asmaca kutuları güncellendi: `{sendtext}`\nGuessed Harfler: `{sendlettersdone}`\nWrong Yanlış Tahmin Şansı: `{6-tries`")
      else:
        if content in lettersdone:
          sendlettersdone=", ".join(lettersdone).upper()
          await ctx.send(f"Zaten "{sendlettersdone}" tahmin ettiniz ve "{content}" buna dahil!")
        else:
          lettersdone.append(content)
          tries=tries+1
          sendlettersdone=", ".join(lettersdone).upper()
          await messageid.edit(content=f"Bu Yanlıştı `{sendtext}`\nWrong Kalan Şansı Tahmin Et: `{sendlZaten "{sendlettersdone}" tahmin ettiniz ve "{content}" buna dahil!ttersdone}`\nGuesses Left: `{6-tries}`")
  if win=="true":
    await ctx.send(f"Tebrikler, doğru anladınız! Metin **{text}** idi ve **{tries}** yanlış cevap(lar)la başarılı bir şekilde tahmin ettiniz!")
  else:
    await ctx.send(f"Aww öldü, yanlış anladın. Metin **{text}**!")
