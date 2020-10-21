Name:           electrum
Version:        4.0.2
Release:        2%{?dist}
Summary:        A lightweight Bitcoin Client

License:        MIT
URL:            https://electrum.org/
Source0:        https://download.electrum.org/%{version}/Electrum-%{version}.tar.gz
Source1:        https://download.electrum.org/%{version}/Electrum-%{version}.tar.gz.asc
#Wed Feb 01 2017, exported the upstream gpg key using the command:
#gpg2 --export --export-options export-minimal 6694D8DE7BE8EE5631BED9502BD5824B7F9470E6 > gpgkey-electrum.gpg
Source2:        gpgkey-electrum.gpg
Source3:        electrum.appdata.xml

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

BuildRequires:  libappstream-glib
BuildRequires:  gnupg2

Requires:       python%{python3_version}dist(pyqt5)

Requires:       zbar
Suggests:       python3-trezor >= 0.11.2
Suggests:       python3-btchip

Conflicts:      python3-trezor < 0.11.2

%description
Electrum is an easy to use Bitcoin client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin block chain.

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q -n Electrum-%{version}
rm -rf Electrum.egg-info
rm -rf packages

#qdarkstyle is an optional dependency that is not yet packed for Fedora
sed -i '/^qdarkstyle*/d' ./contrib/requirements/requirements.txt

%build
%{py3_build}

%install
%{py3_install}
install -Dpm 644 %{SOURCE3} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# Remove shebang lines from .py files that aren't executable, and
# remove executability from .py files that don't have a shebang line:
# Source: dmalcolm.fedorapeople.org/python3.spec
find %{buildroot} -name \*.py \
  \( \( \! -perm /u+x,g+x,o+x -exec sed -e '/^#!/Q 0' -e 'Q 1' {} \; \
  -print -exec sed -i '1d' {} \; \) -o \( \
  -perm /u+x,g+x,o+x ! -exec grep -m 1 -q '^#!' {} \; \
  -exec chmod a-x {} \; \) \)

# Install Desktop file, fix categories
desktop-file-install                                    \
--remove-category="Network"                             \
--add-category="Office"                                 \
--add-category="Finance"                                \
--delete-original                                       \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS
%doc README.rst
%doc RELEASE-NOTES
%doc PKG-INFO
%license LICENCE
%{_bindir}/electrum
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{python3_sitelib}/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Jonny Heggheim <hegjon@gmail.com> - 4.0.2-1
- Updated to version 4.0.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.4-2
- Allow usage of aiorpcx-0.12

* Wed Apr 03 2019 Jonny Heggheim <hegjon@gmail.com> - 3.3.4-1
- Updated to version 3.3.4

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Jonny Heggheim <hegjon@gmail.com> - 3.2.4-2
- Deactiated requires for typing and qdarkstyle

* Tue Jan 01 2019 Jonny Heggheim <hegjon@gmail.com> - 3.2.4-1
- Downgraded to version 3.2.4. Fedora lacks dependencies for 3.3.2

* Sun Dec 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2-3
- Fix typo in pyqt5 requires

* Sun Dec 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2-2
- Enable python dependency generator

* Sat Dec 29 2018 Jonny Heggheim <hegjon@gmail.com> - 3.3.2-1
- Updated to version 3.3.2

* Sun Sep 16 2018 Jonny Heggheim <hegjon@gmail.com> - 3.2.3-1
- Updated to version 3.2.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Jonny Heggheim <hegjon@gmail.com> - 3.2.2-1
- Updated to version 3.2.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.3-2
- Rebuilt for Python 3.7

* Fri Apr 20 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.3-1
- Updated to version 3.1.3

* Mon Mar 26 2018 Jonny Heggheim <hegjon@gmail.com> - 3.1.1-1
- Updated to version 3.1.1

* Mon Feb 19 2018 Jonny Heggheim <hegjon@gmail.com> - 3.0.6-1
- Updated to version 3.0.6

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Jonny Heggheim <hegjon@gmail.com> - 3.0.5-1
- Updated to version 3.0.5

* Sun Jan 07 2018 Jonny Heggheim <hegjon@gmail.com> - 3.0.4-1
- Updated to version 3.0.4

* Thu Dec 14 2017 Jonny Heggheim <hegjon@gmail.com> - 3.0.3-1
- Updated to version 3.0.3

* Sat Dec 09 2017 Jonny Heggheim <hegjon@gmail.com> - 3.0.2-1
- Updated to version 3.0.2

* Sat Aug 12 2017 Jonny Heggheim <hegjon@gmail.com> - 2.9.3-1
- Updated to version 2.9.3

* Thu Aug 10 2017 Jonny Heggheim <hegjon@gmail.com> - 2.9.2-1
- Updated to version 2.9.2

* Tue Aug 01 2017 Jonny Heggheim <hegjon@gmail.com> - 2.9.0-1
- Updated to version 2.9.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Jonny Heggheim <hegjon@gmail.com> - 2.8.3-1
- new version

* Mon Apr 10 2017 Jonny Heggheim <hegjon@gmail.com> - 2.8.2-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.18-2
- Verify the signature of the source tarball

* Tue Jan 24 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.18-1
- new version

* Thu Jan 12 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.17-1
- new version

* Mon Jan 09 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.13-2
- Added suggests python2-btchip

* Tue Jan 03 2017 Jonny Heggheim <hegjon@gmail.com> - 2.7.13-1
- new version

* Tue Nov 29 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-5
- Include appdata.xml file

* Fri Nov 18 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-4
- Updated license to MIT and BSD

* Tue Nov 15 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-3
- Added Provides: bundled(python-SocksiPy)

* Sun Nov 13 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-2
- Added weak dependency on zbar-pygtk

* Wed Nov 09 2016 Jonny Heggheim <hegjon@gmail.com> - 2.7.12-1
- new version

* Tue Apr 26 2016 gyger@fsfe.org - 2.6.4-2
- Fixed for python2 and new packaging requirements.

* Mon Apr 25 2016 gyger@fsfe.org - 2.6.4-1
- Upgrade to new Version.
- Relicenced to MIT.

* Sat Nov 7 2015 gyger@fsfe.org - 2.5.2-1
- Upgrade to new Version.

* Sat Jul 25 2015 gyger@fsfe.org - 2.3.3-1
- Upgrade to new Version.

* Wed Jan 28 2015 gyger@fsfe.org - 2.0.0-4
- Add Dependency on Pbkdf2

* Wed Jan 28 2015 gyger@fsfe.org - 2.0.0-1
- Packaging the Beta Version.

* Wed Jan 28 2015 gyger@fsfe.org - 1.9.8-1
- Initial Packaging for electrum on Fedora
