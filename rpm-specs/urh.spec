%{?python_enable_dependency_generator}
# python 2 not supported

Name:		urh
Version:	2.8.9
Release:	1%{?dist}
Summary:	Universal Radio Hacker: investigate wireless protocols like a boss
License:	ASL 2.0 and GPLv2
URL:		https://github.com/jopohl/urh
Source0:	https://github.com/jopohl/urh/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python3-setuptools, python3-devel, gcc-c++, python3-numpy, desktop-file-utils
BuildRequires:	airspyone_host-devel, hackrf-devel, rtl-sdr-devel, uhd-devel, python3-qt5, python3-Cython
Requires:	python3-numpy, python3-qt5

%description
The Universal Radio Hacker is a software for investigating unknown wireless
protocols.

%prep
%setup -q

# remove *.pyc
find . -name '*.pyc' | xargs rm -f

# remove profiling data
pushd data
rm -f hacker.prof
popd

# remove binaries
pushd data/decodings
rm -f enocean_switchtelegram homematic homematic_complete test
popd
pushd src/urh/dev/native/lib
rm -rf win
popd


%build
%py3_build

%install
%py3_install

# remove cpp files generated by cython
pushd %{buildroot}%{python3_sitearch}/urh/dev/native/lib
rm -f *.cpp
popd
pushd %{buildroot}%{python3_sitearch}/urh/cythonext
rm -f *.cpp
popd


# icon
install -Dpm 0644 data/icons/appicon.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/urh.png

# desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications \
  data/urh.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/urh
%{_bindir}/urh_cli
%{_datadir}/icons/hicolor/128x128/apps/urh.png
%{_datadir}/applications/urh.desktop
%{python3_sitearch}/urh
%{python3_sitearch}/urh-%{version}-*.egg-info

%changelog
* Mon Sep 21 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.9-1
- New version
  Resolves: rhbz#1876872

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.8-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.8-1
- New version
  Resolves: rhbz#1837080

* Mon Apr 27 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.7-1
- New version
  Resolves: rhbz#1828481

* Thu Apr 16 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.6-1
- New version
  Resolves: rhbz#1824311
- Simplified source URL

* Tue Mar 24 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.5-1
- New version
  Resolves: rhbz#1816690
  Resolves: rhbz#1815664

* Sat Mar 21 2020 David Sastre <david.sastre@redhat.com> - 2.8.4-2
- Add AirSpy R2 native support

* Mon Mar  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.4-1
- New version
  Resolves: rhbz#1811369

* Tue Feb 25 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.3-1
- New version
  Resolves: rhbz#1806112

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.2-1
- New version
  Resolves: rhbz#1788393

* Sun Nov 24 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.8.1-1
- New version
  Resolves: rhbz#1763507

* Mon Nov 11 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.5-3
- Rebuilt for new uhd
  Resolves: rhbz#1770877

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.5-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.5-1
- New version
  Resolves: rhbz#1747017

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.4-2
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.4-1
- New version
  Resolves: rhbz#1743014

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.3-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul  1 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.3-1
- New version
  Resolves: rhbz#1725697

* Wed Jun 26 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.2-1
- New version
  Resolves: rhbz#1724216

* Sat Jun 22 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.0-2
- Added missing explicit requirements

* Mon Jun  3 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.7.0-1
- New version
  Resolves: rhbz#1716083

* Mon May 20 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6.0-1
- New version
  Resolves: rhbz#1711889

* Wed Apr  3 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.7-1
- New version
  Resolves: rhbz#1695648

* Mon Feb 25 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.6-1
- New version
  Resolves: rhbz#1680429

* Tue Feb  5 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.5-1
- New version
  Resolves: rhbz#1667686

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.4-2
- Enable python dependency generator

* Thu Jan 10 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 2.5.4-1
- New version
  Related: rhbz#1609532

* Thu Aug  9 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.3-1
- New version
  Resolves: rhbz#1609532

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-2
- Rebuilt for Python 3.7

* Mon Jul  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2.2-1
- New version
  Resolves: rhbz#1596898

* Tue Jun 19 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.1-1
- New version
  Resolves: rhbz#1592165

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.7

* Fri Jun  1 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1.0-1
- New version
  Resolves: rhbz#1585185

* Mon May  7 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.4-2
- Fixed build

* Mon May  7 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.4-1
- New version
  Resolves: rhbz#1575442

* Mon Apr 23 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.2-1
- New version
  Resolves: rhbz#1570453

* Mon Mar 26 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.1-1
- New version
  Resolves: rhbz#1560129

* Tue Mar 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.0-1
- New version
  Resolves: rhbz#1550057

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.2-1
- New version
  Resolves: rhbz#1536440
- Dropped desktop-file-fix patch (upstreamed)

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.1-2
- Remove obsolete scriptlets

* Sat Dec 23 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.9.1-1
- New version
  Resolves: rhbz#1526667

* Wed Nov 22 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.13-1
- New version
  Resolves: rhbz#1514288

* Tue Nov 14 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.11-1
- New version
  Resolves: rhbz#1512741

* Mon Oct 23 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.10-1
- New version
  Resolves: rhbz#1504440

* Mon Sep 18 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.7-1
- New version
  Resolves: rhbz#1492666

* Thu Aug 31 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.5-1
- New version
  Resolves: rhbz#1486742

* Mon Aug 28 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.8.4-1
- New version
  Resolves: rhbz#1485094

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.7.1-1
- New version
  Resolves: rhbz#1473063

* Tue Jul 18 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.7.0-1
- New version
  Resolves: rhbz#1471311

* Mon Jun 19 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.6-1
- New version
- Fixed various problem spotted during Fedora review
  Related: rhbz#1432076

* Fri Mar 10 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 1.5.7-1
- Initial release
