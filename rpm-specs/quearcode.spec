Name:           quearcode
Version:        0.2.6
Release:        3%{?dist}
Summary:        A tool for creating QR Codes

License:        GPLv3+
URL:            https://sourceforge.net/projects/quearcode/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        quearcode.desktop
BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       python3-qrcode python3-gobject hicolor-icon-theme

%description
Convert strings and small files to QR Codes

%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/quearcode
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata

install -m 755 quearcode $RPM_BUILD_ROOT%{_bindir}/quearcode
install -m 644 logo.png $RPM_BUILD_ROOT%{_datadir}/quearcode/
install -m 644 quearcode.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 logo.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/quearcode.png

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}


%files
%doc COPYING README
%{_bindir}/quearcode
%{_datadir}/quearcode
%{_datadir}/applications/quearcode.desktop
%{_datadir}/icons/hicolor/scalable/apps/quearcode.png
%{_datadir}/appdata/quearcode.appdata.xml

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.6-1
- 0.2.6, view and save internally.

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.5-2
- Fix requires.

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.2.5-1
- 0.2.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.4-5
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuild for Python 3.6

* Fri Sep 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.2.4-1
- Typo fix, code cleanup.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Jon Ciesla <limburgher@gmail.com> - 0.2.3-1
- Latest upstream, migrated to Python 3.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 18 2014 Jon Ciesla <limburgher@gmail.com> - 0.2.2-1
- Latest upstream, includes appdata.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.2.1-1
- 0.2.1, better size error handling.

* Wed Sep 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.2-2
- URL fix for review.

* Tue Sep 11 2012 Jon Ciesla <limburgher@gmail.com> - 0.2-1
- 0.2, deeper control of generation.

* Tue Sep 11 2012 Jon Ciesla <limburgher@gmail.com> - 0.1.2-1
- First build.
