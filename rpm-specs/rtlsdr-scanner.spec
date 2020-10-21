Name:		rtlsdr-scanner
Version:	1.3.2
Release:	8%{?dist}
Summary:	Frequency scanning GUI for RTL2832 based DVB-T dongles
License:	GPLv3
URL:		http://eartoearoak.com/software/rtlsdr-scanner
Source0:	https://github.com/EarToEarOak/RTLSDR-Scanner/archive/v%{version}.tar.gz#/RTLSDR-Scanner-%{version}.tar.gz
Source1:	rtlsdr-scanner.desktop
# Icon taken from older release of rtlsdr-scanner
Source2:	rtlsdr_scan.png
BuildRequires:	python3-setuptools, python3-visvis
BuildRequires:	python3-devel, desktop-file-utils
Requires:	python3-wxpython4, python3-matplotlib, python3-matplotlib-wx, python3-numpy
Requires:	python3-pillow, python3-pyserial, python3-pyrtlsdr, hicolor-icon-theme
Requires:	python3-visvis
BuildArch:	noarch
# distribution specific patch changing path to resources
Patch0:		rtlsdr-scanner-1.3.2-fedora.patch
# https://github.com/EarToEarOak/RTLSDR-Scanner/pull/51
Patch1:		rtlsdr-scanner-1.3.2-python3.patch

%description
Frequency scanning GUI for RTL2832 based DVB-T dongles. In other
words a cheap, simple Spectrum Analyser.

%package doc
Summary:	Documentation files for rtlsdr-scanner
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
%{summary}.

%prep
%setup -qn RTLSDR-Scanner-%{version}
%patch0 -p1
%patch1 -p1

find rtlsdr_scanner -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'

# rtlsdr_scan_diag.py is not needed in distribution
rm -f rtlsdr_scanner/rtlsdr_scan_diag.py

# fix name of the application
mv rtlsdr_scanner/__main__.py rtlsdr_scan

# drop python artefact from resources
rm -f rtlsdr_scanner/res/__init__.py

%build
%py3_build

%install
%py3_install

install -Dpm 0755 ./rtlsdr_scan %{buildroot}%{_bindir}/rtlsdr_scan

# Install resources to correct location
install -Dpm 0644 -t %{buildroot}%{_datadir}/%{name}/res rtlsdr_scanner/res/*

# Icon
install -Dpm 0644 %{S:2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/rtlsdr_scan.png

# Desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%files
%license COPYING
%doc readme.md
%{_bindir}/rtlsdr_scan
%{_datadir}/icons/hicolor/256x256/apps/rtlsdr_scan.png
%{_datadir}/applications/rtlsdr-scanner.desktop
%{_datadir}/%{name}
%{python3_sitelib}/rtlsdr_scanner
%{python3_sitelib}/rtlsdr_scanner-*.egg-info

%files doc
%doc doc/Manual.pdf

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov  7 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3.2-5
- Switched to Python 3
  Resolves: rhbz#1738179

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3.2-1
- New version
  Resolves: rhbz#1585444
- Dropped relative-imports patch
- Updated fedora patch

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.22497.10311-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22497.10311-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.22497.10311-4
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22497.10311-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.22497.10311-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.22497.10311-1
- New version
- Fixed imports to be relative
  Resolves: rhbz#1383513

* Tue Sep 20 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.22298.18049-3
- Rebuilt for python2-matplotlib

* Fri Jul 15 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.22298.18049-2
- Fixed icon packaging according to review

* Tue Apr 12 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.22298.18049-1
- Initial release
