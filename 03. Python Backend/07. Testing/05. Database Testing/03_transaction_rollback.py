# 03 — Roll back failed transactions in tests
# Run: pytest 03_transaction_rollback.py -v

import sqlite3


def transfer(conn: sqlite3.Connection, from_id: int, to_id: int, amount: int) -> None:
    conn.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, from_id))
    conn.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, to_id))


def test_rollback_on_error():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INTEGER)")
    conn.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 100), (2, 50)])
    conn.commit()

    try:
        conn.execute("BEGIN")
        transfer(conn, 1, 2, 30)
        raise RuntimeError("simulated failure")
    except RuntimeError:
        conn.rollback()

    bal = conn.execute("SELECT balance FROM accounts WHERE id = 1").fetchone()[0]
    conn.close()
    assert bal == 100
