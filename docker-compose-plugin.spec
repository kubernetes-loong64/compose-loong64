Name: docker-compose-plugin
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Docker compose plugin (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/compose-loong64
BugURL: https://github.com/kubernetes-loong64/compose-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
Docker compose plugin binary for the loong64 (LoongArch) architecture.

%prep
# This example has no source, so nothing here

%build
# Generate the script directly

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 docker-compose %{buildroot}/usr/bin/docker-compose

mkdir -p %{buildroot}/usr/libexec/docker/cli-plugins
install -m 755 docker-compose %{buildroot}/usr/libexec/docker/cli-plugins/docker-compose

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/docker-compose
/usr/libexec/docker/cli-plugins/docker-compose

%changelog
