            BEGIN TRANSACTION;
            CREATE TABLE IF NOT EXISTS cashier (
                id	            INTEGER PRIMARY KEY AUTOINCREMENT,
                name	        VARCHAR UNIQUE,
                active          BOOLEAN,
                date	        TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS base (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            VARCHAR UNIQUE,
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS shift (
                id	            INTEGER PRIMARY KEY AUTOINCREMENT,
                base            REFERENCES base(id),
                shift           INTEGER UNIQUE,
                actual_date     TIMESTAMP,
                period          INT,
                cashier 	    REFERENCES cashier(id),
                active          BOOLEAN,
                date	        TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS measure (
                id      	    INTEGER PRIMARY KEY AUTOINCREMENT,
                code            INTEGER UNIQUE,
                name            TEXT UNIQUE,
                description     TEXT,
                defmass         INTEGER DEFAULT 0,
                active          BOOLEAN,
                date	        TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS supplier (
                id      	    INTEGER PRIMARY KEY AUTOINCREMENT,
                name        	TEXT UNIQUE,
                active          BOOLEAN,
                date	        TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS section (
                id      	    INTEGER PRIMARY KEY AUTOINCREMENT,
                name   	        TEXT UNIQUE,
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS dish (
                id  	        INTEGER PRIMARY KEY AUTOINCREMENT,
                name   	        TEXT UNIQUE,
                section         REFERENCES section(id),
                mass            FLOAT,
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS product (
                id      	    INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT UNIQUE,
                for_sale        BOOLEAN DEFAULT 0,
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS coefficient (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                product         REFERENCES product(id),
                period_start    TIMESTAMP,
                period_end      TIMESTAMP,
                percent         INTEGER,
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS consumption (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                dish            REFERENCES dish(id),
                product         REFERENCES product(id),
                brutto          INTEGER,
                netto           INTEGER,
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS income (
                id      	    INTEGER PRIMARY KEY AUTOINCREMENT,
                base            REFERENCES base(id),
                name	        TEXT UNIQUE,
                nomenculature   INTEGER UNIQUE,
                product         REFERENCES product(id),
                measure         REFERENCES measure(code),
                count           INTEGER,
                mass            FLOAT,
                rest            FLOAT,
                supplier        REFERENCES supplier(id) DEFAULT 1,
                price           FLOAT,
                coefficient     FLOAT,
                shift           REFERENCES shift(shift),
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS calculate (
                id          	INTEGER PRIMARY KEY AUTOINCREMENT,
                base            REFERENCES base(id),
                income          REFERENCES income(id),
                product         REFERENCES product(id),
                dish            REFERENCES dish(id),
                price           FLOAT,
                active          BOOLEAN,
                date            TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS menu (
                id  	        INTEGER PRIMARY KEY AUTOINCREMENT,
                base            REFERENCES base(id),
                dish            REFERENCES dish(id),
                shift           REFERENCES shift(shift),
                portions        INT,
                balance		    INT,
                price	        FLOAT,
                active          BOOLEAN,
                date		    TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS company (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT UNIQUE,
                coefficient     FLOAT,
                active          BOOLEAN,
                date    	    TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS worker (
                id      	    INTEGER PRIMARY KEY AUTOINCREMENT,
                company         REFERENCES company(id),
                card            TEXT UNIQUE,
                name            TEXT UNIQUE,
                employee        INTEGER UNIQUE,
                active          BOOLEAN,
                date    	    TIMESTAMP
                );
            CREATE TABLE IF NOT EXISTS sale (
                id	            INTEGER PRIMARY KEY AUTOINCREMENT,
                base            REFERENCES base(id),
                menu            REFERENCES menu(id),
                shift           REFERENCES shift(shift),
                worker  	    REFERENCES worker(id),
                number	        INTEGER,
                active          BOOLEAN,
                date    	    TIMESTAMP
                );
            COMMIT;
