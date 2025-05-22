CREATE TABLE auctions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL,
    owner_id UUID NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    initial_price INTEGER NOT NULL,
    current_price INTEGER,

    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(productid),
    CONSTRAINT fk_owner FOREIGN KEY (owner_id) REFERENCES users("UserId")
);

CREATE TABLE auction_bids (
    id UUID PRIMARY KEY NOT NULL,
    auction_id UUID NOT NULL,
    user_id UUID NOT NULL,
    bid_amount INTEGER,

    CONSTRAINT fk_auction FOREIGN KEY (auction_id) REFERENCES auctions(id),
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users("UserId")
);


SELECT * FROM auctions
SELECT * FROM auction_bids
