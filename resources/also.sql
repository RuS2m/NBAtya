CREATE OR REPLACE FUNCTION DeleteAllMessages()
    AS $$ DELETE * FROM messages WHERE 1=1 $$
    LANGUAGE SQL;

CREATE OR REPLACE FUNCTION DeleteAllInvisibleMessages()
    AS $$ DELETE * FROM messages WHERE is_available=FALSE $$
    LANGUAGE SQL;