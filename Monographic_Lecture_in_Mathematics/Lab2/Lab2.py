import numpy as np

dims = ["x", "y", "z"]
sigs = ["body_acc", "body_gyro", "total_acc"]
sets = ["test", "train"]

data = {}
for set in sets:
 set_label = []
 set_data = []
 for sig in sigs:
  for dim in dims:
   set_label.append(f"{set}-{sig}-{dim}")
   imported = np.fromfile(f"./data/{set}/Inertial Signals/{sig}_{dim}_{set}.txt")
   set_data.append(imported)
 data.update({f"{set}_data": set_data})
 data.update({f"{set}_label": set_label})

print(np.asarray(data["train_data"]).ndim)

