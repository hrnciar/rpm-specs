%global srcname trezor

%global bashcompdir  %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot %(dirname %{bashcompdir} 2>/dev/null)

Name:           python-%{srcname}
Version:        0.12.0
Release:        1%{?dist}
Summary:        Python library for communicating with TREZOR Hardware Wallet

License:        LGPLv3
URL:            https://github.com/trezor/python-trezor
Source0:        %{pypi_source}
Source1:        51-trezor.rules
BuildArch:      noarch

BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  systemd
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:       %{py3_dist hidapi} >= 0.7.99.post20
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.


%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

install -Dpm 644 bash_completion.d/trezorctl.sh %{buildroot}%{bashcompdir}/trezorctl
install -Dpm 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/51-trezor.rules


%check
#Missing dependency libusb1, rlp and pyblake2
#%{__python3} setup.py test


%files -n python3-%{srcname}
%doc AUTHORS
%doc CHANGELOG.md
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/trezorlib/
%{_bindir}/trezorctl
%{bashcomproot}
%{_udevrulesdir}/51-trezor.rules

%changelog
* Thu Jun 04 2020 Jonny Heggheim <hegjon@gmail.com> - 0.12.0-1
- Updated to version 0.12.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.5-1
- Updated to version 0.11.5

* Mon Sep 23 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.4-3
- Use hashlib instead of pyblake2

* Fri Sep 20 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.4-2
- Disable dependency for python3-construct for Fedora 30 and lower.

* Mon Sep 09 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.4-1
- Updated to version 0.11.4

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.2-2
- Added missing requires on python3-construct

* Tue Apr 02 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.2-1
- Updated to version 0.11.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 0.11.1-1
- Updated to version 0.11.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Jonny Heggheim <hegjon@gmail.com> - 0.10.2-1
- Updated to version 0.10.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Jonny Heggheim <hegjon@gmail.com> - 0.9.1-2
- Added missing requires on python3-libusb1

* Tue Mar 06 2018 Jonny Heggheim <hegjon@gmail.com> - 0.9.1-1
- Updated to version 0.9.1
- Removed Python2 subpackage since Python2 is not longer supported upstream
- Dropped patches for protobuf2
- License is only LGPLv3, since bundled file with BSD license is replaced

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.16-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Jan Beran <jberan@redhat.com> - 0.7.16-4
- Python 3 subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.16-2
- Added patches for Fedora 25 to work with protobuffer2

* Thu Jul 06 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.16-1
- new version

* Mon Jun 19 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.15-3
- Added missing python2-requests requires

* Mon Jun 19 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.15-2
- Included correct requires for python2-trezor

* Mon Jun 19 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.15-1
- new version

* Wed May 03 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.13-1
- new version

* Tue Apr 11 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.12-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Jonny Heggheim <hegjon@gmail.com> - 0.7.8-2
- Include udev-rules

* Sun Nov 27 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.8-1
- new version

* Fri Nov 25 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.7-2
- added bundled(python-protobuf-json)
- included BSD in the license

* Thu Nov 24 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.7-1
- new version

* Thu Nov 17 2016 Jonny Heggheim <hegjon@gmail.com> - 0.7.6-1
- initial package
