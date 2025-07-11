import streamlit as st
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 🌟 앱 제목
st.title("🌌 별빛의 색으로 온도 재기")

# 👋 소개
st.markdown("""
이 앱은 천문학에서 사용되는 **FITS 이미지**를 활용하여 별빛의 색을 분석하고, 별의 온도를 계산하는 앱입니다.  
또한, 이러한 분석이 **CCD 센서**와 **반도체 기술**과 어떻게 연결되는지 설명합니다.
""")

# 🔍 FITS 파일 업로드
uploaded_file = st.file_uploader("FITS 이미지 업로드", type=["fits"])

if uploaded_file is not None:
    # FITS 파일 열기
    with fits.open(uploaded_file) as hdul:
        data = hdul[0].data

    # 데이터 전처리 (Normalize)
    data = np.nan_to_num(data)
    data = np.clip(data, 0, np.percentile(data, 99))
    
    # 이미지 표시
    st.subheader("FITS 이미지 (Normalized)")
    plt.imshow(data, cmap='gray')
    plt.axis('off')
    st.pyplot(plt)

    # 평균 밝기 계산 (전체 평균)
    mean_brightness = np.mean(data)
    st.write(f"🌟 평균 밝기 값: {mean_brightness:.2f}")

    # 🔥 Wien's 법칙 적용 (λ_peak * T = 2.898 × 10⁻³ m·K)
    # 여기선 밝기 값으로 λ_peak을 대략 추정 (가상의 값)
    # 실제로는 스펙트럼 데이터가 필요하지만 교육용으로 간단화
    # 가상의 파장값으로 환산
    pseudo_lambda_peak = 500e-9 * (1 / (mean_brightness + 1e-6))  # 단순한 시뮬레이션
    T = 2.898e-3 / pseudo_lambda_peak
    st.write(f"🌡️ 계산된 별의 온도 (가상 시뮬레이션): {T:.2f} K")

    # 📚 반도체 기술 설명
    st.subheader("🔍 CCD 센서와 반도체 기술 설명")
    st.markdown("""
- 업로드한 FITS 이미지는 **CCD 센서**(Charge-Coupled Device)를 이용하여 얻은 데이터입니다.
- **CCD 센서의 원리**:
    - 빛이 반도체에 닿으면 **광전효과**에 의해 전자-정공쌍이 생성됩니다.
    - 생성된 전하를 픽셀별로 저장하고 이동시켜서 디지털 신호로 변환합니다.
- 이는 **반도체 공정 기술**과 직접 관련 있으며,  
  당신이 관심 있는 **광센서, 이미지 센서**의 기초 기술과 연결됩니다.
""")

else:
    st.info("먼저 FITS 이미지를 업로드해주세요!")
