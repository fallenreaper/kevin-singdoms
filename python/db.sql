-- public."eve_user" definition

-- Drop table

-- DROP TABLE public."eve_user";

CREATE TABLE public."eve_user" (
	character_id int4 NOT NULL,
	character_name varchar NULL,
	refresh_token varchar NULL,
	date_created date NULL,
	last_updated date NULL,
	token_expires date NULL,
	access_token varchar NULL,
	discord_user_id int4 NULL,
	CONSTRAINT eve_user_pk PRIMARY KEY (character_id),
	CONSTRAINT eve_user_un UNIQUE (character_name)
);

-- public.structure_monitor definition

-- Drop table

-- DROP TABLE public.structure_monitor;

CREATE TABLE public.structure_monitor (
	chunk_arrival_time date NULL,
	natural_decay_timer date NULL,
	extraction_start_time date NULL,
	structure_id int4 NOT NULL,
	structure_name varchar NULL,
	moon_id int4 NULL,
	moon_name varchar NULL,
	CONSTRAINT structure_monitor_pk PRIMARY KEY (structure_id)
);

-- public.channel_character_map definition

-- Drop table

-- DROP TABLE public.channel_character_map;

CREATE TABLE public.channel_character_map (
	character_id int4 NOT NULL,
	channel_id int4 NOT NULL,
	CONSTRAINT channel_character_map_pk PRIMARY KEY (channel_id, character_id)
);


-- public.channel_character_map foreign keys

ALTER TABLE public.channel_character_map ADD CONSTRAINT channel_character_map_fk FOREIGN KEY (character_id) REFERENCES "eve_user"(character_id);