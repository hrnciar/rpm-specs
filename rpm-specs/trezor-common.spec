%global commit0 654ee5d8ec575331b6be15343617a8fcfdd66cdd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%if 0%{?fedora} >= 26
%global protobuf2 0
%else
%global protobuf2 1
%endif

Name:    trezor-common
Version: 0
Release: 0.8%{?dist}
Summary: udev rules and protobuf messages for the hardware wallet TREZOR

License:       LGPLv3+
URL:           https://github.com/trezor/%{name}
Source0:       https://github.com/trezor/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildArch:     noarch
BuildRequires: systemd
Conflicts:     python-trezor <= 0.7.16-1

%description
Provides udev rules and protobuf messages for all the hardware wallets from
TREZOR.

%prep
%autosetup -n %{name}-%{commit0}

#option "deprecated" is unknown in protobuf2
%if %{protobuf2}
sed -i 's/, deprecated = true//g' protob/messages.proto
%endif

%build
#Nothing to build

%install
install -Dpm 644 udev/51-trezor.rules %{buildroot}%{_udevrulesdir}/51-trezor.rules

for file in $(find ./protob -name \*.proto); do
  install -Dpm 644 $file %{buildroot}%{_datadir}/trezor/$file
done

%files
%doc README.md
%license COPYING
%{_udevrulesdir}/51-trezor.rules
%{_datadir}/trezor

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Jonny Heggheim <hegjon@gmail.com> - 0-0.1
- initial package
