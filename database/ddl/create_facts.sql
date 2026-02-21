create table review_events (
    review_id int primary key identity(1,1),
    user_id int not null,
    card_id int not null,
    review_datetime datetime not null default getdate(),
    rating int not null,
    response_time_ms int not null,

    constraint fk_review_user
        foreign key (user_id)
        references users(user_id),

    constraint fk_review_card
        foreign key (card_id)
        references cards(card_id)
);
