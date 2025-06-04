import streamlit as st
from blockchain import Blockchain

# Ініціалізація блокчейну
if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()
    st.session_state.pending_transactions = []

st.title("🧱 Симулятор блокчейн-транзакцій")

st.subheader("➕ Додати транзакцію")
sender = st.text_input("Відправник")
receiver = st.text_input("Одержувач")
amount = st.number_input("Сума", min_value=0.01, step=0.01)

if st.button("Додати транзакцію"):
    if sender and receiver:
        transaction = {"from": sender, "to": receiver, "amount": amount}
        st.session_state.pending_transactions.append(transaction)
        st.success("✅ Транзакцію додано")
    else:
        st.warning("⚠️ Всі поля обов'язкові")

st.subheader("🔨 Створення блоку")
if st.button("Створити блок"):
    if st.session_state.pending_transactions:
        st.session_state.blockchain.add_block(st.session_state.pending_transactions)
        st.session_state.pending_transactions = []
        st.success("✅ Блок успішно створено")
    else:
        st.warning("⚠️ Немає транзакцій для додавання")

st.subheader("📄 Ланцюг блоків")
for block in st.session_state.blockchain.chain:
    st.markdown(f"### Блок №{block.index}")
    st.json({
        "Транзакції": block.transactions,
        "Хеш": block.hash,
        "Попередній хеш": block.previous_hash,
        "Nonce": block.nonce,
        "Час": block.timestamp
    })
