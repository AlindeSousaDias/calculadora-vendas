
import streamlit as st

st.set_page_config(page_title="Calculadora de Margem e Markup", layout="centered")
st.title("🧾 Calculadora de Margem e Markup")
st.markdown("Preencha os dados da venda para verificar se está dentro da margem mínima de 15%.")

valor_venda = st.number_input("Valor da Venda Promob (R$)", min_value=0.0, format="%.2f")
custo_materiais = st.number_input("Custo dos Materiais (R$)", min_value=0.0, format="%.2f")
montagem = st.number_input("Montagem (R$)", min_value=0.0, format="%.2f")
transporte = st.number_input("Transporte (R$)", min_value=0.0, format="%.2f")
comissao = st.number_input("Comissão (R$)", min_value=0.0, format="%.2f")
outros_custos = st.number_input("Outros Custos (R$)", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    total_custos = custo_materiais + montagem + transporte + comissao + outros_custos
    lucro = valor_venda - total_custos
    margem = lucro / valor_venda if valor_venda != 0 else 0
    markup = valor_venda / total_custos if total_custos != 0 else 0

    st.subheader("✅ Resultados")
    st.write(f"**Total de Custos:** R$ {total_custos:,.2f}")
    st.write(f"**Lucro Bruto:** R$ {lucro:,.2f}")

    st.subheader("🧮 Cálculos")
    st.write(f"**Margem de Contribuição:** {margem:.2%}")
    st.write(f"**Markup:** {markup:.2%}")

    st.subheader("📊 Interpretação")
    if margem >= 0.15:
        st.success("✅ Projeto saudável! Margem acima de 15%.")
    else:
        st.error("🚨 Atenção: Margem abaixo de 15%. Risco de prejuízo.")
