# 📊 KPI Insight Hub — Food Delivery Analytics

> A comprehensive KPI Analysis Case Study on a Food Delivery platform, built with **Tableau** for interactive dashboards and **Notion** for strategic insight documentation.

![Domain](https://img.shields.io/badge/Domain-Food%20Delivery-orange)
![Tool](https://img.shields.io/badge/Tool-Tableau-blue)
![Data](https://img.shields.io/badge/Records-1000%2B-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 🎯 Project Overview

This project goes **beyond just building charts**. It demonstrates how to:
- Pick a real-world business domain
- Define the right KPIs that actually matter
- Visualize data to uncover hidden patterns
- Write **strategic, actionable insights** — not just descriptions of charts

**The goal:** Prove you can *think*, not just build.

---

## 📈 KPIs Tracked

| # | KPI | What It Measures |
|---|-----|-----------------|
| 1 | **Average Order Value (AOV)** | Revenue per transaction by customer segment |
| 2 | **Customer Acquisition Cost (CAC)** | Marketing efficiency for new users |
| 3 | **Customer Retention Rate** | Platform loyalty and repeat usage |
| 4 | **Average Delivery Time** | Operational & logistics health |
| 5 | **Order Cancellation Rate** | Customer friction points by region |
| 6 | **Contribution Margin** | True profitability after variable costs |

---

## 💡 Key Insights (Summary)

1. **VIP Multiplier Effect** — VIP customers show an AOV of **$55.58**, nearly **2.8x higher** than New customers ($20.05). Yet their marketing cost is near-zero, while New customer CAC peaks at ~$950/month. Shifting 30% of CAC budget into loyalty programs to convert Returning → VIP yields far better ROI.

2. **Stable Delivery Operations** — Average delivery time holds steady around **40 minutes** across all months, hovering right at the average line. This is a positive operational signal, but any upward drift should trigger driver incentive adjustments.

3. **Central Region Cancellation Hotspot** — The Central region shows the highest cancellation rate at **~22%**, significantly above other regions. Targeted quality control and restaurant reliability audits are recommended for this zone.

4. **Contribution Margin Leaders** — Pizza Hut and Burger King consistently lead in contribution margin across months, while smaller restaurants like Taco Bell and Sushi Spot show thinner margins. Prioritizing partnerships with high-margin restaurants improves platform profitability.

> 📄 Full insights with strategic recommendations → [`Notion_Case_Study.md`](./Notion_Case_Study.md)

---

## 🛠️ Project Structure

```
kpi-insight-hub/
├── README.md                  # This file
├── food_delivery_data.csv     # Synthetic dataset (1,000 orders)
├── generate_data.py           # Python script to regenerate data
├── Tableau_Build_Guide.md     # Step-by-step Tableau dashboard guide
├── Notion_Case_Study.md       # Full case study with insights
└── screenshots/               # Dashboard screenshots
```

---

## 🚀 How to Reproduce

### 1. Clone the repo
```bash
git clone https://github.com/HJ291206/kpi-insight-hub.git
cd kpi-insight-hub
```

### 2. (Optional) Regenerate the dataset
```bash
python generate_data.py
```

### 3. Build the Dashboard
- Open **Tableau Public** (free) or Tableau Desktop
- Connect to `food_delivery_data.csv`
- Follow the step-by-step instructions in [`Tableau_Build_Guide.md`](./Tableau_Build_Guide.md)

### 4. Read the Insights
- Open [`Notion_Case_Study.md`](./Notion_Case_Study.md) and copy it into a Notion page for a polished presentation

---

## 📸 Dashboard Preview

The interactive Tableau dashboard includes 6 KPI visualizations:
- **AOV by Customer** — Bar chart segmented by New / Returning / VIP
- **CAC Monthly Trend** — Line chart tracking marketing spend for new users
- **Avg Delivery Time Trend** — Line chart with average reference line
- **Cancellations by Region** — Stacked bar showing cancellation % per region
- **Profitability by Restaurant** — Horizontal bar chart of contribution margin by month

> 🔗 **Live Dashboard:** *Publish to [Tableau Public](https://public.tableau.com/) and add your link here*

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Synthetic data generation |
| **Tableau** | Interactive dashboard & KPI visualization |
| **Notion** | Case study documentation & insight writing |
| **GitHub** | Version control & portfolio hosting |

---

## 👤 Author

**Harsh** — Data Analytics & Business Intelligence  

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
