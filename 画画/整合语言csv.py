import os
import pandas as pd

a = "/Volumes/T7/sunshinegallery/sunshinegallery-client/Assets/Gallery/Bundles/Localization.pack/"
output_file = "整合语言.csv"  # 合并后输出的文件名

csv_files = [f for f in os.listdir(a) if f.endswith(".csv")]

combined_data = pd.DataFrame()

for file in csv_files:
    file_path = os.path.join(a, file)
    df = pd.read_csv(file_path)
    combined_data = pd.concat([combined_data, df])

combined_data.to_csv(output_file, index=False, quoting=1, quotechar='"')

print("合并完成，结果已保存为 %s" % output_file)