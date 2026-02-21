create table users (
    user_id int primary key identity(1,1),
    username nvarchar(100) not null,
    created_at datetime default getdate()
);

create table decks (
    deck_id int primary key identity(1,1),
    deck_name nvarchar(100) NOT NULL
);

create table cards (
    card_id int primary key identity(1,1),
    deck_id int not null,
    front_text nvarchar(255) not null,
    difficulty_level int,
    constraint fk_cards_deck
        foreign key (deck_id)
        references decks(deck_id),
    constraint uq_card_front_deck unique (front_text, deck_id)
);
