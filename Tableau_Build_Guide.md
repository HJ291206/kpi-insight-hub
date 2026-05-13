# Tableau Dashboard Build Guide

This guide will walk you through transforming the raw `food_delivery_data.csv` into a professional Tableau Dashboard.

## Step 1: Connect to Data
1. Open **Tableau Public** (or Desktop).
2. Under "Connect -> To a File", click **Text file**.
3. Select the `food_delivery_data.csv` file from your project folder.
4. Tableau will automatically load the data. Make sure Tableau recognizes **Order Date** as a `Date` type, and the numerical fields (like **Order Value ($)**) as `Measures`.
5. Click **Sheet 1** at the bottom left to start building.

## Step 2: Build KPI 1 - Average Order Value (AOV) by Customer Type
*   **Goal:** See who spends the most.
*   **Columns:** `Customer Type`
*   **Rows:** `Order Value ($)` 
    *   *Click the drop-down on Order Value on the Rows shelf -> Change Measure from `Sum` to `Average`.*
*   **Action:** Change the chart type to a **Bar Chart**. 
*   **Formatting:** Add labels so the average values are visible on top of each bar. Rename the sheet to *"AOV by Customer"*.

## Step 3: Build KPI 2 & 3 - Customer Acquisition Cost (CAC) vs. Retention
*   **Goal:** Track how much we spend to acquire new users.
*   **Columns:** `Order Date` (Set to Month).
*   **Rows:** `Marketing Spend (per user)` (Leave as Sum to see total expenditure, or Average to see CAC per cohort).
*   **Action:** Drag `Customer Type` to the **Color** mark. Filter out `VIP` and `Returning` to exclusively look at the `New` customer trend (this is your CAC).
*   **Formatting:** Make this an **Area Chart** or bold **Line Chart**. Rename the sheet to *"CAC Monthly Trend"*.

## Step 4: Build KPI 4 - Average Delivery Time over Time
*   **Goal:** Visualize operational efficiency.
*   **Columns:** `Order Date` (Set to Week or Month).
*   **Rows:** `Delivery Time (mins)` (Change Measure to `Average`).
*   **Action:** Create a **Line Chart**. 
*   **Analytics Tab:** Drag an **Average Line** from the Analytics pane onto the chart. If the line trends upward, operational efficiency is suffering. 
*   **Rename:** *"Avg Delivery Time Trend"*.

## Step 5: Build KPI 5 - Order Cancellation Rate Map
*   **Goal:** Find out where orders are getting cancelled most often.
*   **Columns:** `Region`
*   **Rows:** Count of Data (or drag `Order ID` and set measure to Count).
*   **Color Mark:** Drag `Is Cancelled` to color. Make Cancelled "Red" and Not Cancelled "Grey".
*   **Action:** Change to a **100% Stacked Bar Chart** to see the *percentage* of cancellations per region easily.
*   **Rename:** *"Cancellations by Region"*.

## Step 6: Build KPI 6 - Contribution Margin
*   **Goal:** Calculate true profit per order.
*   **Action:** We need a calculated field! Go to Analysis -> **Create Calculated Field**.
    *   Name it: `Contribution Margin`
    *   Formula: `[Order Value ($)] - [Variable Costs ($)] - [Marketing Spend (per user)]`
*   **Rows:** `Contribution Margin` (Sum)
*   **Columns:** `Order Date` (Month) and `Restaurant` (Color).
*   **Rename:** *"Profitability by Restaurant"*.

## Step 7: Assemble the Dashboard
1. Click the **New Dashboard** icon at the bottom.
2. Under "Size", choose **Automatic** or a standard desktop size (e.g., 1200 x 800).
3. Drag all your sheets onto the canvas. Arrange them cleanly (KPI summary numbers at the top, trends in the middle, region/restaurant breakdowns at the bottom).
4. Add a nice **Text** title at the top: *Food Delivery Performance Dashboard*.
