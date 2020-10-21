%global gkplugindir %{_libdir}/gkrellm2/plugins

Summary:	GKrellM plugin which shows 3 most CPU intensive processes
Name:		gkrellm-top
Version:	2.2.13
Release:	19%{?dist}
License:	GPL+
URL:		http://gkrelltop.sourceforge.net/
Source:		http://downloads.sf.net/gkrelltop/gkrelltop_%{version}.orig.tar.gz
Patch:		gkrelltop-2.2.13-optflags.patch
Requires:	gkrellm >= 2.2.0
BuildRequires:	gcc, gkrellm-devel >= 2.2.0

%description
A GKrellM plugin which displays the top three CPU intensive processes in a
small window inside GKrellM, similar to wmtop. Useful to check out anytime
what processes are consuming most CPU power on your machine.

%prep
%setup -q -n gkrelltop-%{version}.orig
%patch -p1 -b .optflags

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 gkrelltop.so $RPM_BUILD_ROOT%{gkplugindir}/gkrelltop.so
install -D -m 755 gkrelltopd.so $RPM_BUILD_ROOT%{gkplugindir}/gkrelltopd.so

%files
%doc README
%{gkplugindir}/gkrelltop.so
%{gkplugindir}/gkrelltopd.so

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Robert Scheck <robert@fedoraproject.org> 2.2.13-1
- Upgrade to 2.2.13

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.2.11-2
- Rebuild against gcc 4.4 and rpm 4.6

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 2.2.11-1
- Upgrade to 2.2.11

* Wed Dec 12 2007 Robert Scheck <robert@fedoraproject.org> 2.2.10-1
- Upgrade to 2.2.10
- Initial spec file for Fedora and Red Hat Enterprise Linux
