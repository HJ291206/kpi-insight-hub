# 📊 KPI Analysis Case Study: Food Delivery Optimization

**Domain Focus:** Food Delivery Platform Economy  
**Tools Used:** Tableau (Data Visualization) & Notion (Insight Documentation)

## 📌 Executive Summary
This analysis focuses on the optimization of a hypothetical food delivery platform. By analyzing 6 key performance indicators (KPIs) over a 6-month period, I identified bottlenecks in operational efficiency and opportunities for targeted marketing. **The ultimate goal is to move beyond basic reporting and demonstrate how data drives actionable business strategy.**

---

## 🎯 The 6 Core KPIs Tracked

1.  **Average Order Value (AOV):** Revenue scale per transaction.
2.  **Customer Acquisition Cost (CAC):** Marketing spend efficiency.
3.  **Customer Retention Rate (CRR):** Long-term platform loyalty.
4.  **Average Delivery Time (ADT):** Logistics and operational health.
5.  **Order Cancellation Rate:** Customer friction and restaurant reliability.
6.  **Contribution Margin:** Actual profitability per order post-variable costs.

---

## 💡 Strategic Insights & Recommendations

### 1. The VIP Customer Multiplier Effect (AOV & Marketing)
**Insight:** VIP customers exhibit an Average Order Value almost **2.5x higher** than New Customers, while requiring near-zero ongoing marketing spend. However, New Customer Acquisition Cost (CAC) is steadily rising month-over-month.
*   **Strategic Action:** Pivot the marketing budget allocation. Instead of blindly pouring money into top-of-funnel acquisition, invest 30% of the CAC budget into a loyalty program specifically designed to convert 'Returning' customers into 'VIPs'. 

### 2. The Operational Death Spiral (Delivery Time vs. Cancellations)
**Insight:** There is a direct, positive correlation between Average Delivery Time and Order Cancellation Rate. In the 'West' region, delivery times exceeding 45 minutes lead to a cancellation rate spike of nearly 12%. 
*   **Strategic Action:** Implement dynamic delivery pricing. During peak hours/bad weather in the West region, suppress demand slightly with higher delivery fees, and use that premium to incentivize more drivers to log on, thereby stabilizing the 45-minute threshold.

### 3. Contribution Margin Illusion
**Insight:** We observed high GMV (Gross Merchandise Value) in the 'Central' region. However, after factoring in Variable Costs (delivery pay guarantees, packaging), the **Contribution Margin** is actually the lowest across all regions. We are subsidizing growth at the expense of profitability.
*   **Strategic Action:** Renegotiate restaurant commission structures in the Central region or optimize batching algorithms (assigning one driver to pick up multiple orders from the same restaurant block) to aggressively bring down driver variable payouts per order.

---

## 🛠️ The Technical Build

*   **Data Architecture:** Developed a Python script to simulate a 1,000-row relational dataset encompassing orders, regional mapping, and unit economics.
*   **Dashboarding:** Constructed an interactive Tableau dashboard highlighting KPI trends, utilizing calculated fields for Contribution Margin and area charts for cohort analysis.

> *"Dashboards answer the 'What'. Analytics answers the 'Why'. This case study focuses on the 'So What?'"*
