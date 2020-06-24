Name:		xvarstar
Version:	0.9
Release:	25%{?dist}
Summary:	Astronomical program used for searching GCVS

License:	GPLv2+
URL:		http://virtus.freeshell.org/%{name}/
Source0:	http://virtus.freeshell.org/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
# Public Domain icon
Source2:	http://openclipart.org/people/emyller/emyller_star.svg

BuildRequires:  gcc
BuildRequires:	desktop-file-utils
%if 0%{?rhel}
BuildRequires:	openmotif-devel
%else if 0%{?fedora} >= 24
BuildRequires:  motif-devel
%else
BuildRequires:	lesstif-devel
%endif

%description
XVarStar is a astronomical program written for variable star observers, and is
 used for searching GCVS catalogue.  It allows searching by following criteria:
-star name 
-magnitude 
-type 
-constellation 
-amplitude 
-This searching criteria can be combined so one can search for example all 
variable stars located in Andromeda constellation and with magnitude 
brighter than 5.00.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" \
  sysconfdir="$RPM_BUILD_ROOT%{_sysconfdir}"

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
install -Dpm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/xvarstar.svg


%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/xvarstar.svg
%{_datadir}/applications/%{name}.desktop

%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9-16
- Build against motif on fedora >= 24.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9-11
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.9-6
- Fix summary
- Add icon
- Fix categories

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.9-4
- Grab right Motif implementation
- Remove the broken patch, fix sysconfdir path with make option
- Honor optflags

* Sun Sep  7 2008 <mmahut@fedoraproject.org> - 0.9-3
- Fixing license tag at FUDCon Brno 2008

* Sat Jun 28 2008  <telimektar1er@gmail.com> - 0.9-2
- Removed encoding section from the .desktop and renaming of the patch

* Fri May  2 2008  <telimektar1er@gmail.com> - 0.9-1
- Initial Package


