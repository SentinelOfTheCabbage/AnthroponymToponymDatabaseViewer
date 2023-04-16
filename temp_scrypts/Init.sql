-- Server version: 8.0.31 MySQL Community Server - GPL
CREATE TABLE anthroponym (
    anthroponym_id SERIAL PRIMARY KEY,
    anthroponym VARCHAR(256) UNIQUE,
    original VARCHAR(256) UNIQUE NOT NULL,
    transcription VARCHAR(256) UNIQUE NOT NULL,
    source VARCHAR(512) UNIQUE NOT NULL,
    comments VARCHAR(2048),
    century NUMERIC(4) NOT NULL
);

CREATE TABLE toponym (
    toponym_id SERIAL PRIMARY KEY,
    toponym VARCHAR(512),
    original VARCHAR(512) NOT NULL,
    transcription VARCHAR(512) NOT NULL,
    historical_source VARCHAR(512),
    ageographical_source VARCHAR(512),
    comments VARCHAR(2048),
    century NUMERIC(4)
    geopos VARCHAR(32)
);

CREATE TABLE anthroponym_image(
    anthroponym_id BIGINT UNSIGNED NOT NULL,
    img BLOB NOT NULL,
    CONSTRAINT fk_anthroponym_img
        FOREIGN KEY (anthroponym_id)
	    REFERENCES anthroponym(anthroponym_id)
	    ON DELETE CASCADE
);


CREATE TABLE toponym_image(
    toponym_id BIGINT UNSIGNED NOT NULL,
    img BLOB NOT NULL,
    CONSTRAINT fk_toponym_img
        FOREIGN KEY(toponym_id)
	    REFERENCES toponym(toponym_id)
	    ON DELETE CASCADE
);

CREATE TABLE literature (
    literature_id SERIAL PRIMARY KEY,
    author VARCHAR(512) NOT NULL UNIQUE,
    title VARCHAR(256) NOT NULL UNIQUE,
    published_at SMALLINT NOT NULL UNIQUE
);

CREATE TABLE anthroponym_reference (
    anthroponym_id BIGINT UNSIGNED NOT NULL,
    literature_id BIGINT UNSIGNED NOT NULL,
    pages VARCHAR(100) NOT NULL,
    CONSTRAINT fk_anthroponym_ref
        FOREIGN KEY(anthroponym_id)
	    REFERENCES anthroponym(anthroponym_id)
	    ON DELETE CASCADE,
    CONSTRAINT fk_literature_ref_anth
        FOREIGN KEY(literature_id)
	    REFERENCES literature(literature_id)
	    ON DELETE CASCADE
);

CREATE TABLE toponym_reference (
    toponym_id BIGINT UNSIGNED NOT NULL,
    literature_id BIGINT UNSIGNED NOT NULL,
    pages VARCHAR(100) NOT NULL,
    CONSTRAINT fk_toponym_ref
        FOREIGN KEY(toponym_id)
	    REFERENCES toponym(toponym_id)
	    ON DELETE CASCADE,
    CONSTRAINT fk_literature_ref_top
        FOREIGN KEY(literature_id)
	    REFERENCES literature(literature_id)
	    ON DELETE CASCADE
);