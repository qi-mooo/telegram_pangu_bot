from pyrogram import Client, filters
import pangu
import os

# 获取环境变量中的API_ID和API_HASH
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

# 创建一个客户端
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# 添加一个消息过滤器，当收到消息时，判断是否为机器人发出的消息，如果是，则不处理
@app.on_message(filters.me & filters.text & ~filters.command([]) & ~filters.bot)
def format_pangu(client, message):
    # 获取原始文本
    original_text = message.text
    # 使用pangu模块对文本进行格式化
    formatted_text = pangu.spacing_text(original_text)

    # 如果原始文本和格式化后的文本不一致，则编辑消息
    if original_text != formatted_text:
        message.edit(formatted_text)
        # 打印编辑后的消息的ID、原始文本和格式化后的文本
        print(f"Original text: {original_text}. Formatted text: {formatted_text}.")


# 运行客户端
app.run()