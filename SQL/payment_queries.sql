SELECT payment_id, status 
FROM payments 
WHERE user_id = 101 AND status = 'PENDING';
