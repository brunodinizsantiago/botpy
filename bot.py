import asyncpg
import asyncio

DATABASE_URL = "postgresql://neondb_owner:npg_eox3ak1qSQTN@ep-orange-sound-ac5fc92r-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

async def testar_conexao():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        print("✅ Conexão bem-sucedida!")
        await conn.close()
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")

asyncio.run(testar_conexao())
