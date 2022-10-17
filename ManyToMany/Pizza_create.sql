-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-10-17 17:41:27.114

-- tables
-- Table: Pizza
CREATE TABLE Pizza (
    order_pizza varchar(100)  NOT NULL,
    description varchar(100)  NOT NULL,
    toppingPizza_ingredient varchar(100)  NOT NULL,
    simplePizza_crust_crustType varchar(100)  NOT NULL,
    simplePizza_size_size int  NOT NULL,
    CONSTRAINT pizza PRIMARY KEY (description)
);

-- Table: crust
CREATE TABLE crust (
    crustType varchar(100)  NOT NULL,
    CONSTRAINT crust_pk PRIMARY KEY (crustType)
);

-- Table: order
CREATE TABLE "order" (
    pizza varchar(100)  NOT NULL,
    CONSTRAINT order_pk PRIMARY KEY (pizza)
);

-- Table: simplePizza
CREATE TABLE simplePizza (
    size_size int  NOT NULL,
    crust_crustType varchar(100)  NOT NULL,
    CONSTRAINT simplePizza_pk PRIMARY KEY (size_size,crust_crustType)
);

-- Table: size
CREATE TABLE size (
    size int  NOT NULL,
    CONSTRAINT size_pk PRIMARY KEY (size)
);

-- Table: toppingPizza
CREATE TABLE toppingPizza (
    ingredient varchar(100)  NOT NULL,
    CONSTRAINT toppingPizza_pk PRIMARY KEY (ingredient)
);

-- foreign keys
-- Reference: Pizza_order (table: Pizza)
ALTER TABLE Pizza ADD CONSTRAINT Pizza_order
    FOREIGN KEY (order_pizza)
    REFERENCES "order" (pizza)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Pizza_simplePizza (table: Pizza)
ALTER TABLE Pizza ADD CONSTRAINT Pizza_simplePizza
    FOREIGN KEY (simplePizza_size_size, simplePizza_crust_crustType)
    REFERENCES simplePizza (size_size, crust_crustType)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Pizza_toppingPizza (table: Pizza)
ALTER TABLE Pizza ADD CONSTRAINT Pizza_toppingPizza
    FOREIGN KEY (toppingPizza_ingredient)
    REFERENCES toppingPizza (ingredient)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: simplePizza_crust (table: simplePizza)
ALTER TABLE simplePizza ADD CONSTRAINT simplePizza_crust
    FOREIGN KEY (crust_crustType)
    REFERENCES crust (crustType)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: simplePizza_size (table: simplePizza)
ALTER TABLE simplePizza ADD CONSTRAINT simplePizza_size
    FOREIGN KEY (size_size)
    REFERENCES size (size)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

