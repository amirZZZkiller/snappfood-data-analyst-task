SELECT
    s.VendorID,
    SUM(s.Quantity * s.UnitPrice) AS TotalRevenue,
    ROUND(SUM(s.Quantity * s.UnitPrice *
        CAST(REPLACE(pm.ProfitMargin, '%', '') AS FLOAT) / 100.0), 2) AS TotalProfit,
    ROUND(SUM(s.Quantity * s.UnitPrice) * 1.0 / COUNT(DISTINCT s.OrderID), 2) AS AOV
FROM Sales s
JOIN ProfitMargins pm
  ON s.Product = pm.Product
GROUP BY s.VendorID
ORDER BY TotalProfit DESC;
