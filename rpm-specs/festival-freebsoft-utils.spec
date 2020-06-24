Name:          festival-freebsoft-utils
Version:       0.10
Release:       17%{?dist}
Summary:       A collection of utilities that enhance Festival with some useful features

BuildArch:     noarch
License:       GPLv2+
URL:           http://www.freebsoft.org/festival-freebsoft-utils
Source0:       http://devel.freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz

BuildRequires: festival

Requires: festival
Requires: sox

%description
A collection of utilities that enhance Festival with some useful features. They 
provide all that is needed for interaction with Speech Dispatcher.

Key festival-freebsoft-utils features are:
- Generalized concept of input events. festival-freebsoft-utils allows not only 
  plain text synthesis, but also combining it with sounds. Additionally, 
  mechanism of logical events mapped to other events is provided. 
- Substitution of events for given words. 
- High-level voice selection mechanism and setting of basic prosodic parameters. 
- Spelling mode. 
- Capital letter signalization. 
- Punctuation modes, for explicit reading or not reading punctuation characters. 
- Incremental synthesis of texts and events. 
- Speech Dispatcher support. 
- Rudimentary SSML support. 
- Enhance the Festival extension language with functions commonly used in Lisp.
- Support for wrapping already defined Festival functions by your own code.
- Everything is written in the extension language, no patching of the Festival 
  C++ sources is needed.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/festival/lib/
cp -p *.scm %{buildroot}/%{_datadir}/festival/lib/

%ldconfig_scriptlets

%files
%doc COPYING NEWS README
%{_datadir}/festival/lib/*.scm

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10-5
- Update URLs and modernise spec

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.10-1
- Initial packaging
