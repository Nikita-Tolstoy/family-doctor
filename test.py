from uuid import UUID

from db_models import File, sqlite_db


# id = File.create(f_name="Новый файл 1").id
# print(d)
# d.sa
# fd = File.get_name("a7a78bb9-6dc2-4713-bcbf-fe21948f52f5")
# fd = File.select(File.f_name, File.id).where(File.id == '3fb45c19-bbd5-4673-943a-9a9db87374ba')
# print(fd[0].f_name)

# print(File.get_name('3fb45c19-bbd5-4673-943a-9a9db87374ba'))
# for user in fd:
#     print(user.id)

from uuid import uuid4
def new_id(*name_file):
    f = File.add_file(*name_file)

    return str(f.id)

for i in range(5):
    print(new_id("qwdqdqwdqwddqw"))