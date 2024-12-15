#!/usr/bin/env python3
import argparse
import asyncio

from auth.user import create_superuser

from database.connection import db


async def _connect_and_create_superuser(
    username: str, email: str, password: str
):
    await db.connect()
    await create_superuser(username, email, password)
    await db.disconnect()


def main():
    parser = argparse.ArgumentParser(description="Creates a Superuser")
    parser.add_argument(
        '-u',
        '--username',
        help="Username",
        type=str,
        required=True,
        dest="username"
    )
    parser.add_argument(
        '-e', '--email', help="Email", type=str, required=True, dest="email"
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
        _connect_and_create_superuser(args.username, args.email, args.password)
    )


if __name__ == '__main__':
    main()
