import os
import UnityPy
import shutil

def clean_dir(folder: str):
    if os.path.exists(folder):
        shutil.rmtree(folder, True)
    os.makedirs(folder)

def unpack_all_assets(source_folder: str, destination_folder: str):
    clean_dir(destination_folder)
    # iterate over all files in source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            name, ext = os.path.splitext(file_name)
            if ext != ".bundle":
                continue
            # generate file_path
            file_path = os.path.join(root, file_name)
            # load that file via UnityPy.load
            env = UnityPy.load(file_path)
            tmp_folder = os.path.join(destination_folder, name)
            clean_dir(tmp_folder)

            # iterate over internal objects
            for obj in env.objects:
                # process specific object types
                if obj.type.name in ["Texture2D"]:
                    # parse the object data
                    data = obj.read()

                    # create destination path
                    dest = os.path.join(tmp_folder, data.name)

                    # make sure that the extension is correct
                    # you probably only want to do so with images/textures
                    dest, ext = os.path.splitext(dest)
                    dest = dest + ".png"

                    try:
                        img = data.image
                        img.save(dest)
                    except:
                        print("error: " + dest)

            # alternative way which keeps the original path
            # for path, obj in env.container.items():
            #     if obj.type.name in ["Texture2D", "Sprite"]:
            #         data = obj.read()
            #         # create dest based on original path
            #         dest = os.path.join(tmp_folder, *path.split("/"))
            #         # make sure that the dir of that path exists
            #         os.makedirs(os.path.dirname(dest), exist_ok=True)
            #         # correct extension
            #         dest, ext = os.path.splitext(dest)
            #         dest = dest + ".png"
            #         try:
            #             data.image.save(dest)
            #         except:
            #             print("error2: " + dest)

    print('success')

unpack_all_assets(
    "/Volumes/T7/makerstory/makerstory-client/Build/Android/Bundles/aa/Android/",
    "/Users/mac/Downloads/UnityAssets/aa",
)

# unpack_all_assets(
#     "/Volumes/T7/makerstory/makerstory-client/Build/Android/Bundles/",
#     "/Users/mac/Downloads/UnityAssets/",
# )