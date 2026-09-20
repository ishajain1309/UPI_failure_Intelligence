-- ============================================
-- UPI FAILURE INTELLIGENCE & ANALYTICS
-- SQL ANALYSIS
-- ============================================

-- 1. OVERALL TRANSACTION SUMMARY
-- ============================================

SELECT
    COUNT(*) AS total_transactions,

    SUM(
        CASE
            WHEN transaction_status = 'SUCCESS' THEN 1
            ELSE 0
        END
    ) AS successful_transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failed_transactions,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction;


-- 2. FAILURE BY NETWORK
-- ============================================

SELECT
    network_type,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY network_type

ORDER BY failure_rate DESC;


-- 3. FAILURE BY DEVICE
-- ============================================

SELECT
    device_type,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY device_type

ORDER BY failure_rate DESC;


-- 4. FAILURE BY TRANSACTION TYPE
-- ============================================

SELECT
    transaction_type,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY transaction_type

ORDER BY failure_rate DESC;


-- 5. FAILURE BY SENDER BANK
-- ============================================

SELECT
    sender_bank,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY sender_bank

ORDER BY failure_rate DESC;


-- 6. FAILURE BY RECEIVER BANK
-- ============================================

SELECT
    receiver_bank,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY receiver_bank

ORDER BY failure_rate DESC;


-- 7. FAILURE BY MERCHANT CATEGORY
-- ============================================

SELECT
    merchant_category,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY merchant_category

ORDER BY failure_rate DESC;


-- 8. FAILURE BY HOUR
-- ============================================

SELECT
    hour,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY hour

ORDER BY hour;


-- 9. NETWORK + TRANSACTION TYPE
-- ============================================
-- Only segments with at least 20 transactions

SELECT
    network_type,
    transaction_type,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY network_type, transaction_type

HAVING COUNT(*) >= 20

ORDER BY failure_rate DESC;


-- 10. SENDER BANK + RECEIVER BANK
-- ============================================
-- Only bank pairs with at least 20 transactions

SELECT
    sender_bank,
    receiver_bank,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY sender_bank, receiver_bank

HAVING COUNT(*) >= 20

ORDER BY failure_rate DESC;


-- 11. HOUR + NETWORK
-- ============================================
-- Only segments with at least 20 transactions

SELECT
    hour,
    network_type,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY hour, network_type

HAVING COUNT(*) >= 20

ORDER BY failure_rate DESC;


-- 12. HIGH-VOLUME FAILURE SEGMENTS
-- ============================================
-- At least 20 transactions AND failure rate >= 5%

SELECT
    network_type,
    transaction_type,

    COUNT(*) AS transactions,

    SUM(
        CASE
            WHEN transaction_status = 'FAILED' THEN 1
            ELSE 0
        END
    ) AS failures,

    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'FAILED' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate

FROM upi_transaction

GROUP BY network_type, transaction_type

HAVING COUNT(*) >= 20

   AND
   (
       SUM(
           CASE
               WHEN transaction_status = 'FAILED' THEN 1
               ELSE 0
           END
       ) * 100.0 / COUNT(*)
   ) >= 5

ORDER BY failure_rate DESC;