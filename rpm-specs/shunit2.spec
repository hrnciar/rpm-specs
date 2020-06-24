%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           shunit2
Version:        2.1.6
Release:        18%{?dist}
Summary:        A xUnit based unit testing for Unix shell scripts

License:        LGPLv2
URL:            http://code.google.com/p/shunit2
Source0:        http://shunit2.googlecode.com/files/%{name}-%{version}.tgz
# add makefiles to do install
Source1:        LGPL-2.1
Patch0:         add_makefiles.patch
Patch1:         fix_examples_source_path.patch
BuildArch:      noarch

%description
shUnit2 is a xUnit unit test framework for Bourne based shell scripts,
and it is designed to work in a similar manner to JUnit, PyUnit, etc.
If you have ever had the desire to write a unit test for a shell script,
shUnit2 can do the job.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
iconv -f ISO88592 -t UTF8 doc/shunit2.txt -o doc/shunit2.txt
cp -p %{SOURCE1} doc/

%build
# This section is empty because this package ccontains shell scripts
# to be sourced: there's nothing to build


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} DOCDIR=%{_pkgdocdir}



%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_pkgdocdir}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.6-14
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.1.6-8
- Install docs to %%{_pkgdocdir} where available (#994092).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 17 2011 Hushan Jia <hjia@redhat.com> 2.1.6-3
- fix file list warning

* Tue May 17 2011 Hushan Jia <hjia@redhat.com> 2.1.6-2
- remove duplicate %%doc directive
- fix source include path of examples
- replace license with update-to-date version

* Tue May 3 2011 Hushan Jia <hjia@redhat.com> 2.1.6-1
- initial package

