from interface.run import run_by_text_file, run_by_json_file


for i in range(1, 4):
    if i > 1:
        print("")
    print("Output %d:" % i)
    run_by_text_file(i)


print("\n============= Read by JSON =============")
print("Output 1:")
run_by_json_file(1)
