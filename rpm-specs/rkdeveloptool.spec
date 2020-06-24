Name:          rkdeveloptool
Version:       1.3
Release:       3%{?dist}
Summary:       A simple way to read/write Rock Chips rockusb devices
License:       GPLv2
URL:           http://opensource.rock-chips.com/wiki_Rkdeveloptool
# Upstream doesn't currently push the release tags, upstream issue filed
# https://github.com/rockchip-linux/rkdeveloptool/issues/36
# git archive --format=tar --prefix=%{name}-%{version}/ 081d237ad5bf | xz > ~/%{name}-%{version}.tar.xz
Source0:       %{name}-%{version}.tar.xz
# Source0:       https://github.com/rockchip-linux/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://build.opensuse.org/package/view_file/hardware/rkdeveloptool/99-rkdeveloptool.rules
Source1:       99-rkdeveloptool.rules
Patch0:        rkdeveloptool-gcc-fixes.patch

BuildRequires: autoconf automake
BuildRequires: gcc-c++
BuildRequires: libusbx-devel
BuildRequires: systemd-devel

%description
A simple way to read/write rockusb devices for flashing firmware to Rock Chips
SoC based devices such as those based on the rk3399/3368/3328/3288 etc.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 autoreconf -vif
%configure

%make_build

%install
%make_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-rkdeveloptool.rules

%files
%license license.txt
%doc Readme.txt
%{_bindir}/rkdeveloptool
%{_udevrulesdir}/99-rkdeveloptool.rules

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-2
- Add udev rules for device detection

* Fri Jun 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-1
- Initial package
