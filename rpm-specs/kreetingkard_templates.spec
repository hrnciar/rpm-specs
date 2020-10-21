%define		appname		kreetingkard

%define		mainver		0.2.0
%define		vendorrel	4
%define		repoid		18013



Name:		kreetingkard_templates
Version:	%{mainver}
Release:	%{vendorrel}%{?dist}.16
Summary:	Template files for KreetingKard

License:	GPL+
URL:		http://linux-life.net/program/cc/kde/app/kreetingkard/
Source0:	http://downloads.sourceforge.jp/%{appname}/%{repoid}/%{name}-%{mainver}.tar.gz
# From Mandriva
Requires:	%{appname} >= 0.7.1

BuildArch:	noarch

%description
KreetingKard is a tool for making Japanese greeting cards. It allows you to 
make greeting cards easily by choosing a template and changing the words.

This package contains some template files for KreetingKard.


%prep
%setup -q

find templates/ -name CVS | sort -r | xargs %{__rm} -rf
find templates/ -name Makefile\* -or -name \*.rb | xargs %{__rm} -f

%build
# This package is noarch, however when we set BuildArch as
# noarch, %%configure fails strangefully. So we install the needed files
# manually.
echo "Nothing to do here"

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/apps/%{appname}/
%{__cp} -pr templates/ $RPM_BUILD_ROOT%{_datadir}/apps/%{appname}/

%files
%doc	AUTHORS
%doc	COPYING
%doc	README

%{_datadir}/apps/%{appname}/templates/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.0-4
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.0-3
- F-11: Mass rebuild

* Mon Oct 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.0-2
- Fix typo.

* Thu Oct 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.2.0-1
- Initial spec file
