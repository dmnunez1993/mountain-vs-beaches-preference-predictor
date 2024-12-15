#!/usr/bin/env python3
import argparse
import asyncio

from auth.user import authenticate

from database.connection import db


async def _connect_and_authenticate(username: str, password: str):
    await db.connect()
    user = await authenticate(username, password)
    print(user)
    await db.disconnect()


def main():
    parser = argparse.ArgumentParser(description="Authenticates a user")
    parser.add_argument(
        '-u',
        '--username',
        help="Username",
        type=str,
        required=True,
        dest="username"
    )
    parser.add_argument(
        '-p',
        '--password',
        help="Password",
        type=str,
        required=True,
        dest="password"
    )

    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        _connect_and_authenticate(args.username, args.password)
    )


if __name__ == '__main__':
    main()
