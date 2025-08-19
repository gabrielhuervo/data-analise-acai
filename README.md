# Análise de Comportamento de Clientes em E-commerce

Este projeto de análise de dados explora um dataset sobre o comportamento de clientes numa plataforma de e-commerce. O objetivo é identificar o perfil dos clientes de maior valor, entender os fatores que impulsionam a satisfação e a retenção, e fornecer recomendações estratégicas para a empresa.

A análise foi conduzida utilizando **Python (Pandas)** para a limpeza e exploração inicial dos dados e **Power BI** para a criação de um dashboard interativo com as principais descobertas.

---

### **Como Usar Este Repositório**

* **Apresentação:** Para visualizar a apresentação da análise em HTML, acesse a [página do projeto](https://gabrielhuervo.github.io/data-analise-perfis-ecommerce/)

* **Análise Detalhada:** Para explorar a análise completa, incluindo o código Python, aceda ao [notebook deste projeto](notebook_analise.ipynb). E a apresentação

* **Dashboard Interativo:** Para uma visão geral dos resultados, aceda ao [dashboard no Power BI](dashboard.pbix).

* **Fontes de Dados:** O dataset original (`customer.csv`) e o dataset limpo (`customer_limpo.csv`) estão disponíveis na pasta `src` neste repositório.

---

### **1. Problema de Negócio e Perguntas-Chave**

A gestão da empresa procurou entender como poderia aumentar as vendas e a lealdade dos clientes. Para guiar a investigação, foram definidas as seguintes perguntas:

* **Valor do Cliente:** Qual é o perfil (demográfico e geográfico) dos clientes que mais gastam?

* **Retenção:** Existe uma relação entre o nível de satisfação do cliente e a sua probabilidade de abandonar a plataforma?

* **Estratégia:** A atual estratégia de descontos está a ter um impacto positivo na satisfação e no valor gerado pelo cliente?

---

### **2. Principais Insights e Visualizações**

A análise revelou três fatores críticos que governam o comportamento do cliente: a satisfação é o principal motor da retenção, a geografia determina o valor do cliente e a estratégia de descontos atual mostra-se ineficaz. O dashboard criado no Power BI resume visualmente estas descobertas.

---

### **3. Recomendações Estratégicas Finais**

Com base nos insights obtidos, as seguintes recomendações foram feitas:

1.  **Foco na Experiência do Cliente:** A insatisfação é o principal indicador de abandono. Recomenda-se implementar um sistema proativo para monitorizar a satisfação, especialmente com clientes "Silver", que representam o "momento da verdade" na jornada de lealdade, para reverter experiências negativas antes que o cliente abandone a plataforma.

2.  **Revisão da Estratégia de Descontos:** A análise revelou um paradoxo onde os mercados de menor valor recebem 100% de desconto, enquanto os de maior valor não recebem nenhum. Recomenda-se testar a remoção de descontos em cidades de baixo desempenho e reinvestir o orçamento em estratégias que aumentem o valor percebido da marca.

3.  **Marketing Direcionado (Hiper-segmentação):** O perfil do cliente ideal foi identificado como um homem, com cerca de 30 anos, residente em São Francisco ou Nova York. Recomenda-se direcionar os esforços de aquisição para este público específico para maximizar o retorno sobre o investimento em marketing.