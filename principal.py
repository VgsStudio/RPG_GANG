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
    discord.Activity(name="Test", type=5)
    print("Pai ta on! 😎")
    await client.change_presence(activity=discord.Game(name="$help"))
    pass

listas_personagens = []

@client.command()
async def criar(ctx,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9):
    try:
        antigo_arg1 = arg1
        arg1 = arg1.lower()
        arg2 = int(arg2)
        arg3 = int(arg3)
        arg4 = int(arg4)
        arg5 = int(arg5)
        arg6 = int(arg6)
        arg7 = int(arg7)
        arg8 = int(arg8)
        arg9 = int(arg9)
        
        criar_personagem(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9)

        listas_personagens.append(antigo_arg1)
        
        await ctx.send('''_Nome_ = %s
_Vitalidade_ = %i
_Força_ = %i
_Observação_ = %i
_Destreza_ = %i
_Inteligência_ = %i
_Carisma_ = %i 
_Sorte_ = %i
_Poder_ = %i''' % (antigo_arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9))
    except:
        await ctx.send('_Você esqueceu algum atributo!_')
    pass

@client.command()
async def deletar(ctx,arg1):
    try:
        deletar_personagem(arg1)
        listas_personagens.remove(arg1)
        await ctx.send('_%s será deletado para sempre..._' % arg1)
    except:
        await ctx.send('_Esse personagem não existe!_')
    pass


@client.command()
async def personagens(ctx): 
    s = """ 
    """.join(listas_personagens)
    await ctx.send(s)
    pass

@client.command()
async def atributos(ctx, arg1): 
    atributos = ["vitalidade", "força", "observaçao", "destreza", "inteligencia", 'carisma', "sorte", "poder"]
    arg1 = arg1.lower()
    for x in atributos:
       atri = int(imprimir_personagem(arg1,x))
       await ctx.send('_%s_ = %i' % (x, atri))
    pass 


@client.command()
async def d20(ctx,arg1,arg2):
    antigo_arg1 = arg1
    arg1 = arg1.lower()
    arg2 = arg2.lower()
    Resp = dado20(imprimir_personagem(arg1,arg2))
    await ctx.send('_%s_ tirou %i em %s' % (antigo_arg1, Resp, arg2))
    pass

@client.command()
async def roll(ctx,arg0,arg1):
    int(arg0)
    if arg0 >= 2:
        antigo_arg1 = arg1
        arg1 = arg1.lower()
        Resp = dados_generico(arg0)
        await ctx.send('_%s_ tirou %i' % (antigo_arg1 ,Resp))
    elif arg0 < 0:
        await ctx.send('O dado não pode ter lados negativos!')

    else:
        await ctx.send('O dado tem que ter mais de 2 lados!')
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

