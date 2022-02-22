create table if not exists pm4py.log
(
    eventID varchar(255) null,
    user    varchar(255) null,
    time    varchar(255) null,
    action  varchar(255) null,
    name    varchar(255) null
);

create index log_name_index
    on pm4py.log (name);

create index log_user_index
    on pm4py.log (user);

