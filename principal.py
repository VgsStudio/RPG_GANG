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


@client.command()
async def criar(ctx,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9):
    try:
        arg2 = int(arg2)
        arg3 = int(arg3)
        arg4 = int(arg4)
        arg5 = int(arg5)
        arg6 = int(arg6)
        arg7 = int(arg7)
        arg8 = int(arg8)
        arg9 = int(arg9)
        
        criar_personagem(arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9)
        await ctx.send('''Nome = %s
Vitalidade = %i
Força = %i
Observação = %i
Destreza = %i
Inteligência = %i
Carisma = %i 
Sorte = %i
Poder = %i''' % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9))
    except:
        await ctx.send('Você esqueceu algum par')
    pass

@client.command()
async def deletar(ctx,arg1):
    try:
        deletar_personagem(arg1)
        await ctx.send('%s será deletado para sempre...' % arg1)
    except:
        await ctx.send('Esse personagem não existe!')
    pass


@client.command()
async def d20(ctx,arg1,arg2):
    Resp = dado20(imprimir_personagem(arg1,arg2))
    await ctx.send('%s tirou %i em %s' % (arg1, Resp, arg2))
    pass

@client.command()
async def d10(ctx,arg1):
    Resp = dado10()
    await ctx.send('%s tirou %i' % (arg1 ,Resp))
    pass


@client.command()
async def d8(ctx,arg1):
    Resp = dado8()
    await ctx.send('%s tirou %i' % (arg1 ,Resp))
    pass


@client.command()
async def d6(ctx,arg1):
    Resp = dado6()
    await ctx.send('%s tirou %i' % (arg1 ,Resp))
    pass


@client.command()
async def d4(ctx,arg1):
    Resp = dado4()
    await ctx.send('%s tirou %i' % (arg1 ,Resp))
    pass




client.run(TOKEN)

