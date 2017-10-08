import moxel

model = moxel.Model('moxel/ci-sum-array:latest', where='localhost')
result = model.predict(data=[[1,2]])
print(result)
