
from ..classes.structure import Structure
from ..config import db_con as db
import psycopg2

class StructureService:
    @staticmethod
    def add( s: Structure ) -> Structure:
        
        q = "insert into structure (moon_id, moon_name, structure_id, structure_name, chunk_arrival_time, natural_decay_timer, extraction_start_time) values (%s,%s,%s,%s,%s,%s,%s) returning structure_id;"
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, [s.moon_id, s.moon_name, s.structure_id, s.structure_name, s.chunck_arrival_time, s.natural_decay_time, s.extraction_start_time])
            structure_id = cur.fetchrow()["structure_id"]
            db.commit()
        except:# psycopg2.Error as e:
            db.rollback()
        # except psycopg2.Warning as e:
        #     db.rollback()
        return StructureService.get(structure_id)

    @staticmethod
    def remove( s: Structure ):
        deleted_item = StructureService.get(s.structure_id)
        q = "delete from structure where structure_id = %s"
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, [s.structure_id])
            db.commit()
        except:
            db.rollback()
        return deleted_item

    @staticmethod
    def update( s: Structure ):
        q = """update structure set 
            structure_name=%(structure_name)s and 
            moon_id=%(moon_id)s and 
            moon_name=%(moon_name)s and 
            chunk_arrival_time=%(chunk_arrival_time)s and 
            natural_decay_timer=%(natural_decay_timer)s and 
            extraction_start_time=%(extraction_start_time)s
            where structure_id=%(structure_id)s 
            on conflict do nothing;"""
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, s.to_json())
            db.commit()
        except:
            db.rollback()
        return StructureService.get(s.structure_id)

    @staticmethod
    def get(structure_id:int)-> Structure:
        q = "select * from structure where structure_id=%s limit 1;"
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            cur.execute(q, [structure_id])
        except:
            return None
        if cur.rowcount == 0:
            return None
        data = cur.fetchrow()
        return Structure.from_json(data)