-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-10-01 05:28:06.302

-- tables
-- Table: District
CREATE TABLE District (
    District_ID int  NOT NULL,
    District_name varchar(100)  NOT NULL,
    District_manager_ID int  NOT NULL,
    CONSTRAINT UK_State UNIQUE (District_name, District_manager_ID) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT PK_State PRIMARY KEY (District_ID)
);

CREATE INDEX District_idx_2 on District (District_manager_ID ASC);

-- Table: Employee
CREATE TABLE Employee (
    Employee_ID int  NOT NULL,
    Employee_Name varchar(100)  NOT NULL,
    CONSTRAINT PK_Customer PRIMARY KEY (Employee_ID)
);

CREATE INDEX Employee_idx_1 on Employee (Employee_ID ASC);

-- Table: Region
CREATE TABLE Region (
    Region_ID int  NOT NULL,
    Region_name varchar(100)  NOT NULL,
    region_manager_ID int  NOT NULL,
    CONSTRAINT UK_Vehicle_Plate UNIQUE (region_manager_ID) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT PK_Vehicle PRIMARY KEY (Region_ID)
);

CREATE INDEX Region_idx_1 on Region (region_manager_ID ASC);

-- Table: Store
CREATE TABLE Store (
    Store_ID int  NOT NULL,
    Store_address varchar(100)  NOT NULL,
    store_manager_ID int  NOT NULL,
    CONSTRAINT UK_Country UNIQUE (Store_address) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT PK_Country PRIMARY KEY (Store_ID)
);

CREATE INDEX Store_idx_3 on Store (store_manager_ID ASC);

-- foreign keys
-- Reference: District_Employee (table: District)
ALTER TABLE District ADD CONSTRAINT District_Employee
    FOREIGN KEY (District_manager_ID)
    REFERENCES Employee (Employee_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Employee (table: Store)
ALTER TABLE Store ADD CONSTRAINT Employee
    FOREIGN KEY (store_manager_ID)
    REFERENCES Employee (Employee_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Region_Employee (table: Region)
ALTER TABLE Region ADD CONSTRAINT Region_Employee
    FOREIGN KEY (region_manager_ID)
    REFERENCES Employee (Employee_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

