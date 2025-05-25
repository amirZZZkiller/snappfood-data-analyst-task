SELECT
    s.VendorID,
    SUM(s.Quantity * s.UnitPrice *
        CAST(REPLACE(pm.ProfitMargin, '%', '') AS FLOAT) / 100.0) AS TotalProfit
FROM Sales s
JOIN ProfitMargins pm
  ON s.Product = pm.Product
GROUP BY s.VendorID
ORDER BY TotalProfit DESC
LIMIT 1;
