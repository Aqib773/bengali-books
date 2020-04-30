for idx, file in enumerate(glob(output_path + "/*.jpg"), start=1):
    new_file = output_path + f"/{idx}.jpg"
    os.rename(file, new_file)