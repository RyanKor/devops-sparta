# 1) Docker 설치 여부 확인
if ! command -v docker &> /dev/null
then
    echo "Docker not found. Installing Docker..."

    # 업데이트 및 필수 패키지 설치
    sudo apt-get update -y
    sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

    # Docker 공식 GPG 키 추가
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    # Docker 저장소 설정
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # Docker Engine 설치
    sudo apt-get update -y
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    # 현재 사용자를 docker 그룹에 추가 (필요 시)
    sudo usermod -aG docker $USER

    echo "Docker installed successfully."
else
    echo "Docker is already installed."
fi