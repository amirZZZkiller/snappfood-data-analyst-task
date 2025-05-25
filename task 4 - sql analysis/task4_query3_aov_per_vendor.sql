SELECT
    VendorID,
    ROUND(SUM(Quantity * UnitPrice) * 1.0 / COUNT(DISTINCT OrderID), 2) AS AOV
FROM Sales
GROUP BY VendorID;
