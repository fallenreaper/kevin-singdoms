
from ..classes.user import User
from ..config import db_con as db
import psycopg2

class UserService:
    @staticmethod
    def add( u: User) -> User:
        q = """insert into eve_user
        (character_id, character_name, discord_user_id, access_token, refresh_token, date_created, last_updated, token_expires)
        values 
        (%(character_id)s, %(character_name)s, %(discord_user_id)s, %(access_token)s, %(refresh_token)s, %(date_created)s, %(last_updated)s, %(token_expires)s, )
        on conflict do nothing
        returning character_id;
        """
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, u.to_json())
            db.commit()
        except:
            db.rollback()
            return None
        if cur.rowcount == 0:
            return None
        return UserService.get(cur.fetchrow()["character_id"])

    @staticmethod
    def remove( u: User) -> User:
        u = UserService.get(u.character_id)
        q = "delete from eve_user where character_id = %s;"
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, [u.character_id])
            db.commit()
        except:
            db.rollback()
            return None
        return u

    @staticmethod
    def update( u: User) -> User:
        q = """update eve_user set
        character_name=%(character_name)s and 
        discord_user_id=%(discord_user_id)s and
        access_token=%(access_token)s and
        refresh_token=%(refresh_token)s and 
        date_created=%(date_created)s and 
        last_updated=%(last_updated)s and 
        token_expires=%(token_expires)s
        character_id=%(character_id)s and 
        character_name=%(character_name)s
        where character_id=%(character_id)s
        on conflict do nothing;
        """
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, u.to_json())
            db.commit()
        except:
            db.rollback()
        return UserService.get(u.character_id)

    @staticmethod
    def get( character_id: int) -> User:
        q = "select * from eve_user where character_id=%s"
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, [character_id])
        except:
            return None
        if cur.rowcount == 0:
            return None
        data = cur.fetchrow()
        return User.from_json(data)


