#파이토치(PyTorch)는 파이썬 기반의 오픈 소스 딥러닝 프레임워크로, 직관적인 문법과 GPU 가속 연산을 통해 신경망 모델의 연구·학습·배포를 지원합니다. 
# 원래 메타(구 페이스북) AI 연구팀에서 개발했으며, 현재는 파이토치 재단 및 리눅스 재단의 지원 아래 운영되고 있습니다.

# 핵심 특징

# • 동적 계산 그래프: 코드를 실행하는 시점에 계산 그래프를 동적으로 생성하여 디버깅과 모델 구조 변경이 쉽습니다.
# • 직관적인 파이썬 스타일: NumPy와 유사한 텐서(Tensor) 연산을 제공하며 파이썬 네이티브 방식으로 작성할 수 있습니다.
# • 하드웨어 가속 및 분산 학습: NVIDIA CUDA, TPU 등 GPU/가속기 연산과 대규모 분산 학습(torch.distributed)을 지원합니다.
# • 최신 버전 및 생태계: 2026년 10월 기준 2.15.0 버전이 공개되었으며(Python 3.10 이상 권장), torchvision, torchaudio, torchdata, torchtune, torchao, torchtitan 등 분야별 확장 라이브러리를 갖추고 있습니다

# 모듈 설치 
# python -m pip install torch torchvision torchaudio
# pip install tensorflow 참고

# Tensor -> Numpy 차이 : 형변환 -> Tensor 값 변경 -> in-place 연산 -> 난수 흐름

import torch
import numpy as np

print(torch.__version__) # 2.14.1 + cpu
print('GPU 사용 가능 여부 :', torch.cuda.is_available())
print('GPU 장치 정보 :', torch.cuda.get_device_name(0) if torch.cuda.is_available() else[])
# pytorch는 기본적으로 Eager Execution(즉시 실행) 방식으로 동작

print('\nTensor : pytorch에서 데이터를 담는 기본 자료구조 (숫자 데이터 저장용 다차원 배열)')
# ndarray와 유사하나 pytorch연산에 사용되도록 만들어진 객체 (딥러닝 연산, GPU연산, 자동미분...)
print(12, type(12)) # <class 'int'> 파이썬 상수, 파이썬이 직접 계산
print(torch.tensor([12]))
# tensor(12) <class 'torch.Tensor'> 0d 텐서 (scaler)
print(torch.tensor([[12]])) # tensor([12]) 1d 텐서 (vector)
print(torch.tensor([[[12]]])) # tensor([[12]]) 2d 텐서 (matrix)
print(torch.tensor([[[12, 1]]])) # tensor([[12, 1]]) 

print('\nTensor 속성확인 (텐서의 차원수 확인)')
print(torch.tensor([[12, 1]]).dim()) # 2
print(torch.tensor([[12, 1]]).ndim)
t = torch.tensor([[1,2,3],[4,5,6]], dtype= torch.float32)
print('shape :', t.shape)  # shape : torch.Size([2, 3])
print('dtype :', t.dtype)  # dtype : torch.int16 -> torch.float32

print()
imsi = np.array([1, 2])
print(imsi, type(imsi))  #  <class 'numpy.ndarray'>
imsi[0] = 10
print(imsi)

# PyTorch Tensor
a = torch.tensor([1, 2])
print(type(a)) # <class 'torch.Tensor'>
a[0] = 10
print(a) # tensor([10.,  2.])

print()
a = torch.tensor([1, 2])
b = torch.tensor([3, 4])
c = a + b   # 텐서 요소 더하기
print(c)
d = torch.tensor([3])
e = c + d   # Broadcast 연산도 가능
print(e)

print('\npython, numpy, pytorch 간 형변환 가능')
print(7)
print(torch.tensor(7)) # 상수 -> 텐서(스칼라)
print(torch.tensor(7).item()) # 텐서(스칼라) -> 상수
print(torch.tensor([1, 2]).numpy()) # 텐서 -> numpy

arr = np.array([1, 2])
torch_arr = torch.tensor(arr)
print(torch_arr)                # tensor([1, 2])
print(torch.from_numpy(arr))    # tensor([1, 2])

print('사칙 연산 가능')
# torch.add()  .subtract()  .multiply()   .divide()
torch_result = torch.add(torch_arr, 5)
print(torch_result)

np_result = np.add(torch_result.numpy(),2)
print(np_result) # [8,9]

print()
v1 = torch.tensor(1.0)
print('변경 전 v1 :', v1, id(v1))   # tensor(1.) 2046792579280
v1.fill_(100)   # 기존 참조값 갱신  copy_(), add_(), sub_(), mul_(), div_() : in_place 연산
print('변경 후 v1 :', v1, id(v1))   # tensor(100.) 2046792579280
v1 = 100        # 새로운 객체를 참조
print('변경 후 v1 :', v1, id(v1))   # 100 140720193466584

print()
v1 = torch.tensor(1.0)
print(v1.data_ptr()) # 실제 data 저장위치 출력
v1.copy_(torch.tensor(123.0))
print(v1.data_ptr()) 
print('v1: ', v1)

v2 = torch.ones((2,))
print('v2 :', v2)
print(v2.data_ptr())
v2.copy_(torch.tensor([30.0, 40.0]))
print('v2 :', v2)
print(v2.data_ptr())

print()
aa = torch.zeros((2, 1))
print('aa :', aa)
aa.copy_(torch.ones((2, 1)))
print('aa :', aa)
aa.add_(torch.tensor([[2.0],[3.0]]))
print('aa :', aa)
# sub_() , mul_(), div() 도 동일

print('난수 처리 ----')
torch.manual_seed(42)  # 고정 난수 재현
print(torch.rand(1))

# 균등 분포
print(torch.empty(2).uniform_(0,1))
print(torch.empty(30000).uniform_(0,1).mean())

# 정규 분포
print(torch.normal(mean=0.0, std=1.0, size=[3]))
# print(torch.normal(mean=0.0, std=1.0, size=[30000]).mean())

print()
# GPU 텐서와 numpy 배열에서 알아둘 점
# Pytorch GPU 텐서는 GPU 연산과 자동 미분(Autograd)을 지원하지만 ,
# numpy계열은 cpu연산만 지원 하므로 장치간 메모리 공유동작에 주의
if torch.cuda.is_available():
    gpu_tensor = torch.tensor([1,2,3], device='cuda') # gpu에서 텐서 생성
    np_from_gpu = gpu_tensor.cpu().numpy() # GPU 텐서를 cpu로 이동후 numpy 배열로 변화
    print(f'gpu 텐서 -> 넘파이 배열로 변환 : {np_from_gpu}')
else:
    print('cuda 지원 안함')
