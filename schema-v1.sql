CREATE TABLE spellings (
	id integer,
	spelling text
);

CREATE TABLE forms (
	spelling_id integer,
	id integer,
	spelling text
);

CREATE TABLE lemmas (
	id integer,
	pronunciation_id integer,
	native_definition text,
	language_id integer,
	spelling_id integer,
	rank integer,
	part_of_speech_id integer
);

CREATE TABLE languages (
	id integer,
	name text
);

CREATE TABLE word_lists (
	id integer,
	name text,
	weight float
);

CREATE TABLE word_list_entry (
	id integer,
	frequency float,
	lemma_id integer,
	word_list_id integer
);

CREATE TABLE pronunciation (
	id integer,
	transcription text
);

CREATE TABLE parts_of_speech (
	id integer,
	name text
);

CREATE TABLE contexts (
	id integer,
	text text
);

CREATE TABLE lemma_to_context (
	id integer,
	context_id integer,
	lemma_id integer
);

CREATE TABLE translations (
	id integer,
	lemma_id integer,
	language_id integer
);

CREATE TABLE lemma_to_synonyms (
	id integer,
	lemma_id integer,
	synonym_id integer
);

CREATE TABLE form_list_entry (
	id integer,
	form_id integer,
	forms_list_id integer
);

CREATE TABLE forms_list (
	id integer,
	name text,
	weight float
);

