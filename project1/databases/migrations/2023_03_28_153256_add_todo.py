"""AddTodo Migration."""

from masoniteorm.migrations import Migration


class AddTodo(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("todos") as table:
            table.string("Message2").nullable()


    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("todos") as table:
            pass
