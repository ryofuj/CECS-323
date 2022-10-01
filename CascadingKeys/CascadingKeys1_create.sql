-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-10-01 05:12:07.695

-- tables
-- Table: District
CREATE TABLE District (
    District_ID int  NOT NULL GENERATED true AS IDENTITY,
    District_name varchar(100)  NOT NULL,
    District_manager_ID int  NOT NULL,
    Region_ID int  NOT NULL,
    CONSTRAINT UK_State UNIQUE (District_name, District_manager_ID) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT PK_State PRIMARY KEY (District_ID)
);

CREATE INDEX Region_ID2 on District (Region_ID ASC);

CREATE INDEX District_idx_2 on District (District_manager_ID ASC);

-- Table: Employee
CREATE TABLE Employee (
    Employee_ID int  NOT NULL GENERATED true AS IDENTITY,
    Employee_Name varchar(100)  NOT NULL,
    Store_ID int  NULL,
    Distric_ID int  NULL,
    Region_ID int  NULL,
    CONSTRAINT UK_Customer_License UNIQUE (Store_ID, Distric_ID, Region_ID) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT PK_Customer PRIMARY KEY (Employee_ID)
);

CREATE INDEX Employee_idx_1 on Employee (Employee_ID ASC);

CREATE INDEX Employee_idx_2 on Employee (Store_ID ASC);

CREATE INDEX Employee_idx_3 on Employee (Distric_ID ASC);

CREATE INDEX Employee_idx_4 on Employee (Region_ID ASC);

-- Table: Region
CREATE TABLE Region (
    Region_ID int  NOT NULL GENERATED true AS IDENTITY,
    Region_name varchar(100)  NOT NULL,
    region_manager_ID int  NOT NULL,
    Employee_Employee_ID int  NOT NULL,
    CONSTRAINT UK_Vehicle_Plate UNIQUE (region_manager_ID) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT PK_Vehicle PRIMARY KEY (Region_ID)
);

CREATE INDEX Region_idx_1 on Region (region_manager_ID ASC);

-- Table: Store
CREATE TABLE Store (
    Store_ID int  NOT NULL GENERATED true AS IDENTITY,
    Store_address varchar(100)  NOT NULL,
    store_manager_ID int  NOT NULL,
    District_ID int  NOT NULL,
    Region_ID int  NOT NULL,
    CONSTRAINT UK_Country UNIQUE (Store_address) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT PK_Country PRIMARY KEY (Store_ID)
);

CREATE INDEX Region_ID1 on Store (Region_ID ASC);

CREATE INDEX Store_idx_2 on Store (District_ID ASC);

CREATE INDEX Store_idx_3 on Store (store_manager_ID ASC);

-- foreign keys
-- Reference: District (table: Store)
ALTER TABLE Store ADD CONSTRAINT District
    FOREIGN KEY (District_ID)
    REFERENCES District (District_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: District_1 (table: Employee)
ALTER TABLE Employee ADD CONSTRAINT District_1
    FOREIGN KEY (Distric_ID)
    REFERENCES District (District_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

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

-- Reference: Region (table: District)
ALTER TABLE District ADD CONSTRAINT Region
    FOREIGN KEY (Region_ID)
    REFERENCES Region (Region_ID)  
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

-- Reference: Region_Employee1 (table: Employee)
ALTER TABLE Employee ADD CONSTRAINT Region_Employee1
    FOREIGN KEY (Region_ID)
    REFERENCES Region (Region_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Region_ID (table: Store)
ALTER TABLE Store ADD CONSTRAINT Region_ID
    FOREIGN KEY (Region_ID)
    REFERENCES Region (Region_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Store_ (table: Employee)
ALTER TABLE Employee ADD CONSTRAINT Store_
    FOREIGN KEY (Store_ID)
    REFERENCES Store (Store_ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

