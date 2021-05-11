import discord, os
from discord.ext import commands
from dotenv import load_dotenv
from funcs.create_cha import *
from dados.dados import *


client = commands.Bot(command_prefix = '$')


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


@client.event
async def on_ready():
    print("Pai ta on! 😎")
    await client.change_presence(activity=discord.Game(name="$help"))
    pass

listas_personagens = []
lista_criador = []
@client.command()
async def criar(ctx,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9):
    try:
        arg1 = arg1.lower()
        ARGUMENTOS = [arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9]
        atributos = ["Vitalidade", "Força", "Observaçao", "Destreza", "Inteligencia", 'Carisma', "Sorte", "Poder"]
        

        bloco=discord.Embed(color=0xff6600)
                
        for x,y in zip(ARGUMENTOS, atributos): #Cria o bloco
            x = int(x)
            bloco.add_field(name=y, value=x, inline=False)

        ARGUMENTOS.insert(0, arg1)

        ARGUMENTOS = [arg1, arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9]

        criar_personagem(*ARGUMENTOS)
        
        listas_personagens.append(arg1)
        
       

        criador = ctx.author.name
        lista_criador.append(criador)
        
        await ctx.send(embed=bloco)
    except:
        await ctx.send('**Você esqueceu algum atributo!**')
    pass

@client.command()
async def deletar(ctx,arg1):
    try:
        antigo_arg1 = arg1
        arg1 = arg1.lower()
        deletar_personagem(arg1)
        lista_criador.pop(listas_personagens.index(arg1))
        listas_personagens.remove(arg1)

        await ctx.send('**%s será deletado para sempre...**' % antigo_arg1)
    except:
        await ctx.send('**Esse personagem não existe!**')
    pass


@client.command()
async def personagens(ctx): 
    bloco=discord.Embed(color=0xff6600)
    for x,y in zip(listas_personagens, lista_criador):
        x = str(x)
        bloco.add_field(name=x.title(), value="Criado por %s " % y, inline=False)
    await ctx.send(embed=bloco)
    pass

@client.command()
async def atributos(ctx, arg1): 
    atributos = ["vitalidade", "força", "observaçao", "destreza", "inteligencia", 'carisma', "sorte", "poder"]
    arg1 = arg1.lower()
    
    bloco=discord.Embed(color=0xff6600)

    for x in atributos:
       atri = int(imprimir_personagem(arg1,x))
       bloco.add_field(name=x.title(), value=atri, inline=False)

    await ctx.send(embed=bloco)   
    pass 


@client.command()
async def pericia(ctx,arg1,arg2,arg3):
    pass


@client.command()
async def d20(ctx,arg1,arg2, arg3 = 0):
    antigo_arg1 = arg1
    arg1 = arg1.lower()
    arg2 = arg2.lower()
    arg3 = int(arg3)
    Resp = dado20(int(imprimir_personagem(arg1,arg2))) + arg3

    embed=discord.Embed(color=0xffffff)
    embed.add_field(name="Resultado: ", value="**%s** tirou %i em %s" % (antigo_arg1, Resp, arg2), inline=False)
    await ctx.reply(embed=embed, mention_author=True)
    pass

@client.command()
async def roll(ctx,arg0, arg3: int = 0, *,arg1):

    antigo_arg1 = arg1
    arg1 = arg1.lower()
    Resp = dados_generico(arg0) + arg3
    arg3 = int(arg3)

    embed=discord.Embed(color=0xffffff)
    embed.add_field(name="Resultado: ", value="**%s** tirou %i" % (antigo_arg1, Resp), inline=False)
    await ctx.reply(embed=embed, mention_author=True)
    pass

"""
@client.command()
async def help(ctx):
    await ctx.send('''$criar [nome vitalidade força observaçao destreza inteligencia carisma sorte poder] - Cria o personagem
$deletar [nome] - Deleta um personagem
$atributos [nome] - Mostra os atributos do personagem
$personagens - Mostra todos os personagens criados
$d20 [nome atributo] - Roda um d20 e soma com o atributo
$roll d[n°] - Roda um dado a quantidade n
''')
    
    pass
"""

client.run(TOKEN)

