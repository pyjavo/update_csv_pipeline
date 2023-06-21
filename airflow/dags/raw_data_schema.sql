CREATE TABLE  IF NOT EXISTS `raw_data` (
  `ID` INT NOT NULL,
  `order_number` INT NOT NULL,
  `order_status` VARCHAR(255) NOT NULL,
  `customer_email` VARCHAR(255) NULL,
  `preferred_delivery_date` DATE NULL,
  `preferred_delivery_hours` VARCHAR(255) NULL,
  `sales_person` VARCHAR(255) NULL,
  `notes` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `neighbourhood` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `creation_date` DATE NOT NULL,
  `source` VARCHAR(255) NULL,
  `warehouse` VARCHAR(255) NULL,
  `shopify_id` INT NOT NULL,
  `sales_person_role` VARCHAR(255) NULL,
  `order_type` VARCHAR(255) NULL,
  `is_pitayas` BOOLEAN NULL,
  `discount_applications` VARCHAR(255) NULL,
  `payment_method` VARCHAR(255) NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;