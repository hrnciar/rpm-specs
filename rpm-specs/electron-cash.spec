Name:           electron-cash
Version:        4.0.15
Release:        1%{?dist}
Summary:        A lightweight Bitcoin Cash client

License:        MIT
URL:            https://electroncash.org/
Source0:        https://github.com/Electron-Cash/Electron-Cash/releases/download/%{version}/Electron-Cash-%{version}.tar.gz
Source1:        https://github.com/Electron-Cash/keys-n-hashes/raw/master/sigs-and-sums/%{version}/win-linux/Electron-Cash-%{version}.tar.gz.asc
#Sun 15 Dec 2019, exported the upstream gpg key using the command:
#gpg2 --armor --export --export-options export-minimal D56C110F4555F371AEEFCB254FD06489EFF1DDE1 D465135F97D0047E18E99DC321810A542031C02C > gpgkey-electron-cash.gpg
Source2:        gpgkey-electron-cash.gpg

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

BuildRequires:  libappstream-glib
BuildRequires:  gnupg2

Requires:       qt5-qtbase
Requires:       qt5-qtsvg
Requires:       qt5-qtmultimedia
Requires:       python3-qt5

Requires:       python3-pycryptodomex
Requires:       libsecp256k1 >= 0.20.9
Requires:       zbar
Requires:       tor

Provides:       bundled(google-noto-emoji-color-fonts)

Suggests:       python3-trezor >= 0.11.2

Conflicts:      python3-trezor < 0.11.2

%description
Electron Cash is an easy to use Bitcoin Cash client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin block chain.

%prep
%gpgverify -k 2 -s 1 -d 0
%setup -q -n Electron-Cash-%{version}

#pre-built bundled library
rm -v ./lib/*.so*

#pre-built tor binary
rm -v ./lib/tor/bin/tor

#budled libraries
rm -rfv ./packages/

#qdarkstyle is an optional dependency that is not yet packed for Fedora
sed -i '/^qdarkstyle*/d' ./contrib/requirements/requirements.txt

%build
pyrcc5 icons.qrc -o gui/qt/icons_rc.py
%{py3_build}

%install
%{py3_install}

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.electroncash.ElectronCash.appdata.xml

%files
%doc AUTHORS
%doc README.rst
%doc RELEASE-NOTES
%license LICENCE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.electroncash.ElectronCash.appdata.xml
%{python3_sitelib}/electroncash*
%{python3_sitelib}/Electron_Cash-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jun 03 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.15-1
- Updated to version 4.0.15

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.14-3
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.14-2
- Remove protobuf <3.9 constraint

* Wed Mar 25 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.14-1
- Updated to version 4.0.14

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.12-2
- Require a newer version of libsecp256k1

* Sat Dec 14 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.12-1
- Updated to version 4.0.12

* Tue Nov 19 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.11-1
- Updated to version 4.0.11

* Mon Sep 09 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.10-1
- Updated to version 4.0.10

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.9-3
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.9-2
- Remove locked version for python-dateutil

* Mon Aug 12 2019 Jonny Heggheim <hegjon@gmail.com>
- Updated to version 4.0.9

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.8-1
- Updated to version 4.0.8

* Tue Jun 25 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.7-3
- Added missing dependency on python3-qt5

* Mon Jun 24 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.7-2
- Added missing dependencies

* Fri Jun 21 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.7-1
- Updated to version 4.0.7

* Thu Jun 06 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.6-1
- Updated to version 4.0.6

* Mon May 27 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.5-1
- Updated to version 4.0.5

* Mon May 27 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.4-1
- Updated to version 4.0.4

* Wed May 22 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.3-1
- Updated to version 4.0.3

* Sat Apr 20 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.2-1
- Updated to version 4.0.2

* Thu Apr 04 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.1-1
- Updated to version 4.0.1

* Tue Apr 02 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.0-2
- Added dependency on libsecp256k1 because of CashShuffle

* Sat Mar 30 2019 Jonny Heggheim <hegjon@gmail.com> - 4.0.0-1
- Updated to version 4.0.0

* Mon Feb 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.6-2
- Disabled optional requires qdarkstyle that is not packed for Fedora

* Sun Feb 24 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.6-1
- Updated to version 3.3.6

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.5-3
- Add python3-pycryptodomex as requires

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.5-2
- Bumped the version requires for python3-trezor

* Fri Jan 25 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.5-1
- Updated to version 3.3.5

* Sat Dec 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.4-2
- Enable python dependency generator

* Sat Dec 29 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.4-1
- Updated to version 3.3.4

* Wed Nov 14 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.2-1
- Updated to version 3.3.2

* Sat Jul 21 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.1-1
- Updated to version 3.3.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3-1
- Updated to version 3.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2-2
- Rebuilt for Python 3.7

* Wed Apr 25 2018 Jonny Heggheim <hegjon@gmail.com> - 3.2-1
- Updated to version 3.2

* Tue Mar 20 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.6-2
- Added conflicts on older trezor since it does not work with newer version of
  electron-cash

* Sat Mar 17 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.6-1
- Updated to version 3.1.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.2-1
- Updated to version 3.1.2

* Sun Jan 07 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.1-1
- Updated to version 3.1.1

* Fri Jan 05 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1-1
- Updated to version 3.1

* Fri Dec 15 2017 Jonny Heggheim <hegjon@gmail.com> - 3.0-1
- Inital version
