def save_to_file(file_name, contents):
    stf = open(file_name, "a+")
    stf.write(contents + "\n")
    stf.close()


def save_to_json(file_name, id, content):
    with open(file_name, "a+", encoding="utf-8") as f:
        if f.read() == "":
            data = {}
        else:
            data = json.load(f)
        data["user_id"] = id
        data["user_con"] = content
        # f.write(data + "\n")
        json.dump(data, f, indent=6)
        f.close()