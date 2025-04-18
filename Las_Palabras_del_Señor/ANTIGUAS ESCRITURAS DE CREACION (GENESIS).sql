-- Table: public.companies

-- DROP TABLE IF EXISTS public.companies;

CREATE TABLE IF NOT EXISTS public.companies
(
    "CompanyId" uuid NOT NULL,
    "Name" character varying(255) COLLATE pg_catalog."default",
    "UserId" uuid,
    phonenumber character varying(13) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    CONSTRAINT companies_pkey PRIMARY KEY ("CompanyId"),
    CONSTRAINT "companies_UserId_fkey" FOREIGN KEY ("UserId")
        REFERENCES public.users ("UserId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_user FOREIGN KEY ("UserId")
        REFERENCES public.users ("UserId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.companies
    OWNER to postgres;

-- Table: public.products

-- DROP TABLE IF EXISTS public.products;

CREATE TABLE IF NOT EXISTS public.products
(
    productid uuid NOT NULL,
    name character varying(255) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    price integer,
    companyid uuid,
    CONSTRAINT productos_pkey PRIMARY KEY (productid),
    CONSTRAINT fk_company_id FOREIGN KEY (companyid)
        REFERENCES public.companies ("CompanyId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.products
    OWNER to postgres;


-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    "UserId" uuid NOT NULL,
    "Name" character varying(255) COLLATE pg_catalog."default",
    "Email" character varying(255) COLLATE pg_catalog."default",
    "Password" character varying(255) COLLATE pg_catalog."default",
    "Role" character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY ("UserId")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;
