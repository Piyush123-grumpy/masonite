"""TodoTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Todo import Todo

class TodoTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Todo.bulk_create([
            {"Message":"eat dinner"},
            {"Message":"eaa dinner"},
            {"Message":"dont eat dinner"},

        ]
            

            
        )
