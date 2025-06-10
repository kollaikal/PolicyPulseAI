# utils/rag.py
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def get_rag_summary(summary_text, all_bills):
    documents = [
        Document(page_content=b.get("summary", ""), metadata={"title": b.get("title", "")})
        for b in all_bills if b.get("summary")
    ]

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    vectorstore = Chroma.from_documents(chunks, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    return chain.run(summary_text)
