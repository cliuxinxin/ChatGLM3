from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.directory import DirectoryLoader

from config import *

loader = DirectoryLoader(
    path=DATA_PATH,
    glob="**/*.txt",  # 用于查找文件的 glob 模式，默认为 '**/[!.]*'（所有非隐藏文件）
    loader_cls=TextLoader,  # 指定加载文件的类，默认为 UnstructuredFileLoader
    # 其他可选参数
)

documents = loader.load()

print(len(documents), documents[0].page_content[0:100])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
splits = text_splitter.split_documents(documents)
print(len(splits), splits[0])

embeddings = HuggingFaceEmbeddings(model_name='distiluse-base-multilingual-cased-v1',
                                       model_kwargs={'device': 'cpu'})

db = FAISS.from_documents(splits, embeddings)
db.save_local(DB_FAISS_PATH)


# # 待查询的文本
# query_text = "如何删除iptable"


# # 使用 `embed_query` 生成查询文本的嵌入向量
# query_embedding = embeddings.embed_query(query_text)

# # 使用 `similarity_search_by_vector` 在FAISS索引中搜索最相似的文档
# similar_documents = db.similarity_search_by_vector(query_embedding, k=5)  # k是你想返回的相似文档数量

# # 输出结果
# for doc in similar_documents:
#     print(doc)
