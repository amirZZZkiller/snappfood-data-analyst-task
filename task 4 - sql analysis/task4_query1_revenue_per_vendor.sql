SELECT
    VendorID,
    SUM(Quantity * UnitPrice) AS TotalRevenue
FROM Sales
GROUP BY VendorID;
