import numpy as np
import math

calib = np.load('calib.npy', allow_pickle=True)
calib = np.load('/mnt_2/Results_CRF/newcrfs_MS2_newcrf_smooth_2023_08_02_23_38_16/sync_data/_2021-08-06-11-23-45/calib.npy', allow_pickle=True)

# for k, v in calib.item().items():
#     if 'nir2rgb' in k or 'nir2thr' in k or 'rgbL' in k:
#         print(f'{k}:\n {v}')

for k, v in calib.item().items():
    
    print(f'{k}:\n {v}')

def isRotationMatrix(R) :
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype = R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6
 
# Calculates rotation matrix to euler angles
# The result is the same as MATLAB except the order
# of the euler angles ( x and z are swapped ).
def rotationMatrixToEulerAngles(R) :
 
    assert(isRotationMatrix(R))
 
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
 
    singular = sy < 1e-6
 
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
 
    return np.array([x, y, z])

def eulerAnglesToRotationMatrix(theta) :
 
    R_x = np.array([[1,         0,                  0                   ],
                    [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                    [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                    ])
 
    R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                    [0,                     1,      0                   ],
                    [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                    ])
 
    R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                    [math.sin(theta[2]),    math.cos(theta[2]),     0],
                    [0,                     0,                      1]
                    ])
 
    R = np.dot(R_z, np.dot( R_y, R_x ))
 
    return R

R_nir2rgb = calib.item()['R_nir2rgb']
R_rgb2nir = np.linalg.inv(R_nir2rgb)
T_nir2rgb = calib.item()['T_nir2rgb']

extrinsic = np.zeros((4,4))
extrinsic[:3,:3] = R_nir2rgb
extrinsic[:3, [3]] = T_nir2rgb
extrinsic[3,3] =1
print(extrinsic)
print(np.matmul(extrinsic, np.linalg.inv(extrinsic)))
error_1 = np.linalg.norm(np.identity(4, dtype=extrinsic.dtype) - extrinsic@np.linalg.inv(extrinsic))

extrinsic_h = np.zeros((4,4))
extrinsic_h[:3,:3] = R_nir2rgb.T
extrinsic_h[:3, [3]] = -R_nir2rgb.T@T_nir2rgb
extrinsic_h[3,3] =1

print(np.matmul(extrinsic, extrinsic_h))
error_2 = np.linalg.norm(np.identity(4, dtype=extrinsic.dtype) - extrinsic@extrinsic_h)
print(error_1, error_2)


angles = rotationMatrixToEulerAngles(R_nir2rgb)
R_rgb2nir = eulerAnglesToRotationMatrix(-angles)
print(np.matmul(R_nir2rgb, R_rgb2nir))