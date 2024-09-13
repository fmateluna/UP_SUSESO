CREATE TABLE IF NOT EXISTS registro_licencias_medicas (
    id SERIAL PRIMARY KEY,
    nombre_archivo TEXT,
    contenido_archivo BYTEA
);