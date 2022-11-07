/* Ex6 */
SELECT car_log.license_plate, payment_log.price, payment_log.payment_date, parking.parking_name FROM car_log 
JOIN parking 
ON parking.parking_code = car_log.parking_code 
JOIN payment_log 
ON car_log.id = payment_log.car_id;