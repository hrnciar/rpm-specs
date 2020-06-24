Name:		nicstat	
Version:	1.95
Release:	13%{?dist}
Summary:	CLI utility that prints out network statistics for all network interface 

License:	Artistic 2.0
URL:		http://sourceforge.net/projects/%{name}
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	gcc


%description
nicstat is a Solaris and Linux command-line that prints out network statistics 
for all network interface cards (NICs), including packets, kilobytes per second,
average packet sizes and more.


%prep
%setup -qn %{name}-%{version}


%build
# doesn't have configure script; uses custom Makefile, which boils down to single gcc invocation
gcc %{optflags} %{name}.c -o %{name}


%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%doc README.txt ChangeLog.txt LICENSE.txt


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Tomasz Torcz <ttorcz@fedoraproject.org> - 1.95-9
- rebuilt per request of Xose Vazquez Perez

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Tomasz Torcz <ttorcz@fedoraproject.org> 1.95-1
- update to latest upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Tomasz Torcz <ttorcz@fedoraproject.org> 1.92-5
- remove authors from description (they are already listed in README.txt)

* Thu Jun 13 2013 Tomasz Torcz <ttorcz@fedoraproject.org> 1.92-4
- include LICENSE.txt in doc 

* Thu Jun 13 2013 Tomasz Torcz <ttorcz@fedoraproject.org> 1.92-3
- change URL:

* Wed Jun 12 2013 Tomasz Torcz <ttorcz@fedoraproject.org> 1.92-2
- drop commented out lines (#972719) 

* Mon Jun 10 2013 Tomasz Torcz <ttorcz@fedoraproject.org> 1.92-1
- initial package

