Name:		gcx
Version:	0.9.11
Release:	27%{?dist}
Summary:	Data-reduction tool for CCD photometry

License:	GPLv2+
URL:		http://sourceforge.net/projects/gcx/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	gcx.desktop
Source2:	gcx.svg
Patch0:         gcx-0.9.11-bounds.patch

Requires:	gnuplot
BuildRequires:  gcc
BuildRequires:	gtk+-devel, desktop-file-utils

%description
GCX provides a complete set of data-reduction
functions for CCD photometry, accessible both
from a GUI and the command line. It also controls
CCD cameras and telescopes, and implements
automatic observation scripting.

%prep
%setup -q
%patch0 -p1 -b .bounds

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 src/gcx $RPM_BUILD_ROOT%{_bindir}/gcx
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/gcx/gcx.svg
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/gcx
%{_datadir}/applications/gcx.desktop
%{_datadir}/gcx

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.11-14
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 7 2009 Marek Mahut <mmahut@fedoraproject.org> - 0.9.11-8
- Fix mime association with FITS files (RHBZ#494430)

* Mon Apr 6 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.9.11-6
- Fix a stack overflow (#494345)

* Tue Mar 24 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.9.11-5
- Fix the icon location

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 31 2007 Marek Mahut <mmahut@fedoraproject.org> - 0.9.11-3
- Initial release.
